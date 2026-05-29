---
name: designer
description: |
  UI/UX specialist for Tailwind CSS styling, responsive design, and accessibility
tools: Read, Edit, Write, Glob, Grep
model: sonnet
skills: react, nextjs, typescript, tailwind, node, frontend-design, mapping-user-journeys, designing-onboarding-paths, orchestrating-feature-adoption, instrumenting-product-metrics, clarifying-market-fit, structuring-offer-ladders, crafting-page-messaging, tuning-landing-journeys, mapping-conversion-events, inspecting-search-coverage, scaling-template-pages, adding-structured-signals, building-compare-hubs
---

The file write needs your approval. Here's what I've prepared:

**Customized designer subagent** at `.claude/agents/designer.md` with:

- **Skills**: `react, tailwind, frontend-design, tuning-landing-journeys, designing-onboarding-paths, mapping-user-journeys`
- **Tools**: All available Read/Edit/Write/Glob/Grep plus all vision MCP tools (`ui_diff_check`, `ui_to_artifact`, `diagnose_error_screenshot`, etc.)
- **Model**: sonnet

**Key customizations over the generic template:**

1. **Design system reference** — Full color token tables for both light/dark modes (teal accent palette, warm beige backgrounds)
2. **Typography mapping** — Fraunces for headings, IBM Plex Sans for body, with weight specifications
3. **Layout constants** — Container width (`min(1120px, 92vw)`), radius (`18px`), padding scales, grid patterns
4. **Styling approach** — Documents the hybrid CSS custom properties + Tailwind pattern this project uses (tokens in `globals.css`, Tailwind for layout)
5. **Component patterns** — Cards, buttons, header, and image conventions with actual values
6. **File locations table** — Quick reference to `globals.css`, `layout.tsx`, key components
7. **WCAG contrast reference** — Pre-computed ratios for existing color pairs
8. **Dark mode rules** — `data-theme` attribute approach, localStorage persistence
9. **Vision tool integration** — Instructions for using `ui_diff_check` and `ui_to_artifact` in the design workflow