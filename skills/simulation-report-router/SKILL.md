---
name: simulation-report-router
description: Load when the user wants an existing simulation analysis bundle turned into a report, Markdown/HTML package, PPTX, media inventory, or design-review handoff.
---

# Simulation report router

Reporting consumes a verified analysis bundle; it does not choose a solver and must not rediscover loose files. Route to the independent `simulation-reporting` consumer when the user requests HTML, Markdown, PPTX, or presentation media.

Require a `RunSummary` or equivalent analysis bundle containing:

- analysis title and branch
- package root and summary JSON
- figures, animations, and keyframes
- key metrics
- assumptions and known limits
- verification status

The compatibility bridge is documented in `references/analysis-bundle-contract.md`. Keep `simulation-reporting` separate because it consumes this bundle and does not solve or verify the case.

Preserve the upstream evidence boundary. If a solver or verification gate is `blocked`, report that state and do not write a polished success narrative around it.
