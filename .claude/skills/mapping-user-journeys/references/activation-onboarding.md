# Activation & Onboarding

Reference for first-visit journey analysis — how a new visitor discovers the site and reaches their first useful answer.

## When to use

A visitor lands from search, social, or a direct link and needs to quickly understand what the site offers and find content relevant to their utility question. Audit this journey when checking homepage effectiveness, pillar page clarity, or search-result-to-content paths.

## Patterns

### Homepage entry audit
1. Read `app/page.tsx` and trace every `<Link>` and CTA from the hero section
2. Verify featured posts in the homepage match the most common search-intent topics in `lib/posts.tsx`
3. Check that category summaries (Electricity, Gas, Water, Heating/Cooling) link to their pillar pages under `app/<category>-explained/`
4. Confirm the homepage communicates the site's value proposition within the first screen of content

### Search-result landing paths
1. For a given blog post slug, read `app/[slug]/page.tsx` and confirm it renders correct metadata (title, description, OpenGraph) from the post object in `lib/posts.tsx`
2. Check that the landing page has visible navigation back to its category pillar page
3. Verify the post shows related-content links so the visitor can continue exploring without returning to search

### Pillar page as orientation
1. Read pillar pages (e.g., `app/electricity-explained/page.tsx`) and check they list all posts in that category from `lib/posts.tsx`
2. Confirm pillar pages include a short intro explaining what the visitor will find, not just a list of links
3. Check that pillar pages link to sibling pillar pages (cross-utility navigation)

## Pitfall

A common friction point is the homepage sending visitors to pillar pages that don't link back to specific posts, or blog posts that have no breadcrumb or category link — leaving the visitor on an island. Always verify bidirectional links exist between pillar pages and their child posts.