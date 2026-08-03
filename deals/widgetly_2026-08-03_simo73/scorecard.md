# Acquisition Scorecard (v2) — Widgetly

**Type:** Micro-SaaS / plugin-style tool (Notion widget embeds, B2C/prosumer) · **Asking:** $13,000 (stated 1.6x, reconciled ~1.8–2.1x) · **Budget:** $10,000 (financing possible) · **Date:** 2026-08-03
**Figures reconciled?** Two-source: partial (TrustMRR listing page + `.md` profile only — no seller Stripe export seen). `verify_figures.py`: internally consistent (subs×ARPU=MRR), but **stated 1.6x multiple does not reconcile** with disclosed revenue (asking/TTM-revenue = 1.82x; asking/annualized-current-MRR = 2.09x). Revenue evidence: **marketplace_attested** (TrustMRR "Stripe-verified" badge, not buyer-reconciled from source).
**Sources reviewed:** trustmrr.com/startup/widgetly.md listing profile, widgetly.co product site. Reddit/review/competitor search attempts this session did not return usable results (search tooling misfired) — competitor claims below are general market knowledge, not freshly verified, and are flagged accordingly.

## Verdict

> **MARGINAL (provisional) — 52/100** (completeness 56%)
> Capped by a **structural fragility gate**: Widgetly's entire product is widgets embedded into Notion pages — its existence depends on Notion continuing to allow third-party embeds, a platform dependency the team cannot control or diversify away from. Separately, the business itself is thin: ~$518 MRR across 153 subs at a ~$3.39 ARPU, flat-to-lumpy for ~2.75 years, in a crowded/commodity niche (Notion widget tools are easy to copy and switch away from). The team could easily *operate* this (simple web app + Stripe), but there's little moat to defend and no verified growth channel to scale. Price is also a stretch: $13,000 against a $10,000 ceiling, needing financing, on a multiple that doesn't cleanly reconcile with the disclosed figures. Biggest swing factor: **what's the real acquisition channel** — if it's durable SEO/product-led discovery, this could edge into PROMISING; if it's dependent on directory placements or one Notion-community relationship, it stays MARGINAL-or-worse.

## Scorecard (nine dimensions)

| # | Dimension | Wt | Score /5 | Conf | Weighted | Notes |
|---|---|---|---|---|---|---|
| 1 | Operability & product upside | 15 | 4 | high | 12.0 | Simple full-stack SaaS (widgets + Stripe billing); squarely in team's wheelhouse. Several widgets listed "Coming soon" for a while (Help Widget, Image Generator, AI Bot) — real, obvious upside to ship. |
| 2 | PMF & retention | 15 | 2 | med | 6.0 | 153 subs after ~2.75 years live; MRR down -1.0%/30d; monthly revenue lumpy ($359–$810) with no clear growth trend. No churn rate disclosed. Reads flat, not loved. |
| 3 | Unit economics & upside | 12 | 3 | low | 7.2 | ARPU ~$3.39/mo (tiers €3/€5/€7) is thin. 95% margin is good but on a tiny base. No CoCA/LTV data — channel spend unknown, so LTV:CoCA is unverifiable. |
| 4 | Moat & defensibility | 12 | 1 | med | 2.4 | Notion widget embeds are a crowded, low-differentiation niche (Indify is the best-known incumbent; several other free/cheap alternatives exist). Low switching cost — swap one iframe embed URL for another. No proprietary data, exclusive integration, or brand moat evident. |
| 5 | Growth & market | 8 | 2 | low | 3.2 | Notion's own ecosystem is growing, but Widgetly's revenue hasn't tracked any tailwind — flat/lumpy for 3 years. Also exposed to Notion shipping native equivalents of these widget categories, which would be existential. |
| 6 | Tech & IP health | 8 | 3 | unknown | 4.8 | Presumably a standard web app (Stripe backend). No visibility into codebase quality, hosting, or exact ownership/transferability of code, domain, and accounts. |
| 7 | Transfer / key-person | 10 | 4 | med | 8.0 | Founder Dan Santos has a minimal personal following (72 X followers); brand is product-named, not founder-named. Distribution does not look personality-driven — but not confirmed with the seller. |
| 8 | Deal terms & value | 10 | 2 | high | 4.0 | $13,000 asking vs. $10,000 ceiling — needs financing to close. Stated 1.6x multiple doesn't reconcile against disclosed TTM revenue ($7,150 → 1.82x) or annualized current MRR ($6,216 → 2.09x). On thin, flat, low-ARPU revenue, this reads full-to-high rather than cheap. |
| 9 | Seller & adverse-selection | 10 | 2 | low | 4.0 | MRR declining (-1.0%/30d) while actively listed. Seller adds unverified extra income ($130–160/mo "Google Ads income" + $50/mo legacy Paddle billing) not captured in the Stripe-verified figures — inflates the story with numbers that can't be checked. 15 offers / 2,060 viewers raises bidding-war risk. No stated reason for sale. |
| | **Merit total** | **100** | | | **51.6 → 52** | |

**Gates:** operable [true] · growth-lever-fits [unknown] · revenue-evidence [marketplace_attested] · value-transfers [true, assumed] · IP-transferable [unknown] · **not-fragile [FALSE — Notion embed platform dependency]** · **affordable** [stretch — over ceiling, financing required]

## Fit-to-build read (the team's lens)

The path to *operating* Widgetly is pure engineering: it's a set of embeddable widgets plus Stripe billing, well within the team's full-stack/AI skillset, and there's concrete backlog (AI Bot widget, Image Generator, Help Widget) the team could ship faster than the current owner has. But the path to *value creation* here isn't really "build more widgets" — it's "win a crowded, commodity SEO/discovery niche against a more established incumbent (Indify) with no disclosed acquisition channel." That's a market-share problem, not an engineering problem, and it's the part this team is least equipped to de-risk.

## Does the value transfer? (key-person check)

No evidence the founder's personal brand drives customers — 72 X followers is negligible, and the product is marketed under its own name, not the founder's. That's a mild positive for transfer/key-person. However, the *real* driver of new signups (SEO ranking for "notion widgets," a marketplace/directory listing, a Notion-community relationship, etc.) is unverified. If discovery runs through one un-transferable channel (e.g., a single directory placement or a specific SEO position the seller worked to earn), that risk lives here and in the moat/growth-lever gate — not in founder key-person risk.

## What we know vs. what we're assuming

- **Verified (buyer-reconciled):** Nothing yet — all revenue figures come from TrustMRR's Stripe-API sync (marketplace-attested), not a source export the buyer has reconciled directly.
- **Assumed / marketplace-attested:** MRR $518 (-1.0%/30d), 153 active subs, TTM revenue $7,150, all-time $23,976, 95% margin, domain rating 32, asking $13,000 at a stated 1.6x multiple, listed since 2026-05-19 with 2,060 viewers / 15 offers. Founder-claimed (unverified, outside Stripe): $130–160/mo "Google Ads income," ~$50/mo legacy Paddle billing.
- **Unknown (and how it swings the score):** (1) Actual acquisition channel/mix — if organic/product-led, growth-lever gate clears and Moat/Growth scores could rise; if paid/directory/SEO-treadmill, the deal likely caps at PASS. (2) Reason for sale — undisclosed; given declining MRR during the listing period, this needs a direct, credible answer. (3) Code/domain/account ownership and transfer mechanics. (4) True churn/cohort retention. (5) Why the stated 1.6x multiple doesn't match the disclosed revenue base — needs the seller's own basis for the multiple.

## Seller questions to send (prioritized)

1. **Why are you selling, and why now?** — *resolves: seller/adverse-selection; the MRR is down 1.0% over the last 30 days while the listing is live — is that a blip or a trend, and what's driving it?*
2. **Can you export the last 24 months of Stripe revenue and reconcile the "Google Ads income" (~$130–160/mo) and legacy Paddle billing (~$50/mo) claims with statements/screenshots?** — *resolves: revenue_evidence gate (move from marketplace_attested to buyer_verified); also clarifies whether "Google Ads income" means ad-display revenue on the site (a very different, lower-quality revenue stream than subscriptions) or paid-ads-driven signups.*
3. **Where do new customers actually come from today — organic search, a specific directory/marketplace, word of mouth, paid ads, or a Notion-community relationship — and roughly what % each?** — *resolves: growth_lever_fits gate; this is the single biggest swing factor in the whole evaluation.*
4. **What multiple/basis did you use to price this at $13,000 (1.6x), and are you open to seller financing, a retention-linked earnout, or a holdback?** — *resolves: deal_terms; the stated multiple doesn't reconcile with disclosed revenue, and financing/structure would materially change affordability against our $10,000 ceiling.*
5. **What's monthly/annual churn and cohort retention over the last 12 months, and what % of active subs are on Free vs. paid tiers?** — *resolves: pmf_retention.*
6. **Is 100% of the code, the widgetly.co domain, and all third-party accounts (Stripe, hosting, any Notion partner/marketplace listings) owned by you and transferable without contractor or platform restriction?** — *resolves: ip_transferable and value_transfers gates.*
7. **Has Notion ever changed embed/iframe policy in a way that affected you, and is there a written agreement or partner status with Notion, or is this entirely reliant on Notion's public embed feature continuing to work?** — *resolves: not_fragile — this is the gate currently capping the deal at MARGINAL; a credible answer (e.g., a documented Notion partner relationship, or diversification beyond raw iframe embeds) could lift the cap.*

## Recommended next step

Send questions 1–4 first (adverse-selection, revenue reconciliation, acquisition channel, and price basis) — these resolve the two things actually driving the low score: an unresolved fragility gate (Notion embed dependency) and a commodity moat with an unknown growth engine. If the channel turns out to be durable/organic and the seller can document a real Notion partnership (not just public embed usage), re-score — it could reach PROMISING. If the channel is a single directory/SEO position or the multiple can't be justified, this is a **PASS**: thin, flat, undifferentiated, and priced above budget for what it is.
