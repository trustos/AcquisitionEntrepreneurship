# Verification, benchmarks, and traps

How to turn seller claims into VERIFIED facts, what a fair price looks like, and the two failure modes most likely to bite a technical buyer.

## How to verify each claim (trust, but verify)

- **Revenue** — rebuild the P&L from source data: processor exports (Stripe/Paddle), reconciled against bank statements. Roughly 40%+ of small online deals carry inflated or inaccurate figures, so a typed spreadsheet is not evidence. Screen-share live through the accounts if you can.
- **Traffic / demand** — Google Search Console and analytics read-access; inspect the *trend* (1mo / 6mo / 1yr / all-time), not a single screenshot; probe for penalty or core-update drops.
- **Churn / retention** — ask for a cohort chart; sanity-check against revenue trend. Benchmark: ~1–2%/mo logo churn is strong for SMB/prosumer, ~3–4% is normal, higher is a leaky bucket. NRR ≥100% is excellent.
- **Tech & IP** — confirm the entity owns all code/assets (no contractor-owned IP); review architecture and dependencies under NDA; identify any single-API/model lock-in.
- **Concentration** — any single customer >15–20% of revenue, or one keyword/page >50% of traffic, is a priced risk. Check contracts for change-of-control clauses.
- **Transferability** — verify *control* before close: domain/registrar, hosting, repos, GA4/Search Console/Ads, ESP, affiliate + app-store/developer accounts, trademarks, licensed content. Assume payment processors (Stripe/PayPal) do NOT transfer — plan a billing migration and a revenue-continuity gap.

## Current multiple benchmarks (2025–2026, for sanity-checking price)

Use to score Deal Quality (dimension 7). These move over time — if in doubt, search for the latest.

- **Profitable micro-SaaS:** median ~3.5–4x annual profit/SDE; ~2–3x at $1–5k MRR, ~4–6x at ~$10k MRR with low churn, 7–9x only for premium metrics (growth + NRR >120%). On revenue, bootstrapped SaaS ~3–5x ARR (smaller = lower; the tiniest deals ~3.3x).
- **Content / affiliate:** ~30–40x monthly profit (~2.5–3.3x annual), cut from higher because of Google core updates and AI Overviews. (Against the team's weakness — treat with caution.)
- **Newsletter/media:** ~30–45x monthly, or ~$1–10 per subscriber (higher for B2B/engaged).
- **Shopify/DTC:** ~3–5x SDE. **Amazon FBA:** ~2.5–3.5x SDE (platform-concentration discount).

What moves the multiple: growth (biggest lever), low churn (premium), owner-passivity and diversified traffic (premium); single-channel/customer concentration and decline (discount).

## Deal structures that shift risk to the (better-informed) seller

- **Asset purchase (APA)**, not a share purchase — buy the assets, inherit only liabilities you accept.
- **Seller financing** — online norm ~75% cash down, short (~10 month) payoff, often 0% interest. Refusal to hold any note is a signal.
- **Earnout** — ~70% cash at close, ~30% contingent over 12–36 months, tied to *retention of existing customers* (not new growth — cleaner to measure).
- **Holdback/escrow** — 10–20% held 12–24 months against the seller's reps; release after you verify assets in the inspection window.

## The rewrite trap (the technical buyer's #1 self-inflicted wound)

A tempting rewrite is not a reason to buy, and "the code is ugly" is rarely a dealbreaker. Rewriting inherited software from scratch is a classic value-destroyer: it discards years of encoded bug-fixes, freezes the product while customers wait, and hands competitors a head start. It is *harder to read code than to write it*, so the mess usually looks worse than it is.

Implications for scoring and planning:

- Don't inflate the score because "we'd just rebuild it." Value the customers and cash flow as they are.
- In Tech & IP (dimension 6), reward *transferable and incrementally modernizable*; only penalize when the code is genuinely unownable or so toxic that a risky rewrite is the *only* path.
- Post-close plan: for the first 30–90 days change nothing structural — talk to customers, fix small high-leverage things, learn the ops load — then modernize incrementally (strangler-fig), never big-bang.

## Adverse selection (why is it *really* for sale?)

Assume the seller knows more than you and rationally lists at the peak of trailing metrics — sometimes just before a decline they can already sense. Defenses: primary-source verification (above), structure that shifts risk back (earnout/holdback), and the seller questions on the real reason for sale. A single unexplained red flag that the numbers can't dispel is reason enough to walk.

## Red-flag checklist (any hit → lower Seller-risk score and raise a seller question)

- Revenue only ever shown as a typed spreadsheet or dashboard screenshot.
- Traffic/revenue chart that conveniently starts *after* a past drop.
- One channel, one customer, or one person the whole thing depends on.
- Contractor-owned code or un-relicensable/expiring key dependencies.
- Seller evasive on "why selling" or unwilling to hold any earnout/note.
- Metrics peaking right at listing time with a thin growth story.
- A moat that's actually a non-technical asset the team can't operate (brand, relationships, a license).

## v2 additions (from the 8-deal audit)

- **Reconcile every figure before it feeds the score.** Never trust a single tool/field for a dollar number — a marketplace tool once under-reported all values by 100×. Cross-check against a second/authoritative source (for TrustMRR, the `.md` page or live listing, **not** the MCP), and run `scripts/verify_figures.py` (subs×ARPU ≈ MRR; MRR×12 ≈ ARR; asking ÷ annual ≈ multiple). A marketplace "verified" badge is *attested*, not *reconciled from source* — only source reconciliation is `buyer_verified`.
- **Interrogate a low multiple.** Cheap is usually a symptom, not a bargain — a sub-1× or fire-sale multiple most often means declining revenue, a lemon, or a founder who knows something you don't. Make "why so cheap?" an explicit seller question.
- **Does the value transfer, or walk away with the founder?** Separate the business from the person: if the growth engine is a personal audience (YouTube/X), personal relationships, or the founder's domain expertise, model what survives their exit — often little. (Scored as its own dimension in v2.)
- **Compliance / privacy.** If the target holds regulated or sensitive data (health, finance, minors, PII at scale) or sits in a licensed domain, flag it — that's a burden for a team without compliance muscle. Get the GDPR/CCPA posture, data-processing setup, and any licenses, and price it in.
- **Benchmarks rot.** The multiple ranges above are 2025–2026 snapshots — re-verify current comps per use rather than trusting them blind.
