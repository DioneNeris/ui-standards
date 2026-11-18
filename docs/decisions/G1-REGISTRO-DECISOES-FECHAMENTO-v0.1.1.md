# G1 — Registro de decisões de fechamento v0.1.1

**Objeto:** UI/UX Standards Framework — G1 v0.1.1 candidata saneada  
**Autoridade:** deliberação expressa do Product Owner nesta conversa  
**Status:** DECISÕES REGISTRADAS; G1 APTO À HOMOLOGAÇÃO DOCUMENTAL COM RESSALVAS; NÃO HOMOLOGADO  
**Política:** execução controlada; G2 não autorizado.

## Decisões aprovadas

### DEC-G1-001 — Baseline de acessibilidade
Adotar **WCAG 2.2 nível AA** como baseline-alvo para novas interfaces web. Aplicabilidade e exceções oficiais devem ser avaliadas por projeto; o catálogo interno A11Y é parcial e não exaustivo. Esta decisão não representa auditoria WCAG, validação externa detalhada dos critérios ou declaração de conformidade de qualquer aplicação.

### DEC-G1-002 — Escopo de ampliação
Registrar **alterações não salvas**, **operações em lote** e **paginação** em backlog versionado de expansão normativa. Não criar IDs normativos novos na v0.1.1, não declarar esses fluxos integralmente cobertos e avaliar requisitos externos aplicáveis independentemente da cobertura interna.

### DEC-G1-003 — Ressalvas transferidas
Transferir controladamente para G2/G3: (a) ensaio de repetibilidade entre avaliadores/agentes, (b) exemplos conformes e não conformes complementares, (c) execução dos 53 cenários em integração piloto, (d) testes funcionais/visuais/interativos e verificação técnica detalhada das referências WCAG. Cada entrega deve ter evidência, responsável e decisão de aceite; itens não verificados permanecem não verificados.

## Rastreabilidade dos achados de fechamento

| Achado | Tratamento aprovado | Estado após decisão |
|---|---|---|
| FEC-01 | DEC-G1-001 | Decisão de baseline encerrada; validação técnica detalhada pendente |
| FEC-02 | DEC-G1-003 | Ressalva transferida a G2/G3 |
| FEC-03 | DEC-G1-002 | Decisão de escopo encerrada; backlog pendente de priorização |
| FEC-04 | DEC-G1-003 | Ressalva transferida ao G2 |
| FEC-05 | DEC-G1-003 | Ressalva transferida ao G3 |

## Critérios para eventual homologação documental

1. Manter 53 IDs normativos e 53 cenários associados, sem alegar execução.
2. Preservar a política de execução controlada e a separação entre auditoria read-only e implementação autorizada.
3. Tratar a WCAG 2.2 AA como baseline-alvo, sem declarar conformidade de produto.
4. Manter backlog e ressalvas rastreáveis, com bloqueio de afirmações de cobertura não comprovada.
5. Exigir manifestação expressa do PO para homologação do G1; **a presente deliberação não é homologação**.

## Parecer

**APTO À HOMOLOGAÇÃO DOCUMENTAL COM RESSALVAS CONTROLADAS.** As decisões de fechamento requeridas no parecer v0.1.1 foram tomadas. A evidência disponível é documental e não sustenta homologação irrestrita, conclusão de testes ou início automático do G2.

## Controle de alterações

Este registro é **aditivo**. Nenhum arquivo original da candidata v0.1.1, da matriz, do catálogo de cenários ou do parecer read-only foi alterado.