"""Validate schema and semantic links without performing UI actions."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from .core import COMMIT, FILES, aggregate, load_baseline


class ContractError(ValueError):
    pass


def schema_check(value, name, root):
    schema = json.loads((Path(root) / f'schemas/v1/{name}.schema.json').read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(value), key=lambda e: list(map(str, e.path)))
    if errors:
        raise ContractError(f'{name}: {errors[0].json_path}: {errors[0].message}')


def validate_request(request, root):
    schema_check(request, 'request', root)
    load_baseline(root)
    b = request['baseline']
    if b['commit'] != COMMIT or b['hashes'] != {k: FILES[k][1] for k in ('spec', 'matrix_derived', 'scenarios')}:
        raise ContractError('Baseline does not match pinned package')
    a = request['authorization']
    if any(request['environment'][x] is None for x in ('browser','device','viewport','zoom')) and not request['environment_limitations']:
        raise ContractError('Unknown environment requires limitations')
    if request['output']['delivery'] == 'inline' and request['output']['path'] is not None:
        raise ContractError('Inline output has a path')
    if request['output']['delivery'] == 'file':
        p = request['output']['path']
        if not p or 'write_report' not in a['operations'] or p not in a['writable_paths']:
            raise ContractError('OUTPUT_UNAUTHORIZED')
    if request['skill'] in ('ui-audit', 'ui-code-review') or request['mode'] == 'plan':
        if set(a['operations']) - {'read', 'write_report'}:
            raise ContractError('Read-only mode has write operation')
        allowed = [request['output']['path']] if request['output']['delivery'] == 'file' else []
        if set(a['writable_paths']) != set(allowed):
            raise ContractError('Read-only mode has writable product paths')
    if request['mode'] == 'implement' and ('implement' not in a['operations'] or not a['writable_paths']):
        raise ContractError('AUTHORIZATION_MISSING')
    return request


def validate_result(result, request, root, request_bytes=None):
    schema_check(result, 'result', root)
    validate_request(request, root)
    rules = load_baseline(root)
    if result['skill'] != request['skill'] or result['mode'] != request['mode'] or result['target'] != request['target'] or result['environment'] != request['environment'] or result['authorization_ref'] != request['authorization']['reference'] or result['scope'] != request['target']['scope']:
        raise ContractError('Result does not match request')
    if request_bytes is not None and result['request_ref'] != hashlib.sha256(request_bytes).hexdigest():
        raise ContractError('Request hash differs')
    for key in ('repository','commit','version','hashes'):
        if result['baseline'][key] != request['baseline'][key]:
            raise ContractError('Result baseline differs')
    if result['baseline']['repository_integrity'] != 'VERIFICADA' or result['baseline']['source_provenance'] != 'NAO_VERIFICADA' or result['baseline']['approval_state'] != 'HOMOLOGADA_COM_RESSALVAS':
        raise ContractError('Unsupported baseline status')
    if not result['limitations']:
        raise ContractError('Source provenance limitation missing')
    if result['skill'] in ('ui-audit','ui-code-review') and result['changed_files']:
        raise ContractError('Read-only changed_files must be empty')
    for key in ('started_at','finished_at'):
        if not result[key].endswith('Z'):
            raise ContractError('Time must be UTC')
    if datetime.fromisoformat(result['finished_at'].replace('Z','+00:00')) < datetime.fromisoformat(result['started_at'].replace('Z','+00:00')):
        raise ContractError('End precedes start')
    items = result['rules']
    if len(items) != 53 or len({r['id'] for r in items}) != 53 or {r['id'] for r in items} != set(rules):
        raise ContractError('Expected 53 unique rules')
    evidence = {e['id']: e for e in result['evidence']}
    if len(evidence) != len(result['evidence']):
        raise ContractError('Duplicate evidence')
    for entry in result['evidence']:
        if entry['rule_id'] not in rules:
            raise ContractError('Evidence references unknown rule')
        if entry['artifact'] is None and not entry['limitations']:
            raise ContractError('Missing artifact needs limitation')
        try:
            captured = datetime.fromisoformat(entry['captured_at'].replace('Z', '+00:00'))
            if captured.tzinfo is None:
                raise ValueError('timezone missing')
        except ValueError as exc:
            raise ContractError('Invalid evidence timestamp') from exc
    def proof(eid, rule_id, method, status):
        e = evidence.get(eid)
        if not e or e['rule_id'] != rule_id or e['method'] != method or e['method_result'] != status or e['sufficiency'] != 'SUFICIENTE' or not e['artifact']:
            raise ContractError('EVIDENCE_INSUFFICIENT')
        artifact = e['artifact']
        path = Path(artifact['uri'])
        if not path.is_absolute() or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != artifact['sha256']:
            raise ContractError('Artifact absent or hash mismatch')
    for rule in items:
        rid = rule['id']; baseline = rules[rid]
        if rule['scenario_id'] != baseline['scenario_id'] or rule['required_methods'] != baseline['methods']:
            raise ContractError('Rule differs from baseline')
        method_results = rule['method_results']
        if len({m['method'] for m in method_results}) != len(method_results):
            raise ContractError('Duplicate method')
        statuses = {}
        for item in method_results:
            m, state = item['method'], item['status']
            if (m not in baseline['methods']) != item.get('additional', False):
                raise ContractError('Additional method not marked')
            if state in ('CONFORME','NAO_CONFORME') and item['applicability'] != 'APLICAVEL':
                raise ContractError('Determinate status requires applicable method')
            if state in ('CONFORME','NAO_CONFORME') and m not in request['authorization']['methods']:
                raise ContractError('Method not authorized')
            if (state == 'NAO_APLICAVEL') != (item['applicability'] == 'NAO_APLICAVEL'):
                raise ContractError('Method applicability inconsistent')
            if state in ('CONFORME','NAO_CONFORME','NAO_APLICAVEL'):
                if not item['evidence_ids']:
                    raise ContractError('EVIDENCE_INSUFFICIENT')
                for eid in item['evidence_ids']:
                    proof(eid, rid, m, state)
            elif any(eid not in evidence for eid in item['evidence_ids']):
                raise ContractError('Unknown evidence')
            statuses[m] = state
        for exc in rule['exceptions']:
            if exc['type'] == 'CONFLITO_BLOQUEANTE' and rule['status'] in ('CONFORME', 'NAO_APLICAVEL'):
                raise ContractError('Blocking conflict cannot conclude conformity')
            if exc['rule_id'] != rid or any(eid not in evidence or evidence[eid]['rule_id'] != rid for eid in exc['evidence_ids']):
                raise ContractError('Invalid exception')
            if exc['approval_state'] == 'APROVADA' and (not exc['approver'] or not exc['validity'] or not exc['review_at'] or not exc['evidence_ids']):
                raise ContractError('EXCEPTION_UNAPPROVED')
        if rule['applicability'] == 'NAO_APLICAVEL':
            na = [x for x in rule['exceptions'] if x['type'] == 'NAO_APLICABILIDADE' and x['approval_state'] == 'APROVADA' and x['evidence_ids']]
            if not na:
                raise ContractError('N/A needs justified evidence')
            for eid in na[0]['evidence_ids']:
                e = evidence[eid]
                proof(eid, rid, e['method'], 'NAO_APLICAVEL')
        expected = aggregate(rule['applicability'], baseline['methods'], statuses)
        if rule['status'] != expected:
            raise ContractError(f'GOV-004 mismatch for {rid}: expected {expected}')
    for f in result['findings']:
        if f['rule_id'] not in rules or not f['evidence_ids'] or any(eid not in evidence or evidence[eid]['rule_id'] != f['rule_id'] or evidence[eid]['method'] != f['method'] for eid in f['evidence_ids']):
            raise ContractError('Finding has invalid references')
    return result
