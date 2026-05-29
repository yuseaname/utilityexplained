# Roadmap & Experiments

Reference for testing navigation changes, content layouts, and structural improvements to the site's user journeys.

## When to use

When planning changes to navigation structure, content hierarchy, or page layouts that could improve visitor flow — and when you need to validate those changes against the current journey map before implementing.

## Patterns

### Navigation restructure pre-flight
1. Document the current navigation graph from `lib/site.ts` (`navLinks`, `footerLinks`) and all pillar page links
2. Map the proposed change (e.g., merging two categories, adding a new pillar page) as a diff against the current graph
3. Identify every file that would need updating: `lib/site.ts`, `lib/posts.tsx` (category fields), pillar page components, `Header.tsx`, `Footer.tsx`, `app/sitemap.ts`
4. Check for hardcoded links in individual post content that would break under the restructure

### Content layout experiment
1. Before changing a pillar page layout (e.g., switching from a post list to a card grid), audit which components are used: `PostCard.tsx`, any custom listing components
2. Verify the new layout doesn't break the blog post `[slug]` dynamic route or category filtering logic in `lib/posts.tsx`
3. Test that `npm run build` succeeds with the layout change and the static export generates all expected pages

### New category addition checklist
1. Add the category to `lib/posts.tsx` type definitions and assign relevant posts
2. Create the pillar page route under `app/<category>-explained/page.tsx`
3. Add nav and footer links in `lib/site.ts`
4. Update `app/sitemap.ts` to include the new route
5. Add the category to `Header.tsx` navigation if it's a top-level section
6. Cross-link from existing categories where topics overlap

## Pitfall

Adding a new pillar page or category without updating `app/sitemap.ts` means search engines won't discover it. Always run `npm run build` after structural changes and check the build output for missing routes or static generation errors.