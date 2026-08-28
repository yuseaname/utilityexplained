#!/usr/bin/env python3
"""SQ-045 content-audit fleet — 7 seats on distinct quality angles."""
import json
from pathlib import Path

REPO = "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained"
METRICS = f"{REPO}/.squad/content-metrics.md"
METRICS_JSON = f"{REPO}/.squad/content-metrics.json"
ART = f"{REPO}/.squad/SQ-045/artifacts"
PARENT = "Full-site content-quality audit of utilityexplained.com: identify thin, incomplete, or improvable content on every page; classify retain/improve/consolidate/redirect/remove/replace with specific prescriptions."

FACTS = [
    "Deterministic metrics (2026-08-27, scripts/content_quality_metrics.py): 97 blog articles; 56 under 800 body words; 19 with zero outbound sources; 8 with stale-year refs and no current-year counterpoint; 0 placeholder patterns; all pages updated within 30 days.",
    "The site recently went through an AI-bloat trim (-11.5K lines): many short pages are CONCISE by design — judge whether shortness is tight or incomplete, never assume short = bad.",
    "Existing remediation queue (data/content-remediation-queue.json): 6 P2 'missing_sources' items.",
    "Context: affiliate pivot shipped 2026-08-28 (14 Amazon links, 7 monetized pages). Traffic 860 sess/wk, bounce 91.3%.",
]

def packet(role, mission, extra, *, writes=None, criteria=None):
    p = {
        "role": role,
        "mission": mission,
        "parent_objective": PARENT,
        "context": f"Commander metrics ground truth (READ FIRST, every number pre-verified): {METRICS} (human table) / {METRICS_JSON} (machine). " + extra,
        "known_facts": FACTS,
        "resources": {"roots": [REPO]},
        "constraints": [
            "Read-only audit — no content edits. Writes only to your granted artifact path.",
            "Every page-level claim cites the file; every quality judgment gives a SPECIFIC prescription (what section/table/source/link to add), not 'improve it'.",
            "Do not propose fabricated expertise, testing, or pricing.",
        ],
        "authorized_actions": ["read_file", "list_dir", "search", "run_command", "web_search", "web_fetch"],
        "prohibited_actions": ["write_file", "edit_file"],
        "success_criteria": criteria or ["Per-page findings with file citations + specific prescriptions."],
    }
    if writes:
        p["resources"]["write_paths"] = writes
        p["prohibited_actions"] = []
    return p

packets = {}

packets["prospector"] = packet("prospector",
    "Read ALL 97 blog articles IN FULL. For EVERY page deliver one row in an artifact table: path | words (from metrics) | VERDICT (retain / improve / consolidate-into:[target] / replace / remove) | quality flags (thin-incomplete: topic needs more depth; thin-but-tight: short is correct; generic: says nothing a competitor doesn't; incomplete: section promised but missing, question raised but unanswered; outdated: stats/years stale; unsourced: factual claims without sources) | THE prescription: the 1-3 highest-leverage specific improvements (exact section to add, exact table to build, exact source type to cite, exact link to wire). Envelope: the 15 highest-leverage improvement prescriptions + the 10 pages that should merge/die + distribution counts by verdict.",
    "You are the backbone of this audit. The metrics table gives you words/sources/dates — spend your reading on JUDGMENT: does each page fully answer its title's promise? What would make a reader say 'this is the page I needed'?",
    writes=[f"{ART}/prospector-quality-table.md"],
    criteria=["All 97 pages in the artifact table with verdict + flags + specific prescription.", "Envelope: top-15 prescriptions, 10 merge/die candidates, verdict distribution."])

packets["tracer"] = packet("tracer",
    "Reader-journey completeness audit, topic by topic (not page by page): for each of the 8 core topics (high electric bill / high water bill / high gas bill / reading each bill type / lowering bills / HVAC troubleshooting / fees & charges / rates & plans), walk the journey a real reader takes: entry query -> diagnosis -> understanding the bill -> action -> tools. Report: (1) journey gaps — natural follow-up questions with NO page to serve them (each: the query, the nearest existing page, whether it's a new-page need or an existing-page expansion); (2) dangling promises — any page referencing 'we cover X' / 'see our guide to X' where X doesn't exist or is thin; (3) dead ends — high-traffic pages whose topic naturally continues elsewhere on-site but link nowhere; (4) series inconsistencies — pages in the same series (numbered 01-50) with mismatched depth/format. File:line for every finding.",
    "You are one thread to the bottom: the READER's path through the site, not the files.",
    criteria=["Per-topic journey maps with gaps, dangling promises, dead ends, series inconsistencies — all file:line cited."])

packets["cartographer"] = packet("cartographer",
    "Cluster-level quality design: (1) for EACH cannibalization/overlap cluster (you mapped 12 in the prior audit — READ-ELEC, FEES, HIGH-ELEC, SAVE, COST, SEWER, THERMOSTAT, etc.): name the pages, their word counts (metrics table), which is strongest, and the consolidation design: target page + what each absorbed page contributes (a table? a section? nothing?); (2) weakest-link analysis: for each of the 6 hubs, its 3 weakest linked pages (by quality, not just length); (3) CLUSTER-READ-ELEC final merge plan (7 pages -> 1): exact section outline of the merged page built from the best parts of each; (4) category quality distribution: avg words/sources per category, categories with systematic thinness. Envelope: ranked consolidation queue (which merges first, expected page-count reduction).",
    "You own the SET-level judgment: which pages together form one great page.",
    criteria=["Per-cluster consolidation designs with contributions mapped.", "Ranked merge queue + weakest-links-per-hub."])

packets["verifier"] = packet("verifier",
    "Mechanical quality re-derivation (CONFIRMED/REFUTED/UNVERIFIED per finding): (1) empty-or-near-empty sections: every H2 followed by <40 words before the next H2 (write and run a grep/awk script over content/blog/ — quote it); (2) broken internal links: every markdown /blog/ link whose target file does not exist (script it against the slug list); (3) TOC promises: pages whose headings promise something the section doesn't deliver (check the 20 thinnest from metrics); (4) stale-data scan: pages citing 2023-or-older data with no 2025/2026 counterpoint (the metrics table names 8 — verify each, quote the stale line); (5) FAQ quality: FAQs whose answers repeat the body verbatim vs add value (sample 15); (6) image coverage: topical pages where a diagram/table is the natural format but none exists. Every finding: file:line + quoted text.",
    "Mechanical re-derivation only — scripts and quoted evidence, no vibes.",
    criteria=["Script-backed findings for all 6 sweeps, each file:line + quote."])

packets["mason"] = packet("mason",
    "Bulk claim-level extraction across ALL 97 articles — the sourcing debt map: (1) every specific factual claim (number, %, $ range, date, 'studies show') WITHOUT a nearby source — write them to your artifact grouped by file, quoting the claim (target: complete inventory of the worst 25 files by claim density; skim the rest); (2) claims whose source IS cited but is older than 2024 — flag for refresh; (3) for each of the 19 zero-source pages (metrics table names them): the 3 most load-bearing claims that most need a citation and WHAT authoritative source would cover it (EIA / DOE / ENERGY STAR / EPA WaterSense / utility tariff — name the specific agency dataset or page type, you may web_fetch to confirm it exists); (4) dollar-figure inventory: count of $-ranges per page, which pages are most price-dense (stale-price risk). Artifact = the full map. Envelope: top-10 most-unsourced-load-bearing claims sitewide.",
    "Bulk extraction is your craft — completeness over commentary.",
    writes=[f"{ART}/mason-sourcing-debt-map.md"],
    criteria=["Claim-level artifact: unsourced claims by file, stale sources, zero-source page prescriptions, price-density inventory.", "Envelope: top-10 worst unsourced claims."])

packets["analyst"] = packet("analyst",
    "The benchmark bar (web research, cite URL + retrieved date): for the 8 core topics (high electric/gas/water bill, reading bills, lowering bills, HVAC troubleshooting, fees, rates & plans) find the BEST-ranking competitor/AUTHORITY page per topic (utility company help centers, energy.gov, authoritative publishers) and extract: section structure, depth (approx words), what data they cite, what formats they use (calculators, tables, videos), freshness signals. Deliver: per-topic 'complete treatment checklist' — the sections/data/formats a genuinely complete page carries — plus the 5 formatting standards the best pages share. This is the bar our prescriptions get measured against. NO recommendations about our site beyond mapping the gap themes — prescription work belongs to other seats.",
    "Depth over breadth: 8 topics, the actual best page for each, verified by fetching it.",
    criteria=["8 topic benchmark checklists with cited sources.", "Shared formatting standards of top pages."])

packets["challenger"] = packet("challenger",
    "Adversarial prioritization attack (independent — work from the metrics table + your own reading; ignore other seats): the audit will produce ~100 improvement prescriptions and the site cannot do them all. Attack: (1) which 'improvements' are TRAPS — polishing pages that should merge or die instead (name candidates from the thin list: when is 300 words the right answer vs a symptom?); (2) opportunity-cost ranking — with 860 sessions/wk and 91% bounce, what does the traffic data say matters first (top 15 pages carry most traffic — but does improving them move revenue, or is the constraint discovery/indexation?); (3) the Bing-dependency angle: does content quality even move Bing rankings the way it moves Google, and what does that imply for prioritization?; (4) kill-criteria: what evidence would justify DELETING a page vs fixing it. End with your verdict on where the first 40 hours of improvement work should go (one paragraph, concrete).",
    "Attack the plan before it exists: the trap list, the ranking logic, the kill-criteria.",
    criteria=["Trap list with named candidates.", "Opportunity-cost logic tied to traffic reality + first-40-hours verdict."])

out = Path(f"{REPO}/.squad/SQ-045/packets")
out.mkdir(parents=True, exist_ok=True)
Path(ART).mkdir(parents=True, exist_ok=True)
for name, p in packets.items():
    (out / f"{name}.json").write_text(json.dumps(p, indent=1))
    print(f"wrote {name}.json")
