# Types

When to use: when defining new data shapes, adding fields to existing types, or typing function signatures.

## Core Types (`lib/types.ts`)

These are the central type definitions. Import them with `import type`.

```typescript
export type FAQItem = {
  question: string;
  answer: string;
};

export type PostSection = {
  id: string;
  title: string;
  content: ReactNode;
};

export type Post = {
  slug: string;
  title: string;
  description: string;
  category: string;
  keyword: string;
  date: string;
  readTime: string;
  image: { src: string; alt: string };
  sections: PostSection[];
  faqs: FAQItem[];
  relatedSlugs: string[];
};
```

## Next.js Framework Types

Use Next.js's built-in types for page metadata and params. Never define your own `Metadata` type.

```typescript
import type { Metadata } from "next";

// generateMetadata signature for dynamic routes
export const generateMetadata = async ({
  params
}: {
  params: { slug: string };
}): Promise<Metadata> => { … };

// Page component props — inline, not a named interface
export default function BlogPostPage({ params }: { params: { slug: string } }) { … }
```

## Utility Types in Practice

The project uses `Record<string, string>` for arbitrary key-value payloads and optional properties (`?`) for configuration.

```typescript
type TrackPayload = {
  event: string;
  label?: string;
  value?: string | number;
  href?: string;
  extra?: Record<string, string>;
};
```

## Pitfall

`PostSection.content` is `ReactNode`, not `string`. When building or mapping sections, pass JSX directly — don't wrap in template literals expecting a string return.