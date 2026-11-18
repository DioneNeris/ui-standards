# G2 — Contratos propostos para três skills (NÃO HOMOLOGADOS)

**Status:** proposta documental para revisão do PO. Não constitui implementação, esquema definitivo ou autorização de execução. **Fonte normativa:** especificação G1 v0.1.1 candidata homologada posteriormente com ressalvas, e registros de decisões. Preserve as 53 IDs e seus métodos; não use este documento para mudar as normas.

## Princípios comuns

- Uma fonte normativa central, independente do agente. Adaptadores Codex e Claude Code apenas carregam e invocam o mesmo contrato, sem duplicar regras.
- Toda operação declara `skill`, `contract_version`, `normative_version`, `source_commit`, `scope`, `authorization` e `environment`. Não assumir que dados ausentes foram verificados.
- Saída de auditoria/revisão: `run_id`, executor, data UTC, escopo, ambiente, versão normativa, commit, achados por ID, métodos exigidos e efetivamente executados, evidências por método, exceções e justificativas, limitações, arquivos alterados e estado da execução.
- Status normativos de avaliação de produto são exclusivamente `CONFORME`, `NAO_CONFORME`, `NAO_VERIFICADO`, `NAO_APLICAVEL`. Auditorias documentais podem ter classificação própria, claramente separada. Ausência de método/evidência não é conformidade; N/A requer justificativa.
- Não confundir `status_normativo=CANDIDATA` no CSV original com status de execução ou com a homologação posterior.
- Erros de contrato, entradas incompletas, fonte normativa não verificável ou autorização insuficiente devem interromper a operação relevante e retornar motivo explícito (fail closed), sem executar mudanças.
- A matriz **derivada** é consumível como CSV, mas não prova identidade com o pacote original. O original deve permanecer intacto.

## ui-design

**Objetivo:** orientar ou produzir interface conforme normas aplicáveis, apenas mediante autorização de implementação específica. **Entrada proposta:** tarefa, contexto funcional, stack e restrições, escopo autorizado, normas aplicáveis, artefatos-alvo, evidências disponíveis. **Saída proposta:** decisões de UI por ID, arquivos modificados, diffs, verificações executadas, itens não verificados e limitações. **Proibição:** alterar regras de negócio ou alegar conformidade sem testes.

## ui-audit

**Objetivo:** avaliar interface existente sem alterar o produto. **Entrada proposta:** alvo, ambiente, escopo, versão normativa, métodos autorizados S/V/I/F, exceções declaradas, evidências. **Saída proposta:** resultado por ID/método, evidências reproduzíveis, N/A fundamentado, achados, cobertura e limites. Relatório escrito apenas com autorização explícita.

## ui-code-review

**Objetivo:** revisar código/diff sem alterar o produto. **Entrada proposta:** base/head, diff, escopo, contexto, regras e método S disponível. **Saída proposta:** achados por ID, trechos de código e evidências, risco, método efetivamente utilizado e pendências V/I/F. **Limite:** código isolado não demonstra conformidade visual/interativa/funcional.

## Decisões em aberto antes da aprovação

1. Mapear os quatro tipos GOV-003 aos dois valores de `tipo_excecao` do CSV sem inventar equivalências.
2. Definir formalmente a precedência do registro de execução §3 versus a evidência mínima dos cenários.
3. Escolher formato versionado legível por máquina (JSON Schema ou equivalente), campos obrigatórios, erros e compatibilidade.
4. Definir protocolos de descoberta e carregamento para Codex e Claude Code e ensaiar paridade.
5. Decidir como tratar indisponibilidade do pacote-fonte e do esquema original.

**Nenhum manifesto, adaptador, script ou skill foi implementado por este documento.**
