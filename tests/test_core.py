from __future__ import annotations

import json
import unittest
from pathlib import Path

from workvault_maintenance.audit import audit_root, write_audit_report
from workvault_maintenance.cli import create_run, load_state


class TestWorkVaultMaintenance(unittest.TestCase):
    def test_audit_is_read_only_and_reports_large_files(self) -> None:
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            (tmp_path / "cache").mkdir()
            (tmp_path / "cache" / "large.bin").write_bytes(b"x" * 32)
            before = sorted(str(path.relative_to(tmp_path)) for path in tmp_path.rglob("*"))
            result = audit_root(tmp_path)
            after = sorted(str(path.relative_to(tmp_path)) for path in tmp_path.rglob("*"))
            self.assertEqual(result["files"], 1)
            self.assertEqual(result["cacheish_files"], 1)
            self.assertEqual(result["largest_files"][0]["bytes"], 32)
            self.assertEqual(before, after)

    def test_audit_report_is_machine_readable(self) -> None:
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            output = write_audit_report([tmp_path], tmp_path / "reports" / "audit.json")
            data = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(data["read_only"])
            self.assertEqual(data["roots"][0]["root"], str(tmp_path.resolve()))

    def test_plan_persists_run_state(self) -> None:
        from tempfile import TemporaryDirectory
        from unittest.mock import patch
        with TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            with patch("workvault_maintenance.cli.RUNS", tmp_path / "runs"), patch("workvault_maintenance.cli.ROOT", tmp_path):
                run_dir, state = create_run(["ollama"], apply=False)
                loaded_dir, loaded = load_state(state["run_id"])
            self.assertEqual(loaded_dir, run_dir)
            self.assertEqual(loaded["mode"], "plan")
