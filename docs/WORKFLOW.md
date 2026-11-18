# Collaboration and validation workflow

Repository: https://github.com/DioneNeris/ui-standards
Current working branch: `g2/bootstrap-framework`
Local WSL target: `/home/dione/projects/ui-standards`

## Local agent: preparation
```bash
mkdir -p /home/dione/projects
cd /home/dione/projects
git clone https://github.com/DioneNeris/ui-standards.git  # only if not cloned
cd ui-standards
git fetch origin
git switch g2/bootstrap-framework
git status --short
git rev-parse HEAD
```
If the directory exists, do not reclone or reset. Inspect its state and fetch safely. Do not discard local changes.

## Validation protocol
1. Read `AGENTS.md`, `docs/PROJECT-STATUS.md`, and authoritative G1 originals when present.
2. Inventory files and compare committed originals with supplied source artifacts; record hashes where possible.
3. Check 53 stable rule IDs and one-to-one scenario mapping; inspect baseline, decision records and caveats.
4. Check cross-document consistency, status semantics and evidence schema.
5. If expressly authorized and tooling exists, test agent discovery and skill contracts. Do not treat a static check as visual/interactive validation.
6. Write a report under `tests/reports/` **only when report creation is authorized**. State NOT VERIFIED for unexecuted checks.
7. Commit only authorized files, push, and send branch + commit SHA for ChatGPT review.

Example commit workflow (only after checking scope and diff):
```bash
git diff --check
git status --short
git diff --stat
git add <explicitly-authorized-paths>
git commit -m "test: document G2 validation findings"
git push origin g2/bootstrap-framework
```

## Review and acceptance
ChatGPT reviews pushed commits and findings against normative originals; does not infer success from a green commit or agent assertion. PO approves changes and any merge into main. Never merge automatically.

## Safety
Do not commit secrets, credentials, customer data, screenshots with personal data, or local machine identifiers. Do not install tools or change dependencies without approval. Do not use force push.
