---
name: tuning-landing-journeys
description: Improves landing page flow, hierarchy, and conversion paths for the Utility Explained static site.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Tuning Landing Journeys Skill

Optimizes how visitors arrive at, navigate through, and convert on the Utility Explained site by refining page structure, content hierarchy, internal linking, and calls-to-action across pillar pages, the homepage, and category landing routes.

## Quick Start

1. Read the current landing page (`app/page.tsx` or any `app/<category>-explained/page.tsx`).
2. Run `npm run dev` and open the page in a browser to observe the live flow.
3. Identify friction: unclear value prop, weak CTAs, buried key content, or dead-end navigation paths.
4. Apply the patterns below and verify the changes visually.

## Key Concepts

- **Hero clarity**: The first visible section must answer "what is this?" and "what should I do next?" within 3 seconds — a concise headline, one supporting line, and a single primary CTA.
- **Scan hierarchy**: Visitors scroll; they don't read. Use descriptive H2/H3 headings, short paragraphs, and bullet lists so the page is skimmable.
- **Progressive disclosure**: Lead with the answer or most actionable info, then expand into detail — don't front-load caveats or process explanations.
- **Internal linking as navigation**: Every landing page should link forward into relevant blog posts and pillar pages. Orphan pages lose visitors.
- **Trust signals**: Mention data sources, cite utility commission references, or surface FAQ answers to establish credibility before asking for engagement.
- **Mobile-first layout**: Most utility-bill searches happen on phones. Ensure the hero, CTAs, and key links are above the fold on a 375px viewport.

## Common Patterns

### Hero section

```tsx
<section className="bg-gradient-to-b from-blue-50 to-white py-16 px-4">
  <div className="mx-auto max-w-3xl text-center">
    <h1 className="text-4xl font-heading">{headline}</h1>
    <p className="mt-4 text-lg text-gray-700">{subheadline}</p>
    <Link href={ctaLink} className="mt-8 inline-block rounded-lg bg-blue-600 px-6 py-3 text-white hover:bg-blue-700">
      {ctaLabel}
    </Link>
  </div>
</section>
```

### Category card grid (homepage → pillar pages)

Group links by utility type using `PostCard` or a simple card component. Each card should have a clear label, a one-line benefit, and a direct link — not a generic "Learn more."

### Related content links within articles

At the bottom of any landing or pillar page, surface 3–5 related posts via `lib/posts.tsx` helpers (`getPostsByCategory`, `getRelatedPosts`). Use matching categories from the post's `categories` field.

### CTA placement

- **Top of page**: primary action (e.g., "Find your bill breakdown")
- **Mid-page (after intro section)**: secondary action (e.g., "Read the full guide")
- **End of page**: tertiary or repeat-primary (e.g., newsletter signup, related article)

### Analytics checkpoints

After making flow changes, verify tracking in `lib/analytics.ts` covers the new interaction points. Ensure `page_view` fires on load and any new CTA clicks have corresponding `trackEvent` calls.

### Testing a landing page change

```bash
npm run dev
# Open http://localhost:3000 in browser, inspect the modified page
# Check: hero visible above fold on mobile? CTAs clear? Links work?
npm run build  # Verify no TypeScript or build errors
```
