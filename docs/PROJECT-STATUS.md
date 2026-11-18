# UI Standards — project status

## Confirmed
- Name/repository: `ui-standards`; public GitHub repository `DioneNeris/ui-standards`.
- GitHub is the collaboration and verification handoff between ChatGPT and local Codex/Claude Code.
- G1 v0.1.1 **homologated by PO with caveats** after the candidate and documentary closing records were written.
- Normative scope: 53 rules across eight domains, 53 manual scenarios; WCAG 2.2 AA as target baseline for new web UI.
- Initial G2: technical discovery/contracts for `ui-design`, `ui-audit`, `ui-code-review`; no blanket implementation approval.
- Branch `g2/bootstrap-framework` created after README bootstrap on main.

## This branch
- Bootstrap agent instructions and collaboration protocol.
- **Normative G1 source package not yet committed/verified here.** Original candidate documents and the later PO homologation must be kept distinct.
- No skills, adapters or pilot runtime tests implemented by this documentation step.

## Pending controlled work
1. Commit original G1 v0.1.1 specification, scenario catalog, baseline matrix, evidence schema, decisions and provenance without silently rewriting originals.
2. Validate integrity, 53 IDs, scenario coverage, references and caveats; record discrepancies.
3. Finalize technical skill/adaptor contracts and test strategy; seek PO authorization before implementation.
4. Validate Codex/Claude locally, return evidence by push, then independent GitHub review.
5. PO decision on acceptance, main merge and future release.

## Guardrails
- Never confuse candidate document header with later PO approval, or treat G1 documentary homologation as application conformance.
- Read-only audits, evidence-first status, explicit PO gate decisions.
- Controlled backlog: unsaved changes, bulk actions, pagination.
- No new normative IDs or silent rule changes in v0.1.1.
