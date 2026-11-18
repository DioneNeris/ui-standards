# Validação complementar V1 — ensaios de integração no Claude Code

**Data:** 2026-11-18. **Branch:** `g2/bootstrap-framework`. **Commit de partida:** `fe7f06af2c86e076bbe22a81433d367ca5a7497c` (árvore limpa, igual ao remoto). **Norma:** G1 v0.1.1, baseline fixada `ffc75647ccadcf71b51437bcbe9eb63c0039efc7`. **Autorização:** o PO autorizou na conversa o compartilhamento controlado com o serviço Claude dos arquivos técnicos necessários aos ensaios de integração da V1. Essa autorização não cobre alterar normas, modificar projetos reais ou fazer merge. Este relatório complementa `2026-11-18-validacao-v1-piloto.md` e não reescreve os veredictos dele.

**Estado: V1 continua NÃO PLENAMENTE VALIDADA.** Os ensaios aprovados no Claude não encerram as pendências de isolamento read-only nem de instalação reproduzível.

## Ambiente e método

- Claude Code 2.1.327 (modelo `claude-opus-5-5`), Codex CLI 0.170.0 (não reexecutado), Python 3.14.4, jsonschema 4.19.2, Linux WSL2.
- Projeto descartável no scratchpad da sessão, com fixture sintética `app/cadastro.html` em repositório git próprio. Base `9e77682` e head `62a2426`. No head foram plantadas duas violações detectáveis estaticamente: campo identificado só por placeholder (FRM-003) e botão só com ícone, sem nome acessível (A11Y-003). Há cópias em `evidence/2026-11-18-claude-v1/fixture/`.
- Adaptadores instalados com `scripts/install.py --agents claude` (dry-run, instalação e reexecução idempotente com rc=0). Também foi feita a reexecução idempotente em `/tmp/ui-standards-v1-pilot` para `codex,claude`, com rc=0 e nenhuma escrita.
- Cada ensaio é uma sessão aninhada, executada em sequência, com o comando `claude -p … --output-format stream-json --verbose --setting-sources project --strict-mcp-config --no-session-persistence --add-dir <pacote> --add-dir <inputs>`.
  - Ferramentas permitidas: `Read`, `Glob`, `Grep`, `Skill` e Bash restrito a `validate.py`, `git rev-parse|merge-base|cat-file` (pacote), `git diff|show|log` (fixture), `sha256sum` e `date -u`.
  - Ferramentas negadas: `Edit`, `Write`, `NotebookEdit`, `WebFetch`, `WebSearch` e `Agent`.
  - Variável de ambiente `PYTHONDONTWRITEBYTECODE=1`.
  - Não houve bypass de permissões nem `acceptEdits`.
- O evento `init` confirmou `mcp_servers=[]` e somente plugins builtin, sem plugins nem MCP do usuário. Arquivos compartilhados com o serviço: o pacote técnico (skills, contrato, schemas, scripts, spec/matriz/catálogo G1), a fixture e os requests sintéticos.
- O executor aninhado é do mesmo fornecedor e modelo do agente local, portanto **não é avaliador independente**.

## Resultados

| # | Verificação | Resultado | Evidência e limites |
|---|---|---|---|
| 1 | Descoberta das 3 skills no Claude Code | PASS | O `init` lista `ui-audit`, `ui-code-review` e `ui-design` em `skills` e `slash_commands` (run-01). As skills foram invocadas por `/ui-audit` e `/ui-code-review` (runs 02–04). `/ui-design` foi descoberta, mas não invocada (item 5). |
| 2 | Baseline compartilhada | PASS (Claude) | Nos runs 03 e 04 o agente executou `validate.py baseline --json` e obteve `VALID`, 53 regras. Também executou `validate.py request`, conferiu `merge-base --is-ancestor ffc7564 HEAD` e confirmou os hashes. A mesma validação executada fora da sessão deu o mesmo resultado. |
| 3a | Fluxo `ui-audit` tentativa 1 (run-02) | FALHA DE HARNESS, comportamento correto | A allowlist que configurei exigia caminho absoluto e o agente usou caminho relativo, então a validação da baseline foi negada. O agente parou com `BLOQUEADA`, `rules=[]` e erros estruturados, sem conclusões normativas. O validador **rejeitou** esse resultado (`Result does not match request`), ver achado A1. Arquivo: `result-audit-attempt1.json`. |
| 3b | Fluxo `ui-audit` (run-03) | PASS | `validate.py result` deu `VALID` e `report.py` rc=0. Resultado: `PARCIAL`, 53 regras, 3 `NAO_CONFORME` (FRM-003, A11Y-003, ACT-004) com evidência S, artefato e SHA-256, e 50 `NAO_VERIFICADO`. As duas violações plantadas foram detectadas. Cinco métodos S foram marcados CONFORME, mas a regra permaneceu NAO_VERIFICADO porque faltam V/I, como manda GOV-004. Zero negações de permissão. A tentativa 2 é uma reexecução após correção da allowlist, não edição do JSON. |
| 3c | Fluxo `ui-code-review` (run-04) | PASS | `VALID`. Resultado: `PARCIAL`, 53 regras, os mesmos 3 `NAO_CONFORME` e 4 evidências. O relatório foi renderizado. |
| 3d | Fluxo `ui-design` (plan) | NAO_VERIFICADO | O run-05 foi interrompido pelo limite de uso do serviço: `is_error=true`, nenhuma ferramenta executada, nenhum resultado. O request está validado e preservado em `request-design.json`. |
| 4 | Relatórios rastreáveis | PASS (audit, review) | `report-audit.md` e `report-review.md` trazem `run_id`, baseline, SHA-256 do request, autorização, status por regra, evidências e achados. O envio inline impede que o agente valide a própria saída: a validação foi feita de fora (achado A3). |
| 5 | Read-only (nível de arquivo) | Sem alteração observada; isolamento NAO_VERIFICADO | Os manifestos SHA-256 da fixture e do pacote, e o `git status`, ficaram idênticos antes e depois de cada run (snapshots 00, 02, 03, 04, 05). Comandos fora da allowlist foram negados (`permission_denials` no run-02). Isto não é teste adversarial de sandbox. A sessão gravou tool-results e um diretório de memória em `~/.claude/projects/…`, fora do produto, mesmo com `--no-session-persistence`. |
| 6 | Comparação com Codex | Assimétrica; sem paridade | O ensaio registrado do Codex cobre descoberta e validação da baseline, sem fluxo request/result. O Claude agora tem fluxos completos validados para audit e review. Os achados do Codex não podem ser comparados porque não há resultado do Codex. Codex não foi reexecutado (fora do escopo). |
| 7 | Instalação reproduzível (venv, pip, lock) | NAO_VERIFICADO | Não exercitada. |

## Achados (sem correção aplicada; exigem decisão)

- **A1 — validador rejeita um BLOQUEADA legítimo.** `validate_result` só aceita diagnóstico `BLOQUEADA` quando a baseline local é inválida. Quando o executor não consegue validar por restrição do ambiente, a baseline local passa e o resultado bloqueado é avaliado como completo. A rejeição ocorre já por `scope ≠ target.scope`, e o resultado também falharia na exigência de 53 regras. O contrato §3.2 permite `rules=[]` com BLOQUEADA quando a baseline está indisponível ao executor.
- **A2 — ambiguidade no adaptador.** O comentário `baseline-commit=ffc7564` levou o agente, sem a CLI, a tratar como conflito o fato de HEAD (`fe7f06a`) ser diferente do commit fixado. O carregador compara blobs do commit fixado, então HEAD diferente é esperado. A documentação deve dizer isso explicitamente.
- **A3 — auto-validação impossível com saída inline.** O agente não consegue executar `validate.py result` sobre a própria saída sem escrita. Opções: aceitar stdin no validador ou autorizar um destino temporário. Isso exige decisão.
- **A4 — permissões por padrão textual são frágeis.** Padrões `Bash(...)` dependem da forma exata do comando (absoluto ou relativo, encadeamento). Foi preciso instruir o agente a usar "um comando por chamada".

## Limitações

Fixture sintética de um arquivo, somente método S. Não houve UI renderizada, navegador, WCAG nem execução dos 53 cenários. O julgamento de suficiência foi feito pelo próprio agente. Os URIs de artefato são absolutos no scratchpad da sessão, então a revalidação dos resultados só se reproduz recriando a fixture no mesmo caminho. Transcripts brutos não foram commitados (podem conter o ambiente local); os hashes deles estão em `evidence/2026-11-18-claude-v1/raw-sha256.txt`. Custo aproximado dos runs: US$ 2,65.

## Arquivos alterados

Este relatório e `tests/reports/evidence/2026-11-18-claude-v1/` (requests, results, relatórios renderizados, diff, fixture e hashes). Nenhuma norma, script, skill ou projeto real foi alterado. Não houve merge. O SHA final é informado no retorno ao PO.
