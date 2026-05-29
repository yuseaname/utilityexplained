# Product Analytics

Reference for tracking page views, interaction events, and content funnel analysis on the static site.

## When to use

When evaluating whether the site's analytics setup captures the signals needed to measure user journey effectiveness — which pages attract visitors, where they drop off, and which content pathways lead to deeper engagement.

## Patterns

### Event tracking coverage audit
1. Read `lib/analytics.ts` to understand what events are tracked (page views, link clicks, scroll depth, etc.)
2. Check `app/layout.tsx` and individual page components for analytics initialization calls
3. Verify that key journey transitions fire tracking events: homepage → pillar page, pillar page → blog post, blog post → related post
4. Confirm that navigation link clicks in `Header.tsx` and `Footer.tsx` are tracked as distinct events

### Sitemap and crawl coverage
1. Read `app/sitemap.ts` and verify it includes all static routes and all post slugs from `lib/posts.tsx`
2. Compare the sitemap output against the actual routes under `app/` — any route missing from the sitemap is invisible to search engines
3. Check `app/robots.ts` to confirm no content sections are accidentally disallowed

### Content performance signals
1. Identify which posts have `date` metadata in `lib/posts.tsx` and verify dates are rendered on pages — age affects click-through from search
2. Check that each post page includes structured data (JSON-LD) in `app/[slug]/page.tsx` for rich search results
3. Verify OpenGraph and Twitter card metadata are set for all page types (homepage, pillar pages, blog posts) to measure social sharing

## Pitfall

If analytics are initialized client-side but the site uses static export (`output: 'export'`), ensure tracking scripts don't depend on server-side cookies or session data that won't exist in a static context. Also, `AdSlot.tsx` lazy-loads ad scripts — verify ads don't block content rendering or create layout shifts that hurt engagement metrics.