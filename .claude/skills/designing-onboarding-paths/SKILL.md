---
name: designing-onboarding-paths
description: Designs onboarding paths, checklists, and first-run UI for guiding new visitors through Utility Explained content.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Designing Onboarding Paths Skill

Creates structured onboarding flows that help first-time visitors to Utility Explained find the right utility guide quickly. Works with the existing App Router routes, component library, and static content architecture to build progressive disclosure patterns — welcome banners, category wizards, and step-by-step checklists — without adding runtime dependencies.

## Quick Start

1. Identify the target audience segment (new homeowner, renter, bill troubleshooter) and their entry points.
2. Audit existing routes under `app/` and content categories in `lib/posts.tsx` to map the onboarding journey.
3. Design the path as a sequence of existing pillar pages and blog posts connected by progressive UI cues.
4. Implement onboarding components in `components/` following the project's PascalCase naming and Tailwind styling conventions.

## Key Concepts

- **Progressive disclosure**: Reveal information in steps rather than overwhelming visitors. Start with the utility category (electricity, gas, water) then narrow to their specific concern (high bill, understanding charges, reducing usage).
- **Entry point mapping**: Different visitors arrive with different intents — some from search (specific question), some from the homepage (general curiosity). Onboarding must branch accordingly.
- **Static-friendly patterns**: Since this is a statically exported site (`output: 'export'`), onboarding state must use client-side only mechanisms — `localStorage`, URL search params, or cookie flags — no server-side session storage.
- **Content-driven paths**: Onboarding is anchored to real content. Every step should link to an existing post or pillar page, not placeholder content. Check `lib/posts.tsx` for the full post catalog.
- **Accessibility first**: All onboarding UI must include skip links, proper ARIA labels, and keyboard navigation per the project's existing accessibility standards.

## Common Patterns

### Welcome banner with category selection
A dismissible hero section on the homepage that asks "Which utility bill are you trying to understand?" with links to `/electricity-explained`, `/gas-explained`, `/water-explained`, and `/heating-cooling-explained`. Persist dismissal in `localStorage` so returning visitors see the homepage directly.

### Troubleshooting checklist flow
A step-by-step card component for posts like "electric-bill-spike" or "water-bill-too-high" that walks visitors through: read your meter → check your rate plan → compare to averages → contact your provider. Each step links to a relevant section or related post.

### First-visit category wizard
A multi-step client component (use `"use client"`) that asks 2-3 questions (rent or own? which utility? what's the problem?) then navigates to the most relevant pillar page or blog post. Use URL params or component state — no backend needed.

### Inline onboarding tooltips
Contextual hints on pillar pages that explain unfamiliar terms (kWh, therm, CCF) by linking to `/utilities-glossary`. These are static JSX elements, not interactive widgets — keeping the build fully static.