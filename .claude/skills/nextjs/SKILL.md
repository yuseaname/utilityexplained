---
name: nextjs
description: Configures Next.js App Router, routing, and static generation for the Utility Explained project
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Next.js Skill

Manages the Next.js 14 App Router configuration, page routing, static site generation, and content pipeline for Utility Explained — a static content site pre-rendered at build time with zero runtime database.

## Quick Start

```bash
npm run dev       # dev server with hot reload
npm run build     # production build (static export)
npm run lint      # ESLint check
```

The site uses `output: 'export'` in `next.config.js` to produce a fully static `out/` directory. There is no API layer or server-side runtime — all pages are pre-rendered at build time.

## Key Concepts

### App Router Structure
All routes live under `app/`. Each directory can contain a `page.tsx` (renders the route), `layout.tsx` (wraps child routes), or `loading.tsx` / `error.tsx` for special states.

- `app/page.tsx` — homepage
- `app/[slug]/page.tsx` — dynamic blog post routes
- `app/blog/`, `app/electricity-explained/`, etc. — category listing / pillar pages
- `app/sitemap.ts` — generates `/sitemap.xml` at build time
- `app/robots.ts` — generates `/robots.txt`

### Content Flow
Posts are stored as TypeScript objects in `lib/posts.tsx`, not as markdown files. Helper functions (`getPostsByCategory`, `getPostBySlug`, `getRelatedPosts`) serve content to pages and components. AI-generated posts can be dropped into `lib/generatedPosts/` and wired through `posts.tsx`.

### Static Generation
Dynamic routes like `[slug]/page.tsx` must use `generateStaticParams()` to enumerate all slugs at build time. Without this, static export fails.

### Path Aliases
`@/*` maps to the project root via `tsconfig.json`. Prefer absolute imports over relative paths.

## Common Patterns

### Adding a new blog post
1. Create the post object in `lib/posts.tsx` (follow the existing `Post` type from `lib/types.ts`)
2. Add the slug to `generateStaticParams()` in `app/[slug]/page.tsx`
3. Add an image to `public/images/` if needed

### Adding a new route
1. Create a directory under `app/` (e.g., `app/new-page/`)
2. Add `page.tsx` with a default export component
3. Import shared components from `@/components/` and data from `@/lib/`
4. Export `metadata` for SEO title/description/OpenGraph

### Adding a new component
1. Create `components/NewComponent.tsx` (PascalCase)
2. Export as a named function component
3. Import in pages using `@/components/NewComponent`

### Metadata and SEO
Each page exports a `metadata` constant for title, description, and OpenGraph. The root layout in `app/layout.tsx` sets site-wide defaults (fonts, analytics, header/footer).

### Styling
Tailwind CSS classes are used directly in JSX. Dark mode is handled via the `ThemeToggle` component and Tailwind's `dark:` variant. No CSS modules or styled-components.