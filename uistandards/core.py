"""Load a pinned G1 snapshot and aggregate method results."""
import collections
import csv
import hashlib
import io
import re
import subprocess
from pathlib import Path

COMMIT = 'ffc75647ccadcf71b51437bcbe9eb63c0039efc7'
FILES = {
    'spec': ('framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md', '4b5f2c33f8545c9a1bb8d3fa627fe1a2c76ebab4f964b96153099f64590ab39a'),
    'scenarios': ('tests/scenarios/G1-CATALOGO-CENARIOS-v0.1.1.md', '37c6d84ef09e534043e78be29383fce234186bdd332163535b273af5bd604be3'),
    'original': ('framework/traceability/G1-MATRIZ-BASELINE-v0.1.1.csv', '0a1042c7eb6f1526b78449a747c5317ae8d4829ed7b0844f68c85d8b852ca101'),
    'matrix_derived': ('framework/traceability/derived/G1-MATRIZ-BASELINE-v0.1.1-normalizada.csv', '523c8f31b35f157951cb374ef3b72d26c18f78c52e9b78ce414f2836b8d90e7e'),
}


class BaselineError(ValueError):
    pass


def load_baseline(root):
    root = Path(root).resolve()
    data = {}
    for name, (path, expected) in FILES.items():
        try:
            content = (root / path).read_bytes()
            blob = subprocess.run(['git', '-C', str(root), 'show', f'{COMMIT}:{path}'], check=True, capture_output=True).stdout
        except (OSError, subprocess.CalledProcessError) as exc:
            raise BaselineError(f'Fonte ausente: {path}') from exc
        if hashlib.sha256(content).hexdigest() != expected or content != blob:
            raise BaselineError(f'Hash ou conteúdo divergente: {path}')
        data[name] = content
    original = b''.join(data['original'].splitlines(keepends=True)[2:])
    if original + (b'' if original.endswith(b'\n') else b'\n') != data['matrix_derived']:
        raise BaselineError('Derivação da matriz divergente')
    rows = list(csv.DictReader(io.StringIO(data['matrix_derived'].decode('utf-8'), newline=''), strict=True))
    expected_header = ['index', 'id', 'dominio', 'nivel', 'requisito', 'criterio_aceitacao', 'metodos_requeridos', 'excecoes', 'caso_teste', 'wcag_relacionada', 'status_normativo', 'tipo_excecao']
    if len(rows) != 53 or any(list(r) != expected_header or None in r.values() for r in rows):
        raise BaselineError('Matriz inválida')
    spec = data['spec'].decode()
    catalog = data['scenarios'].decode()
    blocks = {m.group(1): m for m in re.finditer(r'^### ([A-Z0-9]+-\d{3}) — ([^\n]+)\n(.*?)(?=^### |^## |\Z)', spec, re.M | re.S)}
    scenarios = {m.group(1): m for m in re.finditer(r'^## TC-([A-Z0-9]+-\d{3}) — ([A-Z0-9]+-\d{3})\n(.*?)(?=^## |\Z)', catalog, re.M | re.S) if m.group(1) == m.group(2)}
    rules = {}
    for i, row in enumerate(rows):
        ident = row['id']
        methods = row['metodos_requeridos'].split(',')
        block, scenario = blocks.get(ident), scenarios.get(ident)
        if ident in rules or row['index'] != str(i) or not block or not scenario or row['caso_teste'] != 'TC-' + ident or not methods or len(set(methods)) != len(methods) or not set(methods) <= set('SVIF'):
            raise BaselineError(f'ID ou métodos inválidos: {ident}')
        def field(text, label):
            match = re.search(r'\*\*' + re.escape(label) + r':\*\*\s*([^\n]+)', text)
            return match.group(1).strip() if match else None
        body, sc = block.group(3), scenario.group(3)
        if (block.group(2) != row['requisito'] or field(body, 'Nível') != row['nivel'] + ' (interno; candidato)' or field(body, 'Critério') != row['criterio_aceitacao'] or field(body, 'Métodos requeridos') != row['metodos_requeridos'] or field(sc, 'Resultado esperado') != row['criterio_aceitacao'] or field(sc, 'Métodos') != row['metodos_requeridos'] or field(body, 'Caso manual') != row['caso_teste'] + ' (ver catálogo de cenários).' or field(body, 'Observável/protocolo') != field(sc, 'Passos')):
            raise BaselineError(f'Inconsistência na regra {ident}')
        rules[ident] = {'id': ident, 'scenario_id': row['caso_teste'], 'methods': methods, 'requirement': row['requisito'], 'criterion': row['criterio_aceitacao'], 'exception': row['excecoes'], 'spec_line': spec[:block.start()].count('\n') + 1, 'scenario_line': catalog[:scenario.start()].count('\n') + 1}
    if len(blocks) != 53 or len(scenarios) != 53 or set(rules) != set(blocks) or set(rules) != set(scenarios) or collections.Counter(x.split('-')[0] for x in rules) != {'LAY': 6, 'ACT': 8, 'FRM': 8, 'NAV': 6, 'DAT': 6, 'RSP': 7, 'A11Y': 7, 'FDB': 5}:
        raise BaselineError('Conjuntos normativos divergentes')
    return rules


def aggregate(applicability, required, statuses):
    if 'NAO_CONFORME' in statuses.values():
        return 'NAO_CONFORME'
    if applicability == 'NAO_APLICAVEL':
        return 'NAO_APLICAVEL'
    if applicability != 'APLICAVEL' or any(statuses.get(m) not in ('CONFORME', 'NAO_APLICAVEL') for m in required):
        return 'NAO_VERIFICADO'
    return 'CONFORME' if any(statuses.get(m) == 'CONFORME' for m in required) else 'NAO_VERIFICADO'
