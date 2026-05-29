# Feedback & Insights

## When to use
Collecting and interpreting visitor feedback on new features — deciding what signals matter, how to capture them, and how to act on the results.

## Patterns

### 1. Implicit feedback through existing analytics
The primary feedback channel is behavioral data from `lib/analytics.ts`. Track feature usage patterns rather than asking for explicit ratings:
- **FAQAccordion expansions** reveal which questions visitors have
- **ThemeToggle state** reveals dark mode adoption (already tracked via localStorage `upe-theme`)
- **RelatedPosts clicks** reveal content gaps — if visitors consistently leave via a specific related link, the current article may not fully answer their question
- **ReadingProgress abandonment points** (via the scroll tracker) reveal where articles lose readers

### 2. Low-friction explicit feedback via component
For features that need direct input (e.g., "Was this calculator helpful?"), add a simple thumbs-up/thumbs-down or star rating directly below the component. No forms, no email collection, no login gates. Track the response via `sendEvent`.

```tsx
<button onClick={() => sendEvent({ event: "feedback", label: "calculator-helpful", value: 1 })}>
  Helpful
</button>
```

### 3. Content gap identification from search and navigation
Use Google Search Console data (already configured via `app/robots.ts` and sitemap) to identify queries that lead to the site but don't have matching content. Pair with `getRelatedPosts` behavior — if visitors land on a post and don't click any related article, the content cluster may be incomplete.

## Pitfalls
- **Don't add feedback widgets that require third-party services.** No Hotjar, no SurveyMonkey, no Typeform embeds. All feedback must work within the static-export architecture — localStorage + sendBeacon or a simple HTML form that posts to a static endpoint.
- **Avoid survey fatigue.** One feedback prompt per feature, placed below the feature itself, never in a pop-up or floating widget. Visitors are here to read about utility bills, not to rate your UI.