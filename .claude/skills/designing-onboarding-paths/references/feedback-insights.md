# Feedback & Insights

## When to use

When you need to understand why visitors bounce, which onboarding paths work, and what content gaps exist — without adding a full feedback widget or survey tool.

## Patterns

### Implicit feedback via reading depth
Track scroll depth on blog posts using a passive `IntersectionObserver` in a `"use client"` wrapper. Fire a single `article_read_depth` event when the visitor crosses 75% scroll, with the post slug. Posts with low read-depth but high entry traffic are candidates for onboarding improvements — visitors are arriving but the content isn't meeting their intent.

### Content gap detection from 404 paths
Add a simple `app/not-found.tsx` page that logs the attempted URL to analytics (`404_attempted_path`). Cluster these logs monthly — repeated paths like `/solar-panel-cost` or `/how-to-read-water-meter` indicate content visitors expect but don't exist, guiding the editorial roadmap.

### Post-rating micro-survey at article end
At the bottom of each `[slug]/page.tsx`, render a lightweight "Did this help?" component (`components/ArticleFeedback.tsx`) with three options: "Yes", "Somewhat", "No". Store results in `localStorage` as a batch and flush to the analytics endpoint periodically. No backend needed — aggregate client-side data in analytics.

```tsx
const FEEDBACK_KEY = `ue_feedback_${post.slug}`;
// Prevent repeat feedback: check key before rendering buttons
```

## Pitfalls

- **404 tracking via analytics is retrospective, not real-time.** You won't catch content gaps instantly — plan to review 404 logs on a weekly or monthly cadence.
- **`localStorage`-based feedback is siloed per device.** You cannot aggregate it server-side without a collection endpoint. Accept this as directional signal, not statistically rigorous data — use it to prioritize, not to prove.
=====