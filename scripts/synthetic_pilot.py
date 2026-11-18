#!/usr/bin/env python3
"""Deterministic synthetic contract pilot; DOES NOT invoke Codex or Claude agents."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests/contracts"))
from fixtures import request, result

CASES = (("ui-design", "plan"), ("ui-audit", "audit"), ("ui-code-review", "review"))


def invoke(*args):
    completed = subprocess.run([sys.executable, *map(str, args)], cwd=ROOT,
                               capture_output=True, text=True)
    if completed.returncode:
        raise RuntimeError(f"command failed ({completed.returncode}): {completed.stderr}")
    return completed.stdout


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: synthetic_pilot.py OUTPUT_DIRECTORY")
    output = Path(sys.argv[1]).resolve()
    output.mkdir(parents=True, exist_ok=True)
    records = []
    for skill, mode in CASES:
        req = request()
        req["skill"], req["mode"] = skill, mode
        if skill == "ui-design":
            req["design"] = {"artifacts": [], "constraints": []}
        if skill == "ui-code-review":
            req["review"] = {"base": "synthetic-base", "head": "synthetic-head",
                             "diff_scope": "synthetic-only"}
        raw = (json.dumps(req, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()
        res = result(ROOT, req)
        res["request_ref"] = hashlib.sha256(raw).hexdigest()
        res["executor"] = "synthetic-contract-fixture (NOT an AI agent)"
        res["limitations"].append("No agent invocation; no UI observation or isolation test")
        req_path = output / f"{skill}.request.json"
        res_path = output / f"{skill}.result.json"
        report_path = output / f"{skill}.report.md"
        req_path.write_bytes(raw)
        res_path.write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n")
        invoke(ROOT / "scripts/validate.py", "request", "--package-root", ROOT,
               "--file", req_path)
        invoke(ROOT / "scripts/validate.py", "result", "--package-root", ROOT,
               "--file", res_path, "--request", req_path)
        report_path.write_text(invoke(ROOT / "scripts/report.py", "--package-root", ROOT,
                                      "--request", req_path, "--result", res_path))
        records.append({"skill": skill, "mode": mode, "contract_validation": "PASS",
                        "agent_execution": "NAO_VERIFICADO",
                        "rule_count": len(res["rules"]),
                        "files": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in (req_path, res_path, report_path)}})
    manifest = {"pilot_type": "SYNTHETIC_CONTRACT_ONLY",
                "agent_execution": "NAO_VERIFICADO",
                "read_only_isolation": "NAO_VERIFICADO",
                "cases": records}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
