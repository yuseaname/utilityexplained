---
name: node
description: Configures Node.js runtime and package management for the Utility Explained Next.js project
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

# Node.js Skill

Manages the Node.js runtime, npm dependencies, and scripts for this Next.js 14 static site. The project requires Node.js 18+ and uses npm as its package manager with a standard Next.js App Router setup.

## Quick Start

```bash
# Install dependencies
npm install

# Development server (hot reload)
npm run dev

# Production build + static export
npm run build

# Lint
npm run lint
```

## Key Concepts

- **Runtime**: Node.js 18.x+ required (check with `node -v`)
- **Package manager**: npm (lockfile is `package-lock.json`)
- **Framework**: Next.js 14 with `output: 'export'` for static HTML generation
- **TypeScript**: Strict mode, bundler module resolution, `@/*` path alias to project root
- **Scripts**: `dev`, `build`, `start`, `lint` defined in `package.json`

## Common Patterns

- Add a runtime dependency: `npm install <package>`
- Add a dev dependency: `npm install -D <package>`
- Add a component: create a `.tsx` file under `components/`, export a PascalCase function
- Add a route: create `page.tsx` under the appropriate `app/` subdirectory
- Add shared logic: create a `.ts` file under `lib/`
- Debug build failures: check TypeScript errors with `npx tsc --noEmit` before Next.js errors
- Verify static export works: `npm run build` and confirm the `out/` directory is populated