# Key Modules

## When to use

Refer here to understand what each core module does, where to find it, and how modules interact. Essential when debugging build failures, tracing data flow, or adding new features.

## Module map

| Module | Path | Role |
|--------|------|------|
| Post registry | `lib/posts.tsx` | All `Post[]` data, lookup helpers (`getPostBySlug`, `getRelatedPosts`, `getNextReads`) |
| Content types | `lib/types.ts` | `Post`, `PostSection`, `FAQItem` type definitions |
| Site config | `lib/site.ts` | `siteConfig`, `navigation`, `legalLinks` |
| Utilities | `lib/utils.ts` | `formatDate`, `toTitleCase` |
| Analytics | `lib/analytics.ts` | Event tracking configuration |
| Generated posts | `lib/generatedPosts/*.ts` | AI-generated post arrays, merged into `lib/posts.tsx` |
| Root layout | `app/layout.tsx` | Fonts (Fraunces + IBM Plex Sans), metadata, global scripts, header/footer |
| Blog post route | `app/blog/[slug]/page.tsx` | `generateStaticParams`, `generateMetadata`, article rendering, structured data |
| Blog listing | `app/blog/page.tsx` | Paginated post listing |
| Category listing | `app/blog/category/[category]/page.tsx` | Posts filtered by category |
| Sitemap | `app/sitemap.ts` | Dynamic `/sitemap.xml` generation |
| Robots | `app/robots.ts` | `/robots.txt` configuration |

## Data flow

```
lib/types.ts ──defines──> lib/posts.tsx ──imports──> lib/generatedPosts/*.ts
                                                  │
                                                  ▼
                                    app/blog/[slug]/page.tsx  (generateStaticParams)
                                    app/blog/page.tsx          (listing)
                                    app/blog/category/[category]/page.tsx
```

`lib/site.ts` is imported by `app/layout.tsx` and individual pages for metadata/URLs. `lib/utils.ts` is imported wherever date formatting or title casing is needed.

## Component library (`components/`)

17 components total. Key ones:

| Component | Client? | Purpose |
|-----------|---------|---------|
| `Header` | No | Site navigation |
| `Footer` | No | Site footer with links |
| `PostCard` | No | Blog post preview in listings |
| `TableOfContents` | Yes | Scroll-tracking TOC sidebar |
| `FAQAccordion` | Yes | Collapsible FAQ sections |
| `SmartLinker` | Yes | Auto-links key phrases to internal articles |
| `AdSlot` | No | Google AdSense integration |
| `ThemeToggle` | Yes | Dark/light mode switch |
| `ReadingProgress` | Yes | Reading progress bar |
| `LinkTracker` | Yes | Analytics link click tracking |

## Pitfall: `lib/generatedPosts/` is not committed

The `generatedPosts/` directory contains AI-generated content that is imported by `lib/posts.tsx` but excluded from git. If you clone fresh and these files are missing, `npm run build` will fail with import errors. These files must be regenerated or copied from another environment before building.