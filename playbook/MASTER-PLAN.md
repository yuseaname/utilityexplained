# AI Agent Traffic Playbook — UtilityExplained.com Implementation

**Source:** AI_Agent_Traffic_Playbook.html (18 Cheat Codes)
**Target:** utilityexplained.com (Hugo 0.141.0, adsense-base theme, 91 articles)
**Execution Model:** GLM-4.5 (cloud) via Ollama, 3 concurrent subagents
**Started:** 2026-08-10
**Reference Implementation:** rentingexplained.com/playbook/ (sister site, complete)

---

## Subagent Partition

### Subagent A — Content Production
**Cheat Codes:** #01 (Content Hydra), #03 (Content Cascade), #04 (Ghost Writers), #15 (Link Magnet), #16 (Cannibalizer)

| Deliverable | Path | Words |
|---|---|---|
| 5 Writer Personas | playbook/04-ghost-writers/personas.json | — |
| Utility Assistance Programs Guide | content/blog/utility-assistance-programs-liheap.md | 2000+ |
| Net Metering Explained | content/blog/net-metering-explained.md | 1500+ |
| Understanding Your Utility Bill (Pillar) | content/blog/complete-guide-understanding-utility-bill.md | 3000+ |
| EV Charging Impact on Electric Bill | content/blog/ev-charging-impact-electric-bill.md | 1500+ |
| How to Lower Your Electric Bill (Cannibalizer) | content/blog/how-to-lower-electric-bill-complete-guide.md | 2500+ |
| 2026 Utility Cost Index by State (Link Magnet) | content/blog/2026-utility-cost-index-by-state.md | 2000+ |
| Outreach Templates | playbook/15-link-magnet/outreach-templates.md | — |

### Subagent B — Analysis & Strategy
**Cheat Codes:** #02 (Topic Mine), #06 (Void Finder), #07 (Entity Heist), #08 (Moat Builder), #12 (Oracle), #13 (A/B Terminator), #14 (Trend Surfer)

| Deliverable | Path |
|---|---|
| Content Gap Analysis (30+ gaps) | playbook/02-topic-mine/content-gaps.json |
| 5 Content Briefs | playbook/02-topic-mine/briefs/*.md |
| Void Keywords (20+) | playbook/06-void-finder/void-keywords.json |
| Entity Knowledge Graph (50+) | playbook/07-entity-heist/entities.json |
| Competitive Analysis | playbook/08-moat-builder/competitive-analysis.json |
| Optimization Briefs | playbook/12-oracle/optimization-briefs.json |
| A/B Title Variants (20 pages) | playbook/13-ab-terminator/title-variants.json |
| Emerging Trends Report | playbook/14-trend-surfer/emerging-trends.json |

### Subagent C — Technical SEO & Distribution
**Cheat Codes:** #05 (SERP Parasite), #09 (Atomizer), #10 (Echo Chamber), #11 (Community), #17 (Schema Sorcerer), #18 (Velocity Hack)

| Deliverable | Path |
|---|---|
| Schema Audit | playbook/17-schema-sorcerer/audit.json |
| Featured Snippet Guide | playbook/05-serp-parasite/snippet-optimization.md |
| Distribution Assets (5 articles) | playbook/09-atomizer/assets/*.md |
| Social Listening Config | playbook/10-echo-chamber/listening-config.json |
| Community Answer Drafts (15) | playbook/11-community/answer-drafts/*.md |
| 30-Day Content Calendar | playbook/18-velocity/content-calendar.json |
| Quality Gate System | playbook/18-velocity/quality-gates.md |

---

## 30-Day Deployment Timeline (per playbook)

| Week | Focus | Cheat Codes | Target |
|---|---|---|---|
| 1 | Foundation & Recon | #02, #06, #08, #17, #04 | 50+ voids mapped |
| 2 | Content Engine | #01, #03, #17, #12 | 15-25 new pages |
| 3 | Distribution | #09, #10, #11, #13 | 90-200 derivative assets |
| 4 | Optimization & Scale | #05, #14, #15, #16, #18 | 60-100+ total new pages |
