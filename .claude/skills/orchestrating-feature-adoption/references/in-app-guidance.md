# In-App Guidance

## When to use
Designing tooltips, help text, empty states, or contextual cues that teach visitors how to use a feature without leaving the page they're on.

## Patterns

### 1. FAQAccordion as built-in guidance
`components/FAQAccordion.tsx` is already rendered inside blog post pages. For any new interactive feature (calculator, comparison tool), embed a 2–3 question FAQ directly below the component to answer common "how do I…" questions without navigation.

### 2. Breadcrumbs for wayfinding
`components/Breadcrumbs.tsx` already provides hierarchical context on every article page (Home > Blog > Category > Post). When introducing new section-level features (e.g., a glossary lookup), ensure the breadcrumb path reflects the new navigation layer so visitors always know where they are.

### 3. Placeholder and empty-state copy for tools
Interactive components (calculators, estimators) should show clear, helpful empty states before the user inputs data. Use Tailwind utility classes consistent with the site's design system (Fraunces for headings, IBM Plex Sans for body) rather than generic "No data" messages.

```tsx
// Good empty state for a calculator
<p className="text-sm text-gray-500 dark:text-gray-400">
  Enter your monthly kWh usage above to estimate your electricity cost.
</p>
```

## Pitfalls
- **Never use tooltip libraries or hover-only guidance.** Many visitors are on mobile where hover doesn't exist. If a feature needs explanation, the explanation should be visible by default (inline text, FAQ accordion) or revealed on tap (disclosure/summary element).
- **Don't add guidance that duplicates the article content.** If the blog post already explains how to read a bill, a tooltip on the calculator repeating that explanation is noise, not help.