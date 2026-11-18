# G1 v0.1.1 — source inventory and limitations

This directory set contains **copies of retrieved original candidate documents**, not a rewritten or silently amended specification. The original candidate header says NOT HOMOLOGATED because it predates the PO's subsequent G1 homologation with caveats. See `docs/decisions/G1-REGISTRO-DECISOES-FECHAMENTO-v0.1.1.md` and `docs/PROJECT-STATUS.md`.

## Imported originals
- `framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md`
- `tests/scenarios/G1-CATALOGO-CENARIOS-v0.1.1.md`
- `framework/traceability/G1-MATRIZ-BASELINE-v0.1.1.csv`
- `docs/decisions/G1-REGISTRO-DECISOES-FECHAMENTO-v0.1.1.md`
- `docs/decisions/G1-MAPA-SANEAMENTO-AUDITORIA-v0.1.1.md`
- `docs/decisions/G1-PARECER-FECHAMENTO-v0.1.1-READONLY.md`

## Not yet recovered / not asserted complete
The source package's separate evidence schema, original package README and changelog were not located as independently retrievable files in the current source search. Do **not** invent their contents or claim complete source-package integrity. The G1 baseline CSV is present; the original v0.1.0 traceability files have not been substituted for missing v0.1.1 documents.

## Local agent verification required
1. Compare imported files with authoritative source package, if available, including hashes.
2. Count and cross-check 53 unique normative IDs and 53 corresponding scenarios.
3. Verify baseline CSV rows and source IDs; flag gaps without silently repairing them.
4. Check evidence schema and missing artifacts; mark unverified items `NAO_VERIFICADO`.
5. Preserve G1 caveats: WCAG 2.2 AA target only; scenario catalog is not proof of test execution.
6. Return an evidence-backed report and commit SHA for ChatGPT review.

No skill implementation or product UI test is authorized by this inventory.
