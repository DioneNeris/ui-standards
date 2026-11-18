#!/usr/bin/env python3
"""Validate the pinned baseline and V1 request/result documents."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from uistandards.core import BaselineError, load_baseline
from uistandards.validation import ContractError, validate_request, validate_result


def main():
    p = argparse.ArgumentParser()
    p.add_argument('kind', choices=('baseline', 'request', 'result'))
    p.add_argument('--package-root', required=True, type=Path)
    p.add_argument('--file', type=Path)
    p.add_argument('--request', type=Path)
    p.add_argument('--json', action='store_true')
    args = p.parse_args()
    try:
        rules = load_baseline(args.package_root)
        if args.kind == 'baseline':
            output = {'status': 'VALID', 'rule_count': len(rules), 'source_provenance': 'NAO_VERIFICADA'}
        else:
            if not args.file:
                raise ContractError('--file is required')
            data = json.loads(args.file.read_bytes())
            if args.kind == 'request':
                validate_request(data, args.package_root)
            else:
                if not args.request:
                    raise ContractError('--request is required')
                raw = args.request.read_bytes()
                validate_result(data, json.loads(raw), args.package_root, raw)
            output = {'status': 'VALID', 'kind': args.kind}
        print(json.dumps(output, ensure_ascii=False))
        return 0
    except BaselineError as exc:
        print(json.dumps({'code': 'BASELINE_INVALID', 'message': str(exc)}), file=sys.stderr)
        return 3
    except (ContractError, ValueError, OSError) as exc:
        print(json.dumps({'code': 'INVALID_REQUEST' if args.kind == 'request' else 'INVALID_RESULT', 'message': str(exc)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
