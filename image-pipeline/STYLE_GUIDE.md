# Style Guide

## Visual direction

- Photorealistic, situational scenes tied to the page topic.
- Natural light, believable context, no staged studio setups.
- People are optional; if present, keep expressions neutral and candid.
- No text, no UI, no screens, no logos, no product packaging.
- Avoid symmetry and repeated compositions.

## Prompt template (used by 02_refine_prompts.py)

```
Photorealistic scene in a real environment, grounded in the topic:
{topic}

Composition and realism rules:
- Natural lighting, realistic perspective, and credible materials.
- No text or typography in the scene.
- No screens, UI, logos, or branding.
- No ad-like or misleading button visuals.
- Avoid centered symmetry; use organic framing.
- Avoid repeated compositions across slots.

Camera:
- 35mm lens equivalent, shallow-to-moderate depth of field.
- Horizontal framing unless the slot is explicitly vertical.
```

Market localization rules can be injected when a country is detected or set in config.
