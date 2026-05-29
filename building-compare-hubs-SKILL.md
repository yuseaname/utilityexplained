---
name: building-compare-hubs
description: Creates comparison and alternative pages that help visitors discover and choose between utility options
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Building Compare Hubs Skill

Creates comparison articles and alternative-option pages that capture mid-funnel search intent ("gas vs electric heating", "alternatives to central air"). Content follows the same `Post` type in `lib/posts.tsx` as regular articles but uses comparison-specific section structures, cross-linking via `relatedSlugs`, and reciprocal `nextReadMap` entries to build a discovery network between compared options.

## Quick Start

1. Identify the comparison pair or alternative set and its target keyword
2. Create a `Post` entry in `lib/posts.tsx` with a slug like `gas-vs-electric-heating-cost-comparison`
3. Structure sections with `id: "quick-answer"` first, then comparison tables/pros-cons blocks
4. Set `relatedSlugs` to link both sides of the comparison plus relevant pillar pages
5. Add reciprocal entries in `nextReadMap` so each related post points back
6. Update `components/SmartLinker.tsx` with new technical terms for auto-cross-linking
7. Verify with `npm run dev` and `npm run build`

## Key Concepts

### Post-First Comparison Architecture

All comparisons are standard `Post` objects — no custom routes. The existing `app/blog/[slug]/page.tsx` renderer handles everything. The comparison structure comes from `sections` content and `relatedSlugs` linking, not from page-level code.

### Comparison Post Anatomy

| Field | Comparison convention |
|-------|----------------------|
| `slug` | `gas-vs-electric-heating-cost-comparison`, `alternatives-to-central-air` |
| `title` | Include both options naturally: "Gas vs Electric Heating: Cost Comparison" |
| `description` | Problem + what the reader will learn, under 160 chars |
| `category` | Use the dominant utility category ("Heating & Cooling", "Electricity", etc.) |
| `keyword` | Match search intent: "gas vs electric heating cost" |
| `relatedSlugs` | Both compared posts + pillar page + adjacent comparisons |
| `sections[0].id` | Always `"quick-answer"` — the core verdict up front |

### Cross-Linking via nextReadMap

`nextReadMap` is an object mapping slug → `{ label, slugs }` for "Next Read" CTAs. For comparisons, add entries on both sides so a reader on "Gas Heating Explained" sees a link to "Gas vs Electric" and vice versa. This builds a discovery mesh between related content.

### SEO Signals for Comparison Intent

Comparison pages target informational comparison queries. Use "vs" or "alternatives to" in the slug and title. The FAQ section should address decision-focused questions ("Which is cheaper?", "Which is better for small apartments?"). Structured data (FAQ schema) is auto-generated from the `faqs` array.

## Common Patterns

### Side-by-Side Comparison Sections

```typescript
sections: [
  {
    id: 'quick-answer',
    title: 'Gas vs Electric Heating: Quick Answer',
    content: `Electric heating has lower upfront costs...`
  },
  {
    id: 'cost-comparison',
    title: 'Monthly Cost Breakdown',
    content: `| Factor | Gas | Electric |\n|--------|-----|----------|\n| ... |`
  },
  {
    id: 'pros-and-cons',
    title: 'Pros and Cons',
    content: `**Gas Heating**\n- Pro: ...\n- Con: ...\n\n**Electric Heating**\n- Pro: ...`
  },
  {
    id: 'best-for',
    title: 'Which Is Best For You?',
    content: `**Choose gas if:** ...\n\n**Choose electric if:** ...`
  }
]
```

### Alternatives Page Structure

```typescript
sections: [
  {
    id: 'quick-answer',
    title: 'Best Alternatives to Central Air',
    content: `The three most cost-effective alternatives...`
  },
  {
    id: 'top-alternatives',
    title: 'Top Alternatives Compared',
    content: `| Alternative | Best For | Avg Install Cost |\n|-------------|----------|------------------|\n| ... |`
  },
  {
    id: 'ductless-mini-split',
    title: 'Ductless Mini-Split Systems',
    content: `...`
  }
]
```

### Wiring Reciprocal nextReadMap Entries

```typescript
// In lib/posts.tsx nextReadMap object:
'gas-heating-explained': {
  label: 'Compare with electric',
  slugs: ['gas-vs-electric-heating-cost-comparison'],
},
'electric-heating-explained': {
  label: 'Compare with gas',
  slugs: ['gas-vs-electric-heating-cost-comparison'],
},
'gas-vs-electric-heating-cost-comparison': {
  label: 'Dive deeper',
  slugs: ['gas-heating-explained', 'electric-heating-explained'],
},
```

### Adding Comparison Terms to SmartLinker

When new technical terms appear in comparison content, add them to the `terms` map in `components/SmartLinker.tsx` with the relevant post slug. This auto-generates in-content links whenever the term appears across the site.
