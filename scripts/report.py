#!/usr/bin/env python3
"""Render validated JSON as Markdown on stdout; never write files."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from uistandards.core import BaselineError
from uistandards.report import render_report
from uistandards.validation import ContractError


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--package-root', required=True, type=Path)
    p.add_argument('--request', required=True, type=Path)
    p.add_argument('--result', required=True, type=Path)
    a = p.parse_args()
    try:
        raw = a.request.read_bytes()
        print(render_report(json.loads(a.result.read_bytes()), json.loads(raw), a.package_root, raw), end='')
    except (OSError, ValueError, ContractError, BaselineError) as exc:
        print(json.dumps({'code':'INVALID_RESULT','message':str(exc)}), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
