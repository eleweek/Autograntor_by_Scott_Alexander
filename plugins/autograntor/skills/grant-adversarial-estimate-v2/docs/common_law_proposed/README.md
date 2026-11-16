# Proposed Common Law rulings — one file per run

From 2026-10-21, AIs no longer append Proposed rulings to `claude/common_law.md`. That file is frozen at version 2026-10-20.1 (rulings CL-1 to CL-83) until the human user edits it. New Proposed rulings go here instead, as one small file per grant run, so that appending never requires re-writing the whole Common Law.

**Reading.** Every agent reads `claude/common_law.md` in full, then every file in this folder (`project_info` lists them). Together they are the current Common Law. Order of authority is unchanged: the human user's prompt > Adopted rulings > Proposed rulings (here and in Part III of the frozen file) > your own judgment.

**Writing (coordinator only, at the end of a run).**
1. List this folder and find the highest ruling number across the frozen file (CL-83) and every file here. Your first new ruling takes the next number.
2. Write one new file named `<YYYY-MM-DD>_<run-label>.md` (the label is a short tag for the run; it may be the organisation's short name only in the file name, never inside a ruling). Never edit or overwrite an existing file here.
3. Use the ruling template from Part I of `common_law.md`: `### CL-<n>: <title> [Proposed <date>, by <model>]`, then **Rule**, **Why**, optional hypothetical **Example**. Keep rulings general: no grant names, applicant details, forecast results or parameter values from a specific forecast.
4. **The bar.** Before proposing, search `claude/common_law_index.md` (one line per existing ruling) and every file in this folder for a ruling that already covers the situation; cite it instead if one does. Propose only if all three hold: no existing ruling covers it; the call moved a headline mean by more than about 10%; and the situation is one another grant could plausibly raise. At most three new rulings per run; if more seem needed, keep the three that moved the most and put the rest in the report as judgment calls. Fewer, broader rulings beat many narrow ones, and a candidate that merely refines an existing ruling should be written as a one-line note in the report, not a new number.

**Version line for reports.** State the frozen file's version plus the newest file name here, e.g. `Common Law 2026-10-20.1 + proposed through 2026-10-21_example.md`.

**For the human user.** When you adopt a ruling from here, move it into Part II of `common_law.md` (and bump its version); when you strike one, say so in that file so the number is not reused. You may delete files here once their rulings have been adopted or struck.
