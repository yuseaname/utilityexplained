# Feedback & Insights

Reference for interpreting user behavior signals and content gaps to improve the site's navigation and content strategy.

## When to use

When analyzing which content is underperforming, which navigation paths are unused, and where the site fails to answer visitor questions — using code-level signals rather than external analytics tools.

## Patterns

### Orphaned content detection
1. Extract all slugs from `lib/posts.tsx` and all `<Link href="/...">` targets across `app/` and `components/`
2. Any post slug that never appears as a `<Link>` target in another page is orphaned — only reachable via direct URL or search
3. Cross-reference with `app/sitemap.ts` to confirm orphaned posts are at least included in the sitemap
4. For each orphan, identify the most natural pillar page or related post that should link to it

### Category imbalance analysis
1. Group posts by their `category` field in `lib/posts.tsx` and count per category
2. Compare counts against the visual prominence of each category in `Header.tsx` navigation
3. Flag categories with few posts but high nav prominence (overpromises) or many posts but low prominence (hidden value)
4. Check pillar pages for thin categories — do they have enough content to justify a dedicated page, or should they be merged?

### Missing cross-reference scan
1. Grep `app/[slug]/page.tsx` and pillar pages for links to other site pages
2. Identify posts that mention related topics in their body text but don't link to the corresponding post or pillar page
3. Check whether the glossary (`app/utilities-glossary/`) is linked from posts that define technical terms
4. Verify that "utility-bills-costs-explained" posts are cross-linked with the specific utility category posts they reference

## Pitfall

Don't confuse "no internal links" with "no value." A post may be primarily discovered via search and have strong organic traffic without any internal cross-links. The real signal is whether visitors who land on that post have a path to continue exploring — always check for at least one outbound link to related content, even on search-landing pages.