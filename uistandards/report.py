"""Render a validated result without changing project files."""
from .validation import validate_result


def render_report(result, request, root, request_bytes=None):
    validate_result(result, request, root, request_bytes)
    safe = lambda value: str(value).replace('|', '\\|').replace('\n', ' ')
    lines = ['# UI Standards — relatório', '',
             f"Execução: `{safe(result['run_id'])}`; skill: `{safe(result['skill'])}`; estado: `{safe(result['execution_state'])}`.",
             f"Baseline: `{safe(result['baseline']['commit'])}`; proveniência: `{safe(result['baseline']['source_provenance'])}`.",
             f"Escopo: {safe(result['scope'])}; alvo: {safe(result['target']['project'])} @ {safe(result['target']['revision'])}; executor: {safe(result['executor'])}.",
             f"Request SHA-256: `{safe(result['request_ref'])}`; autorização: {safe(result['authorization_ref'])}.", '', '| Norma | Cenário | Resultado | Métodos |', '|---|---|---|---|']
    for rule in result['rules']:
        methods = ', '.join(f"{m['method']}={m['status']}" for m in rule['method_results']) or 'nenhum executado'
        lines.append(f"| {safe(rule['id'])} | {safe(rule['scenario_id'])} | {safe(rule['status'])} | {safe(methods)} |")
    lines += ['', '## Limitações', ''] + [f'- {safe(item)}' for item in result['limitations']]
    lines += ['', '## Evidências', ''] + [f"- {safe(e['id'])}: {safe(e['rule_id'])}/{safe(e['method'])}, {safe(e['observation'])}; artefato: {safe(e['artifact']['uri'] if e['artifact'] else 'ausente')}; SHA-256: {safe(e['artifact']['sha256'] if e['artifact'] else 'ausente')}." for e in result['evidence']]
    lines += ['', '## Achados', ''] + [f"- {safe(f['id'])} ({safe(f['rule_id'])}/{safe(f['method'])}): {safe(f['observation'])}; evidências: {safe(', '.join(f['evidence_ids']))}." for f in result['findings']]
    lines += ['', '## Exceções', ''] + [f"- {safe(r['id'])}: {safe(e['type'])}, {safe(e['approval_state'])}, {safe(e['justification'])}." for r in result['rules'] for e in r['exceptions']]
    return '\n'.join(lines) + '\n'
