---
name: result-render-router
description: Load when the user asks to inspect, verify, render, animate, or report XDMF/VTK/mesh simulation outputs, ParaView fields, scientific figures, or microscopy-adjacent result evidence.
---

# Result and evidence router

Use this branch after a solver run or when the user supplies existing fields. Prefer `paraview-cli` for deterministic render/export and `paraview-verification-rendering` for scientific evidence checks. Use Unity only as an optional interactive review layer, never as the physics solver.

Every render must preserve:

- source case and field
- physical time range and frame provenance
- visualization-only interpolation or smoothing
- thresholds, metrics, and validation boundary
- standard `16:9` or `4:3` canvas unless the user asks otherwise

Return an `EvidenceReport`. A visual sequence alone is not enough for a physical droplet claim: pair it with source-field metrics and connected-component analysis. If only metadata or a partial render is available, mark verification `partial`.
