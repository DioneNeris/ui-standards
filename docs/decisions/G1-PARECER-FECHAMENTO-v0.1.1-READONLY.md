# G1 — Parecer de fechamento documental v0.1.1

**Status:** REVISÃO READ-ONLY; NÃO HOMOLOGADO.  
**Objeto:** pacote `UI-UX-Standards-G1-v0.1.1-CANDIDATA-SANEADA.zip`.  
**Limites:** inspeção documental e consistência interna; sem execução de cenários em produto, sem homologação WCAG, sem alteração de originais.

## Verificações efetuadas

- Especificação candidata, matriz CSV, catálogo CSV/Markdown, mapa AUD-01…AUD-12, esquema de evidência, changelog e README examinados.
- A matriz apresenta 53 linhas; o catálogo apresenta 53 cenários manuais. IDs e correspondência devem permanecer fixos na homologação.
- A matriz não contém resultados de execução; os cenários são descritos como `MANUAL_REPRODUZIVEL`, ainda não executados.
- A baseline WCAG 2.2 AA está explicitamente marcada como proposta dependente de aprovação do PO, com mapeamento parcial e não exaustivo.
- O mapa de saneamento registra AUD-02, AUD-06 e AUD-12 como parciais, AUD-04 como pendente de aprovação/verificação externa e AUD-07 como pendente de decisão de escopo.

## Achados de fechamento

| ID | Grau | Constatação | Encaminhamento |
|---|---|---|---|
| FEC-01 | Bloqueio de homologação sem ressalvas | Baseline WCAG 2.2 AA ainda proposta e mapeamento incompleto; não há validação externa detalhada | Aprovação expressa do baseline e validação técnica das referências; sem alegar conformidade integral |
| FEC-02 | Ressalva documental | Protocolos de regras qualitativas ainda dependem de julgamento; repetibilidade entre avaliadores não demonstrada | Ensaio cruzado em G2/G3 com amostra representativa e registro de divergências |
| FEC-03 | Decisão de escopo | Lacunas de alterações não salvas, operações em lote e paginação registradas sem normas novas | PO decidir se entra no núcleo V0.1.x ou backlog versionado |
| FEC-04 | Ressalva de cobertura | Exemplos positivos/negativos completos não acompanham todas as normas | Completar casos prioritários no G2 antes de uso operacional amplo |
| FEC-05 | Ressalva de validação | 53 cenários são manuais propostos, não testes executados | Validar na integração piloto G3; não confundir cobertura documental com conformidade de produto |

## Parecer

**G1 apto a homologação documental COM RESSALVAS, condicionada à deliberação explícita do PO sobre o baseline WCAG e o escopo das lacunas.** Não há base para homologação irrestrita, para afirmar conformidade WCAG AA de qualquer aplicação ou para autorizar automaticamente G2.

**Ressalvas transferíveis ao G2/G3, se aceitas pelo PO:** repetibilidade entre avaliadores, exemplos completos e execução dos cenários em aplicações reais. **Pendências de decisão no G1:** baseline WCAG e escopo de fluxos não cobertos.

## Decisões solicitadas ao PO

1. Adotar WCAG 2.2 AA como baseline-alvo para novas interfaces web, com verificação de aplicabilidade por projeto e sem declarar conformidade sem auditoria completa?
2. Tratar alterações não salvas, operações em lote e paginação como backlog de expansão normativa, ou incluí-las antes de homologar G1?
3. Aceitar transferir validação prática, repetibilidade e exemplos complementares ao G2/G3, mantendo-as como ressalvas explícitas?

**Controle:** nenhum arquivo da candidata foi modificado. Este parecer é documento novo e independente.