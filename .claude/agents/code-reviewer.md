---
name: code-reviewer
description: |
  Reviews code quality, TypeScript patterns, and Next.js best practices
tools: Read, Grep, Glob, Bash
model: inherit
skills: react, nextjs, typescript, tailwind, node, frontend-design, mapping-user-journeys, designing-onboarding-paths, orchestrating-feature-adoption, instrumenting-product-metrics, clarifying-market-fit, structuring-offer-ladders, crafting-page-messaging, tuning-landing-journeys, mapping-conversion-events, inspecting-search-coverage, scaling-template-pages, adding-structured-signals, building-compare-hubs
---

It seems the write permission needs your approval. The file at `.claude/agents/code-reviewer.md` is ready to be written. Here's a summary of what the customized subagent includes:

**Key customizations from the base template:**

1. **Static export architecture guardrails** — flags `fetch()`, `getServerSideProps`, API routes, `headers()`/`cookies()` that violate `output: 'export'`
2. **`generateStaticParams` enforcement** — every dynamic route must export it with `dynamicParams = false`
3. **Actual file paths and component inventory** — all 17 components, full route tree with real paths like `app/blog/[slug]/page.tsx`
4. **Post data flow** — documents the `lib/generatedPosts/` → `lib/posts.tsx` → `normalizePostImage()` → pages pipeline
5. **SEO checklist** — `generateMetadata`, canonical URLs, JSON-LD schemas (`BlogPosting`, `FAQPage`, `BreadcrumbList`), heading hierarchy
6. **Image conventions** — Next.js `Image` with `sizes`, `/images/articles/{slug}/image.webp` paths, fallback heroes
7. **Analytics specifics** — `sendBeacon` in `lib/analytics.ts`, `LinkTracker`, `data-slot-id` attributes
8. **Security** — `NEXT_PUBLIC_*` boundary, `dangerouslySetInnerHTML` only for trusted JSON-LD, no OpenAI keys in committed code
9. **Relevant skills selected**: `react`, `nextjs`, `typescript`, `tailwind`, `frontend-design`
10. **Relevant MCP tools**: `webReader`, `web_search_prime`, `diagnose_error_screenshot`, `extract_text_from_screenshot`, `ui_diff_check`

Please approve the write permission and I'll save the file.