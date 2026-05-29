# Next.js Workflows

## When to use
Refer to this file when performing multi-step tasks like adding content, creating pages, publishing posts, or running builds.

## Workflow: Add a New Blog Post

1. Create the post object in `lib/posts.tsx` following the `Post` type from `lib/types.ts`. Required fields: `slug`, `title`, `description`, `category`, `keyword`, `date`, `readTime`, `image` (`{ src, alt }`), `sections` (array of `{ id, title, content }` where `content` is JSX), `faqs`, and `relatedSlugs`.
2. The `normalizePostImage` function auto-resolves `image.src` to `/images/articles/<slug>/image.webp` if it doesn't already start with `/images/articles/`. Add the actual image file to `public/images/articles/<slug>/image.webp`.
3. `generateStaticParams()` in `app/blog/[slug]/page.tsx` reads from the `posts` array automatically — no manual slug registration needed.
4. Optionally add curated "next read" entries in the `nextReadMap` in `lib/posts.tsx`.
5. Verify: `npm run build` should succeed without errors.

## Workflow: Add a New Static Page

1. Create directory under `app/` (e.g., `app/my-page/`).
2. Add `page.tsx` with a default export component and a `metadata` export for SEO.
3. Include `alternates: { canonical: \`${siteConfig.url}/my-page\` }` in metadata.
4. Import components from `@/components/` and data from `@/lib/` using path aliases.
5. Add the page path to `app/sitemap.ts` with appropriate priority and changefreq.
6. Verify: `npm run build` succeeds, page appears in `out/my-page/index.html`.

## Workflow: Build and Deploy

```bash
npm run lint     # optional: check for errors first
npm run build    # runs next build → static export to out/
```

The `output: 'export'` config means `npm run build` already produces the `out/` directory — there is no separate `npm run export` step in practice. Deploy the `out/` directory to any static host.

The sitemap (`app/sitemap.ts`) and robots (`app/robots.ts`) are generated at build time as part of the static export. After adding posts or pages, the sitemap updates automatically.

## Pitfalls

- **Pagination sync** — `app/sitemap.ts` and `app/blog/page/[page]/page.tsx` both calculate total pages independently from `posts.length / PER_PAGE`. If you change `PER_PAGE` in one, update both (currently `PER_PAGE = 9`).
- **Canonical URLs** — blog posts use `${siteConfig.url}/blog/${slug}`, not `${siteConfig.url}/${slug}`. The site moved to a `/blog/` prefix; old bare-slug routes no longer exist.
- **Image paths** — the `normalizePostImage` resolver uses `/images/articles/<slug>/image.webp`. If the image pipeline generates a different path, the fallback to category hero images kicks in silently, which may cause inconsistent hero images across posts.