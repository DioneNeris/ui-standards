# G1 v0.1.1 — source inventory and limitations

Six original candidate-document **copies** were imported into `g2/bootstrap-framework`. Their original historical headers are unchanged, including “CANDIDATA / NÃO HOMOLOGADO”. The **later** PO G1 homologation with caveats and G2 authorization are recorded separately in `docs/decisions/2026-11-18-PO-G1-G2-AUDITORIAS.md`; this record is secondary to the conversation, not independent provenance.

## Imported copies — preserved
- `framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md`
- `tests/scenarios/G1-CATALOGO-CENARIOS-v0.1.1.md`
- `framework/traceability/G1-MATRIZ-BASELINE-v0.1.1.csv`
- `docs/decisions/G1-REGISTRO-DECISOES-FECHAMENTO-v0.1.1.md`
- `docs/decisions/G1-MAPA-SANEAMENTO-AUDITORIA-v0.1.1.md`
- `docs/decisions/G1-PARECER-FECHAMENTO-v0.1.1-READONLY.md`

## Derived, not original
- `framework/traceability/derived/G1-MATRIZ-BASELINE-v0.1.1-normalizada.csv`: original matrix with **only the first two extraction-wrapper lines removed**, and final newline ensured. The original has a non-CSV preamble; use the derived file for automated CSV parsing, but do not confuse it with a recovered source. Validate any downstream contract against its header and 53 rows.

## Missing / unverified original package items
- Source ZIP / independent source hashes, so identity with the authoritative source is **NAO_VERIFICADO**.
- Separate machine-readable evidence schema.
- Original package README.
- Original changelog.
- **Scenario catalog CSV**, referenced by the documentary closing opinion; the available Markdown catalog is not proof of equivalence.

Do not fabricate absent originals or substitute v0.1.0 files for v0.1.1. The original evidence model exists in prose in §3 of the specification but is not proof of a separate schema file.

## Documentary verification
Two independent reports (Codex `4321314`, Claude `c6ff988`) found 53 matching rule IDs, 53 scenarios and 53 matrix rows. Neither report proves original-package authenticity, product conformance, execution of scenarios, or functioning skills. See `tests/reports/`.

**Next:** recover and compare source package; validate derived CSV; resolve remaining evidence and contract decisions. No skill implementation or merge is authorized.
