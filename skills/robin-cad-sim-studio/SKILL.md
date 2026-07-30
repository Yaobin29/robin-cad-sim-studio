---
name: robin-cad-sim-studio
description: Load when the user asks for a single CAD-to-simulation workflow, CAD/mesh/FEM/CFD routing, microfluidic chip simulation, result verification, or report packaging across Codex, Claude, Hermes, or Pi-style agents.
---

# Robin CAD Sim Studio

Use this as the one high-level entry point. The host LLM remains responsible for understanding the request and calling tools. This skill is responsible for the scientific workflow boundary: classify, choose a branch, preserve contracts, verify evidence, and state the next action.

## First normalize the task

For important work, create a `TaskBrief` with:

- problem description and `WHY` / `HOW` / `MIX` type
- geometry, materials, physics, boundary conditions, and constraints
- requested outputs and credibility requirements
- current gap, smallest useful model, current action, and next minimal action

For `MIX`, separate explanation from execution before changing geometry or solver settings.

## Route to one branch

| User intent | Route |
| --- | --- |
| CAD, mesh, elasticity, diffusion, general FEA/CFD, design revision | `cad-fem-router` -> `general-fem` |
| T-junction, GelMA/oil, droplets, flow-focusing, chip flow/transport | `chip-simulation-router` -> `microfluidic-cfd` |
| Electrokinetics or other special PDE branch | `chip-simulation-router` or `cad-fem-router` -> `microfluidic-special-physics` |
| Existing XDMF/VTK, ParaView render, video, field evidence | `result-render-router` -> `result-verification` |
| Analysis bundle to HTML/Markdown/PPTX | `simulation-report-router` -> `simulation-report` |

Do not load every backend skill before the branch is known. Keep solver-specific instructions behind the selected route.

## Tool bridge boundary

- CLI is the default deterministic path.
- MCP is optional and should be requested for live Fusion 360 state, GUI/session interaction, or an explicitly interactive tool.
- FreeCAD, Blender, FEniCS, NGSolve, OpenFOAM, ParaView, and Unity remain independent backend capabilities.
- A missing solver or MCP bridge must yield a `blocked` or `partial` `RunSummary`, not an invented result.

## Completion

Return a `RunSummary` and, when interpretation or rendering is requested, an `EvidenceReport`. Preserve input/output paths, metrics, assumptions, known limits, verification state, and one next minimal action. Keep outputs under `outputs/`; research results under `outputs/research/<YYYY-MM>/`; never create `03-research/` or `outputs/outputs/`.

Read `references/backend-routing.md` and `references/verification-rules.md` when the request is a real run rather than a simple route question.
