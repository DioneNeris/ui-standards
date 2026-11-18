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

    def test_nested_symlink_escape_is_rejected_without_external_write(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            target = Path(tmp)
            nested = target / '.agents/skills'
            nested.mkdir(parents=True)
            (nested / 'ui-design').symlink_to(outside, target_is_directory=True)
            result = self.run_install(target)
            self.assertNotEqual(result.returncode, 0, result.stderr)
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_conflict_preflight_does_not_partially_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            conflict = target / '.claude/skills/ui-code-review/SKILL.md'
            conflict.parent.mkdir(parents=True)
            conflict.write_text('user owned')
            result = self.run_install(target)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(conflict.read_text(), 'user owned')
            self.assertFalse((target / '.agents').exists())
            self.assertFalse((target / '.claude/skills/ui-design').exists())

    def test_install_creates_only_six_skill_adapters(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            result = self.run_install(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            installed = sorted(p.relative_to(target).as_posix()
                               for p in target.rglob('SKILL.md'))
            self.assertEqual(len(installed), 6)
            self.assertTrue(all(p.endswith('/SKILL.md') for p in installed))
            for p in target.rglob('SKILL.md'):
                content = p.read_text()
                self.assertIn('Validate pinned normative blobs', content)
