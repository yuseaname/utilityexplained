# Engagement & Adoption

## When to use

When visitors have found their first article but aren't exploring further — the goal is to surface related content and build a reading habit without resorting to aggressive prompts.

## Patterns

### Related-articles rail on blog posts
At the bottom of each `[slug]/page.tsx`, render a "Next steps" section using the post's `category` field from `lib/posts.tsx` to query 3–4 related posts. Use the existing `PostCard` component from `components/PostCard.tsx`. Order by relevance (same category first, then same `tags` overlap).

```tsx
const related = allPosts
  .filter(p => p.slug !== post.slug && p.category === post.category)
  .slice(0, 4);
```

### Reading progress checklist on troubleshooting posts
For posts tagged "troubleshooting" (e.g., `electric-bill-spike`, `water-bill-too-high`, `gas-bill-too-high`), render an inline checklist component (`components/ChecklistProgress.tsx`) that lets visitors tick off steps: "Read your meter", "Check your rate plan", "Compare to averages", "Contact your provider". Persist checked items in `localStorage` keyed by slug (`ue_checklist_{slug}`). This gives a tangible sense of progress without requiring an account.

### Seasonal content carousel on pillar pages
On the four main pillar pages (`/electricity-explained`, `/gas-explained`, `/water-explained`, `/heating-cooling-explained`), add a "Seasonal tips" section that swaps featured posts based on the current quarter. Server-side date logic — no client state needed. For example, Q3 surfaces "time-of-use-electricity" and cooling-related posts.

## Pitfalls

- **Avoid notification-style nudges.** There is no push system and adding one would conflict with the static-export architecture. Keep engagement within the page content itself (in-body suggestions, not popups).
- **Checklist state in `localStorage` does not sync across devices.** Design checklists as nice-to-have convenience, not critical data — a returning visitor on a new device simply sees an unchecked list.