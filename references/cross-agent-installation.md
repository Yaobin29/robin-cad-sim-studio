# Cross-agent installation contract

The plugin has one portable source tree and three thin host adapters. No host adapter owns scientific routing logic.

## Codex

Load `.codex-plugin/plugin.json`, `skills/`, and `.mcp.json`. The Codex manifest may be added to a local marketplace, but the canonical source remains the repository plugin directory.

## Claude

Load `.claude-plugin/plugin.json`, `skills/`, and any explicitly registered MCP bridge. Build a `.plugin` archive with one top-level `robin-cad-sim-studio/` folder. The archive must exclude `.codex-plugin/`, prior archives, secrets, and working memory.

## Hermes and Pi-style hosts

Load the Agent Skills-compatible directories under `skills/`. The Hermes adapter can sync them to `HERMES_SKILLS_ROOT` or the default `~/.hermes/skills/engineering/robin-cad-sim-studio/`; it requires `--apply` before writing. MCP registration is emitted as a portable JSON fragment and is intentionally separate from skill sync.

## Portability boundary

Portable means shared skill text, contracts, route categories, output policy, and adapter behavior. Solver binaries, Python environments, Fusion session state, MCP credentials, and machine-specific paths remain node-local and are discovered at runtime.
