---
name: mapping-conversion-events
description: Defines funnel events, tracking, and success signals for measuring reader-to-visitor conversion on Utility Explained
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Mapping Conversion Events Skill

Maps the reader journey from landing to meaningful engagement on Utility Explained by defining conversion events, funnel stages, and success signals. Builds on the existing `trackEvent` infrastructure in `lib/analytics.ts` and the event delegation in `LinkTracker` to identify where visitors drop off and what behaviors signal high intent.

## Quick Start

1. Review current instrumented events in `lib/analytics.ts` (`TrackPayload` shape) and existing call sites (`FAQAccordion`, `LinkTracker`, `PostCard`).
2. Identify the conversion goal (e.g., deep article read, return visit, ad engagement).
3. Define the funnel stages and the events that mark entry, progression, and completion for each stage.
4. Ensure components along the funnel fire `trackEvent` with descriptive names, consistent labels, and differentiating values.

## Key Concepts

### Conversion Hierarchy

For a content/ad-supported site like Utility Explained, conversions are layered:

| Level | Signal | Why it matters |
|-------|--------|----------------|
| **Page land** | First pageview in a session | Top of funnel — content found via search or external link |
| **Content engagement** | Scroll depth, FAQ expand, time on page | Reader is consuming content, not bouncing |
| **Content progression** | Click to a second article (next-read, related, blog-search) | Reader trusts the site and wants more — strongest engagement signal |
| **Return visit** | Session with referrer = utilityexplained.com | Retained reader, highest lifetime value for ad revenue |

### Existing Events as Funnel Markers

| Funnel Stage | Event | Source Component |
|--------------|-------|-----------------|
| Land | `internal_link_click` (label: `blog-page`, `blog-category`, `post-card`) | `PostCard`, `LinkTracker` |
| Engage | `faq_expand` | `FAQAccordion` |
| Progress | `internal_link_click` (label: `next-read`, `related`) | `RelatedPosts`, `LinkTracker` |
| Search | `internal_link_click` (label: `blog-search`) | `BlogSearch` + `PostCard` |

### Reading Progress (uninstrumented)

`ReadingProgress` computes scroll depth but does **not** fire `trackEvent`. This is a gap — scroll milestones (25%, 50%, 75%, 100%) are high-value engagement signals that should be wired up to mark the "Engage" stage.

## Common Patterns

### Defining a conversion funnel for a pillar page

1. **Entry** — User arrives at `/electricity-explained` (tracked via navigation click or direct landing).
2. **Engagement** — User scrolls past 50% or expands an FAQ.
3. **Conversion** — User clicks through to a specific blog post from the pillar page.

Query the event stream for sessions where `path` matches the pillar, an engagement event fires within 60 seconds, and an `internal_link_click` follows within the same session.

### Adding scroll-depth tracking to ReadingProgress

Wire scroll milestones into the existing `ReadingProgress` component by firing `trackEvent` at percentage thresholds:

```tsx
const thresholds = [25, 50, 75, 100];
const fired = useRef(new Set<number>());

// Inside onScroll:
for (const t of thresholds) {
  if (value >= t && !fired.current.has(t)) {
    fired.current.add(t);
    trackEvent({ event: "scroll_depth", value: t, label: postSlug });
  }
}
```

### Measuring search-to-read conversion

Track sessions where a user both interacts with `BlogSearch` (filter or text input) and subsequently clicks a result. The `PostCard` inside `BlogSearch` already passes `trackingLabel="blog-search"`, so an `internal_link_click` with that label after search interaction counts as a search conversion.

### Success signal: activated reader

An activated reader is a session containing both:
1. A `scroll_depth` event with `value: 75` or higher on any blog post path, **and**
2. An `internal_link_click` with label `next-read` or `related` within the same session.

This combination indicates the reader consumed substantial content and chose to continue exploring — the closest proxy to "conversion" on an ad-supported content site.
