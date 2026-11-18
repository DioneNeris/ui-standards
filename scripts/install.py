#!/usr/bin/env python3
"""Install narrow, project-local skill pointers without overwriting user files."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from uistandards.core import COMMIT, BaselineError, load_baseline

SKILLS = ('ui-design', 'ui-audit', 'ui-code-review')
ROOTS = {'codex': '.agents/skills', 'claude': '.claude/skills'}


def adapter(package, skill):
    return (f'---\nname: {skill}\ndescription: Use when applying the {skill} UI Standards workflow.\n---\n\n'
            f'<!-- ui-standards-generated-v1; baseline-commit={COMMIT} -->\n'
            f'Package root: `{package}`\n\nRead `{package}/skills/{skill}/SKILL.md`, '
            f'`{package}/skills/shared/CONTRACT.md`, and the contract referenced there before acting. '
            'Validate the pinned package baseline; stop on any validation failure.\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--package-root', required=True, type=Path)
    parser.add_argument('--project-root', required=True, type=Path)
    parser.add_argument('--agents', required=True)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    package, project = args.package_root.resolve(), args.project_root.resolve()
    agents = args.agents.split(',')
    if not project.is_dir() or not agents or len(set(agents)) != len(agents) or any(a not in ROOTS for a in agents):
        parser.error('invalid project or agents')
    try:
        load_baseline(package)
    except BaselineError as exc:
        print(json.dumps({'code': 'BASELINE_INVALID', 'message': str(exc)}), file=sys.stderr)
        return 3
    planned = []
    for agent in agents:
        for skill in SKILLS:
            path = project / ROOTS[agent] / skill / 'SKILL.md'
            if not path.resolve().is_relative_to(project) or any(p.is_symlink() for p in [path, *path.parents] if p != project and p.is_relative_to(project)):
                print(json.dumps({'code': 'INSTALL_CONFLICT', 'message': str(path)}), file=sys.stderr)
                return 4
            content = adapter(package, skill)
            if path.exists() and (not path.is_file() or path.read_text() != content):
                print(json.dumps({'code': 'INSTALL_CONFLICT', 'message': str(path)}), file=sys.stderr)
                return 4
            planned.append((path, content))
    try:
        if not args.dry_run:
            for path, content in planned:
                path.parent.mkdir(parents=True, exist_ok=True)
                if not path.exists():
                    with path.open('x', encoding='utf-8') as output:
                        output.write(content)
    except OSError as exc:
        print(json.dumps({'code': 'INSTALL_CONFLICT', 'message': str(exc)}), file=sys.stderr)
        return 4
    print(json.dumps({'status': 'DRY_RUN' if args.dry_run else 'INSTALLED', 'paths': [str(p) for p, _ in planned]}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
