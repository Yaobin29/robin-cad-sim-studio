#!/usr/bin/env python3
"""Sync shared Agent Skills to Hermes without touching secrets or working memory."""
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Robin CAD Sim Studio skills to Hermes.")
    parser.add_argument("--plugin-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--destination", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    plugin_root = args.plugin_root.expanduser().resolve()
    source = plugin_root / "skills"
    destination = (args.destination or Path(os.environ.get("HERMES_SKILLS_ROOT", "~/.hermes/skills/engineering"))).expanduser().resolve() / plugin_root.name
    if not source.is_dir():
        raise SystemExit(f"missing source skills directory: {source}")
    files = sorted(path for path in source.rglob("*") if path.is_file())
    payload = {"status": "ok", "source": str(source), "destination": str(destination), "file_count": len(files), "apply": args.apply}
    if args.apply:
        destination.mkdir(parents=True, exist_ok=True)
        for path in files:
            target = destination / path.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
