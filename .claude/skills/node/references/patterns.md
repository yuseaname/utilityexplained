# Node.js Patterns

## When to use

Refer here when adding dependencies, writing scripts, creating components/routes, or configuring the build pipeline for this Next.js 14 static site.

## Pattern: Adding a new blog post

Posts live as `Post` objects inside `lib/posts.tsx` (manually curated) or in `lib/generatedPosts/` (AI pipeline). Every post must conform to the `Post` type from `lib/types.ts`. The build uses `generateStaticParams` in `app/blog/[slug]/page.tsx` to pre-render all slugs.

```typescript
// lib/posts.tsx — posts array entry
{
  slug: "my-new-article",
  title: "Why Is My Water Bill So High?",
  description: "Short meta description for SEO.",
  category: "Water",
  keyword: "water bill high",
  date: "2026-01-15",
  readTime: "8 min read",
  image: { src: "/images/utility-water.jpg", alt: "..." },
  sections: [{ id: "quick-answer", title: "...", content: <p>...</p> }],
  faqs: [{ question: "...", answer: "..." }],
  relatedSlugs: ["other-article-slug"],
}
```

## Pattern: Adding a new page route

Create `page.tsx` inside the appropriate `app/` subdirectory. Export a default component. For static metadata, export a `metadata` constant; for dynamic metadata, export `generateMetadata`.

```typescript
// app/new-page/page.tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "New Page",
  description: "Page description",
};

export default function NewPage() {
  return <div>Content</div>;
}
```

## Pattern: Adding a shared component

Create a `.tsx` file under `components/` with a PascalCase default export. Import using the `@/` path alias. Avoid `"use client"` unless the component needs interactivity (state, effects, event handlers).

```typescript
// components/MyComponent.tsx
export default function MyComponent({ children }: { children: React.ReactNode }) {
  return <div className="my-component">{children}</div>;
}
```

## Pitfall: `output: 'export'` constraints

The `next.config.js` sets `output: 'export'`, which means:
- No API routes (`app/api/`) — they are silently ignored in static exports.
- No `revalidate`, `redirect()`, or `notFound()` in middleware (the project uses `notFound()` in page components, which is fine).
- No server-side features requiring a Node runtime at request time (ISR, middleware).
- Images must use `unoptimized: true` (already configured) since the static export has no image optimization server.
- `next/image` `priority` works for preloading, but `sizes` should still be set for responsive behavior.