# Remediação integrada pós-auditoria — 2026-11-18

**Escopo autorizado pelo PO:** correções técnicas na branch de trabalho, sem merge, sem alterações normativas G1, sem credenciais e sem chamadas pagas de agentes.

## Implementado

- AUD-02: métodos requeridos marcados NAO_APLICAVEL exigem autorização de método, evidência e exceção contextual NAO_APLICABILIDADE APROVADA vinculada à evidência. A declaração de aprovação continua exigindo conferência humana independente; texto livre não autentica o aprovador.
- AUD-03/AUD-04 (parcial): ui-design/plan não aceita changed_files; implement exige changed_files dentro de writable_paths relativos, sem traversal e sem escrita em caminhos reservados do pacote.
- AUD-05/AUD-06 (parcial): BLOQUEADA só com rules vazias, sem findings/evidence/changed_files/artifacts, com erro e limitação; verificações de identidade, baseline e datas; COMPLETA não admite errors.
- AUD-08: todas as regras devem listar exatamente um resultado por método requerido; fixtures e piloto sintético atualizados.
- AUD-12 (parcial): regressões explícitas para caminhos inseguros, escopo, bloqueio, cobertura de métodos e N/A.
- AUD-10: notas de estado aditivas em AGENTS, contrato candidato e PROJECT-STATUS; texto histórico preservado.
- AUD-01: o preflight descartável sem agentes foi incluído como job separado no workflow CI de push da branch, sem publicar workflow na main. O arquivo workflow_dispatch separado permanece somente preparatório e não foi executado.
- AUD-18: mecanismo proposto para o piloto real: container com pacote e fixture montados somente leitura, saída isolada gravável. **Não implementado nem testado nesta rodada.**

## Pendências explícitas

AUD-07 (aprovação externa e validade temporal das exceções), AUD-09 (evidências portáveis, limites de leitura e janela temporal), AUD-11 (tratamento de erros do CLI e ambiente), AUD-12 (cobertura integral de ramos), AUD-13–17 e AUD-18 permanecem sem comprovação completa. O registro de aprovação de exceções é declarativo, não um controle de identidade. A autorização do PO não inclui execução de agentes reais nem ui-design/implement em produto real.

## Gate

Os commits foram publicados via GitHub. **Nenhuma execução local dos testes ou CI foi observada nesta sessão.** A validação exige conferir o run posterior ao commit deste relatório, seus dois jobs (contratos e preflight descartável), artefatos e hashes. Mesmo CI verde não comprova isolamento de SO nem homologação V1.
