# Roadmap & Experiments

## When to use

When planning the next iteration of onboarding — testing whether a new flow improves content discovery before committing to a full build.

## Patterns

### A/B test welcome banner copy with URL param variants
Add a `?variant=a|b` param to the homepage that toggles between two banner headlines. Randomly assign on first visit via `Math.random() > 0.5`, store the assignment in `localStorage` (`ue_banner_variant`), and include the variant in all analytics events. Compare category click-through rates between variants.

```tsx
const variant = localStorage.getItem("ue_banner_variant") ||
  (Math.random() > 0.5 ? "a" : "b");
trackEvent("onboarding_banner_seen", { variant });
```

### Feature-flag new onboarding components behind a query param
Before adding a new component (e.g., category wizard, checklist) to the default build, gate it behind `?onboarding=wizard` or `?onboarding=checklist`. This lets you build and test on a live deployment without affecting all visitors. In production, simply omit the param to serve the stable experience.

### Phased rollout by content section
Roll out onboarding features one pillar page at a time — start with `/electricity-explained` (highest traffic), measure impact, then expand to gas and water. Track the metric "percentage of visitors who view 2+ pages" before and after adding the onboarding component to each section.

## Pitfalls

- **No server-side feature flags.** Since the site is statically exported, all flag checks must happen client-side. A user who bookmarks a `?onboarding=wizard` URL will always see the experimental UI — plan for this in copy and UX.
- **Avoid branching `lib/posts.tsx` by experiment.** Keep experiment logic isolated in components, not in shared data modules. A bad experiment should not risk corrupting the post catalog.