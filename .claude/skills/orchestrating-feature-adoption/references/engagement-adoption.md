# Engagement & Adoption

## When to use
Measuring and improving how visitors interact with a new feature after initial discovery — tracking usage, encouraging repeat use, and identifying drop-off points.

## Patterns

### 1. Analytics touchpoints via `lib/analytics.ts`
Every interactive feature should fire an event through the existing `sendEvent` utility. ThemeToggle already tracks preference changes; new tools (calculators, comparisons, FAQ accordions) should follow the same pattern.

```tsx
import { sendEvent } from "@/lib/analytics";

// Track a calculator interaction
sendEvent({
  event: "calculator_used",
  label: "electricity-rate-calculator",
  value: calculatedSavings,
});
```

The payload structure (`event`, `label`, `value`, `path`, `timestamp`) is already standardized — reuse it consistently so events are queryable in your analytics backend.

### 2. Related content nudges via `lib/posts.tsx`
The `getRelatedPosts` and `getNextReads` functions already drive the "You might also like" section rendered by `components/RelatedPosts.tsx` in `app/blog/[slug]/page.tsx`. When introducing a new feature tied to specific content (e.g., a gas rate comparison tool), ensure the related-posts logic surfaces those articles to drive tool adoption organically.

### 3. Sticky feature visibility through component persistence
Features that need repeated engagement (like dark mode) persist via `localStorage`. ThemeToggle stores its state under the `upe-theme` key and reads it on hydration with a system-preference fallback. Replicate this pattern for any user preference feature.

## Pitfalls
- **Don't add analytics events without a clear question to answer.** "Feature X was clicked 200 times" is useless without context — pair every event with a conversion goal (did the user finish the calculation? did they click a related article afterward?).
- **Avoid adding engagement prompts mid-article.** The ReadingProgress component in `[slug]/page.tsx` is the only acceptable mid-page UI element. Everything else belongs above or below the article content.