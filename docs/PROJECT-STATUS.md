# UI Standards — project status

**Updated:** 2026-11-18. **Branch:** `g2/bootstrap-framework`.

## Confirmed decisions
- Repository: `DioneNeris/ui-standards`; GitHub is the exchange and verification point for ChatGPT, Codex and Claude Code.
- G1 v0.1.1 **documentarily homologated by PO with controlled caveats**, after the original candidate closing record. See `docs/decisions/2026-11-18-PO-G1-G2-AUDITORIAS.md`.
- G2 technical discovery and controlled documentation remediation authorized; **no implementation of skills, merge to main, or publication authorized**.
- WCAG 2.2 AA is a **target** for new web interfaces, not a product-conformity assertion.

## Current evidence
- Six retrieved candidate-source files committed and preserved; **not** verified byte-for-byte against the absent original source package.
- 53 normative IDs, 53 manual scenarios and 53 matrix records with matching identifiers and documented fields in two independent documentary audits.
- Codex report: `tests/reports/2026-11-18-auditoria-documental-g1.md` (`4321314`).
- Claude Code report: `tests/reports/2026-11-18-auditoria-documental-g1-claude.md` (`c6ff988`).
- Original CSV contains a two-line extraction preamble; a clearly labeled **derived** consumable CSV is provided without modifying the original.
- No pilot execution, detailed external WCAG validation, or runtime skill/adaptor tests.

## Open controlled work
1. Recover source zip and independently compare source hashes and missing files: evidence schema, original README, changelog and scenario catalog CSV.
2. Validate the derived CSV and remediation documentation locally; resolve source provenance.
3. Resolve the exception-type vocabulary and evidence-record precedence before formal skill contracts are accepted.
4. Define and validate G2 contracts and agent discovery; seek separate authorization **before implementation**.
5. Track controlled G2/G3 caveats: evaluator repeatability, positive/negative examples, 53 pilot scenarios, WCAG verification.
6. PO to decide LICENSE and any commit-signing policy separately.

See `docs/BACKLOG-G2-G3.md` and `framework/SOURCE-INVENTORY.md`. G2 **remains open**. No new normative IDs; no automatic merge.
