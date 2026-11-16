#!/usr/bin/env python3
"""Turn the owner's Project-based SKILL.md into the self-contained plugin SKILL.md.

Usage: python3 tools/edit_skill.py originals/SKILL_v2_package_2026-11-12.md \
           plugins/autograntor/skills/grant-adversarial-estimate-v2/SKILL.md

Every change is listed below as an (old, new) pair that must match the source exactly once,
so the difference from the owner's text is reviewable and the script fails loudly if the
source changes. Nothing else in the skill is touched.

What the edits do, in one line each:
  * documents are read from a local copy of the skill's docs/ folder, not from a Claude Project;
  * briefs, ledgers, rulings, milestones and the report are written locally and sent to the
    user, not uploaded to a Project;
  * FutureSearch is skipped cleanly when the connector is absent;
  * ruling numbers used twice in common_law_proposed/ are cited with their file name.
"""
import sys

src, dst = sys.argv[1:3]
s = open(src, encoding="utf-8").read()


def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:80])
    s = s.replace(old, new)


def cut(start, end, new):
    """Replace everything from the heading `start` up to (not including) the heading `end`."""
    global s
    assert s.count(start) == 1 and s.count(end) == 1, (start, end)
    a, b = s.index(start), s.index(end)
    assert a < b
    s = s[:a] + new + s[b:]


# ---------------------------------------------------------------- front matter and intro
rep("Use instead of grant-adversarial-estimate: subagents read the standard documents from the Project, ledgers go through simulate.py and are saved, Proposed rulings go to per-run files.",
    "Use instead of grant-adversarial-estimate: the coordinator stages the bundled docs locally, ledgers go through simulate.py and are saved, Proposed rulings go to per-run files. Self-contained packaging: no Claude Project needed.")

rep("# Adversarial grant estimate (v2)\n",
    """# Adversarial grant estimate (v2)

> **Self-contained packaging (unofficial).** The standard documents ship in the `docs/` folder next to this file. They are the owner's files from the package dated 2026-11-12 (PERCYs v4), byte for byte. Where the owner's skill read from or wrote to a Claude Project, this copy reads a staged local copy and writes local files that it sends to the user; nothing else in the method is changed. Two things to know about the documents:
> 1. **Four ruling numbers are used more than once** across the files in `common_law_proposed/` (CL-86, CL-87 and CL-90 twice each, CL-89 three times), because separate runs numbered their rulings independently. Cite any of these as number plus file name (for example "CL-89 (2026-10-22_cascade)"), and never assume which one another agent meant.
> 2. **Some documents still speak of the Project**: `claude/...` paths, `project_info`, and a frozen `common_law.md` that is not in this package. Read `claude/<name>` as `grant_eval/_docs/<name>`; the core, index and topic files together hold the text of the frozen file.
""")

rep("no per-grant inputs file and no copying of documents (subagents read the standard documents straight from the Project; the coordinator stages only the simulator);",
    "no per-grant inputs file (the coordinator stages the standard documents once per session and subagents read local copies);")

# ---------------------------------------------------------------- modes
rep("Stage only `fetch_manifund.py`, and only if a listing is on Manifund; the simulator is not needed. For each grant the coordinator saves the brief and the application to the Project (see \"Saving the brief\" under Step 0)",
    "Setup stages the documents as usual; the simulator is not run. For each grant the coordinator saves the brief and the application under `grant_eval/_briefs/` and sends them to the user (see \"Saving the brief\" under Step 0)")

rep("Use `project_info` to find the newest `claude/briefs/<Org>_<date>.md`; if there is none, run in full mode and say so. Before Step 1, write `grant_eval/<org>/answers.md` (one Write) and upload it with `local_path` to `claude/briefs/<Org>_<date>_answers.md`.",
    "Find the newest `grant_eval/_briefs/<Org>_<date>.md`: either left by a prepare run in this working directory, or attached by the user and copied there unchanged at Setup. If there is none, run in full mode and say so. Before Step 1, write `grant_eval/_briefs/<Org>_<date>_answers.md` (one Write).")

rep("The grant block then names three Project paths instead of local ones: the brief, `..._application.md` and `..._answers.md`, which estimators and the judge read with `project_read`.",
    "The grant block then names these three files under `grant_eval/_briefs/`: the brief, `..._application.md` and `..._answers.md`, which estimators and the judge read with the Read tool.")

# ---------------------------------------------------------------- call budgets
rep("as parallel `project_read` calls, before doing anything else;",
    "as parallel Read calls, before doing anything else;")

rep("Background subagents are not given the Projects tool, so they cannot read the standard documents (tested 2026-11-11: identical Opus agents had the tool in the foreground and lacked it in the background). Foreground agents launched in the same step still run in parallel.",
    "Each result then arrives in the step that needs it, which keeps the run in one turn. Foreground agents launched in the same step still run in parallel.")

rep("(all staging Writes in one step, both estimators in one step,",
    "(the staging copy in one Bash call, both estimators in one step,")

# ---------------------------------------------------------------- external tools
rep("Every report lists the queries made and their results. **Submit early,",
    "Every report lists the queries made and their results. If the session has no FutureSearch tools, skip FutureSearch entirely: record each question in the brief as \"FutureSearch not connected\" and say so in the report. **Submit early,")

rep("`claude/fetch_manifund.py` (staged at Setup as `grant_eval/_docs/fetch_manifund.py`) reads the listing as data.",
    "`fetch_manifund.py` (staged at Setup as `grant_eval/_docs/fetch_manifund.py`) reads the listing as data.")

rep("If it fails, say so in the brief and fall back to `curl` of the page; never guess a listing's contents.",
    "If it fails, say so in the brief and fall back to `curl` of the page; if the sandbox refuses that too, stop and ask the user to attach the application. Never guess a listing's contents.")

# ---------------------------------------------------------------- the standard documents
rep("These live in the Autograntor Project under `claude/` (so `common_law_core.md` below is `claude/common_law_core.md`). **Subagents read them straight from the Project with the Projects tool (`project_read`)**; nobody copies them. The only files staged on local disk are the scripts that have to run: `simulate.py` with `ledger_template.csv`, `mean_range.py`, and `fetch_manifund.py` for Manifund listings (see Setup). Never reconstruct weights or rulings from memory. If the session has no access to the Project, stop and ask the user to attach it.",
    "These ship with this skill, in the `docs/` folder next to this SKILL.md (the skill's base directory, shown when the skill loads). The coordinator copies the folder once per session to `grant_eval/_docs/` (see Setup), so `common_law_core.md` below is `grant_eval/_docs/common_law_core.md`. **Subagents read those copies with the Read tool**, and the scripts (`simulate.py` with `ledger_template.csv`, `mean_range.py`, and `fetch_manifund.py` for Manifund listings) run from the same folder. Never reconstruct weights or rulings from memory. If the `docs/` folder is missing or incomplete, stop and tell the user.")

rep("**If a subagent has no Projects tool** (or `project_read` fails for it), it stops at once and replies `NO PROJECTS TOOL`; it never reconstructs a document. The coordinator first checks whether that agent was launched in the background; if so, it relaunches it in the foreground with the same prompt instead of staging anything. Only if a foreground agent also lacks the tool does the coordinator fall back for that run: it reads the documents that agent needs, writes verbatim copies under `grant_eval/_docs/` keeping the paths below `claude/`, restarts the agent with local paths and the Read tool, and says so in the report's process notes.",
    "**If a subagent cannot find a file under `grant_eval/_docs/`**, it stops at once and replies `MISSING DOCUMENT` with the path; it never reconstructs a document. The coordinator reruns the Setup check, restages if needed, restarts the agent with the same prompt, and says so in the report's process notes.")

rep("Subagents cannot list the folder, so the coordinator names the current files in every prompt (Setup step 1).",
    "The coordinator names the current files in every prompt (Setup step 4). Rulings whose number is used more than once there are cited with the file name (see the packaging note at the top).")

rep("The frozen original `claude/common_law.md` is the archival source of truth and is not read during runs.",
    "The owner's frozen original `common_law.md` (version 2026-10-20.1, CL-1 to CL-83) is the archival source of truth; it is not part of this package and is not read during runs.")

# ---------------------------------------------------------------- setup
cut("## Setup — stage only the simulator (coordinator)", "## Independence",
    """## Setup — stage the standard documents once per session (coordinator)

Before the first subagent starts, the coordinator copies the skill's `docs/` folder to `grant_eval/_docs/` in the working directory:
1. Copy the whole folder in one Bash call: `mkdir -p grant_eval && { [ -d grant_eval/_docs ] || cp -r "<skill base directory>/docs" grant_eval/_docs; }`. If `grant_eval/_docs/` already exists from an earlier step in this session, do not overwrite it (it may hold this session's new files).
2. If the user keeps files from earlier runs, copy them in now, unchanged: Proposed-ruling files into `grant_eval/_docs/common_law_proposed/`, their own `milestones_added.md` over the staged copy, and saved briefs into `grant_eval/_briefs/`.
3. Verify with one Bash call and paste its output into the run log: `python3 "<skill base directory>/check_staging.py" "<skill base directory>/docs" grant_eval/_docs`. It checks that every bundled file was copied byte for byte, that each of CL-1 to CL-83 and CL-91 has exactly one full text across the core and topic files, that the index has its 84 lines, and that `simulate.py --template`, `simulate.py` on the template, `mean_range.py` and `fetch_manifund.py --help` all run. It then lists the files in `common_law_proposed/`, the ruling numbers used more than once there, and the next free ruling number. `simulate.py` needs numpy; install it if the check says it is missing. If any other check fails, delete the copy and copy again.
4. Record in the run log the `common_law_proposed/` file list from that output. Every subagent prompt names these files, and the report's version line names the newest.

**Never correct, tidy or "fix typos" in a staged copy, and never delegate the staging to a subagent.** Subagents never edit the staged copies and never rebuild them. Grant-specific material (the application, Commons documents) is still read by the pre-pass from its source.

""")

# ---------------------------------------------------------------- independence
rep("From the Project, a subagent reads only the standard documents named in its prompt: it never opens a past report (any file with `grant_forecast` in its name) or anything under `claude/ledgers/`, opens files under `claude/briefs/` only when its prompt names them (score mode), and never calls `project_search` or `project_info` (their results quote or list past reports), and never writes to the Project.",
    "Under `grant_eval/`, a subagent reads only the standard documents named in its prompt and its own grant's folder: it never opens a past report (any file with `grant_forecast` in its name), another organisation's folder or anything under `grant_eval/_ledgers/`, opens files under `grant_eval/_briefs/` only when its prompt names them (score mode), never searches `grant_eval/` as a whole (the results would quote past reports), and never writes under `grant_eval/_docs/`.")

# ---------------------------------------------------------------- prompt layout
rep("the always-read list and the topic-file list above as Project paths (`claude/...`), the names of the current files in `claude/common_law_proposed/`, the instruction to read the always-read files in one step with `project_read` and to reply `NO PROJECTS TOOL` and stop if that tool is missing, the local paths of the staged simulator and template,",
    "the always-read list and the topic-file list above as local paths under `grant_eval/_docs/`, the names of the current files in `grant_eval/_docs/common_law_proposed/`, the instruction to read the always-read files in one step with the Read tool and to reply `MISSING DOCUMENT` and stop if one is not there, the packaging note's two points (duplicate ruling numbers; Project paths in the documents mean the staged folder), the local paths of the staged simulator and template,")

rep("(in score mode, the three Project paths under `claude/briefs/` instead)",
    "(in score mode, the three files under `grant_eval/_briefs/` instead)")

# ---------------------------------------------------------------- step 0
rep("- Read the always-read documents and the index from the Project in one step,",
    "- Read the always-read documents and the index from `grant_eval/_docs/` in one step,")

rep("**Saving the brief.** In every mode the coordinator uploads `brief.md` with `project_write` and `local_path` to `claude/briefs/<Org>_<date>.md`, so that the facts a forecast rested on outlive the session. In prepare mode it also uploads the application text from `source/` to `claude/briefs/<Org>_<date>_application.md` (Read the file first; an upload needs the file read in this session), because the score run starts from these two files.",
    "**Saving the brief.** In every mode the coordinator copies `brief.md` unchanged to `grant_eval/_briefs/<Org>_<date>.md` and sends that file to the user, so that the facts a forecast rested on outlive the session. In prepare mode it also copies the application text from `source/` to `grant_eval/_briefs/<Org>_<date>_application.md` and sends it, because the score run starts from these two files; tell the user to attach both when they start the score run in a new session.")

# ---------------------------------------------------------------- step 4
rep("- **Rulings.** Do not write to `claude/common_law.md`, `claude/common_law_core.md`, `claude/common_law_index.md` or the topic files. For the judge's candidate rulings that pass the bar in `common_law_proposed/README.md` (no existing ruling covers it; moved a headline mean by more than ~10%; reusable by other grants; at most three per run), list the proposed folder again with `project_info` and read its files (other runs may have added some since Setup), find the next free number across the frozen file (CL-83) and that folder, write the rulings to a local file `grant_eval/<org>/<YYYY-MM-DD>_<run-label>.md` in the template from Part I of the core file, and upload it with `project_write` (`local_path`) to `claude/common_law_proposed/<same name>`. Never edit an existing file there. Keep rulings free of grant names, applicant details and forecast results. A candidate that merely refines an existing ruling goes in the report as a one-line note, not a new number.",
    "- **Rulings.** Do not write to `common_law_core.md`, `common_law_index.md` or the topic files, in the staged copy or in the skill's own `docs/` folder. For the judge's candidate rulings that pass the bar in `common_law_proposed/README.md` (no existing ruling covers it; moved a headline mean by more than ~10%; reusable by other grants; at most three per run), take the next free number above the highest one used in the index or in `grant_eval/_docs/common_law_proposed/` (the Setup check prints it), and write the rulings to a local file `grant_eval/_docs/common_law_proposed/<YYYY-MM-DD>_<run-label>.md` in the template from Part I of the core file. Never edit an existing file there. Keep rulings free of grant names, applicant details and forecast results. A candidate that merely refines an existing ruling goes in the report as a one-line note, not a new number. Send the new file to the user with the report and tell them two things: to reuse these rulings in a later session they attach the file (Setup step 2), and whether to send them to the Common Law's owner is their decision. Never submit rulings anywhere yourself.")

rep("Entries go at the end of the Proposed section of `milestones_added.md`: `project_read` `claude/milestones_added.md` immediately before writing (another run may have appended to it), write that text verbatim to a local file with the new entry added at the end of the Proposed section, and upload it with `project_write` using `local_path` to `claude/milestones_added.md`. Do this only when a milestone is actually being added.",
    "Entries go at the end of the Proposed section of the staged `grant_eval/_docs/milestones_added.md`: append with the Edit tool, leave everything else in the file unchanged, and send the updated file to the user with the report, telling them to attach it in a later session to keep the entries (Setup step 2). Do this only when a milestone is actually being added.")

# ---------------------------------------------------------------- step 5
rep("- Common Law version used (frozen version plus the newest proposed file listed at Setup).",
    "- Version line: Common Law version used (frozen version plus the newest proposed file listed at Setup), and \"self-contained packaging of the 2026-11-12 package\".")

rep("Save the report to the Project as `claude/<Org>_grant_forecast_<date>.md` (upload with `local_path`) and send the judge's verdict if the user wants detail.",
    "Save the report as `grant_eval/<org>/<Org>_grant_forecast_<date>.md`, send that file to the user, and send the judge's verdict too if the user wants detail.")

rep("After the report, Read `A_ledger.csv`, `B_ledger.csv`, `judge_ledger.csv` and `tranches.csv` in one step (an upload needs the file read in this session) and upload them unchanged with `project_write` and `local_path` to `claude/ledgers/<Org>_<date>_A.csv`, `claude/ledgers/<Org>_<date>_B.csv` `claude/ledgers/<Org>_<date>_judge.csv` and `claude/ledgers/<Org>_<date>_tranches.csv`. The tranches file is what a later allocation script reads. Then write and upload `claude/ledgers/<Org>_<date>_run.json` with:",
    "After the report, copy `A_ledger.csv`, `B_ledger.csv`, `judge_ledger.csv` and `tranches.csv` unchanged, in one Bash call, to `grant_eval/_ledgers/<Org>_<date>_A.csv`, `grant_eval/_ledgers/<Org>_<date>_B.csv`, `grant_eval/_ledgers/<Org>_<date>_judge.csv` and `grant_eval/_ledgers/<Org>_<date>_tranches.csv`. The tranches file is what a later allocation script reads. Then write `grant_eval/_ledgers/<Org>_<date>_run.json` with:")

rep("No agent reads `claude/ledgers/` during a run.",
    "Send the tranches file and the run record to the user, and the three ledgers if they ask. No agent reads `grant_eval/_ledgers/` during a run.")

open(dst, "w", encoding="utf-8").write(s)

# Anything left that still points at a Project is a missed edit. The packaging note mentions
# these words on purpose, so it is excluded from the count.
body = s.split("## Modes: full, prepare and score", 1)[1]
left = {w: body.count(w) for w in ("project_read", "project_write", "project_info", "project_search",
                                   "Projects tool", "claude/", "the Project", "local_path")}
print("leftover Project references outside the packaging note:", left)
if any(left.values()):
    sys.exit("edit_skill.py: unconverted Project reference(s) remain")
