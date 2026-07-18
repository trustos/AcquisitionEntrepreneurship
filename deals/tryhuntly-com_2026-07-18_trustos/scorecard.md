# Acquisition Scorecard (v2) — Huntly (tryhuntly.com)

**Type:** micro-SaaS / B2B tool (local-business lead finder for web freelancers, Spanish-language markets)  ·  **Asking:** $7,500 (2.5x annualized MRR — highest multiple in the TrustMRR batch)  ·  **Budget:** $3,000  ·  **Date:** 2026-07-18
**Figures reconciled?** verify_figures ✓ arithmetic — but **pricing-tier contradiction:** listing sells $19/$49 tiers, live site sells $9/$19 (ARPU $9.71 confirms the live pricing) · revenue evidence: marketplace_attested
**Sources reviewed:** TrustMRR .md profile, tryhuntly.com (live pricing + product), competitor field (D7, Outscraper, LeadSwift, WebLeads, Lead Scrape)

## Verdict

> **PASS (provisional) — 40/100, OUT OF BUDGET** (completeness 66%)
> The worst value-for-money in the TrustMRR batch: **2.5x annualized revenue for a 3-month-old product** with $272 MRR — while Linkeddit, with 2 years of history, DR 16 and 10k users, asks 0.53x. Verified kill gate: **growth_lever_fits=false** — the only stated channel is the founder's Spanish-language Instagram (@humberbuilds), DR is 0.0, and the audience leaves with him. The product itself is a thin filter over Google Maps data (API-or-scraping unknown — the single structural dependency) in a commodity category owned by D7 Lead Finder, Outscraper, LeadSwift and friends, sold to Spanish-speaking freelancers the team can't support in Spanish, monetizing a pain (businesses without websites) that AI site builders are steadily shrinking. Integrity flag: the listing's pricing tiers don't match the live site's — ARPU $9.71 proves most subs are on the $9 plan the listing doesn't mention. **$7,500 is 2.5x the ceiling.** Biggest swing factor: none — even perfect diligence answers leave the channel gate, the price, and the category standing.

## Scorecard (nine dimensions)

| # | Dimension | Wt | Score /5 | Conf | Weighted | Notes |
|---|---|---|---|---|---|---|
| 1 | Operability & product upside | 15 | 3 | med | 9.0 | Trivial stack, rebuildable in weeks; Spanish-first product/support outside team comfort. |
| 2 | PMF & retention | 15 | 2 | med | 6.0 | 28 subs in 3 months, mostly at $9; episodic freelancer need; no retention history. |
| 3 | Unit economics & upside | 12 | 2 | med | 4.8 | ~$10 ARPU vs Google data costs (API $ or scraping risk); 90% margin claim untested at scale. |
| 4 | Moat & defensibility | 12 | 1 | high | 2.4 | Resells Google's data in a field of entrenched incumbents; DR 0; no asset to defend. |
| 5 | Growth & market | 8 | 2 | med | 3.2 | Saturated category + AI site builders shrink the underlying pain. |
| 6 | Tech & IP health | 8 | 3 | low | 4.8 | Data-pipe method unknown = the whole technical question; 'backend: Stripe' says thin scraper. |
| 7 | Transfer / key-person | 10 | 2 | med | 4.0 | IG audience is the only channel and it doesn't transfer. |
| 8 | Deal terms & value | 10 | 1 | high | 2.0 | 2.5x on 3 months of history at 2.5x the budget — clearly overpriced on every axis. |
| 9 | Seller & adverse-selection | 10 | 2 | med | 4.0 | 3-month flip, aggressive multiple, no reason given, listing/site pricing mismatch. |
| | **Merit total** | **100** | | | **40.2** | |

**Gates:** operable ✓ · growth-lever-fits ✗ (caps → PASS) · revenue-evidence marketplace_attested (provisional) · value-transfers ? · IP-transferable ? · not-fragile ? (Google data pipe — verify) · **affordable** NO ($7,500 vs $3,000 → OUT OF BUDGET)

## Fit-to-build read (the team's lens)

Nothing here needs the team's engineering strength — a Next.js front end over a Google Maps query is a weekend build, and that's reflected in the price of entry for the dozen incumbents already doing it with better data and better SEO. Everything the business needs is what the team lacks: Spanish-language Instagram content, freelancer-community marketing, and ongoing Spanish-speaking support. It is the purest 'buying your weakness' case in the batch, at the batch's highest multiple.

## Does the value transfer? (key-person check)

What transfers: a thin codebase, a DR-0 domain, and ~28 mostly-$9 subscriptions of unknown remaining lifetime. What doesn't: the founder's Instagram audience — the only stated acquisition channel — and whatever Google data access arrangement exists, which is unverified. The honest answer is that almost nothing durable changes hands.

## What we know vs. what we're assuming

- **Verified (buyer-reconciled):** the pricing-tier contradiction (listing $19/$49 vs live $9/$19, confirmed by ARPU $9.71); the 2.3-2.5x multiple math; the commodity competitive field; Spanish-market focus; DR 0; Google Maps as the data source.
- **Assumed / marketplace-attested:** all dollar figures (no explicit Stripe badge seen in the .md extract — even the attestation level needs confirming); 28 subs; 90% margin; 10 offers.
- **Unknown (and how it swings):** data-pipe method (scraping = product can die overnight; API = margin shrinks); sub mix and churn; IG dependence share; why the price tiers changed. No plausible set of answers clears the channel gate, the category, or the 2.5x-budget price.

## Seller questions to send (prioritized)

1. How is Google Maps data sourced — Places API (cost? account transfer?) or scraping? What breaks if Google blocks it? — *resolves: not_fragile / ip / margins.*
2. Listing tiers ($19/$49) vs live site ($9/$19): which is real, when did it change, why? Sub breakdown by plan + read-only Stripe. — *resolves: revenue → buyer_verified / credibility.*
3. Cohort retention of April/May subs. — *resolves: pmf.*
4. Share of signups from your Instagram; signups in weeks you didn't post. — *resolves: growth_lever / value_transfers.*
5. What breaks for a non-Spanish-speaking owner? — *resolves: operability.*
6. Why sell at 3 months while growing +36%/mo, and why 2.5x when peers list at 0.5-1.3x? — *resolves: adverse-selection / deal_terms.*
7. Any structure at a $3,000 level (earnout on 6-month MRR retention)? — *resolves: affordability.*

## Recommended next step

**Pass — don't engage.** Unlike Getbeel (worth one email) or Linkeddit (worth an autopsy), Huntly offers no scenario worth pursuing: the price is 2.5x both the budget and any defensible multiple, the only channel is a Spanish-language personal audience, the data pipe belongs to Google, and the category's incumbents are unbeatable on the team's skills. The 10 claimed offers can have it.