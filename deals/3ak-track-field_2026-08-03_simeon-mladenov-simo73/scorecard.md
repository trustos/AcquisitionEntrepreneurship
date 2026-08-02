# Acquisition Scorecard (v2) — 3AK Track & Field

**Type:** Consumer mobile app (iOS) — sports/fitness training  ·  **Asking:** $350,000 (2.91x ARR)  ·  **Budget:** $10,000 ceiling (financing possible)  ·  **Date:** 2026-08-03
**Figures reconciled?** Arithmetic consistent (subs x ARPU ≈ MRR; verify_figures.py: no flags) · Two-source cross-check: TrustMRR listing + .md match · Revenue evidence: marketplace_attested (RevenueCat API badge — attested, not buyer-reconciled from source). Founder's "$100k lifetime" claim does not reconcile with $33,340 tracked; pre-May 2026 period unverified.
**Sources reviewed:** TrustMRR listing + .md, Apple App Store, 3AK Athletics website, competitor search (Track & Field AI, SprintTimer, Sprint AI)

---

## Verdict

> **PASS (provisional) — 47/100** (completeness 51%)
>
> Two independent kill signals make this a hard pass regardless of product quality. First, the primary acquisition engine is paid social ads (Meta $50–100/day) and TikTok/Instagram content marketing — this team's explicit weakness, triggering the growth-lever kill gate. Second, at $350,000 the asking price is 35x the $10k budget ceiling; even with financing this is an entirely different deal tier. On the merits alone the score lands at 47 (MARGINAL), weighed down by an unverified revenue history, declining post-peak MRR, a crowded competitor set, and a flagship AI feature (stride analysis) with known upload bugs. The 4.8-star rating and 1.4K reviews show real user love, and the SwiftUI/Supabase stack is runnable — but neither overrides the budget reality or the channel mismatch.

---

## Scorecard (nine dimensions)

| # | Dimension | Wt | Score /5 | Conf | Weighted | Notes |
|---|---|---|---|---|---|---|
| 1 | Operability & product upside | 15 | 3 | med | 9.0 | SwiftUI + Supabase runnable; mobile in team wheelhouse. Engineering upside real (better AI, Android). Version 5.9 in 8 months signals active maintenance burden. |
| 2 | PMF & retention | 15 | 2 | low | 6.0 | 4.8 stars / 1.4K ratings = genuine love. Revenue dropped 29% June to July (likely seasonal — US outdoor T&F ends June). Core stride-analysis upload fails after first use. Cohort data unknown. |
| 3 | Unit economics & upside | 12 | 3 | low | 7.2 | 80% margin claimed but effective margin lower after Apple 15–30% cut + ads ($1.5–3k/mo). $3.35 ARPU is thin. Pricing headroom exists (annual up to $49.99). LTV unknown without churn. |
| 4 | Moat & defensibility | 12 | 2 | med | 4.8 | Crowded sports-fitness AI space. Direct competitors: Track & Field AI, Swagger Eyes SprintTimer, Sprint AI. No switching costs. 4.8 stars help marginally. |
| 5 | Growth & market | 8 | 3 | low | 4.8 | Sports AI coaching is a genuine tailwind. July decline likely seasonal (T&F outdoor season). But T&F niche is small and competitor set multiplying. Full annual cycle not yet visible. |
| 6 | Tech & IP health | 8 | 3 | low | 4.8 | Modern stack (SwiftUI, Supabase, RevenueCat). App Store dependency = 15–30% platform cut. IP ownership unconfirmed. Stride analysis bug is unknown severity. |
| 7 | Transfer / key-person | 10 | 2 | med | 4.0 | TikTok/Instagram content is core acquisition channel — if founder is on camera, it doesn't transfer. Meta Ads transfer. App brand appears separate from founder identity, but unconfirmed. |
| 8 | Deal terms & value | 10 | 1 | high | 2.0 | $350k for 8-month-old app, 3 months of tracked rev ($33k all-time), declining July. 35x budget ceiling. Even with financing this is an entirely different deal class. |
| 9 | Seller & adverse-selection | 10 | 2 | med | 4.0 | "Too many projects" is a soft sell. Listed at/near June revenue peak. "$100k" claim vs $33k tracked unreconciled. 8-month-old app going to market early is a mild lemon flag. |
| | **Merit total** | **100** | | | **47** | |

**Gates:** operable PASS · **growth-lever-fits FAIL (KILL → PASS)** · revenue-evidence marketplace_attested · value-transfers unknown · IP-transferable unknown · not-fragile PASS · **affordable: NO — $350k asking vs $10k ceiling (35x over)**

---

## Fit-to-build read (the team's lens)

The stack (SwiftUI + Supabase) is runnable and mobile is in the team's wheelhouse — operability is fine. The engineering upside is real: better AI form analysis, an Android port, deeper personalization, AI-powered coaching improvements. If the team owned this product, they could improve it.

But the business doesn't grow through engineering — it grows through daily TikTok/Instagram content creation and paid Meta Ads management. These are full-time disciplines the team explicitly doesn't staff. Buying this business means immediately hiring or becoming a social-media content creator and ads manager, or watching revenue decay as the organic channel goes cold. That's buying your weakness.

**growth_lever_fits = FALSE → PASS (kill gate)**

---

## Does the value transfer? (key-person check)

This is genuinely uncertain. The 3AK brand appears to stand on its own (dedicated domain, Instagram, TikTok presence), which is encouraging. But the founder's reason for selling is "working on too many projects" — which implies active personal involvement in running those channels. The App Store developer account ("CHRISTIAN MICAH JONES") and 1,086 X followers suggest a solo-founder operation where day-to-day content and community management are founder-driven. Until we see which social accounts transfer and whether the content is founder-on-camera vs brand-produced, value_transfers = unknown.

---

## What we know vs. what we're assuming

**Verified / marketplace-attested:**
- MRR $10,005, 2,984 active subscriptions, ARPU $3.35 (RevenueCat API — attested, not buyer-reconciled)
- Arithmetic consistent: 2,984 x $3.35 = $9,996 ≈ MRR; asking / ARR = 2.91x
- Monthly trend: May $5,089 | June $16,461 | July $11,716 (-29%) | Aug $74 (2 days)
- App Store: 4.8/5 stars, 1.4K ratings, free + IAP, weekly/monthly/annual tiers
- Known bugs: stride analysis fails after first upload; UI text color issues; calorie stats not resetting
- Active update history: v5.1–5.9 across June–Aug (9+ versions in 8 months)
- Competitors confirmed: Track & Field AI, Swagger Eyes SprintTimer, Sprint AI
- Founded December 2025; founder: Christian Rac / Christian Micah Jones, 1,086 X followers

**ASSUMED:**
- July revenue decline is seasonal (US outdoor T&F season ends June) — not verified with historical full-year data
- 80% margin is after RevenueCat/Supabase but may not net out Apple's 15–30% platform cut or ad spend
- IP is founder-owned with no contractor components — inferred from listing language
- Brand/social accounts are transferable — inferred from listing language

**UNKNOWN (and how it swings the score):**
- Monthly churn rate: if >5%/mo, LTV ~$67 and unit economics collapse at $3.35 ARPU; if <2%, LTV ~$168 and economics are interesting. A 1% swing can move merit ±8 pts.
- Pre-May 2026 revenue: founder claims $100k; tracked data shows $33k since May 20. If earlier months averaged ~$11–13k/mo this is consistent. If sub-$5k, the figure is materially inflated and revenue_evidence becomes contradicted.
- Seasonal revenue floor: what does MRR look like in August–October? If floor is $4–5k, real ARR baseline is ~$55k, making $350k nearly 6.5x ARR.
- Content channel ownership: if founder is on camera for TikTok/Instagram, growth stalls post-acquisition without a content creator hire.
- Stride analysis bug severity: a 1-day fix vs. a structural SDK issue are very different for ops load and churn.

---

## Seller questions to send (prioritized)

1. **Full revenue export from Day 1** — Share the complete RevenueCat export from December 2025 through today (monthly breakdown), so we can reconcile the "$100k in 6 months" claim. We see $33,340 tracked from May 20 onward. [Resolves: revenue_evidence, seller_adverse_selection — the foundational number in this deal]

2. **Monthly churn rate + cohort chart** — What is logo churn per month, and can you share a cohort retention chart? What % of active subscriptions are weekly vs monthly vs annual? [Resolves: pmf_retention, unit_economics — single number that can flip the economics]

3. **Off-season revenue floor** — What did MRR look like in August, September, October 2025 (or your earliest months)? Is the June spike tied to the US outdoor track season? What's the seasonal floor to model? [Resolves: growth_market, unit_economics — if floor is $4–5k the real multiple triples]

4. **Content channel: who is the face?** — Who creates the TikTok/Instagram content — you personally on camera, or a brand account a new operator could run? Will all social accounts, ad campaigns, and the developer account transfer? [Resolves: transfer_key_person, growth_lever_fits — the key gate question]

5. **IP and account transfer checklist** — Is 100% of the code owned by you or a legal entity (no contractor IP, no un-relicensable components)? Can the App Store developer account, RevenueCat org, Supabase project, domain, and social handles all transfer cleanly? [Resolves: ip_transferable, value_transfers]

6. **Stride analysis bug** — App Store reviews report the video upload for stride analysis failing after the first use. What is the root cause and current fix status? [Resolves: operability_upside, tech_ip — this is the flagship AI feature]

7. **True cost structure** — Can you share the actual monthly cost breakdown: Apple platform fee (net of their cut), RevenueCat plan, Supabase hosting, Meta Ads actual spend, any contractor costs? [Resolves: unit_economics — the 80% margin needs to be netted against the Apple platform tax]

8. **Deal structure openness** — Are you open to seller financing, an earnout tied to subscriber retention over 12 months, or a holdback in escrow? At $350k vs our $10k ceiling even with financing, we would need creative structure or a significant price reduction. [Resolves: deal_terms — refusal to hold any note is a signal; also, at $350k this is structurally unreachable for this team]

9. **Strategic read** — Why sell at 8 months? What would you do in the next 6 months to grow this if you were staying? [Resolves: seller_adverse_selection, growth_market — free strategic intel and a tell about the ceiling the seller already sees]

---

## Recommended next step

**Pass on this deal.** Two independent veto signals, each sufficient on its own:

1. **Budget:** $350k is 35x the $10k ceiling. Even with "financing possible," this is a $350k acquisition requiring substantial external debt or investor capital — a fundamentally different commitment than the deal class this team is screening in.

2. **Channel mismatch:** The business runs on TikTok/Instagram content creation and Meta Ads management. This team does not do marketing. Buying this means immediately hiring a social content creator and an ads manager to maintain revenue, or watching MRR decay post-acquisition. That is buying the team's biggest operational weakness.

If the budget ceiling ever reaches $50–100k AND the team adds marketing capability, this category of deal (niche sports AI coaching app with real user love) is worth revisiting. But for now: Pass.
