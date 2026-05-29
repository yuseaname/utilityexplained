---
name: structuring-offer-ladders
description: Frames plan tiers, value ladders, and upgrade logic for monetizing content-driven sites like Utility Explained.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Structuring Offer Ladders Skill

Designs tiered value propositions and upgrade pathways for the Utility Explained content site — progressing readers from free blog content through progressively more valuable offerings. This skill focuses on structuring the logic behind tiers, defining what changes at each level, and mapping clear escalation triggers that feel natural within the site's educational mission.

## Quick Start

```bash
npm run dev      # Start dev server to preview pricing/CTA components
npm run build    # Verify static generation still works after changes
```

Offer-related components go in `components/`. Tier configuration and feature matrices live in `lib/`. Any new route (e.g., `/pricing`, `/guides/premium`) goes under `app/` as a static page.

## Key Concepts

- **Value ladder**: A sequence of offerings ordered by both price and depth — free articles at the base, then paid guides, toolkits, or coaching at higher rungs. Each rung must deliver measurable incremental value.
- **Tier boundaries**: Clear, non-arbitrary lines between what's free and what's paid. Avoid paywalling information that's already publicly available; instead gate curation, personalization, tools, or expert access.
- **Upgrade triggers**: Contextual moments within content where a reader naturally wants more — calculator tools, personalized savings plans, downloadable checklists, step-by-step action plans.
- **Anchor and decoy pricing**: The mid-tier should feel like the obvious best value. The highest tier exists primarily to make the mid-tier look reasonable.
- **Static compatibility**: All pricing pages, feature tables, and CTA components must render as static HTML. No client-side checkout — link out to Gumroad, Lemonsqueezy, Stripe Checkout, or similar hosted payment pages.

## Common Patterns

### Tier data model

```typescript
// lib/offers.ts
export interface OfferTier {
  id: string;
  name: string;           // "Free", "Savings Toolkit", "Bill Audit"
  price: number | null;   // null = free
  period?: string;        // "one-time" | "monthly" | "yearly"
  features: string[];
  highlighted?: boolean;  // visually emphasized on pricing page
  ctaText: string;
  ctaUrl: string;         // external checkout or internal route
}
```

### Feature comparison table

Build a responsive `<table>` or card grid under `components/OfferComparison.tsx`. Highlight the recommended tier with a ring/border and "Most Popular" badge. Use `dark:` variants for all colors.

### In-content upgrade prompt

Embed contextual CTAs within blog posts (`lib/posts.tsx` or inline in `[slug]/page.tsx`). A prompt after a "How to read your electricity bill" article might link to a downloadable bill-audit checklist at the next tier.

### Pricing page route

Add `app/pricing/page.tsx` with `export const metadata` for SEO. Import tiers from `lib/offers.ts`. Render static HTML — no `fetch`, no `useEffect`. Link each CTA button to the external checkout URL.
