# Agent operating instructions — UI Standards

> **Current additive state (2026-11-18):** The PO subsequently authorized V1 pilot implementation and a limited remediation round on `g2/bootstrap-framework`. Earlier prohibitions below describe historical stages and do not revoke that authorization. G1 normative sources remain immutable; no merge, release, real-project deployment or paid agent execution is authorized. G2 remains open.


Read this file before acting. Applies to Codex, Claude Code and other agents.

## Mission
Build and validate a portable, open-source UI/UX standards framework for administrative and operational web interfaces. This is a normative framework, not a fixed visual design system or a replacement for product business rules.

## Authority and state
- Product Owner (PO) alone approves normative changes, gate closure, publication and scope expansion.
- G1 v0.1.1 was homologated **with controlled caveats** by the PO in the conversation. The original candidate files may still say "CANDIDATA / NÃO HOMOLOGADA": preserve them unchanged; record the later PO decision separately.
- G2 technical discovery is authorized. This is **not** blanket authorization to implement skills, modify norms, merge, publish a release or change product code.
- WCAG 2.2 AA is a target baseline for new web interfaces, not proof of any application's conformance.
- Until the exact G1 source package is committed and checked for integrity, do not claim the normative baseline is installed.

## Workflow — GitHub is the exchange point
1. ChatGPT prepares authorized changes and pushes to a feature/review branch.
2. Local agent fetches the branch in WSL, inspects source and validates within explicitly authorized scope.
3. Local agent commits and pushes evidence, findings and authorized fixes to the same branch (or a clearly linked review branch).
4. ChatGPT inspects the GitHub diff, reports, provenance and outstanding issues.
5. PO decides acceptance. Only approved work enters main.

Never overwrite another agent's work, force-push, silently rebase shared work, merge into main or tag a release without explicit authorization. Before work, record branch, HEAD, dirty state, task scope and source version. Stop on unexpected changes.

## Permission boundary
- Audit and code review are READ-ONLY with respect to the product/framework being audited. Reports may be written only when explicitly authorized.
- Do not modify source, dependencies, business logic, security, infrastructure or central rules as a side effect of review.
- UI implementation requires a separate, explicit task-scoped authorization.
- If a document is missing, conflicting or ambiguous: report the gap; do not fabricate or silently resolve it.
- Preserve normative IDs, content and evidence traceability. Proposed changes are separate from approved source.

## Normative verification
- G1 contains 53 rules: LAY 6, ACT 8, FRM 8, NAV 6, DAT 6, RSP 7, A11Y 7, FDB 5, with 53 associated manual scenarios.
- Methods: S static, V rendered visual, I interaction, F functional.
- Statuses: CONFORME, NAO_CONFORME, NAO_VERIFICADO, NAO_APLICAVEL.
- CONFORME requires sufficient evidence for every applicable required method; missing tests remain NAO_VERIFICADO unless a violation is established. NAO_APLICAVEL needs verifiable justification.
- Never claim tests were run from the existence of a test catalog, or claim WCAG compliance from internal A11Y rules.
- Unsaved changes, bulk operations and pagination are controlled normative backlog, not new v0.1.1 IDs.
- Cross-agent repeatability, complete examples, 53 scenario execution in pilot applications and detailed WCAG checks remain G2/G3 validation items.

## Required output from local validation
Report: objective, scope/authorization, source commit, normative version, environment/tools, checks executed, per-check results, evidence paths, limitations, unresolved issues, files changed, commit SHA and push branch. Separate documentary inspection from runtime/visual/interactive tests.

## First task on this branch
Inspect repository bootstrap and incoming original G1 artifacts; verify completeness, identity, 53 rule/scenario mappings and governance. Do not implement the three skills or claim successful runtime tests unless specifically authorized.

See `docs/WORKFLOW.md` and `docs/PROJECT-STATUS.md`.
