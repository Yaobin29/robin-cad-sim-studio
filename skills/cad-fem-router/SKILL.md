---
name: cad-fem-router
description: Load when a CAD, mesh, FEM/FEA, general CFD, or design-revision request needs routing from geometry to a solver and verification path.
---

# CAD/FEM router

Create a `RoutePlan` before loading a leaf tool.

| Need | Route |
| --- | --- |
| Parametric engineering CAD or STEP/STL/FCStd | `freecad-cli` or `cad-fem-design-loop` |
| Organic or visual 3D concept | `blender-cli` |
| NGSolve/Netgen mesh or FEM | `ngsolve-cli` |
| FEniCS/FEniCSx special physics | `fenics-cli` and, when needed, the `general-fem` verification path |
| Routine microfluidic flow or passive transport | hand off to `chip-simulation-router` and OpenFOAM |
| ParaView post-processing | `result-render-router` and `paraview-cli` |

Keep `robin-cad-fem-cli` as the low-level CLI selector. Do not merge its leaf skills into this router: selection, execution, and evidence review are separate responsibilities.

The route must record geometry reuse or creation, mesh handoff, solver choice, verification gate, output root, and fallback policy. If a runtime is unavailable, return `blocked` with the missing command and the smallest recovery action.
