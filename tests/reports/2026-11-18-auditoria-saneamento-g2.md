# Auditoria documental read-only — saneamento G1/G2

**Data:** 2026-11-18. **Branch:** `g2/bootstrap-framework`. **Base:** `c6ff988bf0069e73e8f6a11138d7c73f120a0b8f`. **Fonte auditada:** `4544bd8757cf7122a51de274f3a4e72b7efd91aa`, após atualização fast-forward a partir da branch local limpa em `c6ff988`. **Versão:** G1 v0.1.1, cópias candidatas e registro posterior de homologação com ressalvas. **Escopo autorizado:** auditoria documental read-only das alterações posteriores à base, criação, commit e push exclusivamente deste relatório; sem implementar skills, alterar normas ou fazer merge.

**Conclusão:** as sete alterações se enquadram no saneamento descrito pelo registro aditivo, e a verificação encontrou os seis originais inalterados e os 53 registros do CSV derivado idênticos aos da matriz presente. A autorização específica do PO e a identidade do pacote G1 continuam dependentes de fontes primárias externas não disponíveis nesta auditoria. Os contratos são propostas não homologadas; há ambiguidades e pendências abaixo que não devem ser convertidas em normas ou aceites automaticamente.

## Verificações e evidências

| Item | Resultado |
|---|---|
| 1. Sete alterações e escopo | `git diff --name-status c6ff988..4544bd8` identifica sete arquivos em sete commits: decisão aditiva, CSV derivado, README, status, inventário, backlog e contratos propostos. São categorias previstas em `docs/decisions/2026-11-18-PO-G1-G2-AUDITORIAS.md:9-16`. **Compatibilidade documental verificada; autorização primária não verificável:** o próprio registro identifica a conversa externa como fonte e é evidência secundária. Não foram encontrados arquivos de implementação no diff. |
| 2. Seis originais | `git diff --quiet c6ff988..4544bd8 -- <seis caminhos>` retornou 0; comparação individual dos bytes dos blobs da base com os arquivos no HEAD também retornou igualdade para todos. Os caminhos e hashes constam abaixo. Isso prova preservação desde a base, não identidade com o ZIP original ausente. |
| 3. Derivado | Parser CSV estrito Python: cabeçalho igual, 53 registros em cada arquivo, 12 campos em cada linha, 53 IDs únicos em cada, registros e ordem idênticos campo a campo. No nível de bytes, derivado = original depois das duas primeiras linhas **mais um LF final**; não houve outra alteração no restante. A verificação não prova autenticidade da fonte externa. `framework/SOURCE-INVENTORY.md` identifica o derivado e a transformação. |
| 4. Decisões e evidências | `docs/decisions/2026-11-18-PO-G1-G2-AUDITORIAS.md:3-16` distingue a decisão posterior da candidata histórica, discovery/validação G2 e saneamento, limita a aceitação das auditorias ao plano documental e explicita que não prova identidade, testes, WCAG ou paridade. G2 segue aberto e implementação/merge não autorizados. A transcrição resumida e a citação atribuída ao PO não puderam ser confrontadas com a conversa primária; data indicada é a do registro, exceto a terceira decisão, explicitamente datada. |
| 5. Documentação operacional | README, status, inventário e backlog distinguem cópias importadas de pacote íntegro, identificam derivado, ausência de originais, G2 aberto e falta de execução de piloto. README reconhece ausência de licença. Ver observações abaixo sobre repetibilidade, origem do preâmbulo e afirmação ampla de testes. |
| 6. Contratos | `framework/contracts/G2-CONTRATOS-PROPOSTOS.md:1-3,27-35` marca proposta não homologada, preserva IDs/métodos e exige autorização específica para implementação. Não foram identificados novos IDs ou alteração de exigências centrais G1 nos arquivos normativos. Campos e comportamentos como `contract_version`, data UTC e fail closed são **propostas operacionais novas**, não normas G1 aprovadas; seu detalhamento e eventuais efeitos dependem de revisão e decisão do PO. A síntese de status merece esclarecimento abaixo. |
| 7. Pendências adicionais | Permanecem ausentes ZIP e hashes de referência, esquema separado, README/changelog e catálogo CSV originais; persistem validação WCAG detalhada, ensaio de repetibilidade, exemplos, piloto, descoberta/paridade entre agentes e definição de licença e contratos. `docs/BACKLOG-G2-G3.md:7-21` os registra sem fechamento automático. |

## Observações e riscos para decisão

1. **Agregação por método:** o contrato (`framework/contracts/G2-CONTRATOS-PROPOSTOS.md:10`) diz que ausência de método/evidência não é conformidade, mas não explicita a precedência `NAO_CONFORME` quando uma violação já foi demonstrada e outro método está ausente, como estabelecido por GOV-004 (`framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md:13`). A frase é compatível como resumo, mas uma implementação baseada só nela pode escolher indevidamente `NAO_VERIFICADO`. Preservar GOV-004 integralmente na futura definição.
2. **Fonte não verificável e fail closed:** o contrato, linha 12, propõe interromper a operação relevante quando a fonte normativa não for verificável, enquanto a identidade do pacote externo ainda está não verificada. O significado de “fonte verificável”, o escopo da interrupção e a possibilidade de inspeção documental limitada não estão definidos; não inferir autorização nem bloqueio absoluto de toda análise. O item 5 das decisões em aberto já pede tratamento da indisponibilidade da fonte.
3. **Repetibilidade:** o backlog marca DEC-G1-003/a como `PARCIAL` pelas duas auditorias documentais (`docs/BACKLOG-G2-G3.md:10`), mas elas não constituem ensaio formal de repetibilidade com protocolo comum, avaliação de divergências e aceite. A linha reconhece a ausência de aplicação independente em UI real; o grau `PARCIAL` é acompanhamento, não demonstração de repetibilidade ou fechamento da ressalva.
4. **Origem do preâmbulo:** status e inventário o descrevem como preâmbulo de extração. As duas linhas são observáveis, mas sua origem e presença no arquivo-fonte não foram estabelecidas. A descrição não deve ser tomada como prova da proveniência ou motivo dessas linhas.
5. **Alcance da afirmação de testes:** README diz que nenhuma interface foi testada; os relatórios anteriores e esta auditoria demonstram apenas que suas respectivas inspeções não executaram tais testes, e o status registra ausência de piloto. Não foi investigado todo histórico ou atividade externa, portanto a afirmação absoluta não é independentemente demonstrada aqui.
6. **Rastreamento:** `AUD-G2-03` ainda consta `AGUARDA_VALIDACAO`; esta auditoria fornece evidência documental de equivalência da transformação, mas a atualização do backlog e o aceite pertencem ao fluxo autorizado e ao PO. Responsáveis operacionais das pendências ainda não estão atribuídos (`docs/BACKLOG-G2-G3.md:23`).

## Hashes das cópias no commit auditado

```text
4b5f2c33f8545c9a1bb8d3fa627fe1a2c76ebab4f964b96153099f64590ab39a  framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md
37c6d84ef09e534043e78be29383fce234186bdd332163535b273af5bd604be3  tests/scenarios/G1-CATALOGO-CENARIOS-v0.1.1.md
0a1042c7eb6f1526b78449a747c5317ae8d4829ed7b0844f68c85d8b852ca101  framework/traceability/G1-MATRIZ-BASELINE-v0.1.1.csv
62df207bd91c8edfbb978fe24d74eb1557fab6d09ae65a41afbbf52c8a7ce87d  docs/decisions/G1-REGISTRO-DECISOES-FECHAMENTO-v0.1.1.md
07a119e89db165ea4dedec5d1fc6971a4e7c990633a621d209213df1189a122e  docs/decisions/G1-MAPA-SANEAMENTO-AUDITORIA-v0.1.1.md
dd036b38cd2db12971e827ab5a65cc477a67af488dc79ecc83f2e81fd2515510  docs/decisions/G1-PARECER-FECHAMENTO-v0.1.1-READONLY.md
523c8f31b35f157951cb374ef3b72d26c18f78c52e9b78ce414f2836b8d90e7e  framework/traceability/derived/G1-MATRIZ-BASELINE-v0.1.1-normalizada.csv
```

## Método e limites

Leitura de `AGENTS.md`, `docs/WORKFLOW.md`, `docs/PROJECT-STATUS.md`, ambos os relatórios anteriores e dos sete arquivos alterados; revisão do diff e histórico Git; comparação dos blobs e `sha256`; Python 3 de biblioteca padrão (`csv.reader(strict=True)`, `pathlib`, `hashlib`, `subprocess`) sobre o original após ignorar em memória as duas primeiras linhas e sobre o derivado. `git diff --check c6ff988..4544bd8` não apontou problemas de whitespace. A comparação de conteúdo usa as cópias no repositório; não consulta ZIP, conversa primária, documentação WCAG externa ou outro ambiente. Não houve testes visuais, funcionais, interativos, de descoberta/execução de skills ou de produto: **não verificados**. Não houve alteração de fontes ou normas.

Arquivo criado: somente este relatório. Branch de entrega: `g2/bootstrap-framework`. O commit de entrega é identificável pelo histórico Git; seu SHA não pode ser incluído no próprio arquivo sem alterar o hash. Push não constitui aprovação, fechamento de gate ou merge.
