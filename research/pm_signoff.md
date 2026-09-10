# PM Fact-Check, Risk Review & Sign-Off — AI-Hardware Long/Short Book

**Reviewer role:** Portfolio Manager (final fact-check, risk review, sign-off)
**As-of date:** 2026-09-10
**Horizon reviewed:** ~6 months (now through ~end-Q1 2027)
**Documents under review:**
- `research/longs_ai_hardware.md` (branch `cursor/ai-hardware-longs-memo-eb27`) — proposed long book: NVDA 24%, TSM 18%, MU 17%, AVGO 16%, VRT 13%, ANET 12%.
- `research/shorts_ai_hardware.md` (branch `cursor/ai-hardware-short-memo-6763`) — proposed short book: SMCI 30%, ARM 25%, ALAB 20%, MRVL 15%, CRDO 10%.

> **DISCLAIMER — READ FIRST.** This is a **research/educational exercise, NOT investment advice**, and not a recommendation, solicitation, or offer to buy, sell, or short any security. It was produced by an AI agent as a point-in-time review on 2026-09-10 using public web sources that may be incomplete, stale, or wrong. Prices, multiples, and forward figures are approximate and as-of their cited dates; nothing here is verified against a live brokerage/market-data terminal. Short selling carries risk of unlimited loss. The reviewer holds no position. **Do your own diligence and consult a licensed professional.** See full disclaimer in §6.

---

## 1. Executive verdict

**Overall decision: CONDITIONAL SIGN-OFF — APPROVE WITH MODIFICATIONS. Do NOT deploy as-is.**

The good news first, because it is unusual: **both analysts got their numbers right.** I independently re-checked every material headline figure in both memos against primary filings/press releases (NVDA, TSM, MU, AVGO, ANET, VRT on the long side; SMCI, ARM, ALAB, MRVL, CRDO on the short side) and they reconcile. The single figure the longs analyst explicitly could not reconcile — **Micron's $41.46B quarter at ~85% gross margin** — is, in fact, exactly what Micron reported (see §2). So the flag was appropriate skepticism, not a caught error; the number is real, and its *implications* are the issue, not its accuracy.

**The problem is not the facts — it is portfolio construction and unrewarded, correlated risk.** My headline changes:

1. **This is not market-neutral. Sized 1:1 (100% long / 100% short) it is net-SHORT the AI-semis beta factor**, because the short book is concentrated in higher-beta names (SMCI/ALAB/CRDO) than the long book. As delivered it is a *disguised net-short-the-AI-trade macro bet*. Fix: beta-weight the sizing (run the short book at ~70–75% of long notional) so P&L is driven by dispersion, not market direction.
2. **The combined book is aggressively net-long the memory supercycle via MU (17%) with zero offset**, and MU is simultaneously the highest-variance name AND the clearest embodiment of the "circular financing" tail both memos warn about (its 85% GM is being locked in via multi-year *prepaid* Strategic Customer Agreements with the same capital-constrained AI ecosystem). **Trim MU to ~12%.**
3. **The short book is over-concentrated: SMCI at 30% into ~14–15% short interest is a squeeze accident waiting to happen**, and the ALAB+MRVL+CRDO connectivity trio (45% of the short book) is effectively **one factor bet, not three**. Trim SMCI to ~20% with a hard stop; cap the connectivity cluster and treat it as a single position.
4. **Severe catalyst clustering in late-Oct → early-Nov 2026**: ~9 of the 11 names print or hold binary events in a ~3-week window. Size *into* catalysts; do not carry full gross through the cluster.
5. **Shared single points of failure hit both books at once**: TSMC/CoWoS, HBM, hyperscaler capex/financing. The L/S pairing *does* hedge the macro air-pocket (shorts win if longs crater), which is a genuine strength — but a Taiwan shock or memory roll-over is only partially offset because the long book carries the un-hedgeable Taiwan concentration (TSM 18% + NVDA/AVGO all TSMC-dependent).

**Net:** the research is high-quality and honestly caveated; deploy a **beta-neutralized, resized** version with strict single-name/cluster caps and a macro kill-switch. Details in §5.

---

## 2. Fact-check findings

Every material figure was checked against the primary source. Summary: **no material misstatements of reported numbers in either memo.** The findings below are the exceptions worth flagging — mostly staleness, mislabeling, framing, and internal data-hygiene issues, plus the Micron reconciliation the task asked me to scrutinize.

| # | Claim (memo) | Memo | My finding | Source (+date) |
|---|---|---|---|---|
| 1 | Micron FQ3-26 rev **$41.46B**, GAAP GM **84.6%** / non-GAAP **84.9%**, non-GAAP EPS **$25.11**; FQ4 guide **$50.0B ± $1.0B, ~86% GM, non-GAAP EPS $31.00** | Both | **VERIFIED — accurate as reported.** Longs analyst flagged it as "could not reconcile to historical run-rate." Correct instinct (346% YoY; ~85% GM is unprecedented for memory), but the numbers match the filed release verbatim. GAAP EPS guide is **$30.73**; non-GAAP **$31.00** (memo used non-GAAP — correct). The real issue is *sustainability/credibility*, not transcription — see §4. | Micron 8-K / press release, SEC, 2026-06-24 |
| 2 | MU next print is "**FQ1 2027** (~late Sep 2026)" | Longs | **MISLABELED.** Micron's fiscal year ends late August; the imminent late-Sep print is **FQ4-26** (the quarter the $50B guide covers), not FQ1-27. Same event, wrong fiscal tag. Immaterial to thesis. | Micron 8-K, 2026-06-24 |
| 3 | Vertiv "backed by a **$15B backlog**" (reason NOT to short) | Shorts | **MISLEADING / STALE.** Vertiv's **Q2-26 release disclosed NO backlog or orders figure at all**; the ~$15B was an entering-2026 figure (vs $8.5B led-with in Q2-25). The longs memo caught this correctly ("transparency step-down… yellow flag"). Shorts analyst leaned on an undisclosed/stale number. | Vertiv Q2-26 release, 2026-07-29; top1markets analysis, 2026-08-13 |
| 4 | Vertiv price | Both | **INTERNALLY INCONSISTENT across memos**: longs cite ~**$252.83**, shorts cite ~**$262.83** for the same 2026-09-10 date (third-party VRT close was ~$287 on 2026-08-13). Data-hygiene flag; doesn't change the thesis. | Both memos; top1markets, 2026-08-13 |
| 5 | "CRDO FQ2'26 rev **$268m +272%**" | Longs | **STALE.** Credo's most recent print (FQ1-27, ended 2026-08-01) was **$479.0M, +114.7% YoY**. The $268M/+272% is a real but ~3-quarter-old figure. CRDO is only a "not-included" name in the long memo, so low materiality, but the as-of hygiene is off. | Credo 8-K, 2026-09-01 |
| 6 | Broadcom's OpenAI "Jalapeño" described as "merely *comparable* to Vera Rubin" (supports NVDA moat) | Longs | **MIS-ATTRIBUTED, and understates the competitive claim.** On the call, Hock Tan said the **TPU v8i** is "comparable if not surpasses the Vera Rubin GPU," and **Jalapeño "outperforms Grace Blackwell for inference."** The longs memo conflated the two and softened the message — Broadcom's public claim is *more* aggressive than "comparable," which cuts slightly against the NVDA-moat framing (and *for* the AVGO long). | AVGO Q3-FY26 call transcript, 2026-09-09 |
| 7 | Hyperscaler 2026 capex ~**$720–745B** (~$835B incl. Oracle); UBS growth **76%→25%→6%** (2026→28); **82%** call semis most-crowded trade | Both | **VERIFIED.** UBS: capex +76% in 2026 (~$673B base), +25% 2027, +6% 2028. BofA July-26 survey: record **82%** long-semis = most crowded trade ever (up from 80% June); **48%** see AI hyperscaler capex as the likeliest systemic-credit-event source. | Reuters, 2026-07-17; BofA GFMS July 2026 |
| 8 | NVDA Q2-FY27 rev **$96.2B (+106%)**, DC **$89.0B (+117%)**, Q3 guide **$108.0B ±2% @ 74% GM, zero China DC**; ~**70% FY28** growth guide | Both | **VERIFIED** against primary release. (Note: some secondary outlets, e.g. a Fortune line, misprinted the Q3 guide as "$91B" — that was the *prior* Q2 guide; the official Q3 number is $108.0B.) | NVIDIA 8-K/CFO commentary, SEC, 2026-08-26 |
| 9 | AVGO Q3-FY26 rev **$29.6B (+86%)**, AI semi **$16.7B (+221%, +54% QoQ)**, Q4 AI **$21.7B**, FY26 AI **$58B**, FY27 **$115B** / FY28 **$230B** | Longs | **VERIFIED** (rev/AI/guide all match; op margin ~68%, GM 75%). | Broadcom PRNewswire + call, 2026-09-02 / 09 |
| 10 | TSM Q2-26 rev **NT$1,270B / US$40.2B (+36%)**, GM **67.7%**, Q3 guide **US$44.6–45.8B, 65–67% GM**, FY26 "slightly above 40%" USD | Longs | **VERIFIED** against release. | TSMC 2Q26 release / SEC 6-K, 2026-07-16 |
| 11 | ANET Q2-26 rev **$3.036B (+37.7%)**, first $3B quarter, Q3 guide ~**$3.3B**, FY26 ~**$12.6B**, GM held **62–64%** on memory/silicon cost | Longs | **VERIFIED** (incl. the GM-headwind caveat). | Arista 8-K/release + call, 2026-08-04 |
| 12 | SMCI Q4-FY26 non-GAAP GM **17.6%** vs guide 8.2–8.4%, ~75% from deferred-contract mix; Q1-FY27 GM guide **10.4–10.8%**; FY27 rev **$65–72B** | Shorts | **VERIFIED.** Also note an item the short memo omitted: SMCI issued **$4.2B of mandatory convertible preferred** in Q4 (dilution/complexity) — *additional* support for the short. | SMCI release + prepared remarks/call, 2026-08-18; 24/7 Wall St., 2026-09-08 |
| 13 | ARM Q1-FY27 rev **$1.29B (+22%)**, royalties **+22% to $715M**, licensing **+23% to $574M**, non-GAAP EPS **$0.45**; Qualcomm trial **Q4 2026**; DC royalties >2x YoY | Shorts | **VERIFIED.** Qualcomm's countersuit trial is set for Q4 2026 (nuance: this is *Qualcomm suing Arm*, distinct from the Nuvia case Qualcomm already won in 2025). The DC-CPU inflection (Vera in full production on Arm; AWS Graviton5 tens of millions of cores; Axion, Cobalt 200) is a **material risk to the short** — the memo acknowledges it. | Arm 6-K/shareholder letter, 2026-07-29; m1k.tech, 2026-07 |
| 14 | ALAB Q2-26 rev **$392.4M (+104%)**, GM 73.3%, one customer **29%**, four ≥13%, China/Sing/TW most of rev; insiders sold ~**$209.7M/90d** incl. COO Gajendra **90,630 sh @ ~$340.35 on 2026-08-17** | Shorts | **VERIFIED.** 10-Q confirms concentration/geography; Form 4s confirm CEO Mohan AND COO Gajendra each sold **90,630 sh @ $340.36 on 2026-08-17** (plus large May/July sales). Fair caveat: most are 10b5-1 / sell-to-cover, so it's supply overhang, not necessarily a conviction signal. | ALAB 10-Q, 2026-08-04; OpenInsider Form 4s, Aug 2026 |
| 15 | MRVL Q2-FY27 rev **$2.739B (+37%)**, DC +46%, FY27 raised ~**$12B**, FY28 raised to ~**$18B** (from $16.5B); **Investor Day Oct 6, 2026**; Q3 non-GAAP GM guided **57.5–58.5%** | Shorts | **VERIFIED.** Oct-6 NYC Investor Day is company-confirmed; Google warrant (up to 7% of shares on revenue milestones) confirmed; custom "more than doubling" in FY28 with the *material* ramp H2-FY27+. Market-cap cite (~$189B) is a touch low vs third-party ~$212B — immaterial. | Marvell Q2-FY27 release + call, 2026-08-27; IR Investor Day notice |
| 16 | CRDO FQ1-27 rev **$479M (+114.7%)**, top-4 customers **33/28/13/10%** (top-2 ~61%), Q2 guide **$525–535M**, inventory +$62.2M QoQ to $313.1M | Shorts | **VERIFIED.** (Minor: memo says "eighth consecutive beat"; company framed it as the seventh consecutive triple-digit-growth quarter — different metric, immaterial.) | Credo 8-K + call, 2026-09-01 / 08 |

**Valuation sanity checks (position-sizing relevant):** MU ~**$958–1,000 / ~$1.1T** market cap (longs memo ~$971/$1.10T — accurate; note MU screens even cheaper than the memo's 13.3x fwd P/E — some sources put it ~6–8x FY27, reinforcing "cheap on peak earnings"). NVDA ~**$228 / $5.52T**, ~24x forward (memo $215–225 / $5.2–5.5T / 23–25x — accurate). Both confirm the sizing logic is built on real numbers.

**Bottom line on facts:** I would not reject a single position on a factual error. The analysts were disciplined and well-sourced. My value-add is entirely in §4–§5 (risk/construction).

---

## 3. Per-position sign-off

### Long book

| Name | Wt | Decision | One-line rationale |
|---|---:|---|---|
| **NVDA** | 24% | **APPROVE** | Numbers verified, best moat/visibility/valuation trade-off; keep the ≤25% cap since it's the purest macro-beta expression. Watch: AVGO's claim that TPU v8i "surpasses Vera Rubin" is a sharper ASIC threat than the memo conveys. |
| **TSM** | 18% | **APPROVE (with portfolio caveat)** | Cheapest quality in the book; but combined with NVDA/AVGO it stacks an **un-hedgeable Taiwan single-point-of-failure** — acceptable at 18% only because the short book profits in a Taiwan shock (partial hedge). |
| **MU** | 17% | **APPROVE WITH MODIFICATION → trim to ~12%** | Thesis and numbers are real, but it's the highest-variance name AND the epicenter of the circular-financing tail (85% GM locked via prepaid multi-year agreements). Peak earnings on a trough multiple is the classic value trap; it also has no short-side offset. Size it as a satellite, not an anchor. |
| **AVGO** | 16% | **APPROVE** | Elite execution, verified; genuine #2-to-NVDA. Acute ~6-customer XPU concentration (model labs) is the circular-financing hot spot — fine at 16%. |
| **VRT** | 13% | **APPROVE WITH MODIFICATION → trim to ~10%, add hard stop** | Best *diversifier* (power/thermal, non-silicon), but the Q2 revenue miss + **withheld backlog disclosure** is a real yellow flag and the Q3 print is a binary. Reduce and protect with a stop below the Q2-selloff low. |
| **ANET** | 12% | **APPROVE** | Verified; the one internal hedge to the memory-cost thesis (memory inflation is an ANET headwind), which is desirable. Keep. |

### Short book

| Name | Wt | Decision | One-line rationale |
|---|---:|---|---|
| **SMCI** | 30% | **APPROVE WITH MODIFICATION → cut to ~20%, hard stop, size into the print** | Cleanest thesis (management's *own* 10.4–10.8% GM guide undercuts the 17.6% "beat"), and I add the $4.2B mandatory-convert as extra support — but **~14–15% short interest into a low-DTC name is squeeze fuel**. 30% is too big for the most crowded short in the book. |
| **ARM** | 25% | **APPROVE WITH MODIFICATION → cut to ~15–18%** | Valuation + royalty-decel + Q4 Qualcomm trial are real, but the **data-center-CPU inflection is accelerating** (Vera in full production on Arm; Graviton5). This is a pure valuation/timing short against a strengthening narrative — smaller, and size into the Q2 print. |
| **ALAB** | 20% | **APPROVE WITH MODIFICATION → ~12–15%, treat as part of one cluster** | Extreme multiple + 29% single-customer concentration + persistent insider supply, all verified. But it's *executing and broadening* and is one leg of a correlated trio (below). |
| **MRVL** | 15% | **APPROVE WITH MODIFICATION → ~10–12%, size into Oct-6 Investor Day** | "Good news already in the number," FY29 custom ramp deferred to the Oct-6 event — a clean sell-the-news setup. But it's a positioning/valuation call on a raised-guidance, no-sell-rating mega-cap; keep modest. **Note: the longs analyst *rejected* MRVL as too expensive — the two analysts actually agree it's overvalued; there is no long/short conflict here (see §4).** |
| **CRDO** | 10% | **APPROVE (smallest) or REPLACE with cluster cap** | Most concentrated (top-2 ~61%) but also cheapest (~41x fwd on 85%+ growth) → thinnest edge, which is why it's a satellite. Fine at ≤10%, but only counts inside the connectivity-cluster cap. |

**No position is a REJECT on the merits.** The modifications are all resizing/hedging, plus the connectivity-cluster consolidation.

---

## 4. Combined-portfolio risk assessment

### 4.1 Net / gross exposure and factor tilt — *the central issue*
Neither memo specified sizing relative to the other. If deployed the obvious way — **100% long / 100% short (200% gross, ~0% net notional)** — it is **NOT market-neutral**:
- Long-book beta to the AI-semis/SOX factor is high but anchored by mega-cap leaders (NVDA/TSM/AVGO): weighted β ≈ 1.6–1.8.
- Short-book beta is **higher**, dominated by ultra-high-beta names (SMCI, ALAB, CRDO): weighted β ≈ 2.0–2.3.
- Dollar-neutral therefore leaves the combined book **net-SHORT the factor (net β ≈ –0.3 to –0.5)**. In a continued melt-up it loses on beta *before* any single-name thesis plays out — i.e., it is a **disguised short-the-AI-trade macro bet**, exactly the risk the shorts analyst warned about but did not size out.
- **Fix:** beta-weight the books. Run short notional at **~70–75% of long notional**, or shift shorts away from the highest-β small-caps, targeting **net factor β ≈ 0 (±0.2)**. Then P&L is driven by *dispersion* (leaders vs. expensive derivatives), which is the actual edge.

### 4.2 Overlaps and "long-and-short-at-once" check
The task flagged MRVL/ARM/ALAB/CRDO as potential long/short conflicts. On inspection: **there is no literal conflict — the long analyst did not take positions in any of them.** MRVL, ARM, ALAB, CRDO all appear only in the longs memo's "considered but not included" section. In fact:
- **MRVL:** longs analyst *rejected* it as "richest large-cap here (~76x fwd), redundant vs AVGO." The shorts analyst shorts it on valuation. **They agree it's expensive** — the short is consistent with, not contradicted by, the long book.
- **ARM:** longs analyst omitted it (quality franchise, didn't own). Shorted on valuation/timing. No conflict.
- **ALAB/CRDO:** longs analyst admired the fundamentals but declined to buy (too small/expensive for a concentrated book). Shorts them on multiple. This is a "great company, wrong price" tension, not a book conflict.
- **Net:** no name is simultaneously long and short. The premise of a direct conflict does not hold; the tension is thesis-level (secular-quality vs. valuation/de-rate), which is fine and even complementary.

### 4.3 Correlation, crowding, and single points of failure — hitting BOTH books
- **Connectivity cluster (short side):** ALAB + MRVL + CRDO = 45% of the short book and, per the shorts analyst's own source, "reprice together on the same forward multiple compression." **Treat as ONE position** for risk limits — the book has ~2.5 independent short bets, not five.
- **Shared macro spine (both books):** TSMC/CoWoS, HBM/DRAM, hyperscaler capex, and circular/debt/prepay financing underpin *every* name on both sides. Implications:
  - **Air-pocket / financing unwind:** longs crater, shorts profit → the L/S pairing **is a genuine hedge here.** This is the book's best structural feature and argues *for* running them together.
  - **Melt-up:** longs win, shorts lose → the net-short-β problem in §4.1 bites.
  - **Taiwan/CoWoS shock:** hits longs catastrophically (TSM 18% + NVDA/AVGO all TSMC-dependent) and *also* hits the shorts (all TSMC-dependent) → shorts partially offset, but the long book carries the residual, un-hedgeable tail.
  - **Memory roll-over:** hurts MU (17% long, highest variance) with **no offset** — the shorts analyst deliberately did not short memory (correctly calling MU a squeeze risk). The combined book is thus **structurally net-long the memory supercycle**, its least-hedged exposure. This is the strongest argument for the MU trim.
- **Micron / circular-financing nexus:** MU's 85% GM is being underwritten by multi-year **prepaid** Strategic Customer Agreements with the same AI ecosystem both memos flag as debt-/circularly-financed. Being 17% long the beneficiary of that prepay *and* not shorting anything that would offset a memory reversal concentrates precisely the risk the memos identify as systemic. (BofA: 48% of managers see hyperscaler capex as the likeliest systemic-credit-event trigger.)

### 4.4 Catalyst calendar — clustering risk is real and dated
Verified/estimated event dates land in a tight window:
- **~Late Sep 2026:** MU FQ4-26 print (imminent; first test of the $50B/86% trajectory).
- **Oct 6, 2026:** MRVL Investor Day (company-confirmed) — sell-the-news setup for the short.
- **~Mid-Oct:** TSM Q3-26.
- **Late Oct → early Nov (the cluster):** VRT Q3, SMCI Q1-FY27, ARM Q2-FY27, ALAB Q3, ANET Q3, NVDA Q3-FY27.
- **~Dec:** AVGO Q4-FY26, MRVL Q3-FY27, CRDO Q2-FY27.

**~9 of 11 names have a binary event inside ~3 weeks (late-Oct→early-Nov).** A single macro headline in that window (a hyperscaler capex trim, a credit-spread gap, an AI-bubble narrative shock) marks the entire book simultaneously — on *both* sides, in correlated fashion. **Do not carry full gross through the cluster; stagger sizing into individual catalysts.**

### 4.5 Borrow / squeeze
- **SMCI:** ~91.2M sh short, ~14–15% of float, DTC ~1.4, borrow ~0.3% → **sentiment squeeze risk is high even if mechanical squeeze is low.** The 30% weight is the single largest deviation I'd force. Hard stop mandatory.
- **ARM/ALAB/CRDO/MRVL:** cheap, available borrow; low mechanical squeeze; risk is price/momentum in a strong tape.
- **MU (long):** squeeze-prone — but that's *favorable* to a long. Fine.
- **Carry:** low across the short book (no hard-to-borrow names), so cost-of-carry is not a constraint; **crowding and beta are.**

---

## 5. Final reconciled book, weights, and risk limits

**Construction principle:** keep the analysts' security selection (it's sound and well-sourced); fix the *sizing* so the book expresses **dispersion / quality-vs-expensive-derivatives**, held **factor-beta-neutral**, with the macro tail as the intended (hedged) exposure rather than an accidental net-short-β bet.

### 5.1 Long side (100% of long notional; anchor sizing)

| Name | Old | **New** | Change |
|---|---:|---:|---|
| NVDA | 24% | **24%** | keep (≤25% cap) |
| TSM | 18% | **18%** | keep |
| AVGO | 16% | **17%** | +1 |
| MU | 17% | **12%** | **trim** (variance + circular-financing + no offset) |
| ANET | 12% | **13%** | +1 (internal memory-cost hedge) |
| VRT | 13% | **10%** | **trim** + hard stop (execution/backlog opacity) |
| Cash/hedge reserve | 0% | **6%** | dry powder for the catalyst cluster |
| **Total** | 100% | **100%** | |

### 5.2 Short side (rebalanced AND downsized to ~72% of long notional for beta-neutrality)

Weights below are *within the short sleeve*; the **sleeve is run at ~0.72× long notional.**

| Name | Old | **New (of short sleeve)** | Change |
|---|---:|---:|---|
| SMCI | 30% | **22%** | **trim** (squeeze/crowding), hard stop |
| ARM | 25% | **20%** | **trim** (DC-CPU inflection risk), size into print |
| ALAB | 20% | **20%** | keep — but inside cluster cap |
| MRVL | 15% | **20%** | +5, size into Oct-6 Investor Day |
| CRDO | 10% | **12%** | satellite; inside cluster cap |
| Hedge overlay (long semis/AI-capex basket) | — | **6%** | partial factor hedge |
| **Total** | 100% | **100%** | |
| *Memo: ALAB+MRVL+CRDO cluster* | *45%* | *≤52% but risk-limited as ONE position* | treat as single bet |

### 5.3 Risk limits (hard)

- **Net factor β:** target **0.0, band ±0.2** to the AI-semis/SOX factor. Re-check monthly and after any name moves >20%.
- **Gross exposure cap:** ≤ **175%** (vs the naive ~200%); de-gross to ≤125% if the macro kill-switch amber-flags.
- **Single-name max:** long **≤ 24%** (NVDA capped), short **≤ 22%** (SMCI capped).
- **Cluster cap:** ALAB+MRVL+CRDO risk-sized as **one** position; combined contribution to book VaR ≤ the largest single long.
- **Un-hedgeable-tail cap (Taiwan/CoWoS):** aggregate TSMC-dependent *long* exposure (NVDA+TSM+AVGO) monitored as a bloc; do not add.
- **Memory-net cap:** net-long memory (MU, less any memory short) **≤ 12%** — the reason for the MU trim.
- **Borrow/squeeze:** any short with >10% short interest capped at ≤22% of the short sleeve and **mandatory hard stop**.
- **Stops:** SMCI hard stop at a defined level above the crowded-short pain point (e.g., ≥25–30% adverse from entry or a decisive break above the post-print high); VRT long stop below the Q2-selloff low.
- **Catalyst discipline:** carry **≤ 60% of target gross** into the late-Oct→early-Nov cluster; add on confirmation, not anticipation.
- **Portfolio kill-switch (de-risk the whole theme, both sides netted toward the short/hedge):** trigger if **≥2** of — (a) any top-4 hyperscaler *cuts* 2026/27 capex guidance, (b) a major model lab/neocloud reports a financing shortfall, (c) IG/HY spreads on hyperscaler/neocloud debt gap materially wider. This is the shared systemic risk neither single book can diversify.

**Sign-off statement:** With the resizing (MU/VRT/SMCI/ARM trims), beta-neutralization (short sleeve ~0.72× long), cluster consolidation, catalyst staggering, and the kill-switch above, **I sign off on deploying a modified version of this long/short book.** I do **not** sign off on the as-delivered 1:1 sizing, which is an unintended net-short-β macro bet with an unhedged memory long.

---

## 6. Disclaimer (full)

**This document is research and educational analysis only. It is NOT investment advice, a recommendation, or a solicitation to buy, sell, or short any security, and not an offer of any advisory service.** It was produced by an AI agent as a point-in-time exercise on **2026-09-10** from **public web information that may be incomplete, stale, out of context, mis-transcribed, or simply wrong.** Nothing here was verified against a live market-data terminal, brokerage system, or audited internal risk model; betas, exposures, and "kill-switch" levels are illustrative heuristics, not measured risk figures.

**Long/short equity, and short selling in particular, carry severe risk, including unlimited loss on the short side.** Borrow can be recalled; squeezes and forced buy-ins can crystallize losses at the worst time; a correct thesis can be wrong for long enough to be ruinous. The names reviewed here are high-beta, crowded, positively correlated, and concentrated in a single macro theme (AI capex) — they can and likely will move together, producing large, rapid, and potentially permanent losses. Forward-looking figures (company guidance, analyst targets, capex forecasts, catalyst dates) are inherently uncertain and are **not** guarantees; **past performance and projections are not indicative of future results.** Position weights and risk limits are hypothetical and for illustration only.

The reviewer holds no position in any security named, has no ability to guarantee the accuracy of third-party data used, and accepts no liability for decisions made in reliance on this document. **Do your own due diligence and consult a licensed financial professional before making any investment decision.**
