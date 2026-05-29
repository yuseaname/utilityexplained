# Utility Explained

Utility Explained is a Next.js-based static site that provides plain-English guides to help people understand their electricity, gas, and water bills. The project uses a content-driven architecture with static site generation for optimal performance and SEO.

## Tech Stack

| Layer | Technology | Version | Purpose |
|-------|------------|---------|---------|
| Runtime | Node.js | 18.x+ | JavaScript runtime environment |
| Framework | Next.js | 14.x | React framework with static site generation |
| Language | TypeScript | 5.x | Type-safe JavaScript development |
| Styling | Tailwind CSS | - | Utility-first CSS framework |
| Fonts | Google Fonts | - | Fraunces (headings) and IBM Plex Sans (body) |
| Analytics | Custom tracking | - | Basic page view and interaction tracking |
| SEO | Next.js metadata | - | OpenGraph, Twitter cards, sitemap generation |

## Quick Start

```bash
# Prerequisites
- Node.js 18.0 or higher
- npm or yarn package manager

# Installation
git clone https://github.com/your-org/utilityexplained.com
cd utilityexplained.com
npm install

# Development
npm run dev
# or
npm start

# Build for production
npm run build

# Static export (production build)
npm run export  # Creates 'out' directory with static files
```

## Project Structure

```
project/
├── app/                    # Next.js App Router structure
│   ├── [slug]/           # Blog post dynamic routes
│   ├── blog/             # Blog category and listing pages
│   ├── about/            # Static pages
│   ├── electricity-explained/
│   ├── gas-explained/
│   ├── water-explained/
│   ├── heating-cooling-explained/
│   ├── utility-bills-costs-explained/
│   ├── utilities-glossary/
│   ├── layout.tsx        # Root layout with fonts and metadata
│   ├── page.tsx         # Homepage
│   ├── sitemap.ts       # Dynamic sitemap generation
│   └── robots.ts        # robots.txt configuration
├── components/           # Reusable React components
│   ├── AdSlot.tsx       # Google AdSense integration
│   ├── Header.tsx       # Site navigation header
│   ├── Footer.tsx       # Site footer
│   ├── PostCard.tsx     Blog post preview cards
│   ├── ThemeToggle.tsx  # Dark/light mode toggle
│   └── [15 other components]
├── lib/                  # Shared utilities and data
│   ├── site.ts          # Site configuration and navigation
│   ├── posts.tsx        # All blog posts and helper functions
│   ├── utils.ts         # Utility functions (formatDate, etc.)
│   ├── types.ts         # TypeScript type definitions
│   ├── analytics.ts     # Analytics tracking configuration
│   └── generatedPosts/   # Auto-generated post content (not committed)
├── public/              # Static assets
│   ├── images/          # Article images, hero images
│   └── [other static assets]
├── content/             # Markdown content files (not used in current setup)
├── image-pipeline/     # Image generation utilities
└── [config files]
```

## Architecture Overview

This is a **static site generator** using Next.js with the App Router. Content is pre-rendered at build time for optimal performance and SEO. The architecture follows these patterns:

### Content Management
- **Posts**: Stored as TypeScript objects in `lib/posts.tsx` and dynamically generated from AI pipelines
- **Categories**: Each utility type (Electricity, Gas, Water, Heating/Cooling) has dedicated pillar pages
- **Dynamic Routes**: Blog posts use `[slug]/page.tsx` for individual article rendering
- **Static Generation**: All pages are pre-built at deploy time, zero runtime database

### Key Modules

| Module | Location | Purpose |
|--------|----------|---------|
| Post Data | `lib/posts.tsx` | Centralized blog post content and lookup functions |
| Site Config | `lib/site.ts` | Site metadata, navigation, and legal links |
| Layout System | `app/layout.tsx` | Root layout with fonts, metadata, and components |
| Component Library | `components/` | Reusable UI components for site-wide usage |
| Image Pipeline | `image-pipeline/` | AI-powered image generation for articles |

## Development Guidelines

### File Naming
- **Component files**: PascalCase (e.g., `Header.tsx`, `PostCard.tsx`)
- **Route files**: lowercase (e.g., `layout.tsx`, `page.tsx`, `sitemap.ts`)
- **Utility files**: camelCase (e.g., `utils.ts`, `analytics.ts`)
- **Type definitions**: PascalCase (e.g., `types.ts`)

### Code Naming
- **Component functions**: PascalCase (e.g., `export function Header()`)
- **Regular functions**: camelCase (e.g., `function formatDate()`)
- **Variables**: camelCase (e.g., `const featuredPosts`)
- **Constants**: SCREAMING_SNAKE_CASE (e.g., `const SITE_URL`)
- **Boolean props**: is/has/should prefix (e.g., `isLoading`)

### Import Order
1. External packages (React, Next.js)
2. Internal absolute imports (`@/`)
3. Relative imports
4. Type imports (with `type` keyword when possible)

### Import Pattern
```typescript
import React from 'react';
import Link from 'next/link';
import { siteConfig } from '@/lib/site';
import Header from '@/components/Header';
```

### TypeScript Configuration
- **Strict mode**: Enabled
- **Module resolution**: Bundler (for Next.js)
- **Path aliases**: `@/*` maps to project root
- **JSX preservation**: Enabled for React components

## Available Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server with hot reload |
| `npm run build` | Build application for production |
| `npm run start` | Start production server |
| `npm run export` | Generate static export to `out/` directory |
| `npm run lint` | Run ESLint to check code quality |

## Environment Variables

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `NEXT_PUBLIC_ADS_ENABLED` | No | Enable/disable Google AdSense | `true` |
| `NEXT_PUBLIC_ADSENSE_CLIENT` | No | AdSense publisher ID | `ca-pub-1234567890` |
| `NEXT_PUBLIC_AD_SLOT_*` | No | Ad unit slot IDs | `1234567890` |
| `NEXT_PUBLIC_EVENT_ENDPOINT` | No | Analytics tracking endpoint | `https://api.example.com/events` |
| `OPENAI_API_KEY` | Yes (for images) | OpenAI API key for image generation | `sk-...` |

## Key Features

### Content Strategy
- **Pillar Pages**: Comprehensive guides for each utility type
- **Blog Posts**: Specific topics within each utility category
- **FAQ Sections**: Common questions answered within articles
- **Related Content**: Automatic related posts based on categories

### Technical Features
- **Static Site Generation**: Fast load times, excellent SEO
- **Image Optimization**: Next.js automatic image optimization
- **Responsive Design**: Mobile-first with Tailwind CSS
- **Dark Mode**: Theme toggle for user preference
- **Accessibility**: Skip links, proper ARIA labels, semantic HTML

### Performance Optimizations
- **Static Export**: All pages pre-rendered to HTML
- **Image Optimization**: WebP format, lazy loading
- **Code Splitting**: Automatic Next.js code splitting
- **Caching**: Long-term caching strategies

## Deployment

### Static Site Deployment
The site uses `output: 'export'` configuration for static deployment:

1. Build the static site:
```bash
npm run build
npm run export
```

2. Deploy the `out/` directory to any static hosting:
- Netlify
- Vercel
- GitHub Pages
- Cloudflare Pages

### SEO Configuration
- **Sitemap**: Automatically generated at `/sitemap.xml`
- **Robots.txt**: Configured for search engines
- **Canonical URLs**: Properly set for all pages
- **OpenGraph**: Rich social media sharing support
- **Structured Data**: JSON-LD for organization schema

## Content Generation

The site uses an AI-powered content pipeline:
1. Content is generated using OpenAI models
2. Images are automatically created and optimized
3. Posts are structured with metadata, sections, and FAQs
4. All generated content is stored in TypeScript objects

## Additional Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Google AdSense Setup Guide](https://support.google.com/adsense/answer/48182)
- [Next.js Static Export Documentation](https://nextjs.org/docs/pages/api-reference/next-config/output)
- [TypeScript Configuration](https://www.typescriptlang.org/docs/handbook/intro.html)

## Skill Usage Guide

When working on tasks involving these technologies, invoke the corresponding skill:

| Skill | Invoke When |
|-------|-------------|
| nextjs | Configures Next.js App Router, routing, and static generation |
| node | Configures Node.js runtime and package management |
| react | Manages React components, hooks, and state patterns |
| tailwind | Applies Tailwind CSS utility classes and responsive design |
| frontend-design | Creates UI components with Tailwind CSS, typography, and responsive layouts |
| typescript | Enforces TypeScript strict mode and type-safe patterns |
| mapping-user-journeys | Maps in-app journeys and identifies friction points in code |
| instrumenting-product-metrics | Defines product events, funnels, and activation metrics |
| designing-onboarding-paths | Designs onboarding paths, checklists, and first-run UI |
| structuring-offer-ladders | Frames plan tiers, value ladders, and upgrade logic |
| tuning-landing-journeys | Improves landing page flow, hierarchy, and conversion paths |
| orchestrating-feature-adoption | Plans feature discovery, nudges, and adoption flows |
| inspecting-search-coverage | Audits technical and on-page search coverage |
| clarifying-market-fit | Aligns ICP, positioning, and value narrative for on-page messaging |
| crafting-page-messaging | Writes conversion-focused messaging for pages and key CTAs |
| mapping-conversion-events | Defines funnel events, tracking, and success signals |
| building-compare-hubs | Creates comparison and alternative pages for discovery |
| scaling-template-pages | Builds scalable, template-driven search pages |
| adding-structured-signals | Adds structured data for rich results |
