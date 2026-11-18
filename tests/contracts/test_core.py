import unittest
from pathlib import Path

from uistandards.core import aggregate, load_baseline

ROOT = Path(__file__).resolve().parents[2]


class CoreTests(unittest.TestCase):
    def test_loads_53_matching_rules(self):
        rules = load_baseline(ROOT)
        self.assertEqual(len(rules), 53)
        self.assertEqual(rules['LAY-001']['methods'], ['V', 'I'])
        self.assertEqual(rules['LAY-001']['scenario_id'], 'TC-LAY-001')

    def test_violation_precedes_unverified(self):
        self.assertEqual(aggregate('APLICAVEL', ['S', 'V'], {'S': 'NAO_CONFORME'}), 'NAO_CONFORME')

    def test_conformity_requires_all_applicable_methods(self):
        self.assertEqual(aggregate('APLICAVEL', ['S', 'V'], {'S': 'CONFORME'}), 'NAO_VERIFICADO')
        self.assertEqual(aggregate('APLICAVEL', ['S', 'V'], {'S': 'CONFORME', 'V': 'CONFORME'}), 'CONFORME')

    def test_no_applicable_methods_does_not_prove_conformity(self):
        self.assertEqual(aggregate('APLICAVEL', ['S'], {'S': 'NAO_APLICAVEL'}), 'NAO_VERIFICADO')

    def test_altered_baseline_rejected(self):
        import subprocess, tempfile
        from uistandards.core import BaselineError, FILES
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(['git','clone','--quiet','--no-hardlinks',str(ROOT),tmp],check=True)
            p=Path(tmp)/FILES['matrix_derived'][0]
            p.write_bytes(p.read_bytes()+b'changed')
            with self.assertRaises(BaselineError): load_baseline(tmp)
