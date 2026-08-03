# Acquisition Scorecard (v2) — Aprofy

**Type:** Consumer mobile app (iOS study companion) · **Asking:** $4,000 (2.75× ARR / 33× MRR) · **Budget:** $10,000 · **Date:** 2026-08-03
**Figures reconciled?** verify_figures ✓ (subs × ARPU = MRR) · note: TrustMRR states 2.0× but this is computed on last-30-day revenue annualized ($163×12=$1,956); ARR-based multiple is 2.75× · **Revenue evidence:** marketplace_attested (RevenueCat API, not buyer-reconciled from source)
**Sources reviewed:** TrustMRR listing .md, App Store product page, aprofy.app website, Forest benchmark competitor

## Verdict

> **MARGINAL (provisional) — 53/100** (completeness 55%)
>
> Aprofy is a well-built iOS study-timer app (React Native/Expo) that launched in June 2026 and was listed for sale within ~25 days of launch. At $4,000 it buys you a working mobile codebase, RevenueCat paywall infrastructure, Sentry monitoring, and 30 paying subscribers generating $121 MRR — but nothing resembling a proven business yet. MRR growth is 0% in the trailing month, churn is unknown, and the category is crowded (Forest alone has 60M users). The single biggest red flag is the ultra-early exit: a founder who sells within weeks of launch is either (a) an experienced app-flipper or (b) someone who saw early metrics and chose to cut losses — and you can't tell which without a direct answer. Revenue is marketplace-attested (RevenueCat API badge), not buyer-reconciled, so the verdict stays provisional. The team can absolutely operate this stack, and the price is within budget, but MARGINAL is the right rating until churn, IP transfer, and the real reason for the early sale are confirmed.

## Scorecard (nine dimensions)

| # | Dimension | Wt | Score /5 | Conf | Weighted | Notes |
|---|---|---|---|---|---|---|
| 1 | Operability & product upside | 15 | 4 | high | 12.0 | React Native/Expo/TS squarely in wheelhouse. Upside: Android, AI study plans, web app. |
| 2 | PMF & retention | 15 | 2 | low | 6.0 | 30 paying subs, 0% MRR growth, 0 US App Store ratings. Churn unknown. Neutral per rules. |
| 3 | Unit economics & upside | 12 | 2 | low | 4.8 | 85% margin stated. ARPU $4.03/mo. LTV unknown (no churn). CoCA unknown. Scored neutral. |
| 4 | Moat & defensibility | 12 | 2 | med | 4.8 | Crowded category (Forest 60M users). Differentiation real but replicable. Commodity ASO. |
| 5 | Growth & market | 8 | 3 | med | 4.8 | Education productivity stable-growing. AI tailwind plausible. App itself flat. |
| 6 | Tech & IP health | 8 | 3 | med | 4.8 | Modern transferable stack. App Store transfer procedurally possible. IP ownership unconfirmed. |
| 7 | Transfer / key-person | 10 | 3 | low | 6.0 | ASO transfers; TikTok channel provenance unknown. 50k user claim unverified. Scored neutral. |
| 8 | Deal terms & value | 10 | 3 | med | 6.0 | $4k = 33× MRR / 2.75× ARR. Affordable (40% of budget). Fair for code+infra; thin for business. |
| 9 | Seller & adverse-selection | 10 | 2 | med | 4.0 | Listed ~25 days post-launch. "Shifting focus" claim is plausible but suspicious at 2 months. |
| | **Merit total** | **100** | | | **53** | |

**Gates:** operable ✓ · growth-lever-fits ✓ · revenue-evidence marketplace_attested (not buyer-verified) · value-transfers unknown · IP-transferable unknown · not-fragile ✓ · **affordable ✓** ($4k vs $10k ceiling)

## Fit-to-build read (the team's lens)

This is firmly in the wheelhouse on the engineering side. React Native, Expo, TypeScript — standard mobile stack. RevenueCat for subscriptions and Sentry for monitoring are both industry-standard and already wired in, meaning day-one ops are clean. The obvious product upside (Android expansion, AI-driven study recommendations, adaptive scheduling, spaced-repetition flashcard integration) is exactly the kind of feature work this team executes well.

The growth question is different. The primary acquisition channel is ASO + TikTok. ASO is transferable and manageable — any team can improve App Store metadata, screenshots, and localization. TikTok is the unknown: if the founder's early installs came from personal Spanish-language content, that channel does not transfer. If ASO alone drove adoption, the team is fine. This team does not have organic social or content-marketing muscle, so TikTok dependency is a fit risk — resolve it before closing.

## Does the value transfer? (key-person check)

The product is simple and self-contained — study timer, planner, stats. There are no customer relationships, no sales process, no consulting dependency. On the product side, value transfers cleanly. The risk is on the acquisition channel: TikTok content that drove early downloads may be tied to the founder's persona. The seller has only 3 X followers (tiny public social presence), which could mean TikTok is the main channel under a separate account — or it could mean social was never meaningful and ASO was always primary. App Store Connect source analytics would answer this definitively. Until then, the transfer/key-person dimension stays neutral-scored.

## What we know vs. what we're assuming

- **Verified (marketplace-attested):** MRR $121, 30 active subs, ARPU $4.03, 0% MRR growth last 30 days, all-time revenue $485 (Jun $248 + Jul $236), 85% margin, RevenueCat + Sentry stack, React Native/Expo/TypeScript, iOS App Store v1.6.4, asking $4,000, listed 2026-06-29, founded 2026-06-04.
- **Assumed / unverified:** 50,000+ students (website claim, unconfirmed — likely includes free-tier downloads across non-US storefronts); 4.8★ rating (website claim, contradicts 0 ratings in US App Store — possibly Spanish storefront reviews); IP owned solely by founder (no mention of contractors); ASO as primary driver given seller's tiny social footprint.
- **Unknown (and how it swings the score):** Churn rate — if >5%/mo, drops this to PASS; if <2%/mo, upgrades PMF to 3 and unit_economics to 3 (→ ~58 merit). TikTok channel details — if persona-dependent, value_transfers may flip false (→ capped MARGINAL or PASS). IP/App Store transfer confirmation — if problematic, ip_transferable = false (→ capped MARGINAL). True reason for ultra-early exit — seller's credibility hangs entirely on this answer.

## Seller questions to send (prioritized)

1. **Why are you selling 3–4 weeks after launch — what specifically triggered the decision to list so soon?** — *resolves: seller_adverse_selection; deal-breaker if evasive or inconsistent. An app-flipper model (intentional) vs. early-exit-on-stagnation (yellow flag) changes everything.*

2. **Can you share the RevenueCat subscriber export (CSV or full dashboard screenshot) showing active subs, churn by cohort, and plan-type breakdown (monthly vs annual)?** — *resolves: revenue_evidence → buyer_verified; unlocks PMF retention and unit economics. Most critical data gap.*

3. **Is 100% of the code owned by you personally (no contractor IP, no unlicensed libraries), and can the App Store developer account transfer to a new legal entity?** — *resolves: ip_transferable; if either is 'no,' the deal caps at MARGINAL regardless of other factors.*

4. **What drove the 50k+ students you cite on your website — TikTok, organic ASO, or something else? Can you share App Store Connect install-source analytics and your TikTok account stats?** — *resolves: transfer_key_person, growth_lever_fits; if TikTok is founder-persona dependent, that channel does not transfer to this team.*

5. **What is the monthly subscriber churn rate, and can you pull a cohort retention chart from RevenueCat?** — *resolves: pmf_retention, unit_economics (LTV); the single biggest number missing from this evaluation.*

6. **What are your exact monthly operating costs — RevenueCat plan, Sentry plan, Apple developer account, any tools or contractors?** — *resolves: unit_economics; confirms the 85% margin claim.*

7. **Are you open to an earnout or holdback — e.g., 70% at close, 30% held 90 days conditional on MRR staying ≥ $100?** — *resolves: deal_terms; willingness to share downside risk is a quality signal. Refusal on a $4k deal is a yellow flag.*

8. **What would you do to grow this if you were keeping it?** — *free strategic insight and a tell about any growth ceilings already hit.*

## Recommended next step

Send questions 1–5 and evaluate the answers before making an offer. Q1 (the real reason for the early exit) and Q2 (RevenueCat export) are the decision-makers: a credible exit story + verified sub/churn data could upgrade this to PROMISING. If churn is below 3%/mo and IP transfers cleanly, the $4,000 ask is reasonable for the infrastructure + install base and the team can grow it on the engineering path. If the seller is evasive on Q1, or if churn is high, or if TikTok is creator-persona-dependent — pass.