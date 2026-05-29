---
name: scaling-template-pages
description: Builds scalable, template-driven search and listing pages for Utility Explained using Next.js static generation, typed post data, and reusable components.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Scaling Template Pages Skill

Creates new template-driven pages (category hubs, search views, topic indexes) that scale with the existing post system. Every new page type follows the established pattern: typed data in `lib/posts.tsx`, static params via `generateStaticParams`, metadata through `generateMetadata`, and composition from shared components like `PostCard`, `Breadcrumbs`, and `BlogSearch`.

## Quick Start

To add a new template page (e.g. a tag-based listing or state-by-state index):

1. **Define the data shape** — extend `lib/types.ts` if the new page needs fields beyond `Post`, or add a lookup helper to `lib/posts.tsx` (following `getPostsByCategory` / `getCategories`).
2. **Create the route** — add `app/<route>/page.tsx` (or `app/<route>/[param]/page.tsx` for dynamic segments). Export `generateStaticParams`, `generateMetadata`, and a default server component.
3. **Wire the sitemap** — add entries to `app/sitemap.ts` with appropriate `priority` and `changefreq`.
4. **Register navigation** — add the route to `lib/site.ts` `navigation` array if it should appear in the header.

Verify with `npm run build` — static export will fail if any slug is missing from `generateStaticParams`.

## Key Concepts

### Static Generation Contract
All public pages must be fully pre-rendered. Set `export const dynamicParams = false` on any dynamic route so Next.js rejects unknown params at build time rather than falling through to a 404 at runtime.

### Post Data Layer
Posts live as a flat `Post[]` array in `lib/posts.tsx`, imported from generated files under `lib/generatedPosts/`. Lookup helpers (`getPostBySlug`, `getPostsByCategory`, `getCategories`) provide filtered views. New template pages should add helpers here rather than duplicating filter logic in components.

### Metadata & SEO
Every page must export `generateMetadata` returning at minimum `title`, `description`, and `alternates.canonical`. Article pages additionally set `openGraph` and `twitter` card fields. The sitemap (`app/sitemap.ts`) mirrors these pages with priority-weighted entries.

### Component Composition
Template pages compose from the shared component library rather than reimplementing layout:
- `PostCard` — renders a single article preview with image, metadata, category badge, and `trackingLabel` prop
- `Breadcrumbs` — hierarchical navigation trail
- `BlogSearch` — client-side search with category filtering (accepts `allPosts`, `initialPosts`, `categories`)
- `FAQAccordion` — expandable FAQ sections from `post.faqs`
- `Pagination` — numbered page navigation

## Common Patterns

### Dynamic Category Page
```typescript
// app/blog/category/[category]/page.tsx
export const dynamicParams = false;
export function generateStaticParams() {
  return getCategories().map((c) => ({ category: c }));
}
export const generateMetadata = ({ params }) => ({
  title: `${params.category} Articles`,
  alternates: { canonical: `${siteConfig.url}/blog/category/${encodeURIComponent(params.category)}` }
});
```

### Client-Side Search Filter
The `BlogSearch` component handles query + category filtering with a `useMemo`-backed pipeline. Pass it the full post array and category list — it manages its own state. For a new search context, wrap `BlogSearch` in a server component that fetches the right subset of posts.

### Adding a New Data Dimension (Tags, States, etc.)
1. Add the field to the `Post` type in `lib/types.ts`.
2. Populate it in generated post files under `lib/generatedPosts/`.
3. Add a lookup helper in `lib/posts.tsx` (e.g. `getPostsByTag(tag)`).
4. Create the route with `generateStaticParams` deriving values from the new helper.
5. Register sitemap entries and navigation links.
