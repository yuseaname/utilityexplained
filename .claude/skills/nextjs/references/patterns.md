# Next.js Patterns

## When to use
Refer to this file when creating or modifying pages, components, data structures, or build configuration. These are the established conventions in this codebase.

## Pattern: Static Route with Metadata

Every page exports a `metadata` constant (or `generateMetadata` for dynamic routes) with title, description, and canonical URL.

```typescript
// app/contact/page.tsx — static page
export const metadata: Metadata = {
  title: "Contact",
  description: "Send a message or ask a utility bill question.",
  alternates: { canonical: `${siteConfig.url}/contact` }
};

export default function ContactPage() { /* … */ }
```

```typescript
// app/blog/[slug]/page.tsx — dynamic route
export const generateMetadata = async ({ params }: { params: { slug: string } }): Promise<Metadata> => {
  const post = getPostBySlug(params.slug);
  if (!post) return {};
  return {
    title: post.title,
    description: post.description,
    alternates: { canonical: `${siteConfig.url}/blog/${post.slug}` },
    openGraph: { /* title, description, url, images, type */ },
    twitter: { card: "summary_large_image", /* title, description, images */ }
  };
};
```

## Pattern: Dynamic Route with generateStaticParams

Every `[param]` route must export `generateStaticParams` so the static export (`output: 'export'`) succeeds. Set `export const dynamicParams = false` to 404 on unknown slugs.

```typescript
export const dynamicParams = false;

export async function generateStaticParams() {
  return posts.map((post) => ({ slug: post.slug }));
}
```

This pattern is repeated for `app/blog/[slug]/page.tsx`, `app/blog/category/[category]/page.tsx`, and `app/blog/page/[page]/page.tsx`.

## Pattern: Post Content as TypeScript Objects

Posts are not markdown. Each post is a `Post` object (from `lib/types.ts`) with `slug`, `title`, `description`, `category`, `sections` (JSX `ReactNode`), `faqs`, `relatedSlugs`, and `image`. Sections contain inline JSX, not strings.

AI-generated posts are imported from `lib/generatedPosts/` and spread into the `posts` array in `lib/posts.tsx`. The `normalizePostImage` function resolves image paths to `/images/articles/<slug>/image.webp` with a category-based fallback.

Helper functions exported from `lib/posts.tsx`:
- `getPostBySlug(slug)` — single post lookup
- `getPostsByCategory(category)` — filter by category
- `getRelatedPosts(slug)` — related slugs resolved to full posts
- `getNextReads(slug)` — curated next-read links from `nextReadMap`
- `getCategories()` — unique category list

## Pitfalls

- **Missing `generateStaticParams`** — adding a dynamic route without it will fail the static export build silently or produce an empty `out/` for that route.
- **`images.unoptimized: true`** — required in `next.config.js` because static export does not support Next.js image optimization. Forgetting this causes build errors.
- **Path aliases** — always use `@/lib/` and `@/components/` imports. Relative imports work but break consistency with the rest of the codebase.