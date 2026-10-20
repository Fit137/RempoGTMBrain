#!/usr/bin/env python3
"""Audit this brain with the GTM Brain skill's own audit script.

    python3 scripts/audit.py [--max-age-days 90] [--quiet]

The skill is installed inside this repo at .claude/skills/, and its asset templates
carry unfilled placeholders on purpose. The audit is about the brain, not the
installed skill, so this wrapper skips .claude/ and then runs the skill's checks
unchanged on the repository root.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_SCRIPTS = ROOT / ".claude" / "skills" / "go-to-market-brain" / "scripts"

if not (SKILL_SCRIPTS / "audit_brain.py").exists():
    sys.exit("The GTM Brain skill is not installed. Run the install command in README.md first.")

sys.path.insert(0, str(SKILL_SCRIPTS))
import audit_brain  # noqa: E402

audit_brain.SKIP_DIRS.add(".claude")
sys.argv = ["audit_brain.py", str(ROOT), *sys.argv[1:]]
raise SystemExit(audit_brain.main())
