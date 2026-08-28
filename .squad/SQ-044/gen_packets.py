#!/usr/bin/env python3
"""SQ-044 wave-1 packet generator — 10 seats, distinct angles, read-only."""
import json
from pathlib import Path

REPO = "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained"
BRIEF = f"{REPO}/.squad/SQ-044/evidence-brief.md"
SNAP = f"{REPO}/.rybbit-snapshot-2026-08-27/snapshot.json"
ART = f"{REPO}/.squad/SQ-044/artifacts"
PARENT = ("Agency-grade audit + growth blueprint for utilityexplained.com "
          "Amazon Associates pivot (store ID utexplained-20). Enhancement-only, no rebuild.")

FACTS = [
    "Live Rybbit (2026-08-27): last7 860 sessions, bounce 91.3%, pages/session 1.10, duration 62s; Google referrer share only ~2.6%, Bing ecosystem ~68%.",
    "Zero amazon.com links in content/; hugo.toml amazon_tag is 'litwd-20' but the owner's real store ID is 'utexplained-20' (mismatch).",
    "AdSense was BLOCKED by Google ('Low value content', 2026-08-23) and has since been removed (git 6d4390c8, ADR-006) — the site is pivoting to Amazon Associates.",
    "Site: Hugo static, 121 content md files, 509 public HTML pages, 6 hub pages, 7 consolidated categories.",
]

def packet(role, mission, extra_context, *, writes=None, prohibited=("write_file", "edit_file"),
           criteria=None, authorized=None):
    p = {
        "role": role,
        "mission": mission,
        "parent_objective": PARENT,
        "context": f"Read the Commander evidence brief FIRST: {BRIEF} — it contains disk- and API-verified ground truth for this mission (analytics tables, monetization state, constraints). " + extra_context,
        "known_facts": FACTS,
        "resources": {"roots": [REPO], "notes": f"Analytics snapshot JSON (three windows): {SNAP}"},
        "constraints": [
            "Enhancement-only: no rebuild, no destructive changes.",
            "Never fabricate expertise, reviews, testing, prices, or firsthand experience.",
            "Label assumptions as assumptions; verified facts must carry file:line or command evidence.",
        ],
        "authorized_actions": authorized or [],
        "prohibited_actions": list(prohibited),
        "success_criteria": criteria or ["Findings delivered with per-item evidence (path/line/command/URL + date)."],
    }
    if writes:
        p["resources"]["write_paths"] = writes
        p["prohibited_actions"] = []  # writes confined mechanically to write_paths
    return p

packets = {}

packets["scout"] = packet("scout",
    "Recon the utilityexplained repo infrastructure: inventory content/ by section and type; map layouts/ (every baseof/single/list/partial — note anything product-box, CTA, ad-slot, disclosure, author-box related); summarize data/content-remediation-queue.json (how many pages queued, status values); list scripts/ and static/assets; note any monetization plumbing (add_product_boxes.py purpose). Deliver LEADS as a structured inventory — fast, broad, no deep reading.",
    "You are the pathfinder. Structure: inventory tables + one-line notes. Flag anything that looks like monetization infrastructure ready to activate.",
    criteria=["Structured inventory covering content/, layouts/, data/, scripts/, static/ with file counts and notable files.", "Monetization-relevant infrastructure identified with paths."])

packets["executor"] = packet("executor",
    "Mechanical ground-truth sweep of the repo with grep/wc/awk ONLY (quote every command + output): (1) per-page word counts across content/blog — distribution buckets (<600, 600-1200, >1200) and the 15 shortest pages; (2) slug-style split: numbered-prefix slugs vs clean slugs (exact counts); (3) internal-link counts: pages containing links to other /blog/ pages, top-10 most-linked-to pages, count of zero-inlink (orphan) pages; (4) frontmatter audit: % pages with date, lastmod, description, keywords; (5) disclosure/CTA presence per page (grep counts); (6) hardcoded price patterns ($XX.XX) in content — count + worst offenders; (7) sitemap.xml URL count vs public HTML count; (8) image count per page + missing-image references if cheaply checkable.",
    "Numbers must come from commands, never estimation. Deliver a facts table. gemma-style in-head counting is forbidden for every seat: counts arrive via quoted commands only.",
    criteria=["Facts table with every number traceable to a quoted command.", "Covers all 8 sweeps above."])

packets["prospector"] = packet("prospector",
    "TOTAL ingestion of content/**/*.md (all ~121 files, read IN FULL — your 1M window is the point). For EVERY page extract one table row: path | title | slug style | date/lastmod | approx words | primary reader question + search intent (informational / problem-urgency / how-to / comparison / definitional) | content type (explainer, how-to, fee-explainer, comparison, glossary, hub, legal, author) | quality flags (thin <600w, generic listicle, undated stats, stale-year refs, unsupported claims, reads-AI-generated) | Amazon monetization fit (NONE / LOW / MEDIUM / HIGH + which product family serves the intent: smart thermostat, smart plug, leak detector / water sensor, efficient HVAC, weatherization, metering tools, energy monitor) | cannibalization cluster id (pages answering the same question). WRITE the full table to your artifact file; envelope carries only the top-15 opportunities + top-15 worst pages + cluster summary.",
    "This is the dataset the whole audit builds on. Do not skip legal/author pages — classify them too (they matter for E-E-A-T).",
    writes=[f"{ART}/prospector-page-table.md"],
    criteria=["Complete per-page table artifact written covering every content md file.", "Envelope summarizes top opportunities, worst pages, cannibalization clusters."])

packets["tracer"] = packet("tracer",
    "Trace the MONEY PATH end-to-end, entry to termination, with file:line evidence at every hop: (1) visitor lands on a top article (use /blog/how-to-lower-electric-bill-complete-guide/) — which layout renders, what partials fire in what order; (2) where a purchase-intent reader would meet a product recommendation TODAY (trace layouts/ for product boxes, the add_product_boxes.py script, data files it reads/writes) and why they currently meet ZERO affiliate links; (3) the affiliate config thread: hugo.toml amazon_tag -> which partials consume it -> what would emit amazon URLs; (4) disclosure visibility on the article path (where affiliate-disclosure surfaces relative to where links would appear); (5) email capture: does any form/endpoint exist anywhere in layouts or static; (6) exit paths: related-posts, hub links, search. Deliver a hop-by-hop gap map of the conversion funnel + the exact files a link-insertion implementation would touch.",
    "One thread, to the bottom. Every claim: file:line.",
    criteria=["Hop-by-hop funnel trace with file:line evidence.", "Exact file list an affiliate integration must touch, derived from the trace."])

packets["cartographer"] = packet("cartographer",
    "Map the whole site architecture from content/ + public/: (1) hub-and-spoke structure of the 6 hubs vs blog posts vs category taxonomy (7 categories) — which hub owns which posts, coverage counts; (2) internal-linking GRAPH: build adjacency from markdown links, report hubs' out-degree, spokes' in-degree, orphan pages (zero inlinks), dead-end pages (zero outlinks); (3) cannibalization clusters: pages targeting the same query (e.g. numbered vs unnumbered twins like 15-why-utility-bill-higher-same-usage vs why-my-utility-bill-is-higher-with-same-usage); (4) URL taxonomy inconsistency: numbered prefixes, trailing-slash duality, category URL changes from the 17->7 consolidation (find any stale internal links pointing at retired category URLs); (5) depth distribution from homepage. Deliver the architecture map + a ranked list of the 10 highest-leverage structural fixes (each: affected pages, rationale).",
    "You draw the map others navigate by. Include a compact link-graph summary (nodes/edges counts, top hub vs top authority pages by inlinks).",
    criteria=["Architecture map with hub coverage, link graph stats, orphans, clusters, URL issues.", "Ranked top-10 structural fixes with affected pages + rationale."])

packets["verifier"] = packet("verifier",
    "Re-derive every compliance-relevant claim against the repo, verdict per item CONFIRMED / REFUTED / UNVERIFIED + evidence: (1) hugo.toml amazon_tag == 'litwd-20' while owner store ID is utexplained-20; (2) zero amazon.com links in content/; (3) affiliate-disclosure.md exists — quote its operative language; where does it render site-wide (header? footer? per-article near links?) — is placement FTC-clear ('clear and conspicuous, before the link') and does it contain Amazon's required 'As an Amazon Associate I earn from qualifying purchases' sentiment; (4) author pages: do any claim credentials, testing, or firsthand experience the repo cannot substantiate (quote exact claims — these are E-E-A-T fabrication risks); (5) methodology/editorial-policy pages: do they promise things the content does not do (e.g. 'we test products')?; (6) hardcoded prices/$-figures in content that will go stale or mislead (sample the worst 10); (7) claims of expertise/reviews/testing in blog content (grep 'we tested', 'our review', 'hands-on'); (8) robots/noindex/sitemap hygiene; (9) any AdSense residue after the removal commit. Also fetch Amazon Associates Operating Agreement current requirements (cite URL + date) and diff against the site's disclosure language.",
    "You are the checking seat: mechanical re-derivation, no judgment beyond the verdicts.",
    criteria=["Per-claim verdict table (CONFIRMED/REFUTED/UNVERIFIED) with quoted evidence.", "Amazon OA requirements fetched and diffed against site disclosure, cited."])

packets["analyst"] = packet("analyst",
    "External research (web_search/web_fetch, cite URL + retrieved date on every claim): (1) leading utility/energy-savings affiliate publishers — find 5-8 real ones (energy comparison sites, utility-bill-help content sites, HVAC/efficiency affiliates) and extract their content architecture, how they monetize utility-intent traffic (which programs beyond Amazon: energy-provider marketplaces, lead-gen, display), comparison-table patterns, trust signals; (2) Amazon Associates realistic economics for this niche's product families (smart thermostats ~commission rate, leak detectors, smart plugs, energy monitors — current rates, typical EPC if published); (3) keyword demand: the utility-bill question space — what high-volume queries does this corpus NOT cover (state-level average-bill pages, time-of-use, heat-pump/IRA rebates, EV charging, water-lease/infrastructure fees); (4) search-intent monetizability: which utility intents actually convert to product purchases vs pure information; (5) E-E-A-T patterns for YMYL-adjacent money-content publishers (author/bio/review-policy conventions). Deliver a research brief with a realistic revenue model skeleton (assumptions labeled).",
    "Depth over breadth on competitors; numbers with sources; no invented stats.",
    criteria=["Research brief with 5-8 competitor analyses, all claims URL+cited.", "Realistic monetization map of the utility-intent space + labeled revenue assumptions."])

packets["challenger"] = packet("challenger",
    "INDEPENDENT adversarial audit of this affiliate pivot's riskiest assumptions (work from the evidence brief facts + your own web research; do NOT assume any other worker's conclusions): (1) 68% of search traffic is Bing-ecosystem with Google at 2.6% — is Bing-only affiliate traffic durable, and what does Google's absence signal given the AdSense 'low value content' rejection?; (2) 91.3% bounce / 1.10 pages/session — does adding affiliate links to content failing intent produce anything but policy risk and zero CTR? What must be fixed FIRST for links to earn?; (3) the corpus has known AI-content remediation debt (site's own P0) — what is the realistic Google-policy and Amazon-brand risk of monetizing partially-remediated AI content?; (4) store-ID mismatch (litwd-20 vs utexplained-20) — blast radius if links ship before the fix; (5) single-affiliate-program dependency vs this niche's alternatives. For each: what would falsify the concern, earliest observable signal, and a mitigation. End with your verdict on the CURRENT trajectory: APPROVE / FIX / REJECT + the 3 conditions that would change it.",
    "You are the professional skeptic. Attack assumptions, not people. Every concern needs a falsifiable test.",
    criteria=["Each of the 5 risks analyzed with falsification test + early signal + mitigation.", "Final verdict APPROVE/FIX/REJECT with 3 change-conditions."])

packets["operator"] = packet("operator",
    "UX/CRO + template audit from layouts/ and rendered public/ HTML (read the actual templates and 5-6 representative rendered pages incl. the top-traffic article and a hub page): (1) article-page anatomy as rendered — hero/quick-answer position, TOC, heading hierarchy, scanability, table usage, images, related-posts; (2) trust-signal placement — author byline, editorial-policy/methodology links, dates, disclosure position; (3) CTA inventory — what clickable actions exist per article today and their visual weight; (4) email capture — existence, placement, offer; (5) mobile UX signals from the HTML/CSS (nav pattern, font sizes, tap targets, layout shifts, page weight: count/size of images and scripts per page); (6) homepage + hub-page hierarchy. Then spec the affiliate-ready article template: where product boxes, comparison tables, CTA buttons, and per-link disclosures belong for ethical CRO (above-the-fold disclosure, first product mention above fold for high-intent pages, etc). Deliver: findings + a concrete template spec (sections, order, components) the implementation phase can build against.",
    "You own the expedition deliverable: a UX findings doc + template spec. Judge as rendered experience, not code style.",
    criteria=["Rendered-experience findings for article/hub/home templates with example pages.", "Affiliate-ready article template spec: component order, CTA + disclosure placement rules."])

packets["mason"] = packet("mason",
    "Digest the site's PRIOR PLANNING ARTIFACTS into a structured 'already-planned vs done vs owed' inventory so the audit does not re-propose known work: read BLUEPRINT.md (62K), TRANSFORMATION_BLUEPRINT.md (32K), GROWTH_LOG.md (35K), IMAGE_AUDIT_REPORT.md (15K), MISSION_REPORT_2026-08-10.md, data/content-remediation-queue.json, playbook/ (skim index-level). Extract: (1) every initiative ever planned — one row: name, source doc, status (done/partial/planned/abandoned) with evidence (commit or doc section), stated goal/KPI; (2) the P0 editorial remediation scope from GROWTH_LOG Entry 9 — exactly what it demands; (3) remediation queue: count + status breakdown per page; (4) decisions/ADRs referenced (ADR-006 affiliate pivot etc.) and what they committed to; (5) what the site's own docs say about audience/personas. WRITE the full inventory to your artifact; envelope carries the top-line: what's done, what's owed, and the 5 biggest gaps between planned and shipped.",
    "Bulk digestion is your craft. Do not editorialize on quality — inventory only.",
    writes=[f"{ART}/mason-prior-art-inventory.md"],
    criteria=["Full prior-art inventory artifact written (every initiative, status, evidence).", "Envelope: done/owed top-lines + 5 planned-vs-shipped gaps."])

out = Path(f"{REPO}/.squad/SQ-044/packets")
out.mkdir(parents=True, exist_ok=True)
Path(f"{ART}").mkdir(parents=True, exist_ok=True)
for name, p in packets.items():
    (out / f"{name}.json").write_text(json.dumps(p, indent=1))
    print(f"wrote {name}.json ({len(json.dumps(p))} chars)")
print(f"\n{len(packets)} packets -> {out}")
