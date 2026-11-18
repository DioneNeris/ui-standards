import unittest
from pathlib import Path
from fixtures import request, result
from uistandards.report import render_report

ROOT = Path(__file__).resolve().parents[2]

class ReportTests(unittest.TestCase):
    def test_report_contains_run_id_baseline_and_per_rule_status(self):
        req = request()
        res = result(ROOT, req)
        report = render_report(res, req, ROOT)
        self.assertIn(res['run_id'], report)
        self.assertIn('NAO_VERIFICADA', report)
        self.assertIn('LAY-001', report)
        self.assertIn('NAO_VERIFICADO', report)
