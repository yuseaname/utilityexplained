---
name: orchestrating-feature-adoption
description: Plans feature discovery, nudges, and adoption flows for the Utility Explained static site.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Orchestrating Feature Adoption Skill

Guides the introduction of new site features—dark mode, related posts, interactive tools, ads—by planning how visitors discover, understand, and adopt them without disrupting the reading experience.

## Quick Start

Invoke when adding a new user-facing feature to the site. Assess current navigation and component structure, then produce a lightweight adoption plan covering placement, progressive disclosure, and any analytics hooks needed to measure uptake.

## Key Concepts

- **Progressive disclosure** — Introduce features inline (e.g., ThemeToggle in the header) rather than as pop-ups or modals that interrupt article reading.
- **Content-first surfaces** — New features must not displace or clutter pillar pages or blog content; use component slots (AdSlot, sidebar, footer) for non-content UI.
- **Static-safe** — All adoption flows must work without client-side routing or runtime state beyond what React hydration provides. No API calls at runtime.
- **Analytics touchpoints** — Use the existing `lib/analytics.ts` tracking to measure feature interactions (toggle usage, tool clicks, FAQ expansions).

## Common Patterns

| Scenario | Approach |
|----------|----------|
| New toggle or preference | Add to `components/ThemeToggle.tsx` pattern — place in header, persist via `localStorage`, no server dependency |
| Inline interactive tool (calculator, comparison) | Build as a standalone component in `components/`, embed within relevant blog post or pillar page via `[slug]/page.tsx` |
| Content recommendation nudge | Extend the related-posts logic in `lib/posts.tsx`; render as a "You might also like" section below article content |
| Ad placement change | Modify `components/AdSlot.tsx` props and slot IDs; keep ad positions outside the main article flow |
| Onboarding tooltip or banner | Client-only component rendered in `app/layout.tsx`; gate behind a `localStorage` flag so it shows once and dismisses |