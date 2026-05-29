# Modules

When to use: when navigating the codebase, adding new posts, or connecting components to shared data.

## Post Data (`lib/posts.tsx`)

The single source of truth for all blog content. Posts are exported as a typed array with lookup helpers.

```typescript
import posts, { getPostBySlug, getPostsByCategory, getRelatedPosts, getNextReads } from "@/lib/posts";
import type { Post } from "@/lib/types";

const post: Post | undefined = getPostBySlug("my-article");
const allElectricity: Post[] = getPostsByCategory("Electricity");
```

Exported from this module:
- `posts` — full `Post[]` array (default export)
- `getPostBySlug(slug)` — single post or `undefined`
- `getPostsByCategory(category)` — filtered by category name
- `getRelatedPosts(slug)` — based on `relatedSlugs`
- `getNextReads(slug)` — curated next-reads logic

## Site Config (`lib/site.ts`)

Metadata, navigation, and legal links. No types — inferred from the object literal.

```typescript
import { siteConfig } from "@/lib/site";
// siteConfig.name, siteConfig.url, siteConfig.description, siteConfig.ogImage

import { navigation, legalLinks } from "@/lib/site";
// { name: string; href: string }[]
```

## Utilities (`lib/utils.ts`)

Small pure functions with no dependencies.

```typescript
import { formatDate, toTitleCase } from "@/lib/utils";

formatDate("2026-04-25")    // "April 25, 2026"
toTitleCase("electricity")  // "Electricity"
```

## Component Conventions

Components live in `components/` and follow these patterns:
- **No props**: `Header`, `Footer`, `ThemeToggle` — import `siteConfig`/`navigation` directly
- **Post data**: `PostCard`, `RelatedPosts` — accept typed `Post` or `Post[]` props
- **Children / sections**: `FAQAccordion` (items: `FAQItem[]`), `TableOfContents` (sections: `PostSection[]`), `Breadcrumbs` (items: `{ label: string; href?: string }[]`)

## Pitfall

`lib/posts.tsx` is a `.tsx` file (not `.ts`) because post content contains JSX. Don't rename it — the bundler relies on the `.tsx` extension for JSX transform. When importing, always use `@/lib/posts` without the extension.