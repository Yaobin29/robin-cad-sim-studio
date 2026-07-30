---
name: chip-simulation-router
description: Load when the user asks for microfluidic chip simulation, T-junction or flow-focusing droplets, GelMA/oil transport, a chip STEP route, or OpenFOAM plus FEniCS special physics.
---

# Microfluidic router

This is a route selector, not a solver. For routine flow and passive transport choose `microfluidic-cfd` and OpenFOAM. For electrokinetics or another explicitly special PDE choose `microfluidic-special-physics` and FEniCS/FEniCSx. Do not silently replace one with the other.

## Input routes

1. Fluid-domain `STEP` + boundary spec -> mesh -> OpenFOAM.
2. Chip-solid `STEP` from Fusion 360 or FreeCAD + boundary spec -> extract fluid domain -> mesh -> OpenFOAM.
3. Supported template -> use the template runner -> OpenFOAM.
4. Transient two-phase droplet request -> OpenFOAM VOF, `alpha.water` evidence, and connected-component analysis.
5. Web submission or server workflow -> route to the project web app; the browser never runs CFD directly.

The current T-junction preset is in the legacy/runtime template library. Preserve its evidence thresholds (`alpha.water > 0.25` and `> 0.5`) and treat interpolated frames as visualization only.

## Required output

Record `TaskBrief`, `RoutePlan`, `RunSummary`, and, for claims about droplet formation or design quality, `EvidenceReport`. Include boundary-condition assumptions, mesh/solver status, pressure/velocity/transport metrics, source fields, and a next parameter or geometry action.
