# Autograntor plugin (unofficial packaging)

A self-contained packaging of the `grant-adversarial-estimate-v2` skill from Scott Alexander's
[Towards The Autograntor](https://www.lesswrong.com/posts/Sfkv6JF2ozmAkggKu), so that it can be
installed from one place and run without a private Claude Project.

**This is a third party's packaging, not an official release.** The Common Law, the milestone
weights, the PERCYs module, the simulator and the skill are Scott Alexander's work. From version
0.2.0 the documents and scripts are his own files, taken unchanged from his starter package dated
2026-11-12 (PERCYs v4). The only thing changed is where the skill reads and writes: a local folder
instead of a Claude Project.

## What is in the package

| File (under `plugins/autograntor/skills/grant-adversarial-estimate-v2/`) | Status |
|---|---|
| `docs/` (26 files) | **The owner's files, byte for byte**, from the `claude/` folder of the 2026-11-12 package. |
| `docs/common_law_core.md`, `common_law_index.md`, `common_law_topics/*.md` | The frozen Common Law, CL-1 to CL-83, plus Adopted CL-91. |
| `docs/common_law_proposed/*.md` | Ten per-run files with the rulings added after the freeze (CL-84 to CL-94). |
| `docs/milestones_weights.md`, `docs/milestones_added.md` | Canonical weights; Approved and Proposed milestones and parameters. |
| `docs/PERCYs_v4.md` | Pricing rules for persuasion and media grants. |
| `docs/simulate.py`, `docs/ledger_template.csv` | The owner's ledger simulator. Needs numpy. |
| `docs/mean_range.py` | Range-on-the-mean helper for the judge. |
| `docs/fetch_manifund.py` | Reads a Manifund listing as data. Needs network access to manifund.org. |
| `SKILL.md` | The owner's skill with the edits listed under "Changes to the skill". |
| `check_staging.py` | **Added by this packaging.** One command that checks the staged copy. |

`originals/` holds the 2026-11-12 package as received (the ZIP and its `SKILL.md`), and the four
files published with the original post, which the package supersedes.

### Known issues

1. **Four ruling numbers are used more than once.** In `docs/common_law_proposed/`, CL-86, CL-87
   and CL-90 each name two different rulings and CL-89 names three, because separate runs numbered
   their rulings independently. The files are left as the owner wrote them. The skill is told to
   cite these as number plus file name, and `check_staging.py` lists them at every run.
2. **Some documents still mention the Project** (`claude/...` paths, `project_info`, a frozen
   `common_law.md` that is not in the package). The skill tells agents how to read these.
3. **The funder price table (CL-91) is the owner's policy**, for example the funding platform's
   own money at 50 per $1M. Edit `docs/common_law_core.md` if your situation differs, and say so
   when you report results.
4. **Not yet run end to end in this form.** Version 0.2.0 has passed the staging check and the
   tests below. No full grant run has been done with it, and the install step is untested.
5. **Results are still not comparable with the owner's own runs** unless your staged rulings and
   milestones match his at the time of his run.

## Install

**Claude app:** Customize > Plugins > Add > Add marketplace > Add from a repository, and enter this
repository's address. Then install `autograntor`.

**Claude Code:**

```
/plugin marketplace add <owner>/<repo>
/plugin install autograntor@autograntor-prototype
```

**Without a repository:** zip the `plugins/autograntor` folder and upload it as a custom plugin, or
in Claude Code run `claude --plugin-dir ./plugins/autograntor`.

Then ask, for example: *"Use the grant-adversarial-estimate-v2 skill to score [grant name]. The
application is at [link or attached file]."* The skill uses subagents (one Sonnet pre-pass, one
Opus and one Fable estimator, a Fable judge), so a run takes a while. FutureSearch is optional;
without the connector the skill skips it and says so. Lightcone Commons access is not included.

## Changes to the skill

`originals/SKILL_v2_package_2026-11-12.md` is the owner's text. `tools/edit_skill.py` applies every
change as an exact find-and-replace and fails if any does not match, so the difference is
reviewable. In short:

- **Documents come from the skill's own `docs/` folder**, copied once per session to
  `grant_eval/_docs/` and read there, instead of being read from a Claude Project.
- **What the owner's skill uploads to the Project is written locally and sent to the user**:
  briefs (`grant_eval/_briefs/`), ledgers and the run record (`grant_eval/_ledgers/`), new
  Proposed rulings, added milestones and the report. To carry rulings, milestones or a brief into
  a later session, attach the files; the skill copies them in at Setup. Nothing is submitted
  anywhere automatically.
- **Setup is one copy and one check** (`check_staging.py`), replacing the owner's step that
  re-typed the scripts out of the Project.
- **FutureSearch is skipped cleanly** when the connector is absent, and the Manifund reader asks
  for an attached application if the sandbox cannot reach the site.
- **Duplicate ruling numbers are cited with their file name** (known issue 1).

Everything else is untouched: the three modes, the pre-pass, estimators, critique rule, judge,
funging and tranche reporting, call budgets.

## Rebuilding from a newer package

Put the owner's new ZIP in `originals/` and run:

```
python3 tools/build_docs.py originals/<new package>.zip
python3 tests/test_package.py
```

`build_docs.py` unpacks the package's `claude/` folder into `docs/` unchanged and runs
`edit_skill.py`. If the owner's `SKILL.md` has changed, `edit_skill.py` stops at the first edit
that no longer matches; update that edit and rerun. Then update the package name and file count
in `tests/test_package.py`, and the ruling counts in `check_staging.py` if the frozen Common Law
has grown.

## Tests

```
python3 tests/test_package.py
```

Eighteen tests. Four check the packaging: every file in `docs/` is identical to the file in the
owner's ZIP, `SKILL.md` is exactly what `edit_skill.py` produces, and the staging check passes on
a clean copy and fails on an edited one. Fourteen check the owner's simulator and range helper
against numbers that can be verified by hand (for example CL-2's own example: a law moved from
10% to 12% earns 2% of its weight). They describe the simulator; they do not change it.

## What changed from 0.1.0

Version 0.1.0 was built from the four files published with the post, with the gaps filled in:
a reconstructed simulator, no rulings after CL-62, an empty added-milestones file, PERCYs v3.7.
Version 0.2.0 replaces all of that with the owner's files. Consequences:

- **Ledgers from 0.1.0 do not run unchanged.** The owner's simulator names the row column `row`
  (not `name`), takes `--branches` as `{question: P(yes)}` with `branch_val` of `yes` or `no`, and
  takes `--exec` as `{group: {"mean": m, "collapse_p": c}}`.
- **The reconstruction's `given` column is gone.** The owner's simulator has no way to make a
  charge apply only in worlds where a named event happens, so such a charge is paid in every
  world. The mean is unaffected; the median and P(negative) are more pessimistic than they should
  be for grants whose costs depend on success.
- **The money price is no longer a single 20 per $1M.** CL-91 sets a price per funder tier, and
  every forecast reports a base value and a with-funging value.

## Open questions for the owner

1. Should this be public, and under whose account?
2. Where should Proposed rulings from other people's runs go: nowhere, an issue, or a pull request?
3. Are outside contributions to the Common Law wanted at all?
4. Should users be able to layer their own weights and rulings on top, and how should reports label
   results produced that way?
5. Should the duplicate ruling numbers be renumbered at the source?
6. Licence for the Common Law, weights, simulator and skill. None is stated here; all rights remain
   with the author until he says otherwise.
