# Activation & Onboarding

## When to use

When a first-time visitor lands on Utility Explained and needs immediate value — finding the right guide without hunting through categories.

## Patterns

### Dismissible welcome banner on homepage
Render a full-width banner on `app/page.tsx` asking "Which utility bill are you trying to understand?" with four category links (`/electricity-explained`, `/gas-explained`, `/water-explained`, `/heating-cooling-explained`). Mark dismissal in `localStorage` under key `ue_welcome_dismissed`. Gate the banner behind a `"use client"` wrapper (`components/WelcomeBanner.tsx`) that reads the flag on mount and conditionally renders.

```tsx
const DISMISSED_KEY = "ue_welcome_dismissed";
// In useEffect: if (localStorage.getItem(DISMISSED_KEY)) return;
// On dismiss: localStorage.setItem(DISMISSED_KEY, "1");
```

### Smart default homepage content
When the welcome banner is dismissed (returning visitor), rotate the hero section to surface trending or seasonal content instead — e.g., "Why is my electric bill so high in summer?" links during June–September. Pull seasonal slugs from `lib/posts.tsx` by category tag. This requires no state — just a server component with date-based logic.

### Entry-point detection via URL params
On blog post pages (`app/[slug]/page.tsx`), check `searchParams` for a `ref` value (e.g., `?ref=google-ads`, `?ref=landing`). When `ref` is present and `localStorage.getItem("ue_first_visit")` is null, show a one-time "New here? Start with our [category] overview" banner linking back to the relevant pillar page. This catches search-referred first-timers without blocking content.

## Pitfalls

- **Do not block content behind a wizard.** This is an SEO-reliant static site — every page must be fully crawlable. Any multi-step flow must be a client-side overlay, never a gate.
- **`localStorage` is per-origin and synchronous.** Reading it on every page load is fine at this scale, but avoid writing on every render — only write on explicit user action (dismiss, skip).