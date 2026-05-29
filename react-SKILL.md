---
name: react
description: Manages React components, hooks, and state patterns for the Utility Explained Next.js static site
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# React Skill

This skill covers React development within the Utility Explained project — a Next.js 14 static site using React 18, TypeScript, and Tailwind CSS. The site is fully pre-rendered at build time with zero runtime data fetching, so all components must be compatible with static generation.

## Quick Start

```bash
npm run dev      # Start dev server with hot reload
npm run build    # Production build (validates static generation)
npm run lint     # ESLint check
```

## Key Concepts

- **App Router**: All routes live under `app/` using Next.js 14 conventions. Pages export default components; layouts wrap children.
- **Static Generation Only**: No `getServerSideProps` or API routes. Every page is built at export time. Components must not depend on runtime-only APIs (browser-only globals, `window`, etc.) at the top level.
- **Server Components by Default**: Files under `app/` are React Server Components. Add `'use client'` only when a component needs interactivity (click handlers, hooks, state).
- **Path Aliases**: Import project modules via `@/lib/*`, `@/components/*`, etc. Never use relative imports that traverse beyond one level.
- **Styling**: Tailwind CSS utility classes exclusively. No CSS modules, no styled-components, no inline `style` objects unless dynamically computed.

## Common Patterns

### Component Structure

```tsx
// components/MyComponent.tsx
import { siteConfig } from '@/lib/site';

export function MyComponent({ title }: { title: string }) {
  return (
    <section className="max-w-3xl mx-auto px-4 py-8">
      <h2 className="text-2xl font-heading text-gray-900 dark:text-white">
        {title}
      </h2>
    </section>
  );
}
```

### Client Component with State

```tsx
'use client';
import { useState } from 'react';

export function ThemeToggle() {
  const [isDark, setIsDark] = useState(false);
  // ...
}
```

### Import Order

1. `react`, `next/link`, `next/image` (external)
2. `@/lib/*`, `@/components/*` (internal absolute)
3. `type` imports last, using the `type` keyword

### Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Component files | PascalCase | `PostCard.tsx` |
| Component functions | PascalCase | `export function PostCard()` |
| Route files | lowercase | `page.tsx`, `layout.tsx` |
| Props | camelCase, `is`/`has` for booleans | `isLoading`, `hasSidebar` |
| Constants | SCREAMING_SNAKE_CASE | `SITE_URL` |
