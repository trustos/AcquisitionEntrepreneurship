# Acquisition Scorecard (v2) — Linkeddit (linkeddit.com)

**Type:** micro-SaaS / B2B tool (AI Reddit lead-gen & marketing platform)  ·  **Asking:** $5,000 ('0.3x' badge = spike-month annualized; honest 0.53x on MRR)  ·  **Budget:** $3,000  ·  **Date:** 2026-07-18
**Figures reconciled?** two-source ✓ (listing .md + public category sources) · verify_figures ⚠ flagged the 0.3x vs 0.53x gap → reconciled (TrustMRR annualizes last-30d revenue; same pattern as AgentIdeaHub/AppShots) · ARPU flag: 23×$49=$1,127 > $782 MRR · revenue evidence: marketplace_attested
**Sources reviewed:** TrustMRR .md profile, GummySearch shutdown coverage, post-GummySearch competitive field, Linkeddit's own blog/SEO footprint

## Verdict

> **PASS (provisional) — 46/100, OUT OF BUDGET** (completeness 62%)
> Two kill gates, both verified, and one of them existential. **(1) Platform fragility:** the category leader (GummySearch) was shut down by Reddit's commercial API licensing in Nov 2025, and Reddit blocked unauthenticated tool access in May 2026 — one month before Linkeddit was listed. The entire product lives at Reddit's pleasure, and how Linkeddit accesses Reddit data today is unknown. **(2) Growth-lever mismatch, in the seller's own words:** \"Selling because can't provide needed distribution\" — from a founder with 26k X followers. The missing ingredient is exactly the skill the team doesn't have. On top: $5,000 is 1.67x the $3,000 ceiling with 50 competing offers, the +133% spike month is half non-recurring revenue, and 24 months of history ($8.9k all-time vs $782 current MRR) implies most customers churn. Biggest swing factor: the Reddit data-access answer — but even the best answer leaves both gates standing.

## Scorecard (nine dimensions)

| # | Dimension | Wt | Score /5 | Conf | Weighted | Notes |
|---|---|---|---|---|---|---|
| 1 | Operability & product upside | 15 | 3 | med | 9.0 | Stack in wheelhouse (Azure+AWS+Vercel sprawl to audit). Seller says the bottleneck is distribution, not product. |
| 2 | PMF & retention | 15 | 2 | med | 6.0 | $782 MRR after 24 months; ARPU $34 < $49 tier; spike is half non-recurring; category churn is brutal. |
| 3 | Unit economics & upside | 12 | 2 | med | 4.8 | 90% margin claimed — until Reddit's commercial API pricing applies (what killed GummySearch). |
| 4 | Moat & defensibility | 12 | 2 | med | 4.8 | Best assets in batch (DR 16, PH #1, 10k users, own listicle SEO) in a field of a dozen identical clones on Reddit's data. |
| 5 | Growth & market | 8 | 3 | med | 4.8 | Real tailwind (Reddit hot, GummySearch refugees) — created by the same event that proves the platform risk. |
| 6 | Tech & IP health | 8 | 3 | low | 4.8 | Data-access method unknown = the deal question; root domain 404s to bots; stack sprawl. |
| 7 | Transfer / key-person | 10 | 2 | med | 4.0 | 26k-follower founder + PH drove the audience; DR 16 content transfers, audience doesn't. |
| 8 | Deal terms & value | 10 | 2 | high | 4.0 | 0.53x recurring ARR is cheap on paper; 1.67x budget, no financing, 50 offers = no leverage. |
| 9 | Seller & adverse-selection | 10 | 2 | med | 4.0 | Honest reason, damning timing: listed 4 weeks after Reddit's crackdown, during the spike, at 0.5x. |
| | **Merit total** | **100** | | | **46.2** | |

**Gates:** operable ✓ · growth-lever-fits ✗ (seller-declared — caps → PASS) · not-fragile ✗ (Reddit platform lock, verified by GummySearch's death — caps → MARGINAL) · revenue-evidence marketplace_attested (provisional) · value-transfers ? · IP-transferable ? · **affordable** NO ($5,000 vs $3,000 → OUT OF BUDGET)

## Fit-to-build read (the team's lens)

The engineering is done and in-stack — and the seller says so himself: the product works, distribution is what's missing. Every listed channel (X, Reddit engagement, blog/SEO, YouTube, cold email, PH) is content-and-audience marketing. Buying Linkeddit is buying a distribution job from a man with 26,077 followers who says the distribution job was too hard for him.

## Does the value transfer? (key-person check)

Some genuinely does: DR 16, ranking listicles, the product, 10k registered users. The X audience and PH halo don't. But the bigger transfer question is upstream: whatever Reddit data access the product uses — the thing GummySearch couldn't keep — may not transfer, may already be degraded since May 2026, and definitely isn't controlled by the buyer.

## What we know vs. what we're assuming

- **Verified (buyer-reconciled):** GummySearch's shutdown and cause; Reddit's May 2026 unauthenticated-access block; the listing timing one month later; the 0.3x-vs-0.53x multiple framing; the ARPU/tier gap; the fragmented clone field; DR 16 and the self-ranking listicle.
- **Assumed / marketplace-attested:** all dollar figures (Stripe badge); 23 subs; 10k users; 90% margin; PH #1 claim.
- **Unknown (and how it swings):** Reddit data-access method (existential — a bad answer makes this worthless at any price; a good answer still leaves two gates); spike composition; churn curve; the reality of 50 offers; price flexibility.

## Seller questions to send (prioritized)

1. How does Linkeddit access Reddit data — commercial API (agreement? cost?), free tier, or other? Affected by the May 2026 restrictions? Does the access/dev account transfer? — *resolves: not_fragile / ip_transferable; Reddit killed the category leader on exactly this.*
2. Split the $1,654 last-30d into recurring vs one-time; read-only Stripe access; what drove the +133% month? — *resolves: revenue → buyer_verified / pmf.*
3. Monthly churn curve for 12 months; how many of the 23 subs are >3 months old? — *resolves: pmf_retention.*
4. Why is ARPU $34 vs the $49 tier? Any Enterprise deals? — *resolves: unit_economics.*
5. Signup sources with percentages; what happens when you stop posting? — *resolves: growth_lever / value_transfers.*
6. You have 26k followers and cite distribution as the blocker — what failed? — *resolves: adverse-selection.*
7. Any of the 50 offers near asking? Would you take ~$3,000, or an earnout tied to MRR + continued Reddit access at 6 months? — *resolves: deal_terms; the earnout prices the platform risk.*

## Recommended next step

**Pass.** This is the most asset-rich target in the TrustMRR batch (real DR, real users, real brand moment) and still a clear no: the platform that killed the category leader controls the product's oxygen, the seller names distribution — the team's weakness — as the reason he's out, and the price is 1.67x budget with 50 competing offers. If the team ever wants a Reddit-tools position, the GummySearch corpse-field is better studied than bought.