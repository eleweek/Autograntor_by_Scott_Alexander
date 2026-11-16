# Common Law topic file — policy, laws and non-US actors

Verbatim copies of Proposed rulings from Part III of `claude/common_law.md` (frozen original, version 2026-10-20.1), grouped by topic. The original remains the source of truth. Rulings in this file: CL-45, 46, 47, 48, 49, 50, 51, 52, 68, 69. Read it for advocacy and policy organisations, state or federal law rows, c3/c4 questions, electoral work, and any non-US actor.

### CL-45: Ladder rows for successive upgrades of one jurisdiction's law [Proposed 2026-10-18, by Claude]
**Rule:** When a jurisdiction's law can be strengthened in stages (e.g. audits → regulator → emergency authority), price each rung as its increment over the previous rung, give it a probability of being reached by 2030, and credit every rung reached. Fold the expected use of an authority into the rung that creates it (CL-5), not into a separate "use" row. Check the ladder's sum against the nearest federal entry as a stated fraction, and keep each rung at or below the price of a comparable whole law elsewhere (CL-6).
**Why:** Lump rows credit nothing for partial progress and hide where the value is; a separate use row double-counts the authority.

### CL-46: Attributing a multi-year outcome to one year's spending [Proposed 2026-10-18, by Claude]
**Rule:** When a grant funds one year of a multi-year campaign, attribute to that year the share f of the critical-path effort that falls in it (drafting, sponsor recruitment, session timing), stated per row, with the shares across the campaign's years summing to at most one. Do not attribute pro-rata by budget, do not credit the whole outcome to the funded year, and do not use a higher f for a longer-horizon outcome than for a nearer one.
**Why:** Without a stated share, one year of an advocacy organisation is credited with whole laws, which fails CL-9 when multiplied over the years it actually takes.

### CL-47: Grantee-organised candidate fundraising and electoral work [Proposed 2026-10-18, by Claude]
**Rule:** Credit relationship value from candidate fundraising only through the laws and executive actions it makes likelier (CL-5), never as a separate access row. Price partisan-coding risk as a signed exposure row (CL-40) on the "AI risk concern becomes bipartisan" entry, scaling it up only for the tranche that buys electoral or independent-expenditure capacity. Put integrity and trust-norm harm in a CL-11 branch. Where the applicant offers a restricted "no elections" account, price that option and report it to the grantmaker.
**Why:** Access double-counts with the laws; the integrity question divides evaluators and should not be silently resolved; the restricted account turns a values question into a choice.

### CL-48: c4 vs. c3 dollars [Proposed 2026-10-18, by Claude]
**Rule:** Value a restricted-type dollar (c4) by what it buys inside the grantee at that tranche's marginal factor. Do not multiply by the applicant's c3:c4 indifference ratio, and do not raise the CL-4 money price for c4 money: both measure fundraising scarcity, i.e. the replacement value of money, which the grading criterion excludes.
**Why:** Applying a 4:1 or 6:1 ratio would multiply the grant 4–6× on an argument the human user has ruled out and would fail CL-9 against the organisation's average dollar.

### CL-49: Survival of state laws against federal preemption [Proposed 2026-10-18, by Claude]
**Rule:** A state-law row's probability is for enactment; multiply by the probability the law is still substantially in force when graded in 2030. Set the loss factor by what the live federal vehicle would displace: ceiling preemption that codifies transparency-level duties costs transparency-type laws little (≈0.3) and stronger rungs (a state regulator, emergency authority) most of their value (≈0.67). Credit the grantee's anti-preemption work in its own row; do not also raise the survival factor for it.
**Why:** Pricing enactment only, or using a flat survival factor, hides that preemption bites hardest on exactly the rows that carry the most value.

### CL-50: One ledger, one budget for a paired c3/c4 organisation [Proposed 2026-10-18, by Claude]
**Rule:** When a c3 and a c4 share staff and a program, price one program ledger and divide by the joint program cost for the CL-15 average, with the budget built from a realistic hiring ramp (not the end-state run rate from day one, nor the ask). Treat the grant as buying a tranche of that joint program at the marginal factor for what the restricted dollar can fund.
**Why:** Dividing joint program value by one entity's spend inflates both the average dollar and the grant's share; using the end-state rate deflates them.

### CL-51: Leverage factors for non-US national actors [Proposed 2026-10-17, by Claude]
**Rule:** When a US-calibrated weight (a PERCYs M-row, the proposed "member of Congress champion", or a US milestone) is applied to a non-US national actor, multiply by one stated frontier-AI-governance leverage factor. The factor depends on the actor's constitutional role, not only the country:
- **National executive positions:** France or Germany ≈0.2–0.3, UK ≈0.25, EU as a bloc ≈0.4–0.5, other G7 ≈0.1–0.15.
- **Individual legislators:** in presidential or semi-presidential systems where treaty and foreign policy is reserved to the executive, ≈0.10. In parliamentary systems whose legislators shape foreign and EU policy, up to the executive factor.

Apply the factor once. Never apply it again on top of a milestone already priced as a fraction of an international entry, and strip value that flows through separately priced executive rows (CL-5).
**Why:** A single country factor either overprices individual legislators or underprices national executives.

### CL-52: Recruit-on-funding lags, dated windows and part-time roles [Proposed 2026-10-17, by Claude]
**Rule:**
- **Lag.** If funded activity starts only after recruitment, shift it by the stated lag (default 2–3 months from disbursement).
- **Dated windows.** Price rows tied to a dated window (an election, a summit) on the post-lag share of the critical-path work in that window, not the calendar share (CL-46). Don't give extra window credit to money above the ask that arrives after the window.
- **Part-time roles.** Value a 0.5-FTE relationship role at ≈0.5 of the full-time increment if it spans a dated window, ≈0.4 otherwise.

**Why:** Without a rule, estimators invent their own treatment, and rows tied to dated windows can differ by a large factor.

### CL-68: Proposed "actor newly becomes X" milestones that may already have happened [Proposed 2026-10-20, by Claude]
**Rule:** Before crediting a "newly becomes" milestone (a legislator becomes a champion, an organisation takes a position) for a class of actors, check whether some member of that class already meets it. If so, re-scope the row as "an additional actor becomes X", price it at roughly 0.4–0.6 of the original weight (the first instance carried most of the signal), and raise the base rate accordingly.
**Why:** A milestone written for the first instance overstates the headroom once the first instance has happened, and estimators otherwise credit the grant with a signal the world already sent.

### CL-69: External base rates that resolve on a looser event than the row [Proposed 2026-10-20, by Claude]
**Rule:** When an outside forecast's resolution criteria are looser than the event a row prices (e.g. "any mention in a co-signed letter" vs "an explicit organisational position"), do not transplant or discard it. Build a two-rung ladder (CL-45): the loose event at the forecast base rate with a small weight, and the strict event as an increment on top, with its own lower base rate.
**Why:** Transplanting a loose-event base rate inflates the no-grant world for the strict event; discarding it throws away the only external calibration available.
