# Acquisition Scorecard (v2) — ShowFindr (showfindr.app)

**Type:** consumer app (B2C web, freemium)  ·  **Asking:** $600 ('0.9x' badge; ~9.3x all-time revenue)  ·  **Budget:** $3,000  ·  **Date:** 2026-07-17
**Figures reconciled?** two-source ✓ (listing .md + live site) · verify_figures ✓ (internally consistent) · revenue evidence: marketplace_attested
**Sources reviewed:** TrustMRR .md profile, showfindr.app, competitor landscape (Bandsintown, Songkick, Spotify native)

## Verdict

> **PASS (provisional) — 41/100** (completeness 69%)
> Two verified kill gates cap this deal: **growth_lever_fits=false** (a B2C consumer entertainment app whose only path to users is SEO/social/paid consumer marketing — the team's stated weakness; listed channel is 'SEO' with a 0.0 domain rating) and **not_fragile=false** (the product exists entirely at the pleasure of the Spotify API plus an unidentified third-party concert-data source). Beneath the gates the merit is thin anyway: 1 paying subscriber, $64.59 all-time revenue, and free incumbents (Bandsintown ~100M users, Songkick, Spotify's own live-events feed) doing the same job. The biggest swing factor — a genuinely good funnel answer — lifts merit ~10 points and it is still a PASS.

## Scorecard (nine dimensions)

| # | Dimension | Wt | Score /5 | Conf | Weighted | Notes |
|---|---|---|---|---|---|---|
| 1 | Operability & product upside | 15 | 3 | med | 9.0 | Exactly the team's stack (Next.js/Supabase/Vercel/Stripe); runnable in a weekend. But engineering upside can't beat 'the incumbents are free.' |
| 2 | PMF & retention | 15 | 1 | high | 3.0 | 1 active sub, $64.59 all-time in ~6 months, ~600 scans total. The 627% growth badge is one ~$54 payment on a ~$5 base. |
| 3 | Unit economics & upside | 12 | 2 | med | 4.8 | 80% margin claimed; n=1 makes LTV/churn meaningless; freemium B2C vs free incumbents converts poorly. |
| 4 | Moat & defensibility | 12 | 1 | high | 2.4 | Commodity clone of free giants; DR 0, no brand, no data asset. |
| 5 | Growth & market | 8 | 2 | med | 3.2 | Live events healthy, but paid-indie-aggregator niche squeezed by free incumbents and Spotify shipping the feature natively. |
| 6 | Tech & IP health | 8 | 3 | low | 4.8 | Modern owned stack (assumed) but double platform dependency: Spotify API + unknown concert-data source; transfers unverified. |
| 7 | Transfer / key-person | 10 | 3 | low | 6.0 | Nothing founder-personal; what little exists transfers, pending Spotify dev-app transfer. |
| 8 | Deal terms & value | 10 | 2 | high | 4.0 | $600 is trivially affordable but ~9.3x all-time revenue for an unproven clone; the 0.9x badge annualizes one payment. |
| 9 | Seller & adverse-selection | 10 | 2 | med | 4.0 | Built Jan 2026, for sale by July at the first revenue flicker; growth-% dressing; 239 viewers, 0 offers. |
| | **Merit total** | **100** | | | **41.2** | |

**Gates:** operable ✓ · growth-lever-fits ✗ (caps → PASS) · revenue-evidence marketplace_attested (provisional) · value-transfers ? · IP-transferable ? · not-fragile ✗ (Spotify platform lock) · **affordable** yes ($600 ≤ $3,000)

## Fit-to-build read (the team's lens)

The stack is a perfect fit — and it doesn't matter. There is nothing meaningful left to build: matching playlist artists to a concert database is a weekend project on APIs the team could wire themselves. All the value creation is user acquisition for a consumer entertainment product — SEO, social, influencer marketing — which is precisely the work the team has ruled out. This is the definition of buying your weakness: the asset's only missing ingredient is the skill the buyer doesn't have.

## Does the value transfer? (key-person check)

There is no founder audience to lose — but also almost no value to transfer: code, a DR-0 domain, and one subscriber. The real transfer risk is platform, not person: the Spotify developer app (with whatever quota tier it has) and the concert-data agreement must both survive a change of owner, and neither is verified.

## What we know vs. what we're assuming

- **Verified (buyer-reconciled):** the product exists and works as described (live site); the competitive set is free and dominant; figures are internally consistent (subs×ARPU≈MRR, asking/annualized≈0.9x).
- **Assumed / marketplace-attested:** all dollar figures (Stripe badge = attested, not reconciled); 80% margin; ~600 users; 'SEO' as channel (contradicted by DR 0.0).
- **Unknown (and how it swings the score):** Spotify dev-app transferability (false = deal dead); concert-data source & terms (scraping = product dead); what the 1 sub bought (annual would mean true MRR ≈ $4.50); the free-user funnel (best case lifts merit ~10 pts — still PASS).

## Seller questions to send (prioritized)

1. Does the Spotify developer application transfer with the sale, and what API tier is it on (development mode vs extended quota)? — *resolves: ip_transferable/not_fragile; the product exists at Spotify's discretion.*
2. Where does the concert data come from, under what terms and cost, and does that agreement transfer? — *resolves: tech_ip/not_fragile; the second hard dependency.*
3. What exactly did the one active subscriber buy (plan, price, period)? Share read-only Stripe access to reconcile. — *resolves: revenue_evidence → buyer_verified; $58 'MRR' vs $65 all-time doesn't square with a monthly plan.*
4. Share the 90-day funnel: visitors, Spotify sign-ins, scans, free→Pro conversions, traffic sources. — *resolves: pmf/growth-lever; 600 scans in 6 months suggests ~no traffic.*
5. Why sell a 6-month-old project, and what distribution did you try that failed? — *resolves: adverse-selection; the honest answer confirms the growth problem the buyer inherits.*
6. Total monthly running costs (Vercel, Supabase, data API, domain)? — *resolves: unit_economics; at ~$4.50 true MRR even small API costs make it cash-negative.*

## Recommended next step

**Pass.** Both kill gates are verified facts about the business's structure, not unknowns diligence could flip: growth is consumer marketing the team won't do, and the product is a thin layer on two platforms it doesn't control, cloning a feature the incumbents (and Spotify itself) give away free. $600 is cheap, but it buys a weekend project plus a marketing job. Not worth seller questions unless the team wants the codebase as a toy.