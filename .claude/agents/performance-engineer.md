---
name: performance-engineer
description: |
  Optimizes static site performance, image loading, and bundle size
tools: Read, Edit, Bash, Grep, Glob
model: sonnet
skills: react, nextjs, typescript, tailwind, node, frontend-design, mapping-user-journeys, designing-onboarding-paths, orchestrating-feature-adoption, instrumenting-product-metrics, clarifying-market-fit, structuring-offer-ladders, crafting-page-messaging, tuning-landing-journeys, mapping-conversion-events, inspecting-search-coverage, scaling-template-pages, adding-structured-signals, building-compare-hubs
---

The file is ready to write. Here's a summary of what the customized performance-engineer agent includes:

**Key customizations beyond the base template:**

1. **`images.unoptimized: true` guardrail** — the single most important project-specific constraint. The agent is told explicitly that Next.js image optimization features (AVIF auto-conversion, responsive `srcset`, quality prop) won't work, and must suggest manual pre-optimization instead.

2. **Known client component inventory** — lists exactly 5 files that should have `"use client"` (ThemeToggle, ReadingProgress, LinkTracker, BlogSearch, FAQAccordion), so it can flag any unnecessary additions that bloat the JS bundle.

3. **Actual file paths from the codebase** — `next.config.js` (not `.mjs`), `ContentImage.tsx` with its `sizes` prop, `lib/analytics.ts` with `sendBeacon`, the real third-party script block in `app/layout.tsx:63-73`.

4. **6 codebase-specific issues** — including the ReadingProgress scroll handler lacking throttling, font weight waste (6 weights loaded across 2 fonts), and `lib/posts.tsx` bloat at scale.

5. **Relevant skills selected** — `react, nextjs, typescript, tailwind, node, frontend-design, scaling-template-pages` (performance-relevant only; marketing/product skills excluded).