#!/usr/bin/env python3
"""Rebuild the plugin's skill folder from the owner's package.

Usage: python3 tools/build_docs.py [originals/autograntor_package_2026-11-12_percys-v4.zip]

1. Unpacks the package's `claude/` folder, unchanged, into the skill's `docs/` folder.
2. Saves the package's SKILL.md as originals/SKILL_v2_package_<date>.md.
3. Runs tools/edit_skill.py to produce the self-contained SKILL.md.

No document is rewritten: every file under docs/ is byte-for-byte the file in the package
(tests/test_package.py checks this).
"""
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "plugins" / "autograntor" / "skills" / "grant-adversarial-estimate-v2"
DOCS_PREFIX = "autograntor/claude/"
SKILL_MEMBER = "autograntor/skill/grant-adversarial-estimate-v2/SKILL.md"

package = Path(sys.argv[1]) if len(sys.argv) > 1 else sorted((ROOT / "originals").glob("autograntor_package_*.zip"))[-1]
date = re.search(r"\d{4}-\d{2}-\d{2}", package.name).group(0)

docs = SKILL / "docs"
if docs.exists():
    shutil.rmtree(docs)
with zipfile.ZipFile(package) as z:
    for info in z.infolist():
        name = info.filename
        if info.is_dir() or not name.startswith(DOCS_PREFIX):
            continue
        rel = Path(name[len(DOCS_PREFIX):])
        if rel.is_absolute() or ".." in rel.parts:
            sys.exit(f"refusing unsafe path in package: {name}")
        target = docs / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(z.read(info))
    original_skill = ROOT / "originals" / f"SKILL_v2_package_{date}.md"
    original_skill.write_bytes(z.read(SKILL_MEMBER))

subprocess.run([sys.executable, str(ROOT / "tools" / "edit_skill.py"), str(original_skill), str(SKILL / "SKILL.md")], check=True)
print(f"built {SKILL.relative_to(ROOT)} from {package.name}")
