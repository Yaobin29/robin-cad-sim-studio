# Hermes / Pi-style adapter

Hermes and Pi-style hosts consume the Agent Skills-compatible `skills/` directories. Scientific routing remains in the shared skill body; host-specific work is limited to sync and optional MCP registration.

```bash
python3 adapters/hermes/sync-skills.py --dry-run
python3 adapters/hermes/sync-skills.py --apply
python3 adapters/hermes/register-mcp.py
```

The sync destination comes from `HERMES_SKILLS_ROOT`; otherwise it defaults to `~/.hermes/skills/engineering/robin-cad-sim-studio`. The adapter never reads or writes Hermes secrets.
