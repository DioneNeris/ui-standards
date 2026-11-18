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

    def test_stdin_request_and_result_and_reject_double_stdin(self):
        from fixtures import request, result
        req = request()
        raw = json.dumps(req, ensure_ascii=False).encode('utf-8')
        cmd = [sys.executable, str(ROOT / 'scripts/validate.py')]
        valid_request = subprocess.run(
            cmd + ['request', '--package-root', str(ROOT), '--file', '-'],
            input=raw, capture_output=True)
        self.assertEqual(valid_request.returncode, 0, valid_request.stderr)
        with __import__('tempfile').TemporaryDirectory() as tmp:
            path = Path(tmp) / 'request.json'
            path.write_bytes(raw)
            res = result(ROOT, req)
            import hashlib
            res['request_ref'] = hashlib.sha256(raw).hexdigest()
            valid_result = subprocess.run(
                cmd + ['result', '--package-root', str(ROOT), '--file', '-', '--request', str(path)],
                input=json.dumps(res).encode(), capture_output=True)
            self.assertEqual(valid_result.returncode, 0, valid_result.stderr)
        rejected = subprocess.run(
            cmd + ['result', '--package-root', str(ROOT), '--file', '-', '--request', '-'],
            input=b'{}', capture_output=True)
        self.assertEqual(rejected.returncode, 2)
        self.assertEqual(json.loads(rejected.stderr)['code'], 'INVALID_RESULT')

    def test_empty_stdin_is_invalid(self):
        run = subprocess.run(
            [sys.executable, str(ROOT / 'scripts/validate.py'), 'request',
             '--package-root', str(ROOT), '--file', '-'],
            input=b'', capture_output=True)
        self.assertEqual(run.returncode, 2)
        self.assertEqual(json.loads(run.stderr)['code'], 'INVALID_REQUEST')
