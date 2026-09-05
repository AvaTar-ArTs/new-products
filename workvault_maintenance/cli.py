"""CLI and durable run engine for WorkVault Maintenance."""

from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(os.environ.get("WV_HOME", Path.home() / ".workvault-maintenance")).expanduser()
RUNS = ROOT / "runs"
LOCK = ROOT / "run.lock"


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def emit(run_dir: Path, event: str, **data: Any) -> None:
    record = {"ts": now(), "event": event, **data}
    with (run_dir / "events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")


def command_exists(command: str) -> bool:
    from shutil import which

    return which(command) is not None


@dataclass(frozen=True)
class Step:
    provider: str
    action: str
    command: tuple[str, ...] | None
    reason: str
    timeout: int = 1800


def brew_steps() -> list[Step]:
    if not command_exists("brew"):
        return []
    return [
        Step("brew", "update", ("brew", "update"), "refresh package metadata", 600),
        Step("brew", "upgrade", ("brew", "upgrade", "--formula", "--no-ask"), "upgrade formulae", 3600),
        Step("brew", "cleanup", ("brew", "cleanup"), "remove obsolete Homebrew versions", 600),
    ]


def macports_steps() -> list[Step]:
    if not command_exists("port"):
        return []
    return [
        Step("macports", "selfupdate", ("sudo", "port", "selfupdate"), "refresh MacPorts metadata", 900),
        Step("macports", "upgrade", ("sudo", "port", "upgrade", "outdated"), "upgrade outdated ports", 3600),
    ]


def ollama_steps() -> list[Step]:
    if not command_exists("ollama"):
        return []
    return [
        Step("ollama", "version", ("ollama", "version"), "verify local Ollama client", 60),
        Step("ollama", "list", ("ollama", "list"), "inventory installed models", 120),
    ]


def planned_steps(providers: Iterable[str]) -> list[Step]:
    factories = {"brew": brew_steps, "macports": macports_steps, "ollama": ollama_steps}
    result: list[Step] = []
    for provider in providers:
        result.extend(factories[provider]())
    return result


def acquire_lock(run_id: str) -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        owner = LOCK.read_text(encoding="utf-8", errors="replace")
        raise RuntimeError(f"another run owns {LOCK}: {owner}") from exc
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(run_id)


def release_lock() -> None:
    try:
        LOCK.unlink()
    except FileNotFoundError:
        pass


def save_state(run_dir: Path, state: dict[str, Any]) -> None:
    tmp = run_dir / "state.json.tmp"
    tmp.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(run_dir / "state.json")


def load_state(run_id: str) -> tuple[Path, dict[str, Any]]:
    run_dir = RUNS / run_id
    path = run_dir / "state.json"
    if not path.exists():
        raise FileNotFoundError(f"unknown run: {run_id}")
    return run_dir, json.loads(path.read_text(encoding="utf-8"))


def run_step(run_dir: Path, state: dict[str, Any], index: int, step: Step) -> bool:
    if step.command is None:
        return True
    out = (run_dir / f"step-{index:02d}.log").open("a", encoding="utf-8")
    started = time.monotonic()
    emit(run_dir, "step.started", index=index, provider=step.provider, action=step.action, command=list(step.command))
    state["steps"][index]["status"] = "running"
    state["steps"][index]["started_at"] = now()
    save_state(run_dir, state)
    process: subprocess.Popen[str] | None = None
    cancelled = False

    def cancel(_signum: int, _frame: Any) -> None:
        nonlocal cancelled
        cancelled = True
        if process and process.poll() is None:
            os.killpg(process.pid, signal.SIGTERM)

    previous = signal.signal(signal.SIGINT, cancel)
    previous_term = signal.signal(signal.SIGTERM, cancel)
    try:
        process = subprocess.Popen(
            list(step.command), stdout=out, stderr=subprocess.STDOUT, text=True,
            start_new_session=True,
        )
        state["steps"][index]["pid"] = process.pid
        state["steps"][index]["pgid"] = process.pid
        save_state(run_dir, state)
        while process.poll() is None:
            if time.monotonic() - started > step.timeout:
                cancelled = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                emit(run_dir, "step.timed_out", index=index, timeout=step.timeout)
                break
            time.sleep(0.25)
        code = process.returncode
    finally:
        signal.signal(signal.SIGINT, previous)
        signal.signal(signal.SIGTERM, previous_term)
        out.close()
    status = "cancelled" if cancelled or (run_dir / "cancel").exists() else ("succeeded" if code == 0 else "failed")
    state["steps"][index].update(status=status, exit_code=code, finished_at=now())
    emit(run_dir, f"step.{status}", index=index, provider=step.provider, action=step.action, exit_code=code,
         duration_seconds=round(time.monotonic() - started, 2))
    save_state(run_dir, state)
    return status == "succeeded"


def create_run(providers: list[str], apply: bool) -> tuple[Path, dict[str, Any]]:
    run_id = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
    run_dir = RUNS / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    steps = planned_steps(providers)
    state = {"run_id": run_id, "mode": "apply" if apply else "plan", "status": "planned",
             "created_at": now(), "cwd": str(Path.cwd()),
             "steps": [{"provider": s.provider, "action": s.action, "reason": s.reason,
                        "command": list(s.command) if s.command else None, "status": "pending"} for s in steps]}
    save_state(run_dir, state)
    emit(run_dir, "run.created", run_id=run_id, mode=state["mode"], providers=providers, step_count=len(steps))
    return run_dir, state


def execute(run_dir: Path, state: dict[str, Any]) -> int:
    run_id = state["run_id"]
    acquire_lock(run_id)
    state["status"] = "running"
    state["started_at"] = now()
    save_state(run_dir, state)
    emit(run_dir, "run.started", run_id=run_id)
    try:
        for index, entry in enumerate(state["steps"]):
            if entry["status"] == "succeeded":
                continue
            step = Step(entry["provider"], entry["action"], tuple(entry["command"]) if entry["command"] else None, entry["reason"])
            if not run_step(run_dir, state, index, step):
                state["status"] = "cancelled" if entry["status"] == "cancelled" else "failed"
                break
        else:
            state["status"] = "succeeded"
        state["finished_at"] = now()
        save_state(run_dir, state)
        emit(run_dir, "run." + state["status"], run_id=run_id)
        return 0 if state["status"] == "succeeded" else 1
    finally:
        release_lock()


def print_plan(state: dict[str, Any]) -> None:
    print(f"WorkVault Maintenance · {state['mode']} · {state['run_id']}")
    for i, step in enumerate(state["steps"]):
        command = " ".join(step["command"]) if step["command"] else "unavailable"
        print(f"  [{i:02d}] {step['provider']}.{step['action']}: {step['reason']} · {command}")
    print(f"Saved run: {RUNS / state['run_id']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="wv", description="Observable macOS maintenance control plane")
    sub = parser.add_subparsers(dest="command", required=True)
    plan = sub.add_parser("plan", help="create a read-only plan")
    plan.add_argument("providers", nargs="*", choices=["brew", "macports", "ollama"], default=["brew", "macports", "ollama"])
    apply = sub.add_parser("apply", help="execute a plan immediately")
    apply.add_argument("providers", nargs="*", choices=["brew", "macports", "ollama"], default=["brew", "macports", "ollama"])
    for name in ("status", "logs", "report", "cancel", "resume"):
        p = sub.add_parser(name)
        p.add_argument("run_id", nargs="?")
    args = parser.parse_args(argv)
    if args.command in ("plan", "apply"):
        providers = args.providers or ["brew", "macports", "ollama"]
        run_dir, state = create_run(providers, args.command == "apply")
        print_plan(state)
        if args.command == "apply":
            return execute(run_dir, state)
        return 0
    if args.command == "status":
        for path in sorted(RUNS.glob("run_*/state.json"))[-20:]:
            state = json.loads(path.read_text(encoding="utf-8"))
            print(f"{state['run_id']}  {state['status']}  {state['mode']}  {state.get('created_at', '')}")
        return 0
    if not args.run_id:
        parser.error(f"{args.command} requires RUN_ID")
    run_dir, state = load_state(args.run_id)
    if args.command == "logs":
        print((run_dir / "events.jsonl").read_text(encoding="utf-8"), end="")
    elif args.command == "report":
        print(json.dumps(state, indent=2))
    elif args.command == "cancel":
        (run_dir / "cancel").write_text(now(), encoding="utf-8")
        for entry in state.get("steps", []):
            pid = entry.get("pid")
            if entry.get("status") == "running" and isinstance(pid, int):
                try:
                    os.killpg(pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
        print(f"Cancellation requested for {args.run_id}")
    elif args.command == "resume":
        return execute(run_dir, state)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
