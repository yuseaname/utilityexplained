# Engagement & Adoption

Reference for deep-reading journey analysis — how visitors consume multiple pieces of content and develop trust in the site.

## When to use

When auditing whether readers stay on the site beyond their first article. This covers related-content recommendations, cross-category navigation, and the content pathways that turn a single-page visitor into a repeat reader.

## Patterns

### Related-content chain audit
1. In `lib/posts.tsx`, identify posts that declare `relatedPosts` or `category` fields
2. For each post, verify the rendered page in `app/[slug]/page.tsx` displays related-post links
3. Follow a related-post link to its page and check whether it links back to the original — the chain should be reciprocal
4. Flag any post whose related posts are all from a different category (suggests misclassification)

### Category depth journey
1. Pick a category (e.g., "electricity") and list all its posts from `lib/posts.tsx`
2. Trace a path from the pillar page through 3+ posts using only in-page links
3. Check that posts within a category cover a progression (introductory → intermediate → specific problem-solving)
4. Identify categories with fewer than 3 posts — these may feel thin and fail to retain visitors

### Cross-category bridges
1. Check if electricity posts link to gas or water posts where topics overlap (e.g., "understanding your bill" spans all utilities)
2. Read `Footer.tsx` and `Header.tsx` to confirm all categories are accessible from every page
3. Verify that the blog listing page (`app/blog/page.tsx`) groups or filters posts by category

## Pitfall

Related-post suggestions that only point to the newest posts rather than topically relevant ones create shallow engagement. Check that related-post logic in `lib/posts.tsx` is category-aware, not just date-ordered.