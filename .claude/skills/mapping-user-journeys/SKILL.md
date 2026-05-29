---
name: mapping-user-journeys
description: Maps user journeys through the site and identifies friction points by tracing navigation flows, component interactions, and content pathways in code.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Mapping User Journeys Skill

Traces end-to-end paths a visitor takes through Utility Explained — from landing on the homepage or a search result, navigating to pillar pages and blog posts, to finding related content. Identifies dead ends, broken links, missing cross-references, navigation gaps, and SEO friction by inspecting routes, components, links, metadata, and content data.

## Quick Start

Invoke with `/mapping-user-journeys` and optionally specify a journey to audit (e.g., "a new visitor looking for help with a high electricity bill"). If no journey is specified, the skill audits the primary navigation flows: homepage → pillar pages → blog posts → related content.

## Key Concepts

- **Entry points**: Pages reachable from external links (homepage, pillar pages, individual blog posts via search/social)
- **Navigation graph**: The `navLinks` and `footerLinks` in `lib/site.ts` define the site's top-level structure
- **Content cross-linking**: Related posts and category links within `lib/posts.tsx` and article components
- **Route coverage**: Pages defined under `app/` — static routes (`page.tsx`) and dynamic blog routes (`[slug]/page.tsx`)
- **Friction signals**: Orphaned pages (no inbound links), broken internal links, missing related content, unlinked categories, metadata gaps, pages without breadcrumbs or back-navigation

## Common Patterns

### Tracing a journey

1. Identify the entry page in `app/` (e.g., `app/page.tsx` for homepage, `app/[slug]/page.tsx` for blog posts)
2. Read the component tree to find all `<Link>` targets and CTAs
3. Follow each link to its destination page and repeat
4. Check that each destination has outbound links continuing the journey

### Auditing content discoverability

1. List all posts from `lib/posts.tsx` and their categories
2. Cross-reference with pillar pages in `app/electricity-explained/`, `app/gas-explained/`, etc.
3. Verify each post appears on its category pillar page and in related-post suggestions
4. Flag posts with no category assignment or missing cross-links

### Checking navigation completeness

1. Read `lib/site.ts` for declared nav and footer links
2. Verify each link target exists as a route under `app/`
3. Check that pillar pages link back to their parent categories and to relevant blog posts
4. Confirm mobile navigation renders the same link set (inspect `Header.tsx`)