# Contributing to Robin CAD Sim Studio

Thank you for improving the plugin. Keep changes portable and preserve the boundary between host reasoning, skill routing, tool bridges, and backend runtimes.

## Before opening a pull request

Run:

```bash
python3 scripts/validate-contracts
python3 scripts/discover-backends
python3 scripts/package-cross-agent --dry-run
```

For routing changes, update [`evals/evals.json`](evals/evals.json) with a positive, boundary, negative, or regression case. For contract changes, explain compatibility impact and include an example that validates against the schema.

## Design rules

- Keep `SKILL.md` focused on routing, judgment, boundaries, and failure handling.
- Put heavy domain material in `references/` and deterministic logic in `scripts/`.
- Keep solver-specific leaf capabilities independent.
- Prefer CLI-first behavior; make MCP requirements explicit.
- Return `blocked` when a required runtime is absent.
- Never add credentials, machine-specific absolute paths, or host working memory.
- Preserve the output policy: `outputs/` and `outputs/research/<YYYY-MM>/`.

## Pull requests

Describe the problem, the route or contract change, verification performed, and remaining scientific or runtime limitations. Avoid presenting packaging smoke checks as solver validation.
