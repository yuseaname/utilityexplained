---
name: typescript
description: Enforces TypeScript strict mode and type-safe patterns
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# TypeScript Skill

This project uses TypeScript 5.x in strict mode with the Next.js 14 App Router. All source files under `app/`, `components/`, and `lib/` are TypeScript. The `tsconfig.json` enables `strict: true`, bundler module resolution, and the `@/*` path alias mapping to the project root.

## Quick Start

```bash
npx tsc --noEmit    # Type-check without emitting
npm run build       # Build also validates types
npm run lint        # ESLint with eslint-config-next
```

## Key Concepts

- **Strict mode is non-negotiable** — `noImplicitAny`, `strictNullChecks`, and all other strict flags are enabled.
- **Path alias `@/*`** — prefer `@/lib/posts` over relative `../../lib/posts`.
- **Type imports** — use `import type { Post }` for type-only imports to avoid unnecessary runtime references.
- **Bundler resolution** — this is not Node classic resolution; imports resolve per the bundler config in `tsconfig.json`.

## Common Patterns

### Component Props

Define props as an inline type or named interface. Never use `any`.

```typescript
interface PostCardProps {
  post: Post;
  isFeatured?: boolean;
}
export function PostCard({ post, isFeatured = false }: PostCardProps) { … }
```

### Shared Types

Central types live in `lib/types.ts`. Import them from there rather than redefining.

```typescript
import type { Post, Category } from '@/lib/types';
```

### Event Handlers

Type event parameters with React's generic types rather than casting.

```typescript
onChange={(e: React.ChangeEvent<HTMLInputElement>) => setQuery(e.target.value)}
```

### Fetching / Data Access

Functions in `lib/posts.tsx` return typed arrays and objects. Destructure with explicit types when the return shape isn't obvious.

```typescript
import { getAllPosts, getPostBySlug } from '@/lib/posts';
const posts: Post[] = getAllPosts();
```

### Naming Conventions

- Component files and functions: `PascalCase` (`Header.tsx`, `PostCard.tsx`)
- Route and utility files: `camelCase` (`utils.ts`, `page.tsx`)
- Constants: `SCREAMING_SNAKE_CASE` (`SITE_URL`)
- Boolean props: `is`/`has`/`should` prefix (`isLoading`, `hasError`)
```
</thinking>

```markdown
---
name: typescript
description: Enforces TypeScript strict mode and type-safe patterns
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# TypeScript Skill

This project uses TypeScript 5.x in strict mode with the Next.js 14 App Router. All source files under `app/`, `components/`, and `lib/` are TypeScript. The `tsconfig.json` enables `strict: true`, bundler module resolution, and the `@/*` path alias mapping to the project root.

## Quick Start

```bash
npx tsc --noEmit    # Type-check without emitting
npm run build       # Build also validates types
npm run lint        # ESLint with eslint-config-next
```

## Key Concepts

- **Strict mode is non-negotiable** — `noImplicitAny`, `strictNullChecks`, and all other strict flags are enabled.
- **Path alias `@/*`** — prefer `@/lib/posts` over relative `../../lib/posts`.
- **Type imports** — use `import type { Post }` for type-only imports to avoid unnecessary runtime references.
- **Bundler resolution** — this is not Node classic resolution; imports resolve per the bundler config in `tsconfig.json`.

## Common Patterns

### Component Props

Define props as an inline type or named interface. Never use `any`.

```typescript
interface PostCardProps {
  post: Post;
  isFeatured?: boolean;
}
export function PostCard({ post, isFeatured = false }: PostCardProps) { … }
```

### Shared Types

Central types live in `lib/types.ts`. Import them from there rather than redefining.

```typescript
import type { Post, Category } from '@/lib/types';
```

### Event Handlers

Type event parameters with React's generic types rather than casting.

```typescript
onChange={(e: React.ChangeEvent<HTMLInputElement>) => setQuery(e.target.value)}
```

### Fetching / Data Access

Functions in `lib/posts.tsx` return typed arrays and objects. Destructure with explicit types when the return shape isn't obvious.

```typescript
import { getAllPosts, getPostBySlug } from '@/lib/posts';
const posts: Post[] = getAllPosts();
```

### Naming Conventions

- Component files and functions: `PascalCase` (`Header.tsx`, `PostCard.tsx`)
- Route and utility files: `camelCase` (`utils.ts`, `page.tsx`)
- Constants: `SCREAMING_SNAKE_CASE` (`SITE_URL`)
- Boolean props: `is`/`has`/`should` prefix (`isLoading`, `hasError`)