# Piloto real Codex/Claude — protocolo de preparação (2026-11-18)

**Status: PREPARADO; NÃO EXECUTADO; SEM CHAMADAS PAGAS.** Autorização do PO limitada a preparar workflow manual, sem cadastrar credenciais ou executar modelos.

## Workflow

`.github/workflows/ui-standards-real-agent-pilot.yml` usa exclusivamente `workflow_dispatch` e só aceita `g2/bootstrap-framework`. Executa checkout com histórico completo e sem credenciais persistentes, Python 3.11, dependências fixadas por hash, validação da baseline, fixture HTML sintética em `RUNNER_TEMP`, instalação idempotente dos seis adaptadores e checks de integridade do arquivo de produto e HEAD. Publica artefato sem dados sensíveis: hashes, commit da fixture, lista dos adaptadores e status explícito `preflight-only`.

O workflow **não** instala CLIs Codex/Claude, **não** recebe chaves, **não** utiliza `secrets`, **não** chama modelos, **não** testa permissões adversariais efetivas e **não** executa skills por agente. GitHub Actions pode consumir minutos de runner; não há custo de inferência neste workflow.

## Matriz planejada — execução real futura, ainda não autorizada

| Agente | Skill | Modo | Estado |
| --- | --- | --- | --- |
| Codex | ui-design | plan | NAO_VERIFICADO |
| Codex | ui-audit | audit | NAO_VERIFICADO |
| Codex | ui-code-review | review | NAO_VERIFICADO |
| Claude | ui-design | plan | NAO_VERIFICADO |
| Claude | ui-audit | audit | Execução parcial anterior; nova rodada NAO_VERIFICADO |
| Claude | ui-code-review | review | Execução parcial anterior; nova rodada NAO_VERIFICADO |

## Requisitos para uma fase posterior, sob nova autorização

1. Definir e revisar versões exatas e proveniência dos CLIs e mecanismos de autenticação; nunca registrar tokens em arquivos, relatórios ou logs.
2. Autorizar separadamente o custo de inferência, limites de uso e forma de ativação manual; manter o workflow normal de CI independente.
3. Executar cada combinação em fixture descartável independente e fornecer request JSON exato, saída bruta do agente, result JSON, validação semântica e relatório.
4. Provar isolamento por mecanismo externo ao agente (por exemplo, mounts e permissões efetivas) com tentativa adversarial controlada, não apenas instrução de prompt.
5. Separar recusa por falta de permissão de falha funcional; registrar limitações, hashes antes/depois, alterações observadas e custos efetivos.
6. Proibir alteração de normas G1, projetos reais, segredos, merge, release e publicação sem autorização.

**Gate:** preflight verde comprova somente preparação da infraestrutura. Não comprova invocação, paridade, isolamento ou homologação V1.
