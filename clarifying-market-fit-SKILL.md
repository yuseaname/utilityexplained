---
name: clarifying-market-fit
description: Aligns ICP, positioning, and value narrative for on-page messaging across the Utility Explained site
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Clarifying Market Fit Skill

Sharpens the Ideal Customer Profile (ICP), competitive positioning, and value narrative so that every page on Utility Explained speaks directly to the reader it serves. The site targets people confused by utility bills — typically first-time renters, new homeowners, or anyone hit by an unexpected spike — and converts that confusion into trust through plain-English educational content. This skill ensures on-page copy, metadata, and content strategy stay aligned with that audience without drifting into generic SEO filler.

## Quick Start

1. Read `lib/site.ts` for the current site description and navigation structure.
2. Scan `lib/posts.tsx` to review existing post titles, descriptions, and categories.
3. Check `app/page.tsx` for the homepage hero copy and value proposition sections.
4. Audit a target page's `<title>`, `<meta description>`, H1, and intro paragraph for ICP alignment.

## Key Concepts

- **Ideal Customer Profile (ICP)**: The primary reader is a US-based renter or new homeowner who recently received a utility bill they don't understand. Secondary readers include people comparing heating options, budgeting for a new place, or investigating a sudden cost spike. They are not energy professionals — they need jargon-free, practical explanations.
- **Positioning statement**: "Utility Explained translates electricity, gas, and water bills into plain English so you can budget with confidence, not confusion." Every page should reinforce this without restating it verbatim.
- **Search intent over keyword stuffing**: Posts are structured around informational queries ("why is my electric bill so high in winter", "what is a kilowatt-hour"). The title and meta description must answer the query directly — not tease or gate-keep.
- **Category pillars**: Five content pillars map to the route structure in `app/` — Electricity, Gas, Water, Heating & Cooling, and Utility Bills & Costs. New content must fit cleanly into one pillar or justify a new one.
- **Trust signals**: The site earns trust through neutral tone, no product sales pitches, and practical checklists readers can act on immediately. Messaging should never sound like it's selling something.

## Common Patterns

### Auditing a post for ICP alignment

Check these fields in `lib/posts.tsx` for the target post:

- `title` — Does it match a real search query from the target reader? Avoid clickbait qualifiers that don't add specificity.
- `description` — Does it state the outcome the reader gets, not just the topic?
- `keyword` — Is it the exact phrase someone types into Google, not a marketing phrase?
- `category` — Does it map to one of the five pillars?

### Evaluating homepage messaging

The homepage (`app/page.tsx`) must pass three checks:

1. **Who is this for?** The hero H1 should name the problem ("understand your utility bills") in the reader's own words.
2. **Why here and not Google?** The sub-copy should signal depth, structure, and practicality — not just "we have articles."
3. **What's the first action?** The primary CTA should lead to content, not a signup wall or tool.

### Positioning a new content pillar

Before creating a new route under `app/`, validate against existing pillars:

- Does it serve the same ICP or a different audience?
- Is there enough topic depth to support 5+ posts?
- Does it cannibalize or complement an existing category?

If complementary, add the pillar to `site.ts` navigation and create a landing page under `app/<slug>/page.tsx` with an intro, featured posts, and a category description.
