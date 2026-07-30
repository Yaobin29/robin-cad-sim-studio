# Backend routing

## Branch selection

| Branch | Use for | Preferred backend | Fallback |
| --- | --- | --- | --- |
| `general-fem` | CAD-to-mesh, elasticity, diffusion, special PDEs | `fenics-agent` or `ngsolve-agent` | reduced-order estimate with explicit limits |
| `microfluidic-cfd` | routine laminar flow, passive transport, VOF droplets | `openfoam-agent` | `blocked` if runtime or geometry contract is missing |
| `microfluidic-special-physics` | electrokinetics, coupled or unusual PDE branches | `fenics-agent` | do not silently replace with single-phase OpenFOAM |
| `result-verification` | XDMF/VTK inspection, field checks, screenshots, video | `paraview-agent` | metadata-only inspection with `verification_status=partial` |
| `simulation-report` | consume an analysis bundle for HTML/Markdown/PPTX | `simulation-reporting` | Markdown-only package when presentation tooling is absent |

## Tool bridge policy

1. The skill layer selects a branch and records a `RoutePlan`.
2. The CLI bridge is the default deterministic execution path.
3. MCP is requested only for live Fusion 360 state, GUI/session interaction, or an explicitly interactive bridge.
4. A backend may return `ok`, `partial`, or `blocked`; the adapter must preserve this state.
5. The top-level studio should never hide a missing solver behind a proxy result.

## Compatibility names

These names remain valid during migration but are not new canonical entry points:

- `cad-fem-design-loop` -> `robin-cad-sim-studio` -> `cad-fem-router`
- `fenics-paraview-workflow` -> `general-fem` or `result-verification`
- `openfoam-fenics-hybrid-workflow` -> `microfluidic-cfd` plus `microfluidic-special-physics`
- `microfluidic-openfoam-analysis` -> `microfluidic-cfd`
- `simulation-analysis` -> shared `RunSummary` / analysis-bundle producer
- `simulation-reporting` -> `simulation-report` consumer; it remains separate from solving

The low-level `robin-cad-fem-cli` router and its leaf CLI skills are retained because selection and execution are different responsibilities.
