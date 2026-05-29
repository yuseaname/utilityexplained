---
name: adding-structured-signals
description: Adds JSON-LD structured data and schema.org markup to Utility Explained pages for Google rich results.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Adding Structured Signals Skill

Adds schema.org JSON-LD structured data to Utility Explained pages so Google can render rich results (FAQ expandable snippets, article carousels, breadcrumbs, etc.). The site is a statically exported Next.js app; all structured data is inlined via `<script type="application/ld+json">` with `dangerouslySetInnerHTML`.

## Quick Start

```
/adding-structured-signals
```

Audit existing schema coverage first (`grep -r "application/ld+json" app/`), then implement or extend markup for the target page type.

## Key Concepts

- **Injection method** — structured data is rendered as `<script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }} />` inside page components. No shared utility exists yet; schemas are defined inline per page.
- **Post data source** — blog posts are objects in `lib/posts.tsx` with fields like `title`, `description`, `date`, `image`, `faqs` (array of `{ question, answer }`), `category`, and `slug`.
- **Site identity** — `siteConfig` from `lib/site.ts` provides `name`, `url`, and `description` used in Organization and publisher fields across all schemas.
- **Schema types in use** — `Organization` (homepage only), `Article` (pillar pages), `BlogPosting` (blog posts), `FAQPage` (blog posts with FAQs), `BreadcrumbList` (all content pages).
- **No WebSite or SearchAction schema** — not yet implemented; adding a site-level search box schema is a candidate enhancement.
- **No HowTo or Step schema** — tutorial-style posts could benefit from `HowTo` structured data for rich step-by-step results.

## Common Patterns

**Add FAQPage schema to a blog post:**

1. Read `app/blog/[slug]/page.tsx` for the existing `faqLd` pattern (lines 92-103).
2. Ensure the post object in `lib/posts.tsx` has a `faqs` array with `{ question, answer }` entries.
3. Map `post.faqs` into a `FAQPage` JSON-LD object with `Question`/`Answer` entities.
4. Inject via `<script type="application/ld+json">` in the page's JSX.

**Add BlogPosting schema to a blog post:**

1. Follow the `blogPostingLd` pattern in `app/blog/[slug]/page.tsx` (lines 70-90).
2. Include `headline`, `description`, `datePublished`, `dateModified`, `author` (Organization), `publisher` (Organization), `mainEntityOfPage` (WebPage with `@id`), and `image` array.
3. Use `siteConfig.url` for all absolute URLs.

**Add Article + BreadcrumbList schema to a pillar page:**

1. Read an existing pillar page (e.g., `app/electricity-explained/page.tsx`) for the pattern.
2. Create an `Article` JSON-LD with `headline`, `description`, `author`, `publisher`, `datePublished`, `dateModified`, and `mainEntityOfPage`.
3. Create a `BreadcrumbList` JSON-LD with `ListItem` entries: Home (position 1) → pillar page (position 2).
4. Inject both schemas as separate `<script>` tags.

**Add a new schema type (e.g., HowTo):**

1. Define the JSON-LD object inline in the target page component, following schema.org/HowTo spec.
2. Map content sections or steps from the post data into `step` entities with `name` and `text`.
3. Inject alongside existing schemas — multiple JSON-LD blocks are valid per page.
4. Validate with Google's Rich Results Test after build.

**Verify schema correctness:**

1. After editing, run `npm run build` to ensure no TypeScript errors from the new objects.
2. Check that `JSON.stringify` produces valid JSON (no `undefined` values, proper quoting).
3. Confirm all URLs in schema use absolute paths with `siteConfig.url` prefix.
