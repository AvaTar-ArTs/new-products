"""Bounded, read-only workstation audit used by WorkVault Maintenance."""

from __future__ import annotations

import json
import os
import re
from collections import Counter
from pathlib import Path
from typing import Any

SENSITIVE = re.compile(r"oauth|credential|secret|token|password|private[_-]?key|api[_-]?key|\.env$", re.I)
CACHEISH = re.compile(r"(^|/)(node_modules|\.cache|cache|tmp|logs?|sessions?|history|backup|dist|build|\.git)(/|$)", re.I)
SKIP_DIRS = {".Spotlight-V100", ".Trashes", ".TemporaryItems", ".fseventsd", ".DocumentRevisions-V100", "__pycache__"}


def human(size: int) -> str:
    value = float(size)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if value < 1024 or unit == "TB":
            return f"{value:.1f}{unit}" if unit != "B" else f"{int(value)}B"
        value /= 1024
    return f"{size}B"


def audit_root(root: Path, top: int = 20) -> dict[str, Any]:
    root = root.expanduser().resolve()
    result: dict[str, Any] = {"root": str(root), "exists": root.exists(), "files": 0, "bytes": 0,
                              "extensions": {}, "cacheish_files": 0, "sensitive_name_hits": [], "largest_files": [], "errors": 0}
    if not root.exists() or not root.is_dir():
        return result
    largest: list[tuple[int, str]] = []
    extensions: Counter[str] = Counter()
    for directory, subdirs, files in os.walk(root, topdown=True, followlinks=False):
        subdirs[:] = [name for name in subdirs if name not in SKIP_DIRS and not name.startswith(".")]
        current = Path(directory)
        for name in files:
            path = current / name
            try:
                stat = path.stat()
            except OSError:
                result["errors"] += 1
                continue
            size = int(stat.st_size)
            relative = str(path.relative_to(root))
            result["files"] += 1
            result["bytes"] += size
            extensions[path.suffix.lower() or "[none]"] += 1
            if CACHEISH.search(relative):
                result["cacheish_files"] += 1
            if SENSITIVE.search(name) or SENSITIVE.search(relative):
                result["sensitive_name_hits"].append({"path": str(path), "size": size})
            largest.append((size, str(path)))
    largest.sort(reverse=True)
    result["extensions"] = dict(extensions.most_common())
    result["largest_files"] = [{"path": path, "bytes": size, "size": human(size)} for size, path in largest[:top]]
    result["sensitive_name_hits"] = result["sensitive_name_hits"][:top]
    return result


def write_audit_report(roots: list[Path], output: Path, top: int = 20) -> Path:
    report = {"schema_version": "1.0", "read_only": True, "roots": [audit_root(root, top) for root in roots]}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return output
