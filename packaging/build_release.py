#!/usr/bin/env python3
"""Build a reviewable product ZIP from an explicit package manifest.

This builder is intentionally allow-list based. It packages product metadata
and approved repository files; it never recursively bundles a home directory,
mounted volume, credentials, caches, or generated private inventories.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent.parent / "packages"
REPO_ROOT = PACKAGE_ROOT.parent.parent
SECRET_NAME = re.compile(r"(^|[._-])(env|secret|token|credential|password|private[_-]?key)([._-]|$)", re.I)
DENIED_SUFFIXES = {".pem", ".p12", ".pfx", ".key"}


def load_package(package_id: str) -> tuple[Path, dict[str, object]]:
    path = PACKAGE_ROOT / package_id / "product.json"
    if not path.is_file():
        raise FileNotFoundError(f"unknown package: {package_id}")
    return path, json.loads(path.read_text(encoding="utf-8"))


def approved_files(package_path: Path, package: dict[str, object]) -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = [(package_path, "product.json")]
    for raw in package.get("package_files", []):
        source = Path(str(raw)).expanduser()
        if not source.is_absolute():
            source = REPO_ROOT / source
        if not source.is_file():
            raise FileNotFoundError(f"approved package file is missing: {source}")
        if SECRET_NAME.search(source.name) or source.suffix.lower() in DENIED_SUFFIXES:
            raise ValueError(f"refusing secret-like package file: {source}")
        files.append((source, f"approved/{source.name}"))
    return files


def build(package_id: str, output: Path) -> Path:
    package_path, package = load_package(package_id)
    files = approved_files(package_path, package)
    output.parent.mkdir(parents=True, exist_ok=True)
    release = {
        "schema_version": "1.0",
        "package_id": package_id,
        "built_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "files": [archive_name for _, archive_name in files],
        "release_state": package.get("release_state"),
        "note": "Metadata/approved-files bundle; native signing and marketplace review remain separate gates.",
    }
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for source, archive_name in files:
            archive.write(source, archive_name)
        archive.writestr("RELEASE-MANIFEST.json", json.dumps(release, indent=2, sort_keys=True) + "\n")
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build an allow-list product release ZIP")
    parser.add_argument("package_id")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)
    try:
        output = args.output or Path("dist") / f"{args.package_id}.zip"
        print(f"Building {args.package_id} -> {output}")
        print(f"Created: {build(args.package_id, output)}")
        return 0
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
