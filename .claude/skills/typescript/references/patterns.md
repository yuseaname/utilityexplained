# Patterns

When to use: when writing new components, utility functions, or page routes.

## Component Props

Define a named type for any component with more than one prop. Use `import type` for type-only imports.

```typescript
import type { Post } from "@/lib/types";
import Link from "next/link";
import { formatDate } from "@/lib/utils";

type PostCardProps = {
  post: Post;
  trackingLabel?: string;
};

const PostCard = ({ post, trackingLabel }: PostCardProps) => {
  return (
    <article>
      <h2>{post.title}</h2>
      <time>{formatDate(post.date)}</time>
    </article>
  );
};
```

For single-prop or trivial components, inline the type directly in the parameter:

```typescript
export default function RootLayout({ children }: { children: ReactNode }) { … }
```

## Event Handlers & Environment Variables

Type event parameters with React generics. Access env vars with `||` or `??` fallbacks since they're always `string | undefined`.

```typescript
onChange={(e: React.ChangeEvent<HTMLInputElement>) => setQuery(e.target.value)}

const adClient = process.env.NEXT_PUBLIC_ADSENSE_CLIENT || "";
const adsEnabled = process.env.NEXT_PUBLIC_ADS_ENABLED === "true";
```

## Import Order

Follow this sequence in every file:

1. External packages (`import type { Metadata } from "next"`)
2. Internal absolute imports (`import { siteConfig } from "@/lib/site"`)
3. Relative imports (`import Header from "@/components/Header"`)

Always use the `@/*` path alias over relative paths like `../../lib/posts`.

## Pitfall

Never use `any`. With `strict: true`, every implicit `any` is a compile error. If a type isn't obvious, define it in `lib/types.ts` or use a local `type` alias — don't cast with `as`.