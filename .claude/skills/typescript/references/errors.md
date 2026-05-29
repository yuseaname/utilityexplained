# Errors

When to use: when diagnosing build failures, type errors, or runtime issues after adding new code.

## `TS2307: Cannot find module`

Cause: using relative paths instead of the `@/*` path alias, or importing from a file without an existing export.

```typescript
// Wrong — will fail with bundler resolution
import { posts } from "../../lib/posts";

// Correct
import { posts } from "@/lib/posts";
```

Also check that `tsconfig.json` has `"paths": { "@/*": ["./*"] }` — it does, so the alias should always work.

## `TS7006: Parameter implicitly has 'any' type`

Cause: strict mode requires explicit types on all parameters. This most commonly happens with Next.js page props.

```typescript
// Wrong
export default function Page({ params }) { … }

// Correct — type the params object
export default function Page({ params }: { params: { slug: string } }) { … }
```

## `TS2322: Type 'undefined' is not assignable`

Cause: `getPostBySlug` returns `Post | undefined` because the slug might not exist. Always handle the undefined case before using the post object.

```typescript
// Wrong — post could be undefined
const post = getPostBySlug(slug);
return <h1>{post.title}</h1>;

// Correct — guard before use
const post = getPostBySlug(slug);
if (!post) return notFound();
return <h1>{post.title}</h1>;
```

This pattern is already used in `app/blog/[slug]/page.tsx` — follow it for any new dynamic routes.

## `TS2345: Argument of type 'string' is not assignable to parameter of type 'never'`

Cause: calling `.map()` on `process.env.SOME_VAR` or other values TypeScript can't infer as arrays. This typically happens with `NEXT_PUBLIC_AD_SLOT_*` env vars passed to `<AdSlot>`.

Use a fallback or cast only at the component boundary:

```typescript
// The env var is string | undefined — the component should accept that
<AdSlot slot={process.env.NEXT_PUBLIC_AD_SLOT_TOP} />
```

If the component's prop type is too narrow, widen it to `string | undefined`.

## Pitfall

`npm run build` runs `tsc` implicitly — type errors surface as build failures, not warnings. Always run `npx tsc --noEmit` locally before pushing to catch errors early. The build output won't distinguish between a type error and a bundler error without scrolling.