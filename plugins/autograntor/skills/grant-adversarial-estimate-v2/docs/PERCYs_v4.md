# PERCYs v4 — pricing persuasion and communication grants

**Status: adopted by the human user on 2026-11-12. Replaces `claude/PERCYs_v3.7_compact.md`.** Every weight is the v3.7 value; v4 changes structure, not weights. §8 lists the changes and how to read older rulings.

**Unit.** 1 PERCY = one average US adult who is one full unit more concerned about AI risk (on a −1 to +1 scale) than they would otherwise be, for one year.
**Conversion.** 1,000,000 PERCYs = 1,200 utility points.

## 1. One formula

Every row is one class of person:

`PERCYs = people × weight × Δ × years × share`

| Term | Meaning |
|---|---|
| people | Unique people of this class reached in the period. Never views, downloads or impressions. |
| weight | From the ladder (§2). Set by who the person is, never by whether the application named or counted them. |
| Δ | The gap: how much less concerned these people would be without this output, given everything else they see. Averaged over everyone in the row, including those who don't move. May be negative. |
| years | How many years of that gap this period's money buys (§3). |
| share | The fraction of the row that exists only because of the grant. One number, always in that direction. It includes any gate probability. |

In a ledger, every PERCYs row gives these five numbers in its note, in this order, and its `ev` is their product × 1,200 ÷ 1,000,000. Never write the basis in any other form.

## 2. The ladder

| Weight | Who |
|---|---|
| 1 | General public: met it in a feed, wouldn't seek it out |
| 3 | Chooses AI content; tech-literate |
| 10 | Works in or near tech, policy or media |
| 30 | AI researchers outside frontier labs, grad students, safety community, policy-adjacent |
| 100 | Think-tank principals and similar senior people near decision-makers |
| 3,000 | Frontier-lab employees; government AI staff; committee staffers |
| 10,000 | AI-beat journalists and editors |
| 30,000 | House member; senior frontier-lab researcher |
| 100,000 | Chinese senior AI academic or State Council advisor |
| 300,000 | Median Senator |
| 1,000,000 | Leadership Senator; frontier-lab CEO; Cabinet or NSC principal |
| 10,000,000 | President |
| 20,000,000 | Xi |

**Counting people at 3,000 and above.** Give a basis for the count: an attendee list, a survey, analytics, or the default shares below. A weak basis widens the range; it does not lower the weight. Rungs from 30,000 up are individuals: list them or give a number with a source.

**Default shares of a returning audience** (use only when there is no data):

| Audience's main rung | Lab and government AI staff | AI-beat journalists |
|---|---|---|
| 1 General | 0.02% | 0.001% |
| 3 Engaged | 1.5% | 0.06% |
| 10 Professional-adjacent | 4% | 0.25% |
| 30 Field-insider | no reference yet | no reference yet |

These are back-derived from v3.7's reference counts (General is the population base rate) and are placeholders until survey data replaces them. They apply to returning audiences only. A one-off audience gets rows at 3,000 and above only with evidence.

## 3. Δ, years and the split

| What the person got over the period | Δ band | years |
|---|---|---|
| **Glance:** one or two short pieces, under about 15 minutes in total | 0.01–0.03 | 0.1 |
| **Long-form:** one film, long episode, book or event, or the same time in many short pieces | 0.03–0.08 | 1 |
| **Follows, joined this period:** returns monthly or more | 0.10–0.30 | 3 |
| **Follows, already in the audience** | same gap | 1 |

- **Why 3 and 1.** A follower's gap lasts while they follow and fades over about two years afterwards. Keeping an existing follower for one more year pushes that fade-out one year later, which adds exactly one year. A new follower gets the year plus the fade-out. Over n years of following, the total is n + 2.
- **New-follower share** is a forecast input. If nothing is known, use 20%.
- **The bands assume this output is the person's main source on the topic.** Scale Δ down for people who hear the same thing from many other sources or were already convinced without it.
- **Rows at 3,000 and above** use the same definition. Reference gaps for followers: ACX 0.12 lab / 0.10 journalists; 80,000 Hours 0.12 / 0.06; Rob Miles 0.06 / 0.04; MIT Tech Review 0.03 / 0.06; a general-audience creator 0.02 / 0.02; a single guest appearance 0 to −0.01.

**State the split. It is a required input.** Divide every audience among the classes by what each person got over the period, not by the format of the pieces. Forty clips to one person is Long-form or Follows, not forty glances.

- **Channels, podcasts and newsletters:** the returning audience (Follows, divided into joined-this-period and already-there) and the drive-by audience (Glance or Long-form).
- **Short-form and feed content:** the number of unique people who saw one or two pieces (Glance), the number who saw enough to total about 15 minutes (Long-form), and the number who return monthly (Follows). Use platform analytics where they exist: unique viewers, returning viewers, views per viewer.
- **With no data,** assume 95% Glance and 5% Long-form, say so, and widen the range. The 5% comes from the one reference creator in example C and is provisional.

## 4. Kinds of claim

- **Direct or volume:** the grant reaches people itself or keeps a channel running. Same formula; the difference is only in `share`. Shares across all funders of one channel sum to ≤ 1.
- **Relay:** the grant changes what a communicator produces. Price the extra output concretely (pieces × audience) in the communicator's own rows. At most two hops.
- **Pipeline:** programs that create communicators. Forecast alumni output as unique people reached per year (views ÷ a stated number of views per person), including the chance of a breakout. Apply the split and price the rows as above, on rungs 1–30 only. Then multiply by the years of continued output and put the program's share of each alumnus's career in `share`. One person placed in a lab or policy role ≈ 1,500 PERCYs per person-year.
- **Per-view fallback.** Only when unique people cannot be estimated: short-form video ≈ 4 PERCYs per 1,000 views; long-form video ≈ 10 per 1,000 views; newsletter ≈ 21 per 1,000 reads. Each constant has one reference channel's split built in, at about 2 views per person for short-form. A row that uses one must say so.

## 5. Rules

1. State the split (§3) for every audience. Never blend classes into one row.
2. Count unique people. Borrowed reach (a guest spot) is Glance or Long-form, never Follows.
3. Uncertain future events are forecast questions. Put the probability in `share` and report any single gate carrying over half the value.
4. Overlap between grants is not adjusted here. Each grant is scored standalone. The allocation step re-prices a class's rows after a grant reaching that class has been funded.
5. State what share of the grant's theory of change the rows price. If it is mostly not opinion change, say the total is a floor.
6. If rows at 3,000 and above carry over half the total, say so and state the basis for the count.

## 6. Worked examples

**A. Rob Miles, one year (share = 1).** 650,000 unique viewers; 26% returning; 20% of followers new.

| Row | people × weight × Δ × years | PERCYs |
|---|---|---|
| Followers, weight 3 | 169,000 × 3 × 0.12 × 1.4 | 85,176 |
| Drive-by, weight 3, Long-form | 481,000 × 3 × 0.04 × 1 | 57,720 |
| Lab and government staff | 3,000 × 3,000 × 0.06 × 1.4 | 756,000 |
| Journalists | 100 × 10,000 × 0.04 × 1.4 | 56,000 |
| **Total** | | **≈955,000 (≈1,150 utility)** |

(1.4 years = 20% new at 3 + 80% existing at 1.)

**B. ACX, one year.** 300,000 unique readers; 33% returning; 20% of followers new.

| Row | people × weight × Δ × years | PERCYs |
|---|---|---|
| Followers, weight 10 | 99,000 × 10 × 0.15 × 1.4 | 207,900 |
| Drive-by, weight 10, Glance | 201,000 × 10 × 0.02 × 0.1 | 4,020 |
| Lab and government staff | 4,000 × 3,000 × 0.12 × 1.4 | 2,016,000 |
| Journalists | 250 × 10,000 × 0.10 × 1.4 | 350,000 |
| **Total** | | **≈2.58M (≈3,100 utility)** |

**C. Short-form creator grant.** Analytics give 3.66M unique viewers, of whom 160,000 watched enough to count as Long-form.

| Row | people × weight × Δ × years × share | PERCYs |
|---|---|---|
| Glance viewers | 3,500,000 × 1 × 0.01 × 0.1 × 0.8 | 2,800 |
| Long-form viewers | 160,000 × 3 × 0.05 × 1 × 0.6 | 14,400 |

**D. A convening.** 340 attendees, Long-form, Δ 0.07, share 0.75; the attendee list shows 80 lab staff and 40 journalists.

| Row | people × weight × Δ × years × share | PERCYs |
|---|---|---|
| Other attendees, weight 30 | 220 × 30 × 0.07 × 1 × 0.75 | 347 |
| Lab staff | 80 × 3,000 × 0.07 × 1 × 0.75 | 12,600 |
| Journalists | 40 × 10,000 × 0.07 × 1 × 0.75 | 21,000 |

**E. Pipeline.** A creator incubator. Forecast alumni output: 60M short-form views a year, at about 2 views per person, so 30M unique people. No analytics on depth, so the default split applies.

| Row | people × weight × Δ × years | PERCYs per output-year |
|---|---|---|
| Glance, 95% | 28,500,000 × 1 × 0.01 × 0.1 | 28,500 |
| Long-form, 5% | 1,500,000 × 3 × 0.05 × 1 | 225,000 |
| **Total** | | **253,500** |

Then × 2.5 years of continued output × share 0.2125 (0.5 program's share of alumni careers × 0.5 chance the cohorts run × 0.85) ≈ 135,000 PERCYs. Views per person is the sensitive input: at 6 views per person the same 60M views reach 10M people and are worth a third as much.

## 7. Open questions for the human user

1. **What the general-public rows measure.** Polls already show large majorities concerned and in favour of slowing development, so "neutral to concerned" has little headroom on rungs 1–3. The alternative is to define those rows on salience (AI risk becomes a top issue for the person).
2. **Shape of the ladder.** The 50,000 lab and government staff at 3,000 outweigh five frontier-lab CEOs 30 to 1 and the President 15 to 1. Options: raise the top rungs, or split the 3,000 rung into technical and policy staff versus everyone else.
3. **Glance at 0.1 years** is provisional. It rests on field experiments in which the effect of single political ads faded within weeks; a first exposure to an unfamiliar idea may last longer.
4. **Data to replace the defaults.** Creator analytics for the 95/5 split, and a reader survey of one reference channel for the lab-staff share and which sources changed those readers' views.
5. **Back-test the conversion.** Score several Canonical Milestones with a known audience and compare with their listed weights before trusting absolute values.

## 8. Changes from v3.7, and reading older rulings

What changed:
- One ladder replaces the quality bins, the counted classes and the named weights. Weight no longer depends on whether a person was named or counted.
- Existing followers get 1 year, not 3. New followers keep 3.
- Glance is 0.1 years, not 0.5.
- One `share` replaces cf, owned fraction, attributable share and retained share.
- The split is a required input, classed by person, not by piece. Per-view constants are a fallback.
- Overlap between grants moves to the allocation step.

Older rulings and forecasts use v3.7 terms. Read them as follows:

| v3.7 term | v4 |
|---|---|
| F row, quality bin Q | Rows on rungs 1–100; Q is the weight |
| E row | Rows on the 3,000 and 10,000 rungs |
| M row | Rows on rungs 30,000 and above |
| N | people |
| Y | years |
| cf, owned fraction, attributable share, retained share | share |
| Sustained | Follows. Where a ruling says Y = 3, use 3 for people who joined this period and 1 for those already there |
| "Full PERCYs rate" per view | The split where people can be estimated; otherwise the §4 fallback |

Re-score of the reference channels and two past grants under both versions: `claude/PERCYs_v4_rescore_2026-11-12.md`.
