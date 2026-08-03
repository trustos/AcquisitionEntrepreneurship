# Acquisition Scorecard (v2) — Calzy (TrustMRR)

**Type:** Consumer mobile app (iOS-only) — AI photo-based calorie/nutrition tracker · **Asking:** $19,999 (marketplace-stated 1.7x) · **Budget:** $10,000 · **Date:** 2026-08-03
**Figures reconciled?** two-source ✓ (listing page + listing .md) · verify_figures ✓ (flagged a mismatch — see below) · revenue evidence: **marketplace_attested** (RevenueCat sync via TrustMRR, not buyer-reconciled from source)
**Sources reviewed:** trustmrr.com/startup/calzy (page + .md), Apple iTunes lookup API (App Store metadata), app description/pricing

## Verdict

> **PASS (provisional) — 42/100** (completeness 64%)
> Two verified-negative gates cap this deal: the primary growth channels (ASO, blog, content marketing, SEO, TikTok, Instagram) are exactly the team's stated weakness — a content/social-virality treadmill, not product-led/organic growth — and the business is structurally fragile as a single-platform (Apple App Store only, no Android) iOS app with 100% of revenue running through Apple's IAP. On top of the gates, the merit score itself is weak: revenue has fallen >50% from its June peak ($1,282/mo) to the current $558 MRR, the category (AI photo calorie-counting) is now commodity-crowded, and at $19,999 the price is ~2x the $10k budget and ~3.0x *current* run-rate (not the marketplace's advertised 1.7x — see reconciliation). The single biggest swing factor is the revenue decline: if the seller can show this was a one-off dip with recovery already underway, PMF/retention and seller-adverse-selection scores would improve — but as observed, this reads as a peak-and-fade pattern timed suspiciously close to the listing date.

## Scorecard (nine dimensions)

| # | Dimension | Wt | Score /5 | Conf | Weighted | Notes |
|---|---|---|---|---|---|---|
| 1 | Operability & product upside | 15 | 4 | high | 12.0 | Swift/SwiftUI + Supabase + RevenueCat + AI photo recognition — squarely full-stack/AI wheelhouse; real upside (Android, better AI accuracy, wearable integrations) in a fast-commoditizing category. |
| 2 | PMF & retention | 15 | 2 | med | 6.0 | 147 subs, 4.8/5 (54 ratings) reads well, but MRR fell from $1,282 (Jun) to $558 (now), 0% 30d growth — trajectory itself is evidence of weakening retention/reactivation. |
| 3 | Unit economics & upside | 12 | 3 | med | 7.2 | 90% reported margin, but ARPU only ~$3.80/mo across 147 subs; no CAC/LTV disclosed so LTV:CoCA unverifiable. |
| 4 | Moat & defensibility | 12 | 1 | high | 2.4 | Photo-AI calorie tracking is now commodity (Cal AI, MyFitnessPal, Lose It!, Noom, Foodvisor, SnapCalorie, many GPT-vision clones). No proprietary data, network effect, or switching cost beyond habit/streak. |
| 5 | Growth & market | 8 | 2 | med | 3.2 | Category (AI nutrition tracking) has a tailwind, but this specific product's own revenue is declining >50% off peak — contradicts the category story. |
| 6 | Tech & IP health | 8 | 2 | unknown | 3.2 | Standard stack, but ownership/clean-transfer of Apple Developer account, Supabase project, RevenueCat project, and the AI/vision API dependency (provider undisclosed) are all unconfirmed. |
| 7 | Transfer / key-person | 10 | 2 | unknown | 4.0 | No founder identity beyond "Mitologic sp. z o.o."; no TikTok/Instagram/blog handles disclosed, so whether the content/social assets driving distribution transfer with the sale is unverified. X followers: 0 suggests minimal owned social presence. |
| 8 | Deal terms & value | 10 | 1 | high | 2.0 | $19,999 is 2x the $10k budget. On live MRR ($558×12=$6,696 ARR) the true current-run-rate multiple is ~3.0x, not the marketplace-displayed 1.7x (computed off trailing-30-day revenue, not current MRR). Poor value for a declining, commodity, single-platform app. |
| 9 | Seller & adverse-selection | 10 | 1 | med | 2.0 | No reason for sale given. First listed 2026-06-16 — the same month revenue peaked — and revenue has since fallen >50%. Classic list-at-peak, decline-during-diligence pattern. |
| | **Merit total** | **100** | | | **42.0** | |

**Gates:** operable [true] · growth-lever-fits **[false]** · revenue-evidence [marketplace_attested] · value-transfers [unknown] · IP-transferable [unknown] · not-fragile **[false]** · **affordable** [yes, if financed — asking exceeds cash budget alone]

## Fit-to-build read (the team's lens)

The tech itself is squarely operable by this team (Swift/SwiftUI mobile, Supabase, AI/ML integration) — this is not a "we can't run the stack" problem. But the path to *growing* it is a marketing/content problem, not an engineering one: the listing's own stated distribution channels are App Store optimization, blog, content marketing, SEO, TikTok, and Instagram. That's a social-virality/content treadmill, and the revenue history (a sharp spike in June followed by a steep fade) looks exactly like what happens when a single piece of viral content or influencer push drives a temporary subscriber surge that the team then can't replicate. Buying this would mean buying a team's inability to reproduce its own best month — precisely the weakness this buyer is trying to avoid.

## Does the value transfer? (key-person check)

Unclear. No founder or creator identity is disclosed (only the corporate entity "Mitologic sp. z o.o."), and there are no public TikTok/Instagram/blog handles to verify whether the content assets that drove the June revenue spike would actually convey in a sale, or whether they belong to an agency/influencer relationship that ends when the current owner exits. Zero X/Twitter followers suggests limited owned-audience distribution to begin with, which is a mild positive for transfer risk (less to lose) but doesn't resolve the TikTok/Instagram question.

## What we know vs. what we're assuming

- **Verified (buyer-reconciled):** App Store metadata (name, rating 4.8/5 from 54 ratings, release date 2026-01-25, bundle ID, tech stack, pricing tiers) via iTunes lookup API; subs × ARPU ≈ MRR arithmetic checks out ($147 × $3.80 ≈ $558).
- **Assumed / marketplace-attested:** MRR ($558), 30-day revenue ($995), all-time revenue ($2,884), and the monthly revenue trend (May–Aug) — these come from TrustMRR's RevenueCat sync, which is a real payment-provider connection but has not been independently reconciled by us against Stripe/App Store Connect financial reports. The listing's "1.7x" multiple appears to be computed off annualized trailing-30-day revenue ($995×12=$11,940 → 1.67x), not off current MRR ($558×12=$6,696 → 2.99x) — a materially different (and worse) number for the buyer once you use the metric that matters going forward.
- **Unknown (and how it swings the score):** Reason for sale (could flip seller-adverse-selection up or down significantly); churn/retention cohort data (currently inferred only from the MRR trend — real churn numbers could be better or worse); CAC and paid-vs-organic split of the TikTok/Instagram/SEO channels (determines how repeatable growth really is and could shift growth-lever-fits); IP/account transferability (App Store Connect, Supabase, RevenueCat, and the AI vision API vendor); whether the June revenue spike had an identifiable one-off cause (a viral post, a feature launch, App Store featuring) that could be understood and potentially re-triggered.

## Seller questions to send (prioritized)

1. Why are you selling, and why now? *— resolves: seller-adverse-selection; the listing gives no reason, and the timing (listed the same month revenue peaked, then fell >50%) needs a credible explanation.*
2. What caused the spike to $1,282 MRR in June, and what caused the subsequent drop to $558? Can you show a monthly cohort/churn breakdown for that period? *— resolves: PMF & retention, growth & market; this is the single biggest swing factor in the score.*
3. Where do new customers actually come from today — rough % split across ASO, SEO/blog, TikTok, Instagram, and any paid spend? Do you have CAC data? *— resolves: growth-lever-fits gate; determines whether growth is truly organic/product-led or a content/social treadmill this team can't run.*
4. Can you export the last 12 months of revenue directly from App Store Connect / RevenueCat dashboard (not the TrustMRR summary) so we can reconcile the MRR and multiple ourselves? *— resolves: revenue-evidence gate (upgrade from marketplace_attested to buyer_verified).*
5. Is 100% of the code, Supabase project, RevenueCat project, and Apple Developer account owned solely by you/the entity, with no contractor-owned IP or unrelicensable dependencies (including whichever AI/vision API powers food recognition)? *— resolves: IP-transferable gate.*
6. Do any TikTok/Instagram/blog accounts, content assets, or influencer relationships that drove growth transfer with the sale, and would you stay on briefly to hand off the marketing playbook? *— resolves: transfer/key-person dimension.*
7. Are you open to seller financing, a retention-linked earnout, or an escrow holdback given the recent revenue decline? *— resolves: deal terms; shifts risk back onto the better-informed party and tests confidence in the numbers.*

## Recommended next step

Pass, provisionally. The two kill-gate issues (content/social-driven growth channel outside the team's competence, and single-platform App Store fragility) aren't resolved by better data — they're structural to this business. Only reconsider if the seller's answer to "why sell / what caused the drop" reveals a clearly one-off, non-recurring explanation (e.g., a temporary App Store policy issue now resolved) **and** the price comes down substantially toward or below the $10k budget without financing. Otherwise, this fits the profile of a business whose best month the team can't reproduce and whose channel isn't ownable by this team.
