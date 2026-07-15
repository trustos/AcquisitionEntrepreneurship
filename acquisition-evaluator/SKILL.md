---
name: acquisition-evaluator
description: "Evaluate a potential software acquisition (a SaaS, app, website, plugin, API, or online business the user is thinking of buying) against a weighted 0-100 scorecard tuned for a technical founding team that can build almost anything but is not sales or marketing heavy. It researches public unknowns, asks the user only what they can realistically answer, scores build-and-scale fit, retention, unit economics, moat, deal terms and adverse-selection risk, flags every unknown honestly instead of guessing, and generates a prioritized list of due-diligence questions to send the seller. Use whenever the user shares a deal or a listing (Acquire.com, Flippa, Empire Flippers, MicroAcquire, Tiny Acquisitions), an asking price or revenue multiple, or asks to screen, vet, score, benchmark, or run due diligence on a company, app, or product they might buy or acquire."
license: "Proprietary — built for the user's acquisition strategy."
---

# Acquisition Evaluator

A benchmark for deciding whether a small software business is worth buying — built for a **technical founding team that can design, build, modernize, and scale software (web, mobile, AI/ML, cloud/infra) but is deliberately not a sales/marketing shop.** The whole point is to turn a fuzzy target full of unknowns into an honest, comparable 0–100 score, an explicit list of what is still unknown, and a set of questions to put to the seller.

The intellectual backbone is three ideas from the user's own research:

1. **Bending Spoons' filter:** buy proven product-market fit with loyal, low-churn, organically-acquired users; win on operational excellence, not on discovering a market. Avoid ad/channel-dependent revenue that is hard to forecast.
2. **"Buy then build" reality for a small team:** the asset is customers and cash flow, not code; the biggest self-inflicted risk is the urge to rewrite; and the questions that matter are *why is it really for sale* and *can WE, specifically, operate and grow it*.
3. **Disciplined Entrepreneurship rigor:** be honest and evidence-based about the customer, the unit economics (LTV should be at least ~3x the cost to acquire a customer), and the "Core" — the durable advantage. Never fabricate; mark what is verified vs assumed vs unknown.

## When this triggers

Use it whenever the user is weighing a specific target: a listing URL, a screenshot, an asking price, a "should we buy this?", or a pile of half-known facts. If the user has several candidates, run it per candidate so the scores are comparable.

---

## The team competence profile (this is a config — edit it as the team changes)

The single most important lens is **"can THIS team build and scale it?"** Score every target against this profile, which the user confirmed:

**Strong / in the wheelhouse (value creation is an engineering & product problem):**

- Web / full-stack (front-end + back-end, APIs, relational/NoSQL databases)
- Mobile (native and cross-platform iOS/Android)
- AI / ML / data (models, data pipelines, analytics, LLM-based features)
- Cloud / DevOps / infra (scaling, distributed systems, performance, reliability)

**Weak / avoid (success depends on skills the team does *not* have):**

- Sales-led go-to-market (enterprise field sales, SDR teams, long human sales cycles)
- Marketing/SEO/content-dependent growth (the business lives or dies by paid ads, Google rankings, or a content treadmill)
- Non-software moats the team can't operate or replicate (exclusive supplier deals, brand/celebrity, regulatory licenses, physical/logistics, heavy compliance domains)

**The rule of thumb:** a target scores well on fit when the path to more value is *"modernize it, make it faster/more reliable, add the obvious features, add AI, improve UX, raise the too-low price"* — things this team can just *do*. It scores badly when the path to value is *"hire a sales team"* or *"win at SEO"* — things this team can't. Be blunt about this even when the business is otherwise attractive; buying something you can't grow means buying a job, not an asset.

In v2 this is enforced by two sharp gates instead of one vague judgment: **operable** (can the team run/maintain the stack) and **growth_lever_fits** (is the target's #1 customer-acquisition channel product-led/organic — which they can run — versus sales / SEO-content / paid ads / a personal audience — which they can't). `growth_lever_fits = false` is the "buying your weakness" cap → PASS.

---

## Saving evaluations (config)

Every evaluation should be **saved**, not just shown — the sources, the scores, the unknowns, and the seller questions are worth keeping and comparing across deals.

- **Default location:** a `deals/` folder inside the active working / connected project folder. If a `deals/` folder (or a location the user chose earlier in the session) already exists, save there without asking. If none exists, ask the user once where to create it (default: `deals/` in the project folder), then reuse that choice.
- **What gets written** (via `scripts/save_evaluation.py`): a per-deal folder `deals/<target>_<date>/` with `scorecard.md` (human-readable) and `record.json` (structured — scores, gates, verdict, unknowns, seller questions, the inputs you were given, and every source), plus a row appended to a combined `deals/deal-log.xlsx` so deals are sortable side by side.
- **Capture sources as you go:** keep a running list of title + URL for everything you rely on in Phase 2, so it can be saved in the record. This is part of "honest feedback" — the evidence trail travels with the score.

---

## Workflow

Run these phases in order. The guiding principle throughout: **the user has limited knowledge of each target, so do the legwork yourself, ask the user only what they can actually answer, and route everything else to the seller.** Never fill a gap with a guess — an honest "unknown" is more valuable than a confident fabrication.

### Phase 1 — Intake and classify

Extract every known fact from whatever the user gave you (URL, description, numbers, screenshots) into the rubric's dimensions. Then classify the **target type**, because it changes how you score:

- micro-SaaS / B2B tool · consumer or prosumer app (web/mobile) · developer tool / API / infra · marketplace · plugin/extension (WordPress, Shopify, browser) · content/affiliate site · e-commerce/DTC · newsletter/media.

Note the type explicitly. Content/affiliate, e-commerce, and FBA are marketing-and-channel businesses — flag immediately that they sit against the team's weakness, regardless of other merits.

### Phase 2 — Research the public unknowns (do this before asking the user much)

Fill as many gaps as you can from public sources so you don't burden the user. If subagents are available, fan out in parallel; otherwise search inline. Target:

- **Product & reputation:** what it does, reviews (G2, Capterra, Trustpilot, app stores, Reddit), user sentiment, obvious complaints, how loved/sticky it is.
- **Category & competitors:** who else does this, is the space growing or dying, is AI a tailwind or an existential threat to it.
- **Tech & scale signals:** likely stack (BuiltWith/Wappalyzer-style reasoning from the site), app-store ranks/reviews as a proxy for scale, whether the architecture looks like something the team can own.
- **Acquisition channel:** how customers actually arrive (organic/word-of-mouth/product-led vs paid/SEO/single-platform). This drives both the moat score and the fit score.
- **Comparable multiples:** what similar assets sell for now, to sanity-check the asking price. See `references/due-diligence.md` for current benchmark ranges.

For every fact, track provenance: **VERIFIED** (primary/reliable source), **ASSUMED** (reasonable inference — say so), or **UNKNOWN**. Carry these tags into the output.

### Phase 2.5 — Verify & reconcile every figure (do NOT skip — a real deal was mis-scored here)

Numbers are the foundation of the score, and they are often wrong. One evaluation was scored on figures a marketplace tool under-reported by **100×** (a $100k business shown as $1k). Before any number feeds the rubric:

- **Two-source rule:** never trust a single tool/field for a dollar figure — cross-check against a second or authoritative source. For **TrustMRR specifically, read the listing's `.md` profile** (`trustmrr.com/startup/<slug>.md`) or the live page, **not** the MCP tool, whose dollar fields are unreliable. Prefer the seller's own source data (Stripe/bank) over any marketplace badge.
- **Arithmetic sanity check** with the bundled script: `python scripts/verify_figures.py --subs .. --arpu .. --mrr .. --asking .. --multiple ..`. It flags impossibilities (subs × ARPU ≈ MRR; MRR × 12 ≈ ARR; asking ÷ annual-revenue ≈ the stated multiple). If it flags, STOP and reconcile — do not score.
- **Grade the revenue evidence**, don't just tick a box: `buyer_verified` (reconciled from source) > `marketplace_attested` (a "Stripe-verified" badge — attested, not reconciled) > `seller_claimed` > `none`. Only `buyer_verified` lets a deal reach STRONG. (40%+ of small deals carry inflated figures — a badge is not source verification.)

### Phase 3 — Ask the user (one focused round, only what they can answer)

Use the `AskUserQuestion` tool for a single round of up to ~4 questions. Ask only things the *user* plausibly knows or can quickly get — not things only the seller knows (those become seller questions in Phase 6). Good things to ask the user:

- Do they have any private material to share (the full listing, seller-provided P&L / MRR, analytics screenshots, a data room)? This unlocks the highest-value verification.
- Asking price and whether there's a budget ceiling for this deal.
- Anything they already know or specifically worry about; any personal interest/domain knowledge in the space (a mild fit tailwind).
- How far to take it now: quick screen vs full workup.

Keep it short. If the user already provided enough, skip or shrink this round. Don't interrogate them about things they can't know — that's the seller's job.

### Phase 4 — Score against the rubric (v2: nine dimensions)

Read `references/rubric.md` for the **nine** dimensions, weights, and 0–5 anchors. Score each 0–5 with a **confidence** (high/med/low/unknown). **The golden rule for unknowns: score an unknown dimension NEUTRAL (2) with confidence `unknown` — never 1.** A `1` asserts you have evidence it is *bad*; absence of evidence is not that. (Scoring unknowns as 1 was the single biggest source of false PASSes in v1.)

Compute deterministically — never by hand — and pass the budget so affordability is scored, not ignored:

```bash
python scripts/score.py --input scores.json   # run --example for the exact shape
```

`scores.json` holds the nine dimensions (score + confidence), the gate values, and `budget_ceiling` / `asking_price` / `financing_possible`. The script returns the merit total, completeness %, gate results, affordability, and the verdict — including the special states **OUT OF BUDGET**, **INSUFFICIENT DATA**, and **(provisional)**.

### Phase 5 — Apply gates and set the verdict (v2)

Gates come in two kinds (full definitions + decision trees in `rubric.md`):

- **Kill gates — a *verified-negative fact* caps merit.** `operable=false` or `growth_lever_fits=false` → **PASS**. `ip_transferable` / `value_transfers` / `not_fragile` = false, or `revenue_evidence=contradicted` → **MARGINAL**. (`not_fragile` trips only on a *structural* single-point-of-failure — platform lock, one customer >~30%, a sole non-transferable channel — not ordinary early-stage thinness.)
- **Verification gates — an *unknown* does NOT lower merit.** It marks the verdict **(provisional)** and blocks STRONG until you verify. This is deliberate: an unverified 82 should read "PROMISING (provisional)", not be dragged down to look like a mediocre 60. `revenue_evidence` must be `buyer_verified` to clear.
- **Affordability** (computed from the budget): asking > 1.25× ceiling with no financing path → **OUT OF BUDGET**, shown next to the merit tier (e.g. "STRONG on merits, but 33× budget").
- **Completeness < 45% → INSUFFICIENT DATA** — gather more before trusting any tier.

Verdict tiers: **STRONG 75+ · PROMISING 60–74 · MARGINAL 45–59 · PASS <45.** STRONG is only reachable once the gates are *verified* — so a first-pass screen tops out at "PROMISING (provisional)". **Run the re-score loop:** after the seller answers the Phase-6 questions, resolve the gates (revenue → `buyer_verified`, IP/transfer/fragility → true/false) and re-run the scorer. That is how a deal actually earns STRONG.

### Phase 6 — Honest unknowns + seller questions

Two required outputs that make this useful rather than a vanity score:

- **Unknowns & sensitivity:** list what's still unknown, why it matters, and how it would move the score if the answer is good vs bad (e.g., "if churn is >5%/mo this drops from Promising to Pass"). This is where honesty lives — enumerate gaps, don't paper over them.
- **Seller due-diligence questions:** draw from `references/seller-questions.md`, tailored to *this* target's specific unknowns and red flags, prioritized (deal-breakers first), each tagged with the dimension it resolves and a one-line "why we're asking." This is the artifact the user actually sends the seller.

### Phase 7 — Output

Assemble the report using `assets/scorecard-template.md` and present the scorecard inline: verdict + score, the dimension table, the fit-to-build read, what's verified vs assumed vs unknown, the prioritized seller questions, and the recommended next step. Keep the tone the way the user likes it: concise, direct, honest about uncertainty.

### Phase 8 — Save the record (always)

Persist every evaluation so it isn't lost and can be compared with other deals. Don't make this optional — saving the sources and scores is the point.

1. **Pick the save location** per the config above: reuse an existing `deals/` folder (or the user's earlier choice); otherwise ask once (default `deals/` in the project folder), then remember it for the session.
2. **Assemble the record JSON**, capturing everything worth keeping:

```
{
  "target": "example.com",
  "date": "YYYY-MM-DD",
  "analyst": "who ran it (optional — for team attribution)",
  "type": "micro-SaaS | app | content | ...",
  "asking_price": 1234,
  "budget_ceiling": 3000,
  "financing_possible": false,
  "verdict": "STRONG | PROMISING | MARGINAL | PASS | OUT OF BUDGET | INSUFFICIENT DATA (+ optional 'provisional')",
  "score": 0-100,
  "completeness_pct": 0-100,
  "one_line_reason": "the crux in one sentence",
  "dimensions": { "operability_upside": {"score": 0-5, "confidence": "high|med|low|unknown", "note": "..."}, "pmf_retention": {}, "unit_economics": {}, "moat_defensibility": {}, "growth_market": {}, "tech_ip": {}, "transfer_key_person": {}, "deal_terms": {}, "seller_adverse_selection": {} },
  "gates": { "operable": true, "growth_lever_fits": true, "revenue_evidence": "buyer_verified|marketplace_attested|seller_claimed|none|contradicted", "value_transfers": "unknown", "ip_transferable": "unknown", "not_fragile": true },
  "key_unknowns": ["... with why it matters / how it swings the score"],
  "seller_questions": ["prioritized questions ..."],
  "inputs_provided": ["what the user gave you, tagged VERIFIED / ASSUMED / UNKNOWN"],
  "sources": [{"title": "...", "url": "..."}],
  "scorecard_markdown": "the full inline scorecard you just presented"
}
```

**Also fill the structured, import-ready fields** (the saver validates them and the team's reporting app imports on them — put *numbers* here; keep prose in the dimension notes). Leave any value `null` if unknown:

```
  "deal": { "asking_price_usd": 4000, "revenue_multiple": null },
  "metrics": { "mrr_usd": null, "arr_usd": null, "subscriptions": null, "customers": null,
               "growth_30d_pct": null, "margin_pct": null, "domain_rating": null,
               "revenue_evidence": "none | seller_claimed | marketplace_attested | buyer_verified | contradicted" },
  "contact": { "seller_handle": null, "listing_url": "the listing URL", "marketplace": "Reddit | Flippa | TrustMRR | ...", "method": "reddit DM | TrustMRR offer | email" }
```

The saver auto-adds `id`, `schema_version`, `verdict_detail`, `deal.budget_fit`, `created_at`/`updated_at`, and a default `pipeline.status`, and parses the `asking_price` string into `deal.asking_price_usd` — but fill the numbers you know. The canonical contract is `schema/report.schema.json`.

3. **Run the saver** (ensure openpyxl is available for the .xlsx log — `pip install openpyxl --break-system-packages` if the import is missing):

```bash
python scripts/save_evaluation.py --record record.json --dir <deals-folder>
```

It writes `deals/<target>_<date>/scorecard.md` and `record.json`, and appends/updates the row in `deals/deal-log.xlsx` (a `deal-log.csv` backup is always kept too). Re-running for the same target + date updates that entry instead of duplicating it.

4. **Tell the user what was saved and where**, and present the scorecard file so they can open it.

---

## Principles (why this works)

- **An honest unknown beats a confident guess.** The team's money is real; a fabricated number that reads as fact is how people overpay. Tag everything VERIFIED / ASSUMED / UNKNOWN and let the seller questions close the gaps.
- **Fit-to-build is weighted highest on purpose.** A great business you can't grow is a trap for a team without go-to-market muscle. Protect them from buying their own weakness.
- **Respect the rewrite trap.** A tempting rewrite is not a reason to buy, and "the code is messy" is rarely a dealbreaker — see `references/due-diligence.md`. Value the customers and cash flow, plan to modernize incrementally.
- **Assume the seller knows more than you.** Ask *why it's really for sale* and price the answer in. Structure (earnout, holdback, seller note) can shift risk back onto the better-informed party.
- **Keep it comparable.** Same rubric, same weights, same script every time, so deals can be ranked against each other and against the team's buy box.

## Files in this skill

- `references/rubric.md` — the **nine** dimensions, weights, 0–5 anchors, the two-kind gate model, verdict math. Read this every time you score.
- `references/seller-questions.md` — categorized question bank to tailor from in Phase 6.
- `references/due-diligence.md` — how to verify each claim, current multiple benchmarks, red flags, the rewrite-trap and adverse-selection notes, first-90-days.
- `assets/scorecard-template.md` — the output report structure.
- `scripts/verify_figures.py` — **Phase 2.5** arithmetic reconciliation; catches ~100× data errors before they reach the score.
- `scripts/score.py` — deterministic weighted scorer + gate/verdict logic (v2).
- `scripts/save_evaluation.py` — saves the scorecard + JSON record (with sources) and upserts the row in `deals/deal-log.xlsx` (+ `.csv`); supports an `analyst` field for team attribution.
- `scripts/rebuild_log.py` — regenerates the combined `deal-log` from every `record.json` (use on a shared repo instead of hand-merging the binary xlsx: `python scripts/rebuild_log.py --dir deals/`).
- `scripts/normalize_report.py` — makes every record import-ready (adds `id`, `schema_version`, structured `deal`/`metrics`/`contact`/`pipeline`/`verdict_detail`); also migrates + validates old records (`--dir deals/ [--check]`).
- `scripts/rebuild_dataset.py` — exports all records to one `deals/deals.json` for the reporting app.
- `schema/report.schema.json` — the canonical report contract the importing app reads.
