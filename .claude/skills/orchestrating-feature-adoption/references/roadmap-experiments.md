# Roadmap & Experiments

## When to use
Planning a sequence of feature rollouts, A/B tests, or incremental improvements — deciding what to build next and how to validate it before committing.

## Patterns

### 1. Content-driven feature sequencing
Align feature rollouts with content launches. When a new batch of articles ships (e.g., the electricity cost articles), introduce complementary features (rate calculator, comparison tool) alongside them. This pairs discovery with demand rather than building features for content that doesn't exist yet.

Check `lib/posts.tsx` for existing content categories — features should map to categories that already have 3+ posts:
- **Electricity** → rate calculator, TOU comparison
- **Gas** → cost estimator, provider comparison
- **Water** → usage tracker, conservation tips tool
- **Heating/Cooling** → efficiency calculator

### 2. Build-time feature flags for controlled rollouts
Use `NEXT_PUBLIC_<FEATURE>_ENABLED` environment variables to ship code behind a flag. The feature is built and deployable but inactive until the variable is set. This lets you merge feature PRs without exposing them to visitors.

```tsx
// In the component or page
if (process.env.NEXT_PUBLIC_CALCULATOR_ENABLED !== "true") return null;
```

### 3. Validate with analytics before expanding
Before promoting a feature site-wide (header placement, homepage widget), run it as an embedded component on 2–3 relevant blog posts for 1–2 weeks. Use `lib/analytics.ts` events to measure interaction rates. Only promote if the feature achieves meaningful engagement (>5% of page visitors interact).

## Pitfalls
- **Don't overbuild infrastructure for A/B testing on a static site.** There is no server-side experiment framework, no feature-flag service, and no runtime routing. A/B testing means building two variants and swapping via environment variable at build time — not dynamic server-side allocation.
- **Avoid scope creep — features must serve content.** Every new interactive element should answer "which article does this help a visitor understand better?" If there's no clear content connection, it's probably off-roadmap for a content-first site.