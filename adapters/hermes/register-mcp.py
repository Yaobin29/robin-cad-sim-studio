#!/usr/bin/env python3
"""Emit a node-local MCP registration fragment; do not mutate Hermes config by default."""
from __future__ import annotations

import argparse
import json
import os


def main() -> int:
    parser = argparse.ArgumentParser(description="Emit a Robin CAD Sim Studio MCP registration fragment.")
    parser.add_argument("--command", default=os.environ.get("ROBIN_FUSION360_MCP_COMMAND", "robin-cad-sim-fusion360-mcp"))
    parser.add_argument("--server-name", default="fusion360_mcp")
    args = parser.parse_args()
    print(json.dumps({"mcpServers": {args.server_name: {"command": args.command, "args": [], "optional": True}}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
