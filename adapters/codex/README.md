# Codex adapter

Codex loads the portable source through `.codex-plugin/plugin.json`, `skills/`, and the optional `.mcp.json`. The canonical plugin intentionally leaves the default MCP map empty: machine-specific live bridges should be registered by the node adapter or marketplace installation, not hardcoded into portable source.

Use `scripts/discover-backends` for command presence and a backend-specific health check for runtime truth.
