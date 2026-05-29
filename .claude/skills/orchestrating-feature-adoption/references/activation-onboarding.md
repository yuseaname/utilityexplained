# Activation & Onboarding

## When to use
Planning how first-time visitors discover and engage with a new site feature (theme toggle, calculator, comparison tool, newsletter signup).

## Patterns

### 1. Inline component placement (no disruptive modals)
Place new features in existing component slots so they feel native. ThemeToggle lives in `components/Header.tsx` alongside navigation — visitors see it immediately without any onboarding overlay. Follow this pattern for any new preference or tool: add to the header, footer, or article sidebar rather than using pop-ups.

```tsx
// Add a new toggle/tool to Header.tsx alongside ThemeToggle
<Header>
  <Logo />
  <Nav links={siteConfig.navigation} />
  <ThemeToggle />
  <NewFeatureButton />  {/* inline, not a modal */}
</Header>
```

### 2. localStorage-gated banners for one-time announcements
For features that need a brief introduction (e.g., a new bill calculator), use a client-only banner in `app/layout.tsx` gated behind a `localStorage` flag. The banner renders once, the user dismisses it, and it never reappears.

```tsx
"use client";
const [showBanner, setShowBanner] = useState(false);
useEffect(() => {
  if (!localStorage.getItem("upe-calculator-intro")) {
    setShowBanner(true);
  }
}, []);
```

### 3. Contextual first-use hints inside article pages
Instead of a global onboarding flow, surface feature hints within relevant content. A calculator component embedded in `app/blog/[slug]/page.tsx` on a "how to read your electric bill" post is its own discovery moment — no tooltip needed.

## Pitfalls
- **Avoid modals or full-screen overlays on article pages.** They interrupt reading and increase bounce rate. Progressive disclosure through inline placement is always preferred for a content-first site.
- **Don't gate features behind a "tour" or multi-step walkthrough.** This is a static informational site; visitors come to read, not to learn UI.