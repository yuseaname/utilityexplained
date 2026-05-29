# Type Definitions

## When to use

Refer here when defining or consuming data shapes — especially post content, FAQ items, image assets, or site configuration objects.

## Core content types (`lib/types.ts`)

```typescript
type FAQItem = {
  question: string;
  answer: string;
};

type PostSection = {
  id: string;       // used as HTML id for anchor links
  title: string;
  content: ReactNode; // JSX — not a plain string
};

type Post = {
  slug: string;
  title: string;
  description: string;       // meta description (SEO)
  category: string;          // "Electricity" | "Gas" | "Water" | "Heating & Cooling" | "Utility Bills"
  keyword: string;           // primary target keyword
  date: string;              // "YYYY-MM-DD"
  readTime: string;          // "12 min read"
  image: { src: string; alt: string };
  sections: PostSection[];
  faqs: FAQItem[];
  relatedSlugs: string[];
};
```

## Site configuration types (`lib/site.ts`)

The config object is untyped but follows this implicit shape:

```typescript
const siteConfig = {
  name: string;
  description: string;
  url: string;              // canonical origin, e.g. "https://utilityexplained.com"
  ogImage: string;          // absolute URL to OG image
  socials: { email: string };
};

const navigation = Array<{ name: string; href: string }>;
const legalLinks = Array<{ name: string; href: string }>;
```

## Next.js metadata type

Pages export `Metadata` from `next` for SEO:

```typescript
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: string | { default: string; template: string };
  description: string;
  alternates: { canonical: string };
  openGraph: { title: string; description: string; url: string; images: Array<{url: string; width: number; height: number; alt: string}>; type: string };
  twitter: { card: string; title: string; description: string; images: string[] };
};
```

## Pitfall: `PostSection.content` is `ReactNode`, not `string`

When writing or generating posts, the `content` field must be JSX (`<p>...</p>`, `<ul>...</ul>`, etc.), not a plain string. Passing a string here will type-check but render without HTML formatting (just concatenated text with no paragraph breaks).