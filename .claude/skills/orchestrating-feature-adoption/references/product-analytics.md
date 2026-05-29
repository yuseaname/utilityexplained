# Product Analytics

## When to use
Setting up measurement for feature rollouts — defining what to track, how to instrument it, and how to interpret the results against site goals.

## Patterns

### 1. Event schema via `lib/analytics.ts`
All tracking goes through a single `sendEvent` function that posts JSON to `NEXT_PUBLIC_EVENT_ENDPOINT`. The schema is fixed: `{ event, label, value, href, extra, path, timestamp }`. New features must use this existing schema — do not introduce parallel tracking (no Google Tag Manager events, no inline `fetch` calls to other endpoints).

```tsx
// Every feature interaction maps to this schema
sendEvent({
  event: "faq_expanded",       // what happened
  label: "water-bill-breakdown", // which feature instance
  value: 1,                     // optional numeric value
  path: "/blog/water-bill-too-high",
});
```

### 2. Static-safe tracking — no runtime queries
This is a static-export site (`output: 'export'`). Analytics instrumentation must work without a server, database, or API. The `sendBeacon`/`fetch keepalive` approach in `analytics.ts` is the only approved pattern. Do not add client-side analytics SDKs that require initialization against a backend.

### 3. Feature flagging via environment variables
Follow the existing pattern: `NEXT_PUBLIC_ADS_ENABLED` gates `AdSlot.tsx` rendering. New features should use the same `NEXT_PUBLIC_<FEATURE>_ENABLED` pattern so they can be toggled at build time without code changes.

## Pitfalls
- **Don't track page views — Next.js static export handles that.** Focus events on *interactions* (toggle clicks, calculator submissions, FAQ expansions). Page view tracking is already handled by the Rybbit analytics script in `app/layout.tsx`.
- **Avoid sending personally identifiable information in events.** The analytics endpoint receives path and event data only — do not add email, ZIP code, or utility account details to any event payload.