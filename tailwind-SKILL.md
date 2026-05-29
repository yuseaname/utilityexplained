---
name: tailwind
description: Applies Tailwind CSS utility classes and responsive design patterns to Next.js components in the Utility Explained project
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Tailwind Skill

This skill applies Tailwind CSS utility classes to style Next.js components and pages in the Utility Explained project. The codebase uses **custom CSS with BEM-like class names and CSS custom properties** defined in `app/globals.css`. All theming flows through `:root` / `[data-theme="dark"]` variables — never hardcode colors or spacing. Components use semantic `className` values that map to rules in `globals.css`. When adding Tailwind utilities, extend the theme config to reference the same CSS variables so styles stay consistent with the existing design system.

## Quick Start

1. Read `app/globals.css` to see all available classes, CSS variables, and responsive breakpoints.
2. Check existing components in `components/` for usage patterns (e.g., `PostCard.tsx`, `Header.tsx`).
3. Apply classes using `className="..."` on JSX elements — do not use inline styles or raw hex values.

## Key Concepts

### CSS Custom Properties (theming)
All colors, shadows, and radii are defined as CSS variables on `:root` (light) and `[data-theme="dark"]`:
- `--bg`, `--bg-alt` — background colors
- `--ink`, `--muted` — text colors
- `--accent`, `--accent-soft` — brand/interactive colors
- `--border`, `--shadow`, `--radius` — structural tokens

When configuring Tailwind, map these variables in `tailwind.config.ts` under `theme.extend` so utility classes resolve to the same values (e.g., `colors: { accent: 'var(--accent)' }`).

### Class naming convention
BEM-like single-dash naming: `.post-card`, `.post-card__image`, `.post-card__content`, `.category-badge--active`. Modifiers use `--`, blocks use no separator, elements use `__`.

### Responsive breakpoints
Two breakpoints in `globals.css` media queries:
- `960px` — collapses two-column layouts (e.g., article + TOC goes single-column)
- `720px` — stacks header/nav, tightens article body padding

Extend Tailwind's `screens` to match: `lg: '960px'`, `md: '720px'`.

### Font usage
- **Headings**: `--font-heading` (Fraunces) — applied via parent selectors like `.hero h1`, `.section h2`
- **Body**: `--font-body` (IBM Plex Sans) — set on `body`

## Common Patterns

| Pattern | Classes |
|---------|---------|
| Page wrapper | `className="container section"` |
| Card | `className="hero-card"` (has bg, border, radius, shadow) |
| Article card | `className="post-card"` with child `post-card__image` and `post-card__content` |
| Pill button | `className="button"` or `className="category-badge"` |
| Badge active state | `className="category-badge category-badge--active"` |
| Two-column article | `className="article-layout"` with `.article-body` + `.toc` children |
| FAQ accordion | `className="faq"` containing `.faq-item` > `.faq-question` + `.faq-answer` |
| Hero image | `className="article-hero"` (320px height, rounded, cover fit) |
| Ad slot | `className="ad-slot"` with child `.ad-slot__label` + `.ad-slot__box` |
| Sticky header | `className="site-header"` > `.header-inner` (uses `backdrop-filter: blur`) |

### Adding a new component style
1. Define the CSS class in `app/globals.css` using existing CSS variables.
2. Add a responsive override at the appropriate breakpoint if needed (`960px` or `720px`).
3. Use the class via `className` in your TSX component.
4. If the component needs dark mode support, rely on the CSS variables — they automatically adapt via `[data-theme="dark"]`.
