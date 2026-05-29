---
name: instrumenting-product-metrics
description: Defines product events, funnels, and activation metrics for the Utility Explained site
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Instrumenting Product Metrics Skill

Instruments user behavior across the Utility Explained site by defining tracked events, wiring them into components, and mapping them to funnels and activation metrics. The site uses a custom `trackEvent` system (`lib/analytics.ts`) that fires JSON payloads via `navigator.sendBeacon` to `NEXT_PUBLIC_EVENT_ENDPOINT`, with event delegation in `LinkTracker` and direct calls in interactive components like `FAQAccordion`.

## Quick Start

To add a new tracked event:

1. Call `trackEvent` from a `"use client"` component or the existing `LinkTracker` event delegation layer.
2. Use the `TrackPayload` shape: `{ event, label?, value?, href?, extra? }`.
3. For link clicks, add `data-track`, `data-track-label`, and `data-track-value` attributes to the `<a>` tag — `LinkTracker` picks these up automatically.
4. For non-link interactions (toggles, search, accordion), call `trackEvent` directly with a descriptive `event` name and relevant `label`/`value`.

## Key Concepts

### Event Payload Schema

```typescript
type TrackPayload = {
  event: string;          // e.g. "faq_expand", "internal_link_click"
  label?: string;         // human-readable context (question text, link source)
  value?: string | number; // slug, index, or numeric metric
  href?: string;          // destination URL (for link events)
  extra?: Record<string, string>; // arbitrary additional properties
};
```

`trackEvent` automatically appends `path` (current URL) and `ts` (ISO timestamp).

### Existing Instrumented Events

| Event | Source | Trigger |
|-------|--------|---------|
| `internal_link_click` | `LinkTracker` (delegation) | Click on any `<a data-track>` |
| `faq_expand` | `FAQAccordion` | User opens an FAQ answer |

Link clicks carry contextual labels from `trackingLabel` props (`next-read`, `related`, `blog-search`, `blog-page`, `blog-category`, `post-card`).

### Event Delivery

Events are sent via `navigator.sendBeacon` (preferred) with `fetch`+`keepalive` fallback. Delivery is fire-and-forget. The endpoint is configured via `NEXT_PUBLIC_EVENT_ENDPOINT` — if unset, all tracking is a no-op.

## Common Patterns

### Adding a tracked link

Wrap with existing `PostCard` `trackingLabel` or add data attributes directly:

```tsx
<a
  href="/blog/my-article"
  data-track="internal_link"
  data-track-label="cta-banner"
  data-track-value="my-article"
>
  Read more
</a>
```

### Tracking a new interaction

```tsx
"use client";
import { trackEvent } from "@/lib/analytics";

<button onClick={() => trackEvent({ event: "theme_toggle", value: isDark ? "dark" : "light" })}>
```

### Defining a reading funnel

Map page-level events to a content consumption funnel:

1. **Landing** — `internal_link_click` with label `blog-page` or `blog-category` (user found a post)
2. **Engagement** — `faq_expand` (user explored content depth)
3. **Progression** — `internal_link_click` with label `next-read` or `related` (user continued reading)

Track funnel drop-off by joining events on `path` and `ts` within a session window on the receiving endpoint.

### Activation metric

A reasonable activation signal for this content site is a user who reads a full article and clicks a related/next-read link within the same session. Instrument this by ensuring every blog post page has `RelatedPosts` rendered with the `trackingLabel="next-read"` path, then query the event stream for sessions containing both a `path` matching a blog slug and a subsequent `internal_link_click` with `label: "next-read"`.
