# Piloto sintético V1 — protocolo e critérios de evidência

**Status: execução pendente de CI para este commit.** O piloto aqui é exclusivamente de **contratos e relatórios**, não uma execução dos agentes Codex ou Claude.

## Objetivo

Reproduzir para `ui-design` (plan), `ui-audit` (audit) e `ui-code-review` (review) o fluxo request JSON → validação de request → result JSON sintético com 53 regras `NAO_VERIFICADO` → validação de result → relatório Markdown. Nenhum resultado afirma inspeção de UI, conformidade, ou comportamento do agente.

## Execução

`python scripts/synthetic_pilot.py <diretorio-descartavel>` em checkout completo, com histórico do commit fixado e dependências do lock. O CI executa em `RUNNER_TEMP` e publica o artefato `ui-standards-v1-synthetic-contract-evidence`, com requests, results, relatórios e manifest com SHA-256 de cada arquivo. Os arquivos não são gravados em projetos reais.

## Matriz de aceite

| Critério | Estado antes do CI |
| --- | --- |
| Request/result/report sintético de ui-design | NAO_VERIFICADO |
| Request/result/report sintético de ui-audit | NAO_VERIFICADO |
| Request/result/report sintético de ui-code-review | NAO_VERIFICADO |
| Correspondência de SHA-256 do request | NAO_VERIFICADO |
| Invocação real Codex das três skills | NAO_VERIFICADO |
| Invocação real Claude das três skills | PARCIAL, evidência anterior separada |
| Isolamento read-only por fronteira externa | NAO_VERIFICADO |
| Paridade Codex/Claude | NAO_VERIFICADO |

O artefato sintético **não** constitui evidência de execução real de skills, isolamento adversarial ou conformidade WCAG. Não promover os resultados sintéticos a homologação da V1. O próximo gate real exige invocação das três skills por agente em ambiente descartável, entradas/saídas, logs, hashes antes/depois e fronteira de permissões independente do agente. Nenhum merge, release ou alteração da baseline G1 foi autorizado.
