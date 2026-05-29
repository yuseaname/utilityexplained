# In-App Guidance

## When to use

When visitors encounter unfamiliar utility terminology (kWh, therm, CCF, demand charge) within articles and need inline context without leaving the page.

## Patterns

### Glossary-linked term highlights
Scan article content in `lib/posts.tsx` for known utility terms and wrap them in `<Link href="/utilities-glossary#term-anchor">` tags at render time in the `[slug]/page.tsx` template. Use a deterministic term-matching approach — a `glossaryTerms` map in `lib/posts.tsx` that maps canonical terms to their anchor slugs.

```tsx
const GLOSSARY_TERMS: Record<string, string> = {
  "kilowatt-hour": "kwh",
  "kWh": "kwh",
  "therm": "therm",
  "CCF": "ccf",
  "demand charge": "demand-charge",
};
```

### Expandable inline definitions for high-frequency terms
For the 5–10 most common terms, render a collapsible `<details>` element directly in the article body instead of linking away. This is pure HTML — no JavaScript, fully static, accessible by default.

```tsx
<details>
  <summary className="font-medium text-blue-600 cursor-pointer">kWh (kilowatt-hour)</summary>
  <p className="mt-1 text-sm text-gray-600">The unit your electric company uses to measure energy use. One kWh powers a 100-watt light bulb for 10 hours.</p>
</details>
```

### Breadcrumb trail with context labels
On pillar pages and blog posts, render a breadcrumb (`components/Breadcrumb.tsx`) that shows the content hierarchy: Home > Electricity Explained > Why Is My Electric Bill So High? This helps visitors orient themselves and navigate up to broader content. Use the existing `siteConfig.navigation` from `lib/site.ts` for the category labels.

## Pitfalls

- **Do not add tooltip libraries.** JavaScript tooltip systems (Tippy, Popper) add bundle weight to a static site and break accessibility. Use `<details>` elements or glossary links instead — zero runtime cost, works without JS.
- **Glossary anchors must match `utilities-glossary` page headings.** If the glossary page is restructured, these links silently break. Keep the term map in one place (`lib/posts.tsx`) and validate at build time.