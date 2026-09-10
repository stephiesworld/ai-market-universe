# Short Book: AI Hardware & Adjacent Names — ~6-Month Horizon (Sep 2026 → ~Mar 2027)

**Analyst:** Equity research (point-in-time exercise)
**As-of date:** 2026-09-10
**Horizon:** ~6 months (now through approximately end of Q1 2027)
**Status:** Research / educational analysis only. See the DISCLAIMER at the end.

---

## 0. How to read this memo (honesty & uncertainty notes)

- This is a **point-in-time** research exercise built almost entirely from **public web sources gathered on 2026-09-10**. Figures are cited inline with a source name and date.
- I did **not** have a live market-data terminal. Prices, market caps, and forward multiples are taken from the cited secondary/aggregator sources on or near their publication dates and **will have moved**. Treat every price and multiple as approximate and **as-of the cited date**, not as of this moment.
- Third-party valuation multiples (e.g., MarketScreener forward P/E, 24/7 Wall St. commentary) are **aggregator estimates**, not primary filings. Where a number is an estimate, a projection, or something I could not corroborate against a primary filing, I flag it.
- Shorting is **asymmetric and dangerous**: losses are theoretically unlimited, and in a strong AI tape a crowded short can squeeze violently. Every name below carries a real "this is why I could be wrong" section, and Section 3 treats squeeze/crowding as a first-order risk, not an afterthought.
- This memo does **not** short NVIDIA. The bear catalysts (custom-silicon substitution, capex digestion, credit stress) mostly point *through* NVDA to smaller, higher-multiple, more concentrated derivatives of the same demand. NVDA's own numbers were still accelerating at the last print (see below), which makes it a poor risk/reward short over this window.

---

## 1. Executive summary & the bear backdrop

**The setup.** AI-hardware equities enter autumn 2026 priced for continued hyper-growth, while the *rate of change* of the demand that funds them is, for the first time this cycle, credibly at risk of decelerating. The short thesis in this memo is **not** "AI demand collapses now." It is narrower and more tradable: **a subset of expensive, concentrated, single-cycle or over-earning AI-hardware derivatives are priced for perfection into a window where (a) year-over-year capex growth mathematically decelerates, (b) the semis trade is historically crowded, (c) credit markets are beginning to question the financing of the buildout, and (d) several of these names have self-identified, near-term catalysts (margin resets, guidance "already in the number," lock-up-free insider selling) that can trigger multiple compression without any change in the secular story.**

**What is genuinely still strong (and argues for caution on the short side):**
- **NVIDIA Q2 FY27 (reported 2026-08-26):** revenue $96.2B (+106% y/y), Data Center $89.0B (+117% y/y); Q3 FY27 guide $108.0B ±2% (above the ~$105.15B consensus), with management guiding ~70% revenue growth for FY28 (*NVIDIA press release, 2026-08-26; Futurum Group, 2026-08-26*). This is not a company rolling over.
- **Hyperscaler capex is still being *raised*, not cut.** Combined 2026 capex guidance across Microsoft/Alphabet/Amazon/Meta sits near **$720–745B** (~$835B including Oracle), with Alphabet, Amazon and Meta all raising mid-year (*TIKR / TMT Finance, Jul 2026*). Amazon said capacity constraints likely persist through 2027 (*TMT Finance, Jul 2026*).
- **Memory is in genuine shortage.** Micron's FQ3-26 (reported 2026-06-24) printed $41.46B revenue with DRAM ASPs up in the low-60s% q/q, data-center revenue >$25B, and management guiding FQ4 to ~$50B at ~86% gross margin, with DRAM/NAND tight "beyond calendar 2027" (*Micron press release & call, 2026-06-24*). **Memory is a squeeze risk, not a short — see §2.6.**

**What is cracking (the bear catalysts for the window):**
1. **Decelerating growth *rate*.** UBS estimates hyperscaler capex growth falling from ~76% in 2026 to ~25% in 2027 and ~6% in 2028 (*UBS via Reuters/Resultsense, 2026-07-17*). Suppliers are priced off the *level* of spend continuing to compound; a second-derivative roll-over is enough to compress multiples on the most expensive derivatives.
2. **Crowding.** BofA's July 2026 survey found **82% of fund managers call semiconductors the most crowded trade** (*BofA via Reuters/Resultsense, 2026-07-17*). Crowded longs unwind faster than they build.
3. **Financing stress.** Cover ratios on Big Tech bond issuance fell from ~5x in February to <2x by July; Apollo's Torsten Slok flagged the deterioration; the BIS warned in June that disappointing returns could turn the boom into a "protracted bust" (*Reuters/Resultsense, 2026-07-17*).
4. **Circular-financing & depreciation scrutiny.** Michael Burry and others have publicly argued a growing share of AI revenue is "circularly financed" (Nvidia equity stakes + multi-year purchase commitments across OpenAI/Oracle/CoreWeave/AMD), and that under-depreciation of AI hardware is inflating hyperscaler earnings; Nvidia's 5-year CDS has reportedly roughly doubled over two months (*Business Insider, Jul 2026; 24/7 Wall St., 2026-08-13 & 2026-08-21*). Whether or not one buys the full thesis, it is now a **narrative risk** that can de-rate the whole cohort on any bad headline.
5. **Custom silicon (ASIC) substitution.** Merchant-GPU and merchant-connectivity suppliers face hyperscaler in-house programs (Trainium, TPU, Maia, etc.). This is a slow structural risk but a fast *sentiment* risk for the connectivity/ASIC-attach cohort.

**Bottom line.** Over ~6 months the highest-expected-value shorts are the **priced-for-perfection derivatives** with idiosyncratic, near-dated catalysts — not the mega-cap compounders. The book below is deliberately split between **idiosyncratic** shorts (SMCI margin reset & governance; ARM valuation + litigation + royalty deceleration) and **cohort/valuation** shorts (ALAB, MRVL, CRDO) whose fates are correlated (a real risk flagged in §3).

---

## 2. The short book (ranked)

| Rank | Ticker | Thesis type | Conviction | Weight |
|-----:|:-------|:------------|:-----------|------:|
| 1 | SMCI | Margin normalization + governance/accounting overhang | High | 30% |
| 2 | ARM | Valuation + royalty deceleration + Qualcomm litigation | Medium-High | 25% |
| 3 | ALAB | Valuation + customer concentration + insider selling | Medium | 20% |
| 4 | MRVL | "Upside already in the number" + cohort de-rate | Medium | 15% |
| 5 | CRDO | Extreme customer concentration + priced growth | Low-Medium | 10% |
| | | **Total** | | **100%** |

Weights are a share of a notional **short book** (i.e., 100% = the total short exposure), not of a long/short fund's gross. Sizing logic and portfolio construction are in §3.

---

### 2.1 SMCI — Super Micro Computer — **Rank 1, High conviction, 30%**

**(a) Bear thesis.** Super Micro is a low-moat, low-margin AI-server integrator whose Q4 FY26 earnings contained a large, **management-admitted non-recurring** margin spike that flatters the trailing picture and, on the bear view, sets up a "beat then normalize" disappointment. Q4 FY26 (reported 2026-08-18) non-GAAP gross margin was **17.6%** versus guidance of ~8.2–8.4% — but the CFO attributed **~75% of the improvement to a favorable mix driven by contracts *deferred* out of Q4 into Q1**, plus lower tariff costs and lower inventory reserves he called "non-recurring." Management then guided Q1 FY27 gross margin back down to **10.4–10.8%** (*Super Micro Q4 FY26 call / press release, 2026-08-18; 24/7 Wall St., 2026-09-08*). Structurally, Taiwanese ODMs operate at ~4–11% gross margins versus SMCI's mid-teens, capping durable pricing power (*Hindenburg Research, 2024*). Layered on top is an **unresolved governance/accounting overhang**: related-party suppliers Ablecom and Compuware (controlled by the CEO's brothers) were paid ~$983M over three years, and material weaknesses in internal control over financial reporting have been a recurring concern (*Hindenburg Research, 2024; Forbes, 2024-08-30*). *Uncertainty flag: the Hindenburg-era allegations are from 2024; I did not find a 2026 primary filing confirming current remediation status, so treat the governance point as a standing overhang/narrative risk rather than a fresh 2026 disclosure.*

**(b) Catalyst(s) in the window.** The single cleanest catalyst is **Q1 FY27 earnings (quarter ends 2026-09-30, typically reported late Oct / early Nov 2026)**. The bear outcome: revenue grows but gross margin lands at ~10.5% as guided, confirming the Q4 spike was a head-fake, and/or the $65–72B FY27 revenue range (*Super Micro press release, 2026-08-18*) is not reaffirmed. A quiet period began 2026-09-11, so the 10.4–10.8% guide "stands" into the print (*24/7 Wall St., 2026-09-08*).

**(c) Valuation snapshot (as-of).** Shares closed ~**$39.59** (up ~26–28% over the prior month) as of *24/7 Wall St., 2026-09-08*. FY26 net sales $39.1B, FY26 GAAP net income $2.2B ($3.26 dil. EPS); FY27 revenue guided $65–72B (*Super Micro press release, 2026-08-18*). The stock is **not** expensive on headline P/E — this is **not** a valuation short; it is a **margin-quality + governance** short. *I did not independently verify a current P/E multiple.*

**(d) Key risk to the short (squeeze/upside).** If the deferred contracts land at *better* margins than guided, or FY27's $65–72B range proves conservative, the "margin magic is temporary" thesis breaks and the stock re-rates up hard. SMCI carries **elevated short interest (~91.2M shares, ~13.9–15.3% of float, as-of the 2026-08-14 FINRA settlement)** (*CurvedTrading / Market Monitors, Aug 2026*) — that is real squeeze fuel, though **days-to-cover is only ~1.4 and borrow is cheap (~0.3%)**, so a *forced* squeeze is less likely than a sentiment-driven one. This is the crowding risk that keeps a single-name cap on the weight.

**(e) Conviction:** High — because the disappointing outcome is *management's own guidance*, not my forecast.

**(f) Weight:** 30% (largest, but capped by the crowded short interest).

---

### 2.2 ARM — Arm Holdings — **Rank 2, Medium-High conviction, 25%**

**(a) Bear thesis.** ARM is a genuinely great franchise trading at a **near-indefensible multiple** while its highest-margin engine (royalties) decelerates and a binary legal risk approaches. Q1 FY27 (reported 2026-07-29) revenue was $1.289B (+22% y/y), royalties +22% to $715M, licensing +23% to $574M, non-GAAP EPS $0.45 (*Arm shareholder letter / SEC 6-K, 2026-07-29*). But Q2 guidance calls for royalties **up only "low-teens" y/y** — a deceleration from +22% — while licensing (lumpier, lower quality) carries the growth (*Arm Q1 FY27 call, 2026-08-07*). On valuation, MarketScreener shows **~223x FY27 P/E and ~154x FY28 P/E** (EV/Sales ~49x / ~36x) (*MarketScreener, accessed 2026-09*); 24/7 Wall St. cites a **trailing P/E of ~298** and notes Q1 **GAAP EPS of $0.25 missed** the ~$0.40 estimate with operating margin compressing to ~7% from ~11% on heavy AGI-CPU R&D and SBC (*24/7 Wall St., 2026-09-08*). *Uncertainty flag: 223x/298x are aggregator/estimate figures, not a primary filing; the point is directional — the multiple leaves no room for a royalty miss.*

**(b) Catalyst(s) in the window.** (i) **Q2 FY27 earnings (~early Nov 2026)** — the "royalties only low-teens" guide is the first test; any confirmation of decelerating royalty growth against a ~200x multiple is a de-rate catalyst. (ii) **Qualcomm litigation trial expected Q4 2026** — a binary legal event within the window (*24/7 Wall St., 2026-09-08*). (iii) China exposure / export-control headlines.

**(c) Valuation snapshot (as-of).** ~**$264** with a "hold," 24/7's bear case ~$212 (*24/7 Wall St., 2026-09-08*); ARM +135% YTD / +90% 1y but −6% over the prior month (*same source*). MarketScreener FY27 estimates ~$6.05B revenue (+23%), ~$1.34B net income (*MarketScreener, accessed 2026-09*).

**(d) Key risk to the short (squeeze/upside).** ARM's AGI-CPU / data-center CPU story is real and accelerating: management said AGI-CPU customer demand has grown past **$2B across FYE27–28** (from an initial ~$1B), Neoverse shipments surpassed 1.5B cores, and data-center royalties **more than doubled y/y** (*Arm shareholder letter, 2026-07-29*). A strong licensing quarter or a data-center royalty inflection can sustain the multiple far longer than a bear expects — expensive stocks with a credible AI narrative are the most dangerous shorts. Short interest ~16.9M shares, ~2.6 days-to-cover (as-of 2026-07-31), borrow low (~0.3–0.4%) (*short-interest trackers, Aug 2026*).

**(e) Conviction:** Medium-High — the valuation and royalty-deceleration are well-supported; the risk is timing (multiples can stay stretched).

**(f) Weight:** 25%.

---

### 2.3 ALAB — Astera Labs — **Rank 3, Medium conviction, 20%**

**(a) Bear thesis.** ALAB is a high-quality connectivity story priced at an extreme multiple with **severe customer concentration** and **persistent, sizable insider selling** — a combination that historically compresses multiples when growth merely *decelerates to still-great*. Q2 2026 (reported 2026-08-04) was excellent: record revenue $392.4M (+104% y/y, +27% q/q), GAAP gross margin 73.3%, GAAP net income $153.1M (*Astera Labs press release / 10-Q, 2026-08-04*). But the 10-Q shows **one customer at 29% of revenue and four customers each ≥13%**, with China/Singapore/Taiwan generating most revenue (*ALAB 10-Q via StockTitan, Aug 2026*); an earlier filing had five customers at ~90% of revenue (*EBC Financial, 2026*). The multiple is the issue: commentary pegs ALAB around a **~165x** valuation test with a market cap ~**$53.85B** (*MarketBeat, 2026-09-04; EBC Financial, 2026*). Meanwhile **insiders sold ~$209.7M of stock over the trailing 90 days** (e.g., COO Sanjay Gajendra sold 90,630 shares at ~$340.35 on 2026-08-17), disclosed as 10b5-1 / tax-withholding sales but a steady supply overhang nonetheless (*MarketBeat, 2026-09-04*).

**(b) Catalyst(s) in the window.** (i) **Q3 2026 earnings (~early Nov 2026)** — the Scorpio X-Series fabric-switch ramp is the guided growth driver; any ramp slip, or a "great but in-line" print, is a de-rate catalyst at 165x. (ii) **Interconnect-standard risk headlines** — if a large customer signals a shift toward NVLink Fusion / UALink / CXL alternatives, ALAB could face qualification-cycle revenue risk (*EBC Financial, 2026*). (iii) Continued insider-sale disclosures.

**(c) Valuation snapshot (as-of).** Market cap ~$53.85B; Q2 non-GAAP EPS $0.80 vs $0.69 est.; Q3 EPS guide ~$1.16–1.21; consensus ~"Moderate Buy," avg target ~$348 (*MarketBeat, 2026-09-04*). ~165x earnings framing per *EBC Financial, 2026*. *Aggregator multiples; not a primary filing.*

**(d) Key risk to the short (squeeze/upside).** ALAB is executing and *broadening* (Aries + Scorpio + optical + custom), which is exactly the "multi-point of the connectivity layer" story bulls pay up for; a Scorpio beat pushes it higher. Short interest is modest (~8.8M shares, ~5.0% of float, ~1.9 days-to-cover, as-of 2026-08-14; borrow ~0.4%) (*CurvedTrading, Aug 2026*) — squeeze risk is moderate, but the stock's beta and momentum make it whippy.

**(e) Conviction:** Medium.

**(f) Weight:** 20%.

---

### 2.4 MRVL — Marvell Technology — **Rank 4, Medium conviction, 15%**

**(a) Bear thesis.** Marvell's fundamentals are strong, but the stock's problem is that **the good news is already in the number** and the *material* custom-silicon payoff has been **explicitly deferred to FY29+**. Q2 FY27 (reported ~2026-08-27) revenue was a record $2.739B (+37% y/y), data-center +46% y/y, and management *raised* FY27/FY28 revenue outlook to ~$12B/$18B (*Marvell press release & call, Aug 2026*). Yet the stock sold off because CEO Matt Murphy confirmed the July Google warrant/agreement revenue is **already reflected in FY28 guidance**, with the big impact "in fiscal 2029 and beyond" — converting a potential upward revision into an input **already spent** (*S3H.com, Aug 2026; Motley Fool transcript, 2026-08-31*). At ~$224 the company was ~$189B, ~10.5x FY28 sales / ~31x an FY28-two-years-out earnings number that requires the custom ramp on schedule; a cohort de-rate to ~20x the same FY28 earnings implies ~$140–150 **without a single guidance cut** (*S3H.com, Aug 2026*).

**(b) Catalyst(s) in the window.** (i) **Investor Day, 2026-10-06** — a classic "sell-the-news" setup: management *deferred* the FY29 custom framework to this event, so it now carries outsized expectations; anything short of a raised, clearly-attributable FY29 custom target risks a de-rate (*S3H.com, Aug 2026*). (ii) **Q3 FY27 earnings (~early Dec 2026)** — Q3 non-GAAP gross margin was *guided down* to 57.5–58.5% on custom mix, and Communications is expected to decline low-to-mid-teens sequentially (*Marvell press release, Aug 2026*). (iii) Cohort-wide multiple compression (see §3).

**(c) Valuation snapshot (as-of).** ~**$224.34** post-Q2 (~$189B cap), ~10.5x FY28 sales; +184% YTD / +222% 1y; joined the S&P 500 in June; street avg ~$295 with no sell ratings (*S3H.com, Aug 2026*). *Third-party arithmetic, not a filing.*

**(d) Key risk to the short (squeeze/upside).** Custom bookings are "exceptionally robust," data center is guided to >60% growth in FY28, and a strong Oct-6 Investor Day with a broken-out, accelerating attach line could retest the ~$330 high (*S3H.com; Motley Fool, 2026-08-31*). "No sell ratings" means positioning is one-sided long — good for a contrarian short thesis but painful if the tape stays strong. Borrow is liquid/cheap (mega-cap, S&P 500 member).

**(e) Conviction:** Medium (the de-rate is a valuation/positioning call, not a fundamental-deterioration call).

**(f) Weight:** 15%.

---

### 2.5 CRDO — Credo Technology — **Rank 5, Low-Medium conviction, 10%**

**(a) Bear thesis.** Credo is the **most customer-concentrated** name in the book: Q1 FY27 (reported 2026-09-01) disclosed the top four customers at **~33%, ~28%, ~13%, ~10%** of revenue — i.e., the **top two are ~61%** (*Credo Q1 FY27 press release, 2026-09-01; Credo call, 2026-09-08*). Any single hyperscaler order push-out lands directly on the P&L. Despite an eighth consecutive beat (Q1 FY27 revenue $479M, +114.7% y/y; non-GAAP net margin ~49%), **the stock gapped down hard** on the print — a tell that the growth is priced (*24/7 Wall St., 2026-09-03*). Inventory climbed ~$62.2M q/q to ~$313.1M, worth watching for a demand/inventory mismatch (*24/7 Wall St., 2026-09-03*).

**(b) Catalyst(s) in the window.** (i) **Q2 FY27 earnings (~early Dec 2026)** — the guide is $525–535M; the risk is a customer-concentration disclosure showing a top-2 customer stepping down, or optical revenue (guided >$600M for FY27) tracking behind. (ii) Cohort de-rate alongside ALAB/MRVL.

**(c) Valuation snapshot (as-of).** ~**$165** with a **forward P/E ~41** (down from a trailing ~90), non-GAAP gross margin ~68%; 18 of 19 analysts Buy/Strong Buy, avg target ~$283 (*24/7 Wall St., 2026-09-03*). CRDO is the **cheapest** name here on forward earnings, which is precisely why it gets the **smallest weight** — the valuation cushion makes it a lower-conviction short.

**(d) Key risk to the short (squeeze/upside).** Forward P/E ~41 against 85%+ revenue growth and ~50% net margins is **not obviously expensive**; if the top-two customers hold and optical scales to $600M, CRDO re-rates up. Short interest is small (~6.1M shares, ~3.3% of shares out, ~1.4 days-to-cover; *AltIndex / ShortInterestHistory, Aug 2026*) so squeeze risk is muted, but the cheap multiple caps the downside — this is a **satellite** short, not a core one.

**(e) Conviction:** Low-Medium.

**(f) Weight:** 10%.

---

### 2.6 Names deliberately NOT shorted (and why)

- **NVDA** — still accelerating (Q3 FY27 guide $108B, ~70% FY28 growth guide); shorting the cycle leader into an up-guide is poor risk/reward (*NVIDIA, 2026-08-26*).
- **MU (Micron)** — **a squeeze risk, not a short.** DRAM/NAND in genuine shortage, ASPs +low-60s% q/q, FQ4 guide ~$50B at ~86% gross margin, tightness "beyond 2027," HBM4 ramping 2x faster than HBM3E (*Micron, 2026-06-24*). Shorting a company in the fat part of an up-cycle is a classic way to get run over.
- **VRT (Vertiv)** — rich but backed by a raised FY26 guide ($14B sales, ~$6.70 adj. EPS), a **$15B backlog**, and broad bullish targets ($338–381); despite a ~3-month pullback to ~$262.83 (as-of 2026-09-10), the order/backlog momentum makes it a low-quality short right now (*Vertiv Q2 2026 release; 24/7 Wall St., 2026-09-10; TIKR, 2026*). Candidate for a watchlist if orders decelerate.
- **AVGO (Broadcom)** — AI/custom-silicon backlog too strong to fight here (AI chip sales projected to ~double to ~$16B in the Sept-2026 quarter per *TIKR, Jul 2026*); it is a *cause* of the cohort's de-rate risk, not the cleanest expression of it.
- **Semicap (ASML/AMAT/LRCX/KLAC), TSM, AMD, ANET, COHR, DELL** — not enough fresh, corroborated 2026 bear evidence gathered in this pass to justify a sized short; noted for future work in §4.

---

## 3. Portfolio-level view

**Book construction.** Five names, long-nothing (pure short book for this exercise). Weights: SMCI 30 / ARM 25 / ALAB 20 / MRVL 15 / CRDO 10.

**Net factor exposure.** This book is, in factor terms, **short high-momentum, short high-beta, short expensive-growth, and implicitly long quality/value**. Every name is a high-beta AI-semis/hardware derivative, so the book has a large **negative loading on the same latent "AI-capex / SOX momentum" factor**. In a continued melt-up led by NVDA/AVGO/Micron, this book loses on beta *before* any single-name thesis plays out. A disciplined implementation would **beta-/factor-hedge** (e.g., a partial long in a broad semis or AI-capex basket, or long the cheapest, highest-quality names like a Micron/Broadcom) so that the P&L is driven by **dispersion** (the expensive derivatives de-rating relative to the leaders) rather than by an outright market-direction bet. As a naked short book it is effectively a **short-the-AI-trade macro bet**, which is higher-variance than the single-name theses warrant.

**Crowding.** Semis are the single most crowded trade on the street — **82% of managers** in BofA's July 2026 survey (*Reuters/Resultsense, 2026-07-17*). Crowded *longs* can unwind sharply (good for shorts), but crowded *shorts* squeeze (bad). SMCI stands out with **~14–15% short interest** — the most crowded *short* in the book and the reason its weight is capped at 30% despite being the highest-conviction idea.

**Correlation among the shorts.** High, and asymmetrically so on the downside-for-the-short (i.e., they rally together). **ALAB, MRVL and CRDO are a single connectivity/custom-silicon cohort** that "reprices together on the same forward multiple compression" (*S3H.com, Aug 2026*) — combined they are 45% of the book, so effective diversification is lower than the five-name count implies. SMCI (server integration / governance) and ARM (IP licensing / litigation) are the genuine **idiosyncratic diversifiers**; their catalysts (SMCI margin print; ARM royalty guide + Qualcomm trial) are largely independent of the connectivity cohort. Net: the book has roughly **two-and-a-half independent bets**, not five.

**Borrow & short-squeeze considerations (as-of the 2026-08-14 FINRA settlement unless noted; *CurvedTrading / Market Monitors / AltIndex, Aug 2026*):**

| Ticker | Short interest | % of float/shares | Days to cover | Borrow fee | Squeeze read |
|:-------|:---------------|:------------------|:--------------|:-----------|:-------------|
| SMCI | ~91.2M sh | ~13.9–15.3% | ~1.4 | ~0.3% | **Highest squeeze risk** (crowded short), but low DTC/borrow means sentiment-, not mechanics-, driven |
| ARM | ~16.9M sh (7/31) | — | ~2.6 | ~0.3–0.4% | Moderate; expensive-but-loved names squeeze on any AI-CPU beat |
| ALAB | ~8.8M sh | ~5.0% | ~1.9 | ~0.4% | Moderate |
| MRVL | mega-cap, liquid | low | low | low (GC) | Low mechanical squeeze; high beta/momentum whip |
| CRDO | ~6.1M sh | ~3.3% | ~1.4 | low | Muted (low DTC) |

Borrow is **cheap and available** across the book (no hard-to-borrow names), so **carry cost is low** and the main squeeze risk is **price/sentiment (a strong AI tape), not a mechanical borrow squeeze** — except SMCI, where the sheer size of the short base is itself a risk.

**Overall book risk statement.** This is a **crowded, high-beta, positively-correlated short book expressed against a still-rising capex backdrop.** Its edge is *dispersion and de-rating*, not market timing. Sized naked and unhedged it can lose 20–40% in a squeeze quarter even if every thesis is eventually right. Recommended risk controls: (i) beta/factor hedge as above; (ii) hard single-name stops on SMCI given short crowding; (iii) size *into* catalysts (earnings, Oct-6 Investor Day) rather than carrying full size through a strong tape; (iv) treat the connectivity trio as one position for risk-limit purposes.

---

## 4. Methodology & data provenance

**Method.** Candidate universe taken from the mandate; final book selected by favoring names with (a) demanding valuations, (b) a *near-dated, falsifiable* catalyst inside the ~6-month window, (c) idiosyncratic risk (governance, concentration, litigation, self-guided margin resets), and (d) manageable borrow. Macro backdrop assembled from capex trackers, sell-side survey data, and credit commentary. Every material figure is cited inline with source + date. Where a figure is an aggregator estimate or could not be corroborated against a primary filing, it is flagged in-line and in §0.

**Primary sources (filings / company releases):**
- NVIDIA — Q2 FY27 results, 2026-08-26 (investor.nvidia.com; SEC 8-K exhibit).
- Super Micro (SMCI) — Q4/FY26 results & Q1 FY27 guidance, 2026-08-18 (ir.supermicro.com; Motley Fool call transcript).
- Arm (ARM) — Q1 FY27 shareholder letter & SEC 6-K exhibit, 2026-07-29; earnings call, 2026-08-07.
- Astera Labs (ALAB) — Q2 2026 results & 10-Q, 2026-08-04 (asteralabs.com; StockTitan).
- Marvell (MRVL) — Q2 FY27 results, ~2026-08-27 (investor.marvell.com); earnings call, 2026-08-31 (Motley Fool).
- Credo (CRDO) — Q1 FY27 results, 2026-09-01 (investors.credosemi.com; EDGAR); earnings call, 2026-09-08.
- Micron (MU) — FQ3 2026 results & call, 2026-06-24 (SEC press release; company presentation).

**Secondary / analytical sources:**
- Hyperscaler capex: Platformonomics Q2 2026 Scoreboard (Jul 2026); TIKR (2026); TMT Finance (Jul 2026).
- Capex-growth deceleration, crowding, financing stress: UBS & BofA via Reuters/Resultsense/The Star (2026-07-17).
- Circular financing & depreciation: Business Insider (Jul 2026); 24/7 Wall St. (2026-08-13, 2026-08-21); Forbes (2026-08-17); Grep News (Burry thesis breakdown).
- Valuation/commentary: MarketScreener (ARM, accessed 2026-09); 24/7 Wall St. (SMCI 2026-09-08; ARM 2026-09-08; CRDO 2026-09-03; VRT 2026-09-10); EBC Financial (ALAB); S3H.com (MRVL, Aug 2026); MarketBeat (ALAB, 2026-09-04).
- Short interest / borrow: CurvedTrading & Market Monitors (SMCI, ALAB, Aug 2026); AltIndex & ShortInterestHistory (CRDO, Aug 2026); short-interest trackers (ARM, 7/31 settlement).

**Known limitations / what I could not verify:**
- **No live market data.** All prices/market caps/multiples are as-of their cited dates and are stale relative to today; several come from secondary aggregators, not exchange feeds.
- **Forward multiples (223x/154x ARM; ~165x ALAB; ~41x CRDO; ~31x FY28 MRVL) are estimates/derived arithmetic**, sensitive to which EPS/period is used; treat as directional.
- **Governance items on SMCI** rest substantially on 2024 short-seller/press material; I did not confirm current (2026) remediation status against a primary filing.
- **Short-interest data lag** ~2 weeks (FINRA settlement convention); positioning may have shifted.
- **Some secondary sources are opinion/commentary** (e.g., 24/7 Wall St., S3H.com) and may embed their own biases; I used them for framing and cross-checked figures against primary releases where possible.
- Catalyst *dates* (earnings reporting dates) are **estimated** from historical cadence unless a company confirmed them; the Marvell Investor Day (2026-10-06) is company-confirmed.

---

## 5. DISCLAIMER

**This document is research and educational analysis only. It is NOT investment advice, a recommendation, or a solicitation to buy, sell, or short any security.** It was produced as a point-in-time analytical exercise from **public information gathered on 2026-09-10 that may be incomplete, stale, out of context, or simply wrong.** Nothing here has been verified against a live market-data or brokerage system.

**Short selling carries risk of unlimited loss.** A short position can lose far more than the capital committed; borrow can be recalled; short squeezes, forced buy-ins, and margin calls can force losses at the worst possible time; and in a strong or trending market a fundamentally sound short thesis can be badly wrong for a long time — long enough to be ruinous before it is ever "right." The names in this memo are high-beta, crowded, and positively correlated, which amplifies all of these risks.

No representation is made that any strategy described will be profitable. Figures, valuations, and catalyst dates are approximate and as-of the cited sources. Do your own diligence and consult a licensed financial professional before making any investment decision. The author holds no position and receives no compensation tied to any security named here.
