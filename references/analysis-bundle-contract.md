# Analysis bundle bridge

The existing `simulation-analysis` skill remains a compatibility producer for solver-specific bundles. The portable studio treats its bundle as a `RunSummary` extension rather than a separate reasoning layer.

Minimum bridge fields:

```json
{
  "analysis_title": "...",
  "analysis_slug": "...",
  "analysis_branch": "general-fem or microfluidic-cfd",
  "package_root": "/abs/path",
  "summary_json_path": "/abs/path/summary.json",
  "primary_figure_paths": [],
  "animation_paths": {},
  "keyframe_paths": [],
  "key_metrics": {},
  "assumptions": [],
  "known_limits": [],
  "verification_status": "partial"
}
```

When this bridge is consumed by `simulation-reporting`, the report layer must preserve the upstream `assumptions`, `known_limits`, and `verification_status`. It may add presentation metadata, but it must not add solver claims.
