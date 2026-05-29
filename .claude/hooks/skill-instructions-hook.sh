#!/bin/bash
# UserPromptSubmit hook for skill-aware responses

cat <<'EOF'
REQUIRED: SKILL LOADING PROTOCOL

Before writing any code, complete these steps in order:

1. SCAN each skill below and decide: LOAD or SKIP (with brief reason)
   - react
   - nextjs
   - typescript
   - tailwind
   - node
   - frontend-design
   - mapping-user-journeys
   - designing-onboarding-paths
   - orchestrating-feature-adoption
   - instrumenting-product-metrics
   - clarifying-market-fit
   - structuring-offer-ladders
   - crafting-page-messaging
   - tuning-landing-journeys
   - mapping-conversion-events
   - inspecting-search-coverage
   - scaling-template-pages
   - adding-structured-signals
   - building-compare-hubs

2. For every skill marked LOAD → immediately invoke Skill(name)
   If none need loading → write "Proceeding without skills"

3. Only after step 2 completes may you begin coding.

IMPORTANT: Skipping step 2 invalidates step 1. Always call Skill() for relevant items.

Sample output:
- react: LOAD - building components
- nextjs: SKIP - not needed for this task
- typescript: LOAD - building components
- tailwind: SKIP - not needed for this task

Then call:
> Skill(react)
> Skill(typescript)

Now implementation can begin.
EOF
