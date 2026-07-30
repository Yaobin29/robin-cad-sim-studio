# Claude adapter

Claude uses the same `skills/`, contracts, CLI commands, and optional MCP registration. The Claude-specific surface is only `.claude-plugin/plugin.json` plus the uploadable `.plugin` archive. Build it with `scripts/package-cross-agent` or the local `claude-plugin-packager` skill.
