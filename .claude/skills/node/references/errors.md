# Common Errors and Fixes

## When to use

Refer here when `npm run build` fails, `npm run dev` shows unexpected errors, or TypeScript compilation errors appear. Covers project-specific gotchas beyond generic Next.js issues.

## Build failure: missing generated posts

**Error:** `Module not found: Can't resolve '@/lib/generatedPosts/...'`  
**Cause:** `lib/generatedPosts/` files are not committed to git. A fresh clone has no generated content.  
**Fix:** The generated post files must be present before building. Obtain them from the content pipeline or another environment. Check `lib/posts.tsx` imports to see exactly which files are needed.

## Build failure: TypeScript strict mode violations

**Error:** `Type 'string' is not assignable to type '...'` or similar strict errors  
**Cause:** `tsconfig.json` has `strict: true`. Common triggers: missing type annotations on function params, assigning `string | undefined` to `string`, or using `any`.  
**Fix:** Run `npx tsc --noEmit` to get the full list before the Next.js build swallows some errors. Fix type annotations. For `Post` objects, ensure all fields match `lib/types.ts`.

## Static export error: dynamic features unsupported

**Error:** `Page with dynamic rendering enabled was detected` or `output: 'export' requires all pages to be statically rendered`  
**Cause:** Using `revalidate`, `headers()`, `cookies()`, or `searchParams` in a page component without `generateStaticParams`.  
**Fix:** For dynamic routes, provide `generateStaticParams` (as done in `app/blog/[slug]/page.tsx`). For truly dynamic pages, this project cannot support them — it's a fully static export.

## Image optimization warning in static export

**Error:** `Image Optimization has been disabled` or images fail to load  
**Cause:** `next.config.js` sets `images.unoptimized: true` (required for `output: 'export'`), so all images are served as-is without Next.js optimization.  
**Fix:** Use properly sized WebP images in `public/images/`. Don't rely on `next/image` for auto-format conversion — it won't happen with `unoptimized: true`.

## Pitfall: `@types/react` version mismatch

`package.json` has `react@18.3.1` but `@types/react@19.2.7`. This mismatch can cause confusing type errors (e.g., `children` prop complaints) that don't appear at runtime. Pin `@types/react` to `18.x` if type errors seem incorrect for React 18 APIs.