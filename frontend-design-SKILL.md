---
name: frontend-design
description: Creates UI components with Tailwind CSS, typography, and responsive layouts for the Utility Explained static site.
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Frontend Design Skill

Builds and styles UI components for the Utility Explained Next.js static site using Tailwind CSS, Google Fonts (Fraunces headings, IBM Plex Sans body), and a mobile-first responsive approach. All components must support dark mode via the `dark:` variant and produce semantic HTML with proper ARIA attributes.

## Quick Start

```bash
npm run dev          # Start dev server at localhost:3000
npm run build        # Verify production build succeeds
```

Components live in `components/` (PascalCase filenames). Route-level markup goes in `app/` (lowercase filenames). Site-wide layout, fonts, and metadata are configured in `app/layout.tsx`.

## Key Concepts

- **Mobile-first**: Base styles target small screens; use `md:` and `lg:` breakpoints for larger viewports.
- **Dark mode**: All color values must have a `dark:` counterpart. Theme toggle state is managed in `ThemeToggle.tsx`.
- **Typography scale**: Use `font-heading` (Fraunces) for headings, body default (IBM Plex Sans) for prose.
- **Static export**: `output: 'export'` is enabled — no client-side data fetching, no API routes.
- **Imports**: Use `@/` path alias for all internal imports. Order: external packages, `@/` imports, relative imports, type imports.
- **Naming**: Components PascalCase (`PostCard.tsx`), utilities camelCase, constants SCREAMING_SNAKE_CASE, booleans `is`/`has`/`should` prefixed.

## Common Patterns

### Component skeleton

```tsx
import React from 'react';
import { siteConfig } from '@/lib/site';

export function MyComponent({ title }: { title: string }) {
  return (
    <section className="mx-auto max-w-3xl px-4 py-8">
      <h2 className="font-heading text-2xl font-bold text-gray-900 dark:text-gray-100">
        {title}
      </h2>
    </section>
  );
}
```

### Color pattern

Use `gray-900` / `gray-100` for text, `gray-50` / `gray-900` for backgrounds. Accent colors reference the site's utility categories — blue for electricity, orange for gas, cyan for water, red for heating/cooling.

### Responsive container

```
mx-auto max-w-4xl px-4 sm:px-6 lg:px-8
```

### Prose sections

Article content uses `<article>` with `prose dark:prose-invert max-w-none` classes (if `@tailwindcss/typography` is available) or manual spacing: `space-y-4 text-gray-700 dark:text-gray-300 leading-relaxed`.

### Semantic requirements

- Use `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>` instead of generic `<div>` where appropriate.
- Include `aria-label` on landmark regions.
- Ensure skip-link functionality is preserved in the root layout.
