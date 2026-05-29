---
name: react
description: |
  Manages React components, hooks, and state patterns.
  Use when: implementing or refactoring React work, troubleshooting hooks, components, data fetching, or aligning new changes with the repository's existing conventions
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# React Skill

This fallback skill keeps React work aligned with the conventions already present in this repository. Prefer extending the closest existing implementation over inventing a new abstraction, and verify neighboring states before finishing.

## Quick Start

### Inspect the current implementation

```sh
rg -n "react|hooks|components|data-fetching" .
rg --files | rg "react|hooks|components"
```

### Make the smallest compatible change

- Reuse the closest existing component, hook, or route pattern before adding a new abstraction.
- Keep state, styling, and interaction logic in the same layer used by neighboring files.
- Prefer small, reviewable changes over broad rewrites of established UI structure.

### Verify before finishing

- Check responsive behavior and the primary interactive states affected by the change.
- Verify empty, loading, error, and disabled states if the surface exposes them.
- Confirm accessibility basics still hold: labels, focus states, semantics, and contrast.

## Key Concepts

| Concept | Why it matters | What to check |
|---------|----------------|---------------|
| Existing patterns | Keeps the repo coherent | Start from the nearest matching implementation before editing |
| Scope control | Prevents abstraction creep | Keep the change in the same layer as surrounding code |
| Verification | Catches regressions early | Recheck adjacent states, edge cases, and integration points |
| References | Speeds up repeat work | Use the linked topic files when the task needs deeper guidance |

## Common Patterns

### Hooks

**When:** The task touches hooks in React work.

- Inspect the nearest existing implementation before introducing a new pattern.
- Reuse naming, file placement, and helper utilities that are already established in this repo.
- Keep the change easy to review and easy to extend without widening scope unnecessarily.

### Components

**When:** The task touches components in React work.

- Inspect the nearest existing implementation before introducing a new pattern.
- Reuse naming, file placement, and helper utilities that are already established in this repo.
- Keep the change easy to review and easy to extend without widening scope unnecessarily.

### Data Fetching

**When:** The task touches data fetching in React work.

- Inspect the nearest existing implementation before introducing a new pattern.
- Reuse naming, file placement, and helper utilities that are already established in this repo.
- Keep the change easy to review and easy to extend without widening scope unnecessarily.

## See Also

- [Hooks](references/hooks.md)
- [Components](references/components.md)
- [Data Fetching](references/data-fetching.md)
- [State](references/state.md)
- [Forms](references/forms.md)
- [Performance](references/performance.md)