# Validação da implementação V1 piloto

**Data:** 2026-11-18. **Branch:** `g2/bootstrap-framework`. **Base:** `ffc75647ccadcf71b51437bcbe9eb63c0039efc7`, árvore limpa e remoto iguais antes do trabalho. **Norma:** G1 v0.1.1, cópias preservadas. **Autorização:** PO homologou o contrato e P1/P2/P3 na conversa e autorizou implementação, testes e ensaios controlados; registro secundário em `docs/decisions/2026-11-18-PO-V1-PILOTO.md`. Não autoriza alterar G1, modificar projeto real, merge ou release.

**Estado: V1 NÃO PLENAMENTE VALIDADA e não pronta para aplicação em projeto real.** Há componentes executáveis e testes passando, mas permanecem lacunas essenciais de segurança, paridade e completude do contrato descritas abaixo. A presença de scripts e skills não constitui aceite ou homologação da implementação.

## Arquitetura e arquivos

- `uistandards/core.py`: baseline fixada ao commit fonte, SHA-256, comparação com blobs Git, matriz derivada, 53 IDs/cenários, métodos e agregação; `validation.py`: JSON Schema e verificações semânticas; `report.py`: Markdown a partir de resultado validado.
- `schemas/v1/`: schemas Draft 2020-12 de request e result; `requirements-lock.txt`: jsonschema e transitivas fixadas com hashes de distribuições.
- `scripts/validate.py`, `report.py`, `install.py`: validação, relatório em stdout e adaptadores locais idempotentes. `skills/`: três instruções e contrato comum; adaptadores apontam à mesma cópia local da baseline.
- `tests/contracts/`: fixtures sintéticos e testes; `.gitignore`: arquivos gerados Python; `docs/V1-PILOTO.md`: instruções e limites; `docs/decisions/2026-11-18-PO-V1-PILOTO.md`: registro aditivo da autorização. `skills/shared/CONTRACT.md` teve correção do caminho do validador após o commit técnico inicial.
- Arquivos normativos originais e catálogo não foram modificados; `git diff --quiet ffc75647 -- framework/specification framework/traceability tests/scenarios` retornou 0. As únicas alterações são as listadas acima e este relatório.

## Resultados dos critérios

| Critério | Resultado | Evidência e limites |
|---|---|---|
| 53 normas e métodos | PASS | `python3 scripts/validate.py baseline --package-root . --json`: `VALID`, `rule_count=53`, `source_provenance=NAO_VERIFICADA`. Testes validam rejeição de matriz adulterada. |
| Correspondência com 53 cenários | PASS | Carregador compara ID e caso na spec, CSV e catálogo, além de campos e métodos; teste `test_loads_53_matching_rules`. Não é execução de cenários. |
| Contratos de entrada e saída | NAO_VERIFICADO | Schemas passaram `Draft202012Validator.check_schema`; fixtures positivas parciais para três skills e entradas incompletas/duplicadas foram exercitadas. Nem todos os ramos, versões, erros e estados de bloqueio foram testados. |
| Agregação GOV-004 | PASS | Testes de todos métodos conformes, método ausente, violação comprovada com outro ausente e nenhum método aplicável; teste com artefato por método. Não valida automaticamente suficiência substantiva. |
| Read-only | NAO_VERIFICADO | Testes rejeitam operação de escrita declarada e o instalador detecta links externos. Instrução textual e campos de autorização não impõem sandbox. Não foi realizado teste adversarial de ação de agente nem de estado externo. **Não usar auditoria em produto até isolamento verificável.** |
| Evidência insuficiente | PASS | Testes rejeitam conformidade sem evidência, suficiência insuficiente e arquivo de evidência alterado. A adequação real de uma evidência continua dependente do avaliador. |
| N/A explícito | PASS | Testes aceitam justificativa/evidência com aprovação e rejeitam falta ou pendência. Interpretação deve respeitar GOV-003. |
| Descoberta e execução das 3 skills nos 2 agentes | NAO_VERIFICADO | Adaptadores foram instalados em `/tmp/ui-standards-v1-pilot`. Codex CLI 0.170.0 descobriu e invocou as três skills em sandbox read-only e informou validação da baseline, sem avaliar produto. Não houve fluxo completo com request/result e evidência. Claude Code 2.1.327 identificou os wrappers, mas com ferramenta de leitura restrita não conseguiu ler o pacote e validar baseline. Ensaio posterior com acesso ao pacote foi recusado pela revisão automática por risco de envio de instruções e contratos ao serviço externo; os dois processos iniciados em paralelo foram interrompidos. Não inferir paridade. |
| Relatórios rastreáveis | NAO_VERIFICADO | `test_report_contains_run_id_baseline_and_per_rule_status` confirma renderização parcial de fixture; ainda falta ensaio ponta a ponta com request serializado, resultado de skill real e revisão do relatório completo. |
| Instalação local | NAO_VERIFICADO | Dry-run, idempotência, preservação de conflito e rejeição de link externo passaram em projeto temporário. Instalação de dependências via lock e atualização entre versões não foram comprovadas: Python do ambiente não dispõe de `pip` nem `ensurepip`. Hashes dos pacotes foram consultados no índice PyPI; não são verificação de uma instalação efetiva. |

## Verificações realizadas

- `python3 -m unittest discover -s tests/contracts -v`: **25 testes OK**, incluindo negativos e fixtures; nenhum teste de produto.
- `python3 -m compileall -q uistandards scripts tests/contracts`: sucesso; `Draft202012Validator.check_schema` aceitou os dois schemas.
- Instalação e invocações exclusivamente em diretório descartável. Teste inicial do Codex no sandbox externo falhou por sistema de arquivos somente leitura; repetição com o sandbox read-only do próprio Codex executou a descoberta. Claude sem acesso ao pacote não validou baseline.
- Busca por padrões comuns de chaves privadas e tokens nos arquivos novos não retornou achados; isso não prova ausência de todos os segredos. Nenhum teste visual, funcional de interface, WCAG, leitor de tela ou piloto de produto foi executado.

## Pendências para revisão independente

1. Garantir e ensaiar efetivamente isolamento read-only para produto, dados e ambiente; reforçar restrições de implementação e caminhos reais, inclusive corridas e links simbólicos. O instalador faz pré-checagens, mas não oferece transação atômica em caso de falha concorrente.
2. Completar e testar os fluxos dos três agentes com request/result e relatório reais, sem simular integração indisponível; a integração Claude com leitura do pacote requer tratamento da rejeição automática e autorização explícita apropriada.
3. Completar validação de todos os requisitos do contrato: estado `BLOQUEADA` com baseline ausente e `rules=[]` foi exercitado na API, mas falta teste ponta a ponta desse ramo pela CLI; códigos estruturados e versões têm cobertura parcial; `format` date-time do `jsonschema` instalado não estava disponível e são usadas verificações Python para datas principais, que exigem mais casos RFC 3339. O validador atual aceita artefatos locais absolutos, não todos os tipos de URI previstos. Fonte original, homologação e integridade não devem ser confundidas.
4. Verificar integridade e versão dos scripts e skills instalados, além da baseline; testar atualização segura e instalação reproduzível em venv com pip e lock. O instalador detecta alteração dos adaptadores, mas não atesta todo o pacote.
5. Completar testes das exceções GOV-003, conflitos, N/A, referências e suficiência, testes end-to-end dos relatórios, e revisão independente antes de permitir uso. Não inferir WCAG ou execução dos 53 cenários pelos testes de contrato.
6. A identidade do pacote G1 com ZIP autoritativo, validação WCAG externa, exemplos e repetibilidade em UI real permanecem pendências controladas de G2/G3.

## Reprodução e entrega

Ver comandos em `docs/V1-PILOTO.md`. A versão de Python aqui foi 3.14.4, jsonschema 4.19.2; Codex 0.170.0 e Claude Code 2.1.327. O primeiro commit técnico é `b07833f`; o SHA final é identificado por `git rev-parse HEAD` após o commit que contém este próprio relatório, pois um arquivo não pode conter o SHA do próprio commit sem alterá-lo. O SHA final e o resultado do push devem ser informados no retorno ao PO. Nenhum merge ou release foi realizado.
