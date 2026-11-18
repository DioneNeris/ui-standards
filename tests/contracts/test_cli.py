import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class CliTests(unittest.TestCase):
    def test_baseline_cli(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/validate.py'), 'baseline', '--package-root', str(ROOT), '--json'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['rule_count'], 53)

    def test_missing_request_fails_structured(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/validate.py'), 'request', '--package-root', str(ROOT), '--file', '/missing/no.json'], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('code', json.loads(result.stderr))
