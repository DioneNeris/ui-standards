import copy
import unittest
from pathlib import Path
from uistandards.validation import ContractError, validate_request, validate_result

ROOT = Path(__file__).resolve().parents[2]


class ValidationTests(unittest.TestCase):
    def test_incomplete_request_rejected(self):
        with self.assertRaises(ContractError):
            validate_request({'skill': 'ui-audit'}, ROOT)

    def test_incomplete_result_rejected(self):
        with self.assertRaises(ContractError):
            validate_result({'rules': []}, {}, ROOT)

from fixtures import request, result

class ValidFixtureTests(unittest.TestCase):
    def setUp(self):
        self.req = request()
        self.res = result(ROOT, self.req)

    def test_valid_partial_result_for_53_rules(self):
        validate_result(self.res, self.req, ROOT)

    def test_false_conformity_is_rejected(self):
        self.res['rules'][0]['status'] = 'CONFORME'
        with self.assertRaises(ContractError):
            validate_result(self.res, self.req, ROOT)

    def test_not_applicable_needs_evidence(self):
        self.res['rules'][0].update(applicability='NAO_APLICAVEL', status='NAO_APLICAVEL')
        with self.assertRaises(ContractError):
            validate_result(self.res, self.req, ROOT)

    def test_duplicate_rule_rejected(self):
        self.res['rules'][1] = copy.deepcopy(self.res['rules'][0])
        with self.assertRaises(ContractError):
            validate_result(self.res, self.req, ROOT)

    def test_refuse_read_only_write(self):
        self.req['authorization']['operations'].append('implement')
        with self.assertRaises(ContractError):
            validate_request(self.req, ROOT)

class EvidenceTests(unittest.TestCase):
    def test_proven_violation_overrides_missing_method(self):
        import hashlib, tempfile
        req = request(); req['authorization']['methods'].append('V'); res = result(ROOT, req)
        with tempfile.TemporaryDirectory() as tmp:
            artifact = Path(tmp) / 'evidence.txt'; artifact.write_text('observed violation')
            res['evidence'].append({'id':'e1','rule_id':'LAY-001','method':'V','flow':'fixture','element':'fixture','state':'fixture','steps':['observe'],'observation':'violation','artifact':{'uri':str(artifact),'sha256':hashlib.sha256(artifact.read_bytes()).hexdigest(),'media_type':'text/plain'},'captured_at':'2026-11-18T12:00:00Z','executor':'reviewer','method_result':'NAO_CONFORME','sufficiency':'SUFICIENTE','sufficiency_reason':'shows violation','assessor':'reviewer','limitations':[]})
            r=res['rules'][0]; r['applicability']='APLICAVEL'; r['status']='NAO_CONFORME'; r['method_results']=[{'method':m,'applicability':'APLICAVEL' if m=='V' else 'INDETERMINADA','status':'NAO_CONFORME' if m=='V' else 'NAO_VERIFICADO','evidence_ids':['e1'] if m=='V' else [],'reason':'observed' if m=='V' else 'not run'} for m in r['required_methods']]
            validate_result(res,req,ROOT)
            res['evidence'][0]['captured_at']='invalid'
            with self.assertRaises(ContractError): validate_result(res,req,ROOT)
            res['evidence'][0]['captured_at']='2026-11-18T12:00:00Z'
            req['authorization']['methods'].remove('V')
            with self.assertRaises(ContractError): validate_result(res,req,ROOT)
            req['authorization']['methods'].append('V')
            artifact.write_text('changed')
            with self.assertRaises(ContractError): validate_result(res,req,ROOT)

    def test_unapproved_method_rejected(self):
        req = request(); res = result(ROOT, req)
        row = res["rules"][0]
        row["method_results"] = [{"method":m, "applicability":"INDETERMINADA", "status":"NAO_VERIFICADO", "evidence_ids":[], "reason":"not run"} for m in row['required_methods']]
        row["method_results"][0]['applicability'] = 'APLICAVEL'
        # A method not run is allowed to be described; it cannot be claimed as executed.
        row["method_results"][0]["status"] = "CONFORME"
        with self.assertRaises(ContractError): validate_result(res,req,ROOT)

    def test_complete_evidence_and_applicable_methods(self):
        import hashlib, tempfile
        req=request(); req['authorization']['methods']=['V','I']; res=result(ROOT,req)
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'proof'; p.write_text('proof'); h=hashlib.sha256(p.read_bytes()).hexdigest()
            row=res['rules'][0]; row['applicability']='APLICAVEL'; row['status']='CONFORME'; row['method_results']=[]
            for m in ('V','I'):
                eid='proof-'+m
                res['evidence'].append({'id':eid,'rule_id':row['id'],'method':m,'flow':'f','element':'e','state':'s','steps':['observe'],'observation':'criterion observed','artifact':{'uri':str(p),'sha256':h,'media_type':'text/plain'},'captured_at':'2026-11-18T12:00:00Z','executor':'reviewer','method_result':'CONFORME','sufficiency':'SUFICIENTE','sufficiency_reason':'supports criterion','assessor':'reviewer','limitations':[]})
                row['method_results'].append({'method':m,'applicability':'APLICAVEL','status':'CONFORME','evidence_ids':[eid],'reason':'observed'})
            validate_result(res,req,ROOT)
            row['method_results'][0]['applicability']='INDETERMINADA'
            with self.assertRaises(ContractError): validate_result(res,req,ROOT)
            row['method_results'][0]['applicability']='APLICAVEL'
            row['exceptions'].append({'rule_id':row['id'],'type':'CONFLITO_BLOQUEANTE','context':'collision','justification':'outside competence','evidence_ids':[],'approver':None,'validity':None,'review_at':None,'impact':'blocked','approval_state':'PENDENTE'})
            with self.assertRaises(ContractError): validate_result(res,req,ROOT)
            row['exceptions'].clear()
            res['evidence'][1]['sufficiency']='INSUFICIENTE'
            with self.assertRaises(ContractError): validate_result(res,req,ROOT)

    def test_blocking_conflict_cannot_be_conform(self):
        req=request(); res=result(ROOT,req)
        row=res['rules'][0]
        row['exceptions'].append({'rule_id':row['id'],'type':'CONFLITO_BLOQUEANTE','context':'collision','justification':'outside competence','evidence_ids':[],'approver':None,'validity':None,'review_at':None,'impact':'blocked','approval_state':'PENDENTE'})
        row['status']='NAO_APLICAVEL'; row['applicability']='NAO_APLICAVEL'
        with self.assertRaises(ContractError): validate_result(res,req,ROOT)

    def test_verified_not_applicable(self):
        import hashlib, tempfile
        req=request(); res=result(ROOT,req)
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'proof'; p.write_text('no dialogs'); h=hashlib.sha256(p.read_bytes()).hexdigest()
            row=res['rules'][0]; row['applicability']='NAO_APLICAVEL'; row['status']='NAO_APLICAVEL'
            res['evidence'].append({'id':'na-proof','rule_id':row['id'],'method':'V','flow':'f','element':'e','state':'s','steps':['inspect'],'observation':'absent','artifact':{'uri':str(p),'sha256':h,'media_type':'text/plain'},'captured_at':'2026-11-18T12:00:00Z','executor':'reviewer','method_result':'NAO_APLICAVEL','sufficiency':'SUFICIENTE','sufficiency_reason':'absence documented','assessor':'reviewer','limitations':[]})
            req['authorization']['methods'].append('V')\n            row['exceptions'].append({'rule_id':row['id'],'type':'NAO_APLICABILIDADE','context':'scope','justification':'absent','evidence_ids':['na-proof'],'approver':'PO','validity':'pilot','review_at':'2027-01-01','impact':'not applicable','approval_state':'APROVADA'})
            validate_result(res,req,ROOT)
            row['exceptions'][0]['approval_state']='PENDENTE'
            with self.assertRaises(ContractError): validate_result(res,req,ROOT)

class ThreeSkillTests(unittest.TestCase):
    def test_valid_requests_and_partial_results_for_each_skill(self):
        for skill, mode in [('ui-design','plan'),('ui-audit','audit'),('ui-code-review','review')]:
            req=request(); req['skill']=skill; req['mode']=mode
            if skill=='ui-design': req['design']={'artifacts':[],'constraints':[]}
            if skill=='ui-code-review': req['review']={'base':'base','head':'head','diff_scope':'scope'}
            with self.subTest(skill=skill):
                validate_request(req,ROOT)
                validate_result(result(ROOT,req),req,ROOT)

    def test_orphan_evidence_rejected(self):
        req=request(); res=result(ROOT,req)
        res['evidence'].append({'id':'bad','rule_id':'NO-999','method':'S','flow':'f','element':'e','state':'s','steps':['inspect'],'observation':'none','artifact':None,'captured_at':'2026-11-18T12:00:00Z','executor':'x','method_result':'NAO_VERIFICADO','sufficiency':'INDETERMINADA','sufficiency_reason':'none','assessor':'x','limitations':['none']})
        with self.assertRaises(ContractError): validate_result(res,req,ROOT)

    def test_missing_baseline_allows_only_blocked_diagnostic(self):
        import shutil, tempfile
        from uistandards.core import BaselineError
        req=request(); res=result(ROOT,req)
        res['execution_state']='BLOQUEADA'; res['rules']=[]
        res['baseline']['repository_integrity']='FALHOU'
        res['errors']=[{'code':'BASELINE_MISSING','message':'missing','affected_ids':[],'action':'restore'}]
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree(ROOT/'schemas',Path(tmp)/'schemas')
            validate_result(res,req,Path(tmp))
            res['execution_state']='COMPLETA'
            with self.assertRaises((ContractError,BaselineError)): validate_result(res,req,Path(tmp))

class BlockedDiagnosticRegressionTests(unittest.TestCase):
    def test_executor_cannot_access_baseline_even_when_validator_can(self):
        req = request()
        res = result(ROOT, req)
        res['execution_state'] = 'BLOQUEADA'
        res['rules'] = []
        res['baseline']['repository_integrity'] = 'NAO_VERIFICADA'
        res['errors'] = [{'code': 'BASELINE_MISSING', 'message': 'executor access denied',
                          'affected_ids': [], 'action': 'grant read access'}]
        validate_result(res, req, ROOT)
        res['findings'] = [{'id':'f','rule_id':'LAY-001','method':'S','observation':'claim',
                            'impact':'unknown','evidence_ids':[]}]
        with self.assertRaises(ContractError):
            validate_result(res, req, ROOT)

    def test_blocked_result_rejects_identity_or_write_claims(self):
        req = request()
        res = result(ROOT, req)
        res['execution_state'] = 'BLOQUEADA'
        res['rules'] = []
        res['baseline']['repository_integrity'] = 'NAO_VERIFICADA'
        res['errors'] = [{'code': 'BASELINE_MISSING', 'message': 'access denied',
                          'affected_ids': [], 'action': 'retry'}]
        validate_result(res, req, ROOT)
        res['changed_files'] = ['app/cadastro.html']
        with self.assertRaises(ContractError):
            validate_result(res, req, ROOT)
        res['changed_files'] = []
        res['target'] = dict(res['target'], project='different')
        with self.assertRaises(ContractError):
            validate_result(res, req, ROOT)

class AdversarialAuthorizationTests(unittest.TestCase):
    def blocked(self):
        req = request()
        res = result(ROOT, req)
        res['execution_state'] = 'BLOQUEADA'
        res['rules'] = []
        res['baseline']['repository_integrity'] = 'NAO_VERIFICADA'
        res['errors'] = [{'code': 'BASELINE_MISSING', 'message': 'denied',
                          'affected_ids': [], 'action': 'request access'}]
        return req, res

    def test_blocked_cannot_bypass_unauthorized_write(self):
        req, res = self.blocked()
        req['authorization']['operations'].append('implement')
        with self.assertRaises(ContractError):
            validate_result(res, req, ROOT)

    def test_blocked_cannot_bypass_forged_baseline(self):
        req, res = self.blocked()
        req['baseline']['commit'] = 'a' * 40
        res['baseline']['commit'] = 'a' * 40
        with self.assertRaises(ContractError):
            validate_result(res, req, ROOT)

    def test_blocked_cannot_bypass_scope_mismatch(self):
        req, res = self.blocked()
        res['scope'] = 'unrelated'
        with self.assertRaises(ContractError):
            validate_result(res, req, ROOT)

    def test_blocked_rejects_claimed_normative_rules(self):
        req, res = self.blocked()
        res['rules'] = result(ROOT, req)['rules']
        with self.assertRaises(ContractError):
            validate_result(res, req, ROOT)

    def test_blocked_rejects_changed_files_and_artifacts_claims(self):
        req, res = self.blocked()
        res['changed_files'] = ['app/changed.html']
        with self.assertRaises(ContractError):
            validate_result(res, req, ROOT)

    def test_blocked_checks_exact_request_bytes(self):
        import hashlib, json
        req, res = self.blocked()
        raw = json.dumps(req, sort_keys=True).encode()
        res['request_ref'] = hashlib.sha256(raw).hexdigest()
        validate_result(res, req, ROOT, raw)
        with self.assertRaises(ContractError):
            validate_result(res, req, ROOT, raw + b' ')

class IndependentAuditRegressions(unittest.TestCase):
    def test_plan_rejects_claimed_changes(self):
        req = request(); req['skill'] = 'ui-design'; req['mode'] = 'plan'
        req['design'] = {'artifacts': [], 'constraints': []}
        res = result(ROOT, req); res['changed_files'] = ['app/a.html']
        with self.assertRaisesRegex(ContractError, 'Read-only changed_files'):
            validate_result(res, req, ROOT)

    def test_implement_rejects_out_of_scope_changes(self):
        req = request(); req['skill'] = 'ui-design'; req['mode'] = 'implement'
        req['design'] = {'artifacts': [], 'constraints': []}
        req['authorization']['operations'].append('implement')
        req['authorization']['writable_paths'] = ['app/']
        res = result(ROOT, req); res['changed_files'] = ['outside/a.html']
        with self.assertRaisesRegex(ContractError, 'outside writable paths'):
            validate_result(res, req, ROOT)

    def test_implement_rejects_unsafe_paths(self):
        for path in ('../outside', '/etc', '.claude/skills', 'framework/', '.git/config'):
            req = request(); req['skill'] = 'ui-design'; req['mode'] = 'implement'
            req['design'] = {'artifacts': [], 'constraints': []}
            req['authorization']['operations'].append('implement')
            req['authorization']['writable_paths'] = [path]
            with self.subTest(path=path), self.assertRaisesRegex(ContractError, 'writable path'):
                validate_request(req, ROOT)

    def test_blocked_rejects_artifacts(self):
        req = request(); res = result(ROOT, req)
        res['execution_state'] = 'BLOQUEADA'; res['rules'] = []
        res['baseline']['repository_integrity'] = 'FALHOU'
        res['errors'] = [{'code':'BASELINE_MISSING','message':'missing','affected_ids':[],'action':'retry'}]
        res['artifacts'] = [{'uri':'file:///tmp/report','sha256':'0'*64,'media_type':'text/plain'}]
        with self.assertRaisesRegex(ContractError, 'Invalid blocked diagnostic'):
            validate_result(res, req, ROOT)

    def test_complete_rejects_errors(self):
        req = request(); res = result(ROOT, req)
        res['execution_state'] = 'COMPLETA'
        res['errors'] = [{'code':'OTHER','message':'error','affected_ids':[],'action':'retry'}]
        with self.assertRaisesRegex(ContractError, 'Complete execution'):
            validate_result(res, req, ROOT)

    def test_missing_required_method_rejected(self):
        req = request(); res = result(ROOT, req)
        res['rules'][0]['method_results'] = []
        with self.assertRaisesRegex(ContractError, 'Missing required method'):
            validate_result(res, req, ROOT)

    def test_method_na_requires_authorization_and_approved_exception(self):
        import hashlib, tempfile
        req = request(); req['authorization']['methods'] = ['V']
        res = result(ROOT, req)
        row = res['rules'][0]
        row['applicability'] = 'APLICAVEL'
        row['status'] = 'CONFORME'
        with tempfile.TemporaryDirectory() as tmp:
            artifact = Path(tmp) / 'proof'
            artifact.write_text('synthetic')
            digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
            for method, state in [('V','CONFORME'),('I','NAO_APLICAVEL')]:
                eid = 'e-'+method
                res['evidence'].append({'id':eid,'rule_id':row['id'],'method':method,
                    'flow':'fixture','element':'fixture','state':'fixture','steps':['inspect'],
                    'observation':'synthetic','artifact':{'uri':str(artifact),'sha256':digest,'media_type':'text/plain'},
                    'captured_at':'2026-11-18T12:00:00Z','executor':'fixture','method_result':state,
                    'sufficiency':'SUFICIENTE','sufficiency_reason':'synthetic only',
                    'assessor':'fixture','limitations':[]})
            row['method_results'] = [
                {'method':'V','applicability':'APLICAVEL','status':'CONFORME','evidence_ids':['e-V'],'reason':'observed'},
                {'method':'I','applicability':'NAO_APLICAVEL','status':'NAO_APLICAVEL','evidence_ids':['e-I'],'reason':'not applicable'}]
            with self.assertRaisesRegex(ContractError, 'Method not authorized'):
                validate_result(res, req, ROOT)
            req['authorization']['methods'].append('I')
            with self.assertRaisesRegex(ContractError, 'approved exception'):
                validate_result(res, req, ROOT)
            row['exceptions'].append({'rule_id':row['id'],'type':'NAO_APLICABILIDADE',
                'context':'fixture','justification':'approved externally','evidence_ids':['e-I'],
                'approver':'PO','validity':'pilot','review_at':'2027-01-01',
                'impact':'not applicable','approval_state':'APROVADA'})
            validate_result(res, req, ROOT)
