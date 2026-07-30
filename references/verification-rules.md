# Verification and evidence rules

## Required framing

Important tasks must record:

- problem description
- problem type: `WHY`, `HOW`, or `MIX`
- core goal
- current gap
- smallest useful model
- current action
- next minimal action

For `MIX`, split interpretation from execution before changing geometry or solver settings.

## Evidence levels

| Evidence | Meaning | Allowed claim |
| --- | --- | --- |
| Direct solver evidence | Mesh-backed fields, logs, metrics, and saved case | Report the computed result with assumptions |
| Visual evidence | ParaView screenshots or time sequence tied to source fields | Describe visible morphology or field pattern |
| Proxy / normalized interpretation | Reduced model, normalized metric, or interpolation | Label as proxy; do not call it a physical measurement |
| Validation evidence | Experiment, benchmark, or external reference comparison | State what was compared and what remains unvalidated |

For VOF droplet claims, require both a visual sequence and connected-component analysis for `alpha.water > 0.25` and `alpha.water > 0.5`. Interpolated frames are visualization smoothing, not new physical evidence.

## Status rules

- `ok`: requested branch ran and required artifacts exist.
- `partial`: some requested artifacts or verification gates are missing; list them.
- `blocked`: a required solver, MCP bridge, input geometry, or boundary contract is unavailable.

Never convert `blocked` to `ok` by substituting a different physics model without recording that change in `assumptions` and `known_limits`.

## Output paths

- General outputs: `outputs/<branch>/<date>/`.
- Research outputs: `outputs/research/<YYYY-MM>/<project>/`.
- Never create a top-level `03-research/` or nested `outputs/outputs/`.
- Preserve input paths, output paths, logs, metrics, assumptions, and verification state in the `RunSummary`.
