---
name: crafting-page-messaging
description: Writes conversion-focused messaging for pages and key CTAs across the Utility Explained content site, ensuring copy drives readers deeper into the site.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Crafting Page Messaging Skill

Writes and refines the on-page copy that moves visitors from "browsing" to "engaged" — hero headlines, subheadlines, section headings, CTA button text, card descriptions, and page-level value propositions. The skill treats every text element as a conversion lever, grounded in the site's educational mission and the search intent of renters and new homeowners trying to understand their utility bills.

## Quick Start

```bash
npm run dev          # Preview copy changes live at localhost:3000
npm run build        # Confirm static generation still succeeds
```

Start by reading the site's voice anchors: `lib/site.ts` (tagline, description) and the homepage hero in `app/page.tsx`. Then inspect the content data model in `lib/types.ts` and posts in `lib/posts.tsx` to understand the fields that carry messaging weight — `title`, `description`, `keyword`, `sections[0]` (the quick-answer), and `faqs`.

## Key Concepts

- **Conversion hierarchy on a content site**: The primary "conversion" is reading a full article. Secondary conversions are clicking to a related post, subscribing, or visiting a pillar page. Every piece of copy should pull toward one of these outcomes.
- **Search-intent alignment**: Posts have a `keyword` field in `lib/posts.tsx`. The `title`, `description`, and first section should echo the searcher's phrasing while the rest of the page earns trust through depth. A mismatch between keyword and headline loses the visitor before the first scroll.
- **Voice consistency**: The site speaks in second person ("your bill"), avoids jargon without inline explanation (define kWh, therms, CCF on first use), and targets an 8th-grade reading level. Read `app/page.tsx` for the canonical tone — confident but conversational, never condescending.
- **CTA specificity over cleverness**: "Pick your first guide" outperforms "Learn more" because it sets an expectation. Button text should describe the next state, not the current action. Every CTA on the homepage and pillar pages should answer "what happens when I click this?"
- **Progressive disclosure**: The homepage hero makes a single promise ("understand your bills — no jargon, no stress"). Section headings deliver on sub-promises ("How it works", "Popular explainers"). Individual posts solve a concrete problem. Messaging should narrow at each level, never broaden.

## Common Patterns

### Writing a post headline and description

Read the post object in `lib/posts.tsx`. The `title` should contain the `keyword` naturally and telegraph the outcome ("7 Reasons + Fixes"). The `description` (used as the meta description and `PostCard` excerpt) must stand alone in a SERP — include the problem, a hint of the solution, and a reason to click, all under 160 characters.

### Crafting hero copy for a new pillar page

Pillar pages live under `app/electricity-explained/`, `app/gas-explained/`, etc. The `<h1>` should state the reader's goal ("Understand Your Gas Bill"), the subhead should acknowledge their frustration ("Charges, rates, and meter readings explained in plain English"), and the first CTA should send them to the most relevant post, not back to the homepage.

### Auditing CTA text across the site

Grep for `className="button"` and `<Link` elements across `app/` and `components/`. Each CTA should pass three checks: (1) it describes the destination ("Read the full guide"), not a generic action ("Click here"); (2) it matches the reading level of the surrounding copy; (3) it creates forward momentum, never loops back.

### Writing FAQ questions and answers

FAQs in each post's `faqs` array serve dual purposes — they answer real reader questions *and* capture long-tail search traffic. Questions should mirror natural query phrasing ("How do I know if my water meter is broken?" not "Water meter diagnostics"). Answers should be 2-4 sentences, start with a direct response, and link contextually to related posts via `relatedSlugs`.

### Section headings within a post

Post sections (the `sections` array) use `id` and `title` fields that become anchor links. Headings should follow a problem→explanation→action structure. The first section is always `id: "quick-answer"` and must deliver the core answer in the opening paragraph so searchers and screen readers get immediate value.
