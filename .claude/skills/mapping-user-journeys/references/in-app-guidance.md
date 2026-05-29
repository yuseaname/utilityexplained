# In-App Guidance

Reference for navigation aids, progressive disclosure, and wayfinding elements that help visitors orient themselves and find content.

## When to use

When evaluating whether visitors can understand where they are on the site, what else is available, and how to get to the next useful piece of content without relying on the browser's back button.

## Patterns

### Breadcrumb and wayfinding audit
1. Read `app/[slug]/page.tsx` and check for a breadcrumb or category indicator showing `Home > Category > Post Title`
2. Verify pillar pages (`app/<category>-explained/page.tsx`) display breadcrumbs linking back to the homepage
3. Check that `Header.tsx` highlights the current section in the navigation when on a pillar or blog page

### CTA placement and clarity
1. Scan each page type for call-to-action elements — "Read more," "Learn about X," "See all posts"
2. Verify CTAs on blog posts point to the category pillar page or related posts, not just back to the homepage
3. Check that CTAs are visually distinct from body text (use `components/PostCard.tsx` as the reference for link styling)

### Progressive content disclosure
1. Check whether pillar pages use collapsible FAQ sections, expandable guides, or summarized post previews rather than full article text
2. Verify that long blog posts have a table-of-contents or jump links to sections
3. Confirm the glossary page (`app/utilities-glossary/`) is linked from posts that use technical terms

## Pitfall

A navigation header that collapses all categories into a "More" dropdown on mobile effectively hides content from touch users. Always audit `Header.tsx` for mobile equivalence — every link visible on desktop must be reachable on mobile within two taps.