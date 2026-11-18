# Auditoria documental read-only — G1 v0.1.1

Data: 2026-11-18. Fonte: commit `92c5717ec117f71d2e781ceb9e92eb8a619bebf8`, branch `g2/bootstrap-framework`, inicialmente limpa e acompanhando `origin/g2/bootstrap-framework`. Versão examinada: G1 v0.1.1 candidata saneada e registros posteriores disponíveis. Objetivo: verificar integridade, 53 normas/cenários, rastreabilidade, governança e riscos para Codex e Claude Code. Autorização: inspeção documental read-only e criação, commit e push deste único relatório; sem alteração de originais, implementação de skills, merge ou testes de interface.

Ambiente: repositório local Linux/WSL, Git, `rg`, Python 3 (bibliotecas padrão `csv`, `re`, `collections`, `pathlib`) e `sha256sum`. Evidências são os caminhos versionados e hashes abaixo, relativos à raiz no commit fonte. Não havia pacote original independente disponível no repositório para comparação byte a byte; hashes são impressões dos arquivos presentes, não certificados de autenticidade.

## Resultados documentais

| Verificação | Resultado e evidência |
|---|---|
| Presença | Os seis arquivos listados em `framework/SOURCE-INVENTORY.md:5` estão presentes e versionados. O esquema de evidência separado, README e changelog originais não foram recuperados (`framework/SOURCE-INVENTORY.md:13`). O parecer também menciona catálogo CSV (`docs/decisions/G1-PARECER-FECHAMENTO-v0.1.1-READONLY.md:9`), ausente da árvore; não se pode presumir seu conteúdo ou equivalência ao Markdown. |
| Identidade e integridade do pacote | **NAO_VERIFICADO**: não há pacote de referência independente, manifesto de hashes assinado ou comparação possível com os originais. Há commits individuais de importação, mas nomes de commits e hashes locais não provam identidade com a origem. Não afirmar baseline instalada ou pacote completo. |
| IDs | 53 cabeçalhos normativos, 53 cenários e 53 linhas de dados, todos únicos e com conjuntos de IDs iguais. Distribuição: LAY 6, ACT 8, FRM 8, NAV 6, DAT 6, RSP 7, A11Y 7, FDB 5. IDs sequenciais por domínio e índices da matriz de 0 a 52. |
| Vínculos | 53 relações individuais `ID → TC-ID → ID` coincidem entre especificação, matriz e cabeçalhos do catálogo, sem ausências ou duplicações. Em todas as linhas, requisito da matriz coincide com título da norma; nível, critério, métodos, caso manual e protocolo da especificação coincidem com matriz/catálogo onde comparáveis; resultado esperado e métodos do cenário coincidem com a matriz. Todos os cenários contêm pré-condição, passos, resultado, métodos, evidência mínima e N/A. Comparação textual não prova suficiência semântica, repetibilidade ou execução. |
| Leitura da matriz | `framework/traceability/G1-MATRIZ-BASELINE-v0.1.1.csv:1` contém duas linhas de invólucro `<PARSED TEXT...` antes do cabeçalho real na linha 3. Um leitor CSV convencional toma a primeira linha como cabeçalho e não obtém as colunas esperadas. A contagem acima usou explicitamente as linhas a partir da terceira; preservar o arquivo e investigar a origem antes de criar qualquer transformação. Não se sabe se o invólucro existia no original. |
| Governança e evidência | `framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md:7` define precedência e exceções; linhas 13 e 21–23 definem agregação por método, N/A justificado e campos de execução. O modelo textual não permite verificar completude ou identidade do esquema separado ausente. Mapa AUD-05/AUD-09 registra saneamento documental no pacote examinado anteriormente, não comprova que esse esquema esteja nesta árvore. |
| Estado e decisão | Especificação, matriz e registro de decisões conservam estado candidato/não homologado; todas as 53 linhas da matriz trazem `CANDIDATA`. `AGENTS.md:10` e `docs/PROJECT-STATUS.md:6` registram homologação posterior pelo PO com ressalvas. O registro de decisões (`docs/decisions/G1-REGISTRO-DECISOES-FECHAMENTO-v0.1.1.md:35`) diz expressamente que aquela deliberação ainda não é homologação. O inventário remete a esse registro e ao status, mas não identifica uma evidência independente da manifestação posterior (data/referência/transcrição). Tratar a homologação como estado informado pelo projeto, com proveniência primária **NAO_VERIFICADA**, sem alterar os originais. |
| Estado do bootstrap | `docs/PROJECT-STATUS.md:13-18` ainda diz que o pacote não foi commitado e lista os originais como pendentes; seis cópias já constam no commit fonte. A ressalva de pacote completo e integridade não verificados continua válida. `README.md:5` também descreve incorporação futura; estado histórico pode confundir consumidores. |
| Ressalvas | `docs/decisions/G1-REGISTRO-DECISOES-FECHAMENTO-v0.1.1.md:10-17` registra WCAG 2.2 AA como alvo para novas interfaces, mapeamento parcial, backlog de alterações não salvas/lote/paginação e transferência de repetibilidade, exemplos, piloto e validação WCAG a G2/G3. O catálogo declara 53 especificados e zero executados (`tests/scenarios/G1-CATALOGO-CENARIOS-v0.1.1.md:2`). Nenhuma conformidade WCAG ou de produto decorre desta auditoria. |

## Riscos e pendências para integração

1. Recuperar pacote G1 autoritativo completo, inclusive esquema, README, changelog e catálogo CSV referido, e comparar cada arquivo e hash com procedência verificável. Resolver a origem do invólucro da matriz sem modificar silenciosamente os originais.
2. Registrar separadamente evidência rastreável da decisão posterior do PO e das ressalvas, e reconciliar os documentos de status mediante fluxo autorizado. A decisão anterior e a homologação posterior são eventos distintos; nenhuma alteração normativa é proposta aqui.
3. Consumidores automáticos podem interpretar o invólucro como cabeçalho CSV, os estados `CANDIDATA` como status de execução, ou o catálogo como testes aprovados. Preservar separação baseline/execução, métodos e evidência por método; ausência de verificação permanece `NAO_VERIFICADO`, salvo violação comprovada, e N/A exige justificativa verificável.
4. Os contratos de `ui-design`, `ui-audit` e `ui-code-review` são apenas descritivos (`framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md:571`); não há implementação ou adaptadores na árvore. `AGENTS.md` fornece instruções compartilhadas, porém descoberta e aplicação efetivas por Codex e Claude Code, contratos, paridade e repetibilidade **não foram testadas**. A ausência de arquivo de instruções específico para Claude Code é risco de descoberta, não prova de falha. Exigir autorização e validação posterior antes de confiar na integração.
5. Priorizar e rastrear as ressalvas com responsável, evidência e aceite; realizar ensaios entre avaliadores, exemplos positivos/negativos, piloto de 53 cenários e revisão detalhada WCAG nas fases autorizadas. Não inferir cobertura integral para os itens do backlog.

## Método e limites

Inspeção de `AGENTS.md`, `docs/WORKFLOW.md`, `docs/PROJECT-STATUS.md`, `framework/SOURCE-INVENTORY.md`, especificação, catálogo, matriz e três registros de decisão; inventário com `rg --files` e `git ls-tree`; contagem e comparação em memória com expressões regulares para cabeçalhos/blocos e `csv.DictReader` após remover apenas em memória as duas primeiras linhas. Compararam-se também campos textuais por ID; não foi feita auditoria externa de WCAG nem validação semântica exaustiva das exceções. `git ls-remote` falhou por resolução DNS no ambiente inicial; a referência remota local não comprova estado remoto atual. Testes visuais, interativos, funcionais, de descoberta de agentes e de produto: **NAO_VERIFICADO / não executados**, fora do escopo.

## Impressões SHA-256 no commit fonte

```text
4b5f2c33f8545c9a1bb8d3fa627fe1a2c76ebab4f964b96153099f64590ab39a  framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md
37c6d84ef09e534043e78be29383fce234186bdd332163535b273af5bd604be3  tests/scenarios/G1-CATALOGO-CENARIOS-v0.1.1.md
0a1042c7eb6f1526b78449a747c5317ae8d4829ed7b0844f68c85d8b852ca101  framework/traceability/G1-MATRIZ-BASELINE-v0.1.1.csv
07a119e89db165ea4dedec5d1fc6971a4e7c990633a621d209213df1189a122e  docs/decisions/G1-MAPA-SANEAMENTO-AUDITORIA-v0.1.1.md
dd036b38cd2db12971e827ab5a65cc477a67af488dc79ecc83f2e81fd2515510  docs/decisions/G1-PARECER-FECHAMENTO-v0.1.1-READONLY.md
62df207bd91c8edfbb978fe24d74eb1557fab6d09ae65a41afbbf52c8a7ce87d  docs/decisions/G1-REGISTRO-DECISOES-FECHAMENTO-v0.1.1.md
```

Arquivo criado: este relatório apenas. Branch de entrega: `g2/bootstrap-framework`. O SHA do commit de entrega é identificado pelo histórico Git que contém este arquivo; não pode ser embutido no próprio conteúdo sem alterar o SHA. Push e revisão/aceite pelo PO são etapas distintas; este relatório não homologa o pacote nem fecha gate.
