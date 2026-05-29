# Product Analytics

## When to use

When you need to measure whether onboarding flows are actually working — are visitors finding the right content, completing checklists, or bouncing from the homepage?

## Patterns

### Page-level entry and exit tracking
The site already has a custom analytics module (`lib/analytics.ts`). Extend it to fire events at key onboarding moments:

- `onboarding_banner_seen` — when WelcomeBanner renders (not dismissed)
- `onboarding_banner_dismissed` — when visitor clicks "Don't show again"
- `onboarding_category_selected` — when visitor clicks a category link from the banner
- `checklist_step_completed` — when a checklist item is checked, with `{ post, step }` payload

```tsx
trackEvent("onboarding_category_selected", { category: "electricity", source: "welcome_banner" });
```

### Content funnel via URL params
Append `?ref=onboarding` to links within onboarding components. This lets you segment traffic in analytics: visitors who arrived via the welcome banner vs. organic search. Process these params server-side in `app/[slug]/page.tsx` metadata or client-side in `analytics.ts`.

### `localStorage`-based cohort detection
On first visit (no `ue_first_visit` key), set a timestamp. On subsequent visits, calculate days-since-first-visit to build crude cohort segments: new (0–1 day), returning (2–7), loyal (8+). Use this to segment onboarding engagement without requiring user accounts.

## Pitfalls

- **`localStorage` is not sent to the server.** You cannot use it in `generateStaticParams` or `metadata` exports. All localStorage-dependent logic must live in `"use client"` components, and analytics events must fire from the client.
- **Don't over-instrument.** For a content site with modest traffic, track 4–5 key events max. Anything more creates noise without actionable signal.