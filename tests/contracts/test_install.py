import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'scripts/install.py'


class InstallTests(unittest.TestCase):
    def run_install(self, target, *args):
        return subprocess.run([sys.executable, str(SCRIPT), '--package-root', str(ROOT), '--project-root', str(target), '--agents', 'codex,claude', *args], capture_output=True, text=True)

    def test_dry_run_and_idempotence_and_conflict(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            self.assertEqual(self.run_install(target, '--dry-run').returncode, 0)
            self.assertEqual(list(target.iterdir()), [])
            self.assertEqual(self.run_install(target).returncode, 0)
            self.assertEqual(self.run_install(target).returncode, 0)
            skill = target / '.claude/skills/ui-audit/SKILL.md'
            skill.write_text('user content')
            self.assertNotEqual(self.run_install(target).returncode, 0)
            self.assertEqual(skill.read_text(), 'user content')

    def test_rejects_symlink_escape(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            target = Path(tmp)
            (target / '.claude').symlink_to(outside, target_is_directory=True)
            self.assertNotEqual(self.run_install(target).returncode, 0)
            self.assertEqual(list(Path(outside).iterdir()), [])
