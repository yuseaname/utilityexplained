# Policy Guardrails

The pipeline enforces the following rules:

- OpenAI Images API only; the only allowed model is `gpt-image-1`.
- No ads-like visuals, no deceptive UI, no misleading button imagery.
- No text overlays inside images.
- No UI, screens, logos, or brand marks.
- No stock-photo symmetry or repeated composition patterns.
- Avoid CLS/LCP regressions: include width/height or aspect-ratio wrappers.
- Inline images are lazy-loaded; hero images may be eager with `fetchpriority=high`.
- Placement is plan-only by default; HTML edits require `--apply`.
