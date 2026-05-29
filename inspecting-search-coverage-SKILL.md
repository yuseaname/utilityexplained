---
name: inspecting-search-coverage
description: Audits technical and on-page search coverage gaps for Utility Explained content, metadata, sitemaps, and structured data.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Inspecting Search Coverage Skill

Audits the Utility Explained site for search visibility gaps — checking that published posts have correct metadata, canonical URLs, structured data, sitemap entries, and internal linking. The site is a statically exported Next.js app with posts defined in `lib/posts.tsx` and SEO configured via the Next.js metadata API.

## Quick Start

```
/inspecting-search-coverage
```

The audit reads `lib/posts.tsx` for the full post inventory, `app/sitemap.ts` for sitemap coverage, and spot-checks rendered pages for meta tags, OpenGraph, and JSON-LD.

## Key Concepts

- **Post registry** — all published posts live as objects in `lib/posts.tsx`; any post not exported from `allPosts` is invisible to the site.
- **Metadata pipeline** — each dynamic route under `app/[slug]/page.tsx` generates `metadata` via `generateMetadata()` using post data (title, description, canonical, OpenGraph).
- **Sitemap generation** — `app/sitemap.ts` maps over `allPosts` plus static pillar pages to produce `/sitemap.xml`.
- **Structured data** — JSON-LD organization schema is defined in `app/layout.tsx`; articles may add Article schema in their page components.
- **Internal linking** — related posts, pillar pages, and the glossary form the internal link graph; orphans reduce crawl efficiency.
- **Canonical enforcement** — `.htaccess` rewrites clean URLs and enforces non-www; metadata sets canonicals per page.

## Common Patterns

**Audit all posts for missing metadata:**
1. Read `lib/posts.tsx` and collect every slug and its metadata fields.
2. For each post, check that `title`, `description`, `category`, and `date` are non-empty strings.
3. Flag any post missing an `excerpt` or `keywords` array.

**Verify sitemap completeness:**
1. Read `app/sitemap.ts` and identify which pages it includes.
2. Compare the slug list from `allPosts` against sitemap entries.
3. Check that pillar page routes (`/electricity-explained`, `/gas-explained`, `/water-explained`, `/heating-cooling-explained`, `/utility-bills-costs-explained`, `/utilities-glossary`) are present.
4. Report orphans — posts in the registry but missing from the sitemap.

**Spot-check on-page SEO for a specific post:**
1. Read `app/[slug]/page.tsx` to understand the `generateMetadata` function.
2. Trace how `title`, `description`, `openGraph`, and `canonical` are derived from post data.
3. Verify heading hierarchy: one `<h1>` matching the title, logical `<h2>`/`<h3>` nesting in the content.
4. Confirm the canonical URL uses `SITE_URL` from `lib/site.ts` with no trailing-slash mismatch.

**Internal link graph analysis:**
1. Grep across `lib/posts.tsx` and component files for internal `<Link>` or `<a href>` references to other site pages.
2. Identify posts that are never linked from any other post or pillar page (orphan posts).
3. Check that pillar pages link to their child blog posts.

**Structured data coverage:**
1. Grep for `application/ld+json` across the `app/` directory.
2. Verify the base Organization schema in `app/layout.tsx` has valid `url`, `name`, and `sameAs` fields.
3. Check whether blog post pages emit Article or BlogPosting JSON-LD.

**Robots and crawlability:**
1. Read `app/robots.ts` and confirm it allows all major crawlers for production.
2. Read `.htaccess` (if present) for redirect rules that might affect crawl paths.
3. Verify no `noindex` meta tags are accidentally set in page components.
