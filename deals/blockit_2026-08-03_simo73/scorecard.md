# Acquisition Scorecard (v2) — Blockit

**Type:** consumer/prosumer mobile app (B2C, subscription) — fitness-gamified screen-time blocker · **Asking:** $9,500 (~0.9x annualized total revenue per TrustMRR; ~2.5x annualized true recurring MRR) · **Budget:** $10,000 · **Date:** 2026-08-03
**Figures reconciled?** Two-source check done (TrustMRR listing page + `.md` profile). `verify_figures.py` flagged the stated 0.9x multiple against MRR-annualized ($321×12) as off by ~2.7x — reconciled: TrustMRR's 0.9x is computed against **annualized total revenue** ($834×12 ≈ $10,008), not recurring MRR. Revenue evidence: **marketplace_attested** (RevenueCat API-verified by TrustMRR; not buyer-verified from source dashboard).
**Sources reviewed:** trustmrr.com/startup/blockit (listing page + `.md` profile); general category knowledge of "exercise-to-unlock" screen-time apps (unverified against live App Store/competitor search — search tools returned no usable results this session).

## Verdict

> **PASS (provisional) — 53/100** (completeness 50%)
> This is squarely in the team's technical wheelhouse (native iOS/Android + on-device pose-detection ML, NestJS/Postgres backend) — the engineering itself is very buildable and improvable. But the business is capped by the **growth-lever-fits gate**: the listing states growth is "100% organic via short-form content" (TikTok/Instagram) — a content-creation treadmill that lives or dies on someone's ability to keep producing viral video, not a skill in this team's profile. That single verified fact caps the deal at PASS regardless of the underlying merit score. Secondary concerns: PMF/retention and true unit economics are unverified (no churn data, ARPU is thin at ~$3.31/active sub, and $834 of "30-day revenue" doesn't match the $321 MRR — a chunk of revenue is one-time/annual, not steady recurring), and 30-day growth is flat at 0.0% right as the 5-month-old business is listed for sale.

## Scorecard (nine dimensions)

| # | Dimension | Wt | Score /5 | Conf | Weighted | Notes |
|---|---|---|---|---|---|---|
| 1 | Operability & product upside | 15 | 5 | high | 15.0 | Exact stack match: SwiftUI, Kotlin, NestJS/Postgres, on-device pose detection. Founder's own note (conversion 1.3%→3-5% potential) is a clear, buildable upside lever. |
| 2 | PMF & retention | 15 | 2 | low | 6.0 | 97 active subs, 4.7/5 rating (n=9, too small to trust), but no churn/retention data at all. Neutral score per golden rule — absence of evidence isn't evidence of bad, but it's genuinely thin. |
| 3 | Unit economics & upside | 12 | 2 | med | 4.8 | 80% margin is attractive, but ARPU is very low (~$3.31/sub/mo), no CAC baseline to compute LTV:CoCA (claimed "no ad spend" makes the ratio look infinite but untested), and $834 30-day revenue vs $321 MRR implies meaningful one-time/annual-prepay mix, not pure steady recurring. |
| 4 | Moat & defensibility | 12 | 1 | low | 2.4 | Pose-detection "exercise to unlock" mechanic uses standard off-the-shelf tooling (MediaPipe-class libraries) — technically easy to clone. No network effect, no switching cost, no proprietary data moat identified. |
| 5 | Growth & market | 8 | 3 | low | 4.8 | Digital-wellbeing/fitness-gamification is a real trending niche (esp. with Gen-Z short-form audiences), but also fast-copied. 30-day revenue/MRR growth reported at 0.0% — flat right at the point of sale. |
| 6 | Tech & IP health | 8 | 4 | med | 6.4 | Real native codebase (not a no-code wrapper), GitHub connected with genuine ongoing activity (706 contributions/year). Presumed owned by the solo founder — not yet confirmed in writing. |
| 7 | Transfer / key-person | 10 | 2 | low | 4.0 | Growth channel is short-form content — unclear whether published from a personal founder account or a branded app account. If personal, virtually none of the distribution survives the founder's exit. |
| 8 | Deal terms & value | 10 | 3 | med | 6.0 | $9,500 fits inside the $10,000 ceiling (affordable, no financing needed). Multiple is reasonable-ish once you use true recurring MRR (~2.5x annualized) for a 5-month-old, unverified, thin-ARPU app — not cheap, not egregious. |
| 9 | Seller & adverse-selection | 10 | 2 | low | 4.0 | Reason given is generic ("moving to next project"). Business is only 5 months old and already for sale, with growth flatlined at 0% in the most recent 30 days — consistent with a viral-spike-then-plateau pattern common in indie-flip listings. Not proven, but a real caution flag. |
| | **Merit total** | **100** | | | **53.4 → 53** | |

**Gates:** operable **true** · growth-lever-fits **false** (caps to PASS) · revenue-evidence **marketplace_attested** (provisional) · value-transfers **unknown** (provisional) · IP-transferable **unknown** (provisional) · not-fragile **true** · **affordable: yes** ($9,500 within $10,000 ceiling, no financing required)

## Fit-to-build read (the team's lens)

The *product* is a great fit — cross-platform native mobile + a real ML feature (on-device pose detection), exactly the "modernize it, add obvious features, add AI" profile the team excels at. The *problem* is that the path to more revenue here isn't primarily an engineering problem — it's "keep making TikToks that go viral," which is a content-creator skill, not a software-engineering one. Buying this asset means either the team takes on ongoing short-form content production themselves (outside their stated strengths) or hires/outsources it (added cost and a new dependency), while the underlying app itself has limited additional engineering upside beyond the founder's already-identified conversion-rate fix.

## Does the value transfer? (key-person check)

Unclear and unverified. If the TikTok/Instagram accounts driving growth are the founder's personal handles, essentially none of the distribution conveys at sale — a buyer would inherit a decent app with zero incoming traffic. If they're branded app accounts, the audience conveys but the *skill* to keep it growing (content creation cadence, trend-following, editing) still doesn't automatically transfer with the account. This is the single highest-leverage question to send the seller before proceeding.

## What we know vs. what we're assuming

- **Verified (TrustMRR-attested, cross-checked page + .md profile):** MRR $321, active subs 97, 30-day revenue $834, asking price $9,500, 0.9x stated multiple (reconciled to annualized total revenue basis), 80% margin, founded March 2026, App Store rating 4.7/5 (n=9), tech stack (SwiftUI/Kotlin/NestJS/Postgres), GitHub connected with real commit activity, growth channel stated as "100% organic via short-form content" (TikTok/Instagram/ASO), reason for sale ("moving to next project").
- **Assumed / marketplace-attested only (not buyer-verified from source):** All revenue/subscriber figures come from TrustMRR's RevenueCat integration, not a Stripe/RevenueCat dashboard the buyer has inspected directly. Founder's own restated numbers ("~7,000 active users, ~$317 MRR, ~1.3% conversion") differ slightly from platform figures and weren't independently checked.
- **Unknown (and how it swings the score):** Churn/retention trend (could move PMF from 2→4 or confirm decline); whether social accounts are personal or branded, and whether they transfer (could move transfer/key-person and even reverse the growth-lever call if growth turns out to be more product-led/ASO-driven than content-creator-driven); code/IP ownership and Apple Developer account transferability; competitive crowding in the "exercise-to-unlock" niche (search tools returned no usable results this session — genuinely unresearched, not just unavailable); true cause of the 0% 30-day growth (plateau vs. seasonal vs. algorithm change).

## Seller questions to send (prioritized)

1. What % of new users/revenue come from your personal TikTok/Instagram account vs. a branded app account, and do those social handles transfer at sale? — *resolves: growth-lever-fits, transfer/key-person; this is the single fact that could most change the verdict.*
2. Can you export the last 5 months of revenue directly from RevenueCat/App Store Connect (not the TrustMRR dashboard), and what's the recurring-vs-one-time/annual split? — *resolves: revenue-evidence, unit economics; reconciles the $834/30-day vs $321-MRR gap.*
3. What's monthly subscriber churn, and do you have a retention/cohort chart? — *resolves: PMF & retention; currently the single weakest-evidence dimension.*
4. Why has 30-day revenue/MRR growth flattened to 0.0% right as you're listing it for sale — what changed? — *resolves: seller/adverse-selection, growth & market.*
5. Is 100% of the code, the Apple Developer account, and the Google Play account owned solely by you and transferable (no contractor-owned IP)? — *resolves: IP-transferable gate.*
6. Are you open to a short earnout or holdback tied to 60–90 days of post-sale retention, given the growth-channel uncertainty? — *resolves: deal terms; shifts risk back onto the better-informed seller.*

## Recommended next step

Pass, provisionally. The growth-lever gate is tripped by a fact stated in the seller's own listing (organic short-form-content growth), which sits outside this team's stated strengths regardless of how the other numbers verify. If the user wants to pursue anyway, question 1 above is the one that could flip the picture — if the audience is a transferable branded account and ASO/product virality (not personal content creation) turns out to be the real driver, this would be worth a full re-score. Otherwise, treat this as a pass and move to the next candidate.
