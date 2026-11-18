# UI/UX Standards Framework — Especificação normativa v0.1.1 CANDIDATA SANEADA

**Estado:** CANDIDATA — NÃO HOMOLOGADA. **Origem:** v0.1.0 + auditoria documental AUD-01…AUD-12. **Natureza:** saneamento proposto, não alteração retroativa dos originais. **Escopo:** sistemas administrativos e operacionais internos. **Não foram executados testes de produto, navegador ou leitores de tela.**

## 1. Autoridade, aplicação e execução

**GOV-001 (APROVADA):** auditoria estritamente somente leitura; implementação somente em escopo explicitamente autorizado; alteração de negócio, segurança, dependências ou normas centrais exige autorização específica. A aprovação desta etapa autoriza apenas a criação de novos documentos candidatos.

**GOV-002:** identificar obrigações externas efetivamente aplicáveis e requisitos funcionais; em caso de conflito entre ambos, registrar e escalar sem escolher unilateralmente. Dentro de espaço não conflitante, aplicar regras obrigatórias internas; convenções locais previamente aprovadas prevalecem sobre convenções gerais do framework. Preferências estéticas não afastam obrigações.

**GOV-003:** classificar desvios em (a) **não aplicabilidade** demonstrada, (b) **alternativa equivalente** com teste de equivalência e aprovação técnica/PO, (c) **waiver de convenção** com justificativa e responsável, (d) **conflito bloqueante** escalado ao PO/responsável legal ou técnico. Waiver não dispensa obrigação externa aplicável. Registrar norma, tipo, contexto, evidência, aprovador, validade, revisão e impacto na homologação.

**GOV-004:** resultados por método: CONFORME, NAO_CONFORME, NAO_VERIFICADO, NAO_APLICAVEL. A norma só pode receber CONFORME quando **todos os métodos requeridos aplicáveis** tiverem evidência suficiente. Um método não executado mantém a conclusão agregada NAO_VERIFICADO, salvo violação já demonstrada (NAO_CONFORME). N/A exige justificativa verificável. Sem evidência, sem conformidade.

**GOV-005:** níveis `Obrigatória` e `Convencional` são **internos**; `Obrigatória` não implica obrigação legal. Proveniência de obrigação externa exige SC/referência e análise de aplicabilidade; a baseline WCAG proposta não equivale a declaração de conformidade de produto.

## 2. Baseline de acessibilidade proposta (AUD-04)

**Proposta sujeita a homologação do PO:** WCAG **2.2 nível AA** para novas interfaces web, observando aplicabilidade, exceções oficiais, requisitos legais e escopo de auditoria. O conjunto WCAG é mais amplo que os sete IDs A11Y; o mapeamento aqui é **parcial e não exaustivo**. Não declarar 'WCAG AA conforme' apenas por satisfazer o catálogo. RSP-004: SC 2.5.8 tem mínimo de 24×24 CSS px com exceções oficiais; 44×44 CSS px é alvo interno recomendado, não obrigação WCAG. Contraste: avaliar SC 1.4.3 e 1.4.11 conforme conteúdo/estado; foco SC 2.4.7 e 2.4.11. Referência: https://www.w3.org/TR/WCAG22/ . **Interpretação detalhada ainda requer validação contra fonte oficial na homologação.**

## 3. Evidência e relatório (AUD-05, AUD-09)

Baseline normativa é separada de resultados de execução. Um registro de execução exige: `run_id`, projeto, repositório/versão/commit, tela/fluxo, versão normativa, ambiente, navegador/SO/dispositivo (quando relevante), viewport e zoom, estado de dados/permissão, passos, método, data, executor, evidência/URI ou caminho, achado relacionado, resultado por método, conclusão e limitações. Dados pessoais devem ser removidos das evidências. Não alterar baseline para registrar auditorias.

## 4. Estados e versionamento (AUD-11)

`PROPOSTA → CANDIDATA → APROVADA → DESCONTINUADA`; rejeição retorna a PROPOSTA ou é arquivada com motivo. Somente PO homologa especificação e mudanças normativas centrais. Revisão técnica não equivale a aprovação. Versões publicadas são imutáveis; nova candidata usa nova versão. Projetos fixam tag/commit, e migração requer análise de impacto, changelog e autorização. Antes de 1.0, mudanças incompatíveis podem ocorrer e devem ser destacadas.

## 5. Catálogo preservado (53 IDs)

Métodos: S=estático, V=visual renderizado, I=interativo, F=funcional. `Métodos requeridos` indica a cobertura mínima para a regra quando aplicável; técnicas adicionais podem ser necessárias. Critérios qualitativos são operacionalizados pelos cenários e observáveis, não por números universais inventados.

### LAY-001 — A sequência de apresentação deve respeitar o fluxo funcional da tela.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** A sequência visual acompanha a tarefa sem retornos desnecessários.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Descrever tarefa e sequência esperada; identificar cada retorno de seção e se é exigido pela operação. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Ordem operacional alternativa documentada. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-LAY-001 (ver catálogo de cenários).

### LAY-002 — Componentes relacionados devem compartilhar eixos de alinhamento.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Eixos coerentes entre componentes funcionalmente relacionados.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Componentes relacionados devem compartilhar eixos de alinhamento. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Desvio com função identificável. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-LAY-002 (ver catálogo de cenários).

### LAY-003 — Espaçamentos devem utilizar a escala definida pelo projeto.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Valores correspondem a tokens ou escala; exceções identificadas.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Espaçamentos devem utilizar a escala definida pelo projeto. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,V
- **Exceção original:** Ajuste pontual documentado. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-LAY-003 (ver catálogo de cenários).

### LAY-004 — Cards devem representar agrupamentos funcionais.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Cada card tem finalidade clara, sem fragmentação artificial.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Nomear finalidade de cada card; registrar cards com apenas um elemento sem motivo de agrupamento. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Separação por estado ou permissão justificada. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-LAY-004 (ver catálogo de cenários).

### LAY-005 — Largura e densidade devem ser adequadas à tarefa.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Sem dispersão ou compressão que dificulte a operação.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Registrar largura, zoom, conteúdo real e pontos onde campos ficam truncados ou exigem deslocamento desnecessário. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Densidade especial de fluxo operacional documentada. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-LAY-005 (ver catálogo de cenários).

### LAY-006 — Organização visual não pode ocultar conteúdo ou impedir ações essenciais.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Informações e ações essenciais permanecem disponíveis.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Organização visual não pode ocultar conteúdo ou impedir ações essenciais. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Sem exceção por preferência estética. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-LAY-006 (ver catálogo de cenários).

### ACT-001 — Cada grupo de ações deve possuir hierarquia primária inequívoca.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Uma ação principal identificável por grupo funcional.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Listar ações do grupo e seu tratamento visual; verificar se duas ações de resultados distintos possuem a mesma proeminência. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Grupos independentes têm hierarquias próprias. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-ACT-001 (ver catálogo de cenários).

### ACT-002 — Em formulários LTR com rodapé, usar primário à direita por padrão.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Posição coerente em telas equivalentes.
- **Observável/protocolo:** 1. Preparar contexto/estado. 2. Se houver rodapé de formulário LTR, comparar telas equivalentes e design system local. Primário à direita é default apenas na ausência de convenção local aprovada; não migrar isoladamente. 3. Registrar evidência por método e conclusão.
- **Métodos requeridos:** V
- **Exceção original:** Convenção local aprovada e consistente. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-ACT-002 (ver catálogo de cenários).

### ACT-003 — Ações destrutivas devem ser distinguíveis e protegidas conforme risco.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Consequências compreensíveis e salvaguardas proporcionais.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I,F em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Ações destrutivas devem ser distinguíveis e protegidas conforme risco. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I,F
- **Exceção original:** Proteção equivalente comprovada. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-ACT-003 (ver catálogo de cenários).

### ACT-004 — Rótulos devem comunicar claramente a operação ou resultado.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Ações diferentes possuem nomes diferenciáveis.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Executar cada ação e comparar rótulo com o efeito real; registrar ambiguidade concreta. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,V,I
- **Exceção original:** Ícone isolado somente com nome acessível e significado inequívoco. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-ACT-004 (ver catálogo de cenários).

### ACT-005 — Ações equivalentes devem manter posição e aparência consistentes.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Padrão previsível em contextos equivalentes.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Ações equivalentes devem manter posição e aparência consistentes. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Contexto operacional distinto documentado. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-ACT-005 (ver catálogo de cenários).

### ACT-006 — Estados de processamento devem prevenir duplicações indevidas.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Repetições não criam operações duplicadas indevidas.
- **Observável/protocolo:** 1. Preparar contexto/estado. 2. Acionar submissão repetidamente durante atraso de resposta; conferir ausência de duplicação no resultado e tratamento idempotente quando necessário. 3. Registrar evidência por método e conclusão.
- **Métodos requeridos:** S,I,F
- **Exceção original:** Operações explicitamente repetíveis. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-ACT-006 (ver catálogo de cenários).

### ACT-007 — Ações secundárias não devem competir visualmente com a principal.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Proeminência secundária inferior à primária.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Comparar peso visual, cor, tamanho e posição de ações primária e secundárias no mesmo grupo. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Ações de grupos independentes. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-ACT-007 (ver catálogo de cenários).

### ACT-008 — Ordem visual e de foco deve preservar sequência compreensível.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** DOM, foco e apresentação não geram sequência contraditória.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Ordem visual e de foco deve preservar sequência compreensível. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,I
- **Exceção original:** Sem exceção que comprometa navegação. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-ACT-008 (ver catálogo de cenários).

### FRM-001 — Campos devem seguir sequência lógica de preenchimento.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Ordem corresponde ao fluxo operacional.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Executar preenchimento completo na ordem apresentada e registrar saltos de contexto. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Ordem alternativa justificada por dependências. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FRM-001 (ver catálogo de cenários).

### FRM-002 — Labels acima dos campos são o padrão inicial.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Posicionamento consistente nos formulários equivalentes.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Labels acima dos campos são o padrão inicial. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Padrão específico de componente documentado. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FRM-002 (ver catálogo de cenários).

### FRM-003 — Campos devem possuir identificação persistente e acessível.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Nome acessível e identificação não dependente de placeholder.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Campos devem possuir identificação persistente e acessível. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,I
- **Exceção original:** Não dispensável quando requerido por acessibilidade. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 3.3.2, 4.1.2
- **Caso manual:** TC-FRM-003 (ver catálogo de cenários).

### FRM-004 — Campos relacionados devem ser agrupados visualmente.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Proximidade e estrutura tornam grupos reconhecíveis.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Campos relacionados devem ser agrupados visualmente. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Agrupamento alternativo justificado. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FRM-004 (ver catálogo de cenários).

### FRM-005 — Erros devem identificar campo ou grupo e orientar correção.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Mensagem localizável e específica.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,V,I,F em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Erros devem identificar campo ou grupo e orientar correção. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,V,I,F
- **Exceção original:** Erro global quando não atribuível a campo. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 3.3.1, 3.3.3
- **Caso manual:** TC-FRM-005 (ver catálogo de cenários).

### FRM-006 — Falhas de validação não devem apagar dados válidos desnecessariamente.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Dados válidos persistem após erro.
- **Observável/protocolo:** 1. Preparar contexto/estado. 2. Preencher campos válidos, induzir erro em outro campo, submeter e confirmar preservação de dados não sensíveis. 3. Registrar evidência por método e conclusão.
- **Métodos requeridos:** F
- **Exceção original:** Restrição de segurança ou privacidade documentada. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FRM-006 (ver catálogo de cenários).

### FRM-007 — Campos curtos não devem ter largura excessiva sem justificativa.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Largura proporcional ao dado esperado.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Usar valores típicos e limites documentados; registrar truncamento, largura e legibilidade. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Consistência de grid que não prejudique uso. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FRM-007 (ver catálogo de cenários).

### FRM-008 — Envio deve apresentar resultado compreensível.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Confirmação ou erro verificável após submissão.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações I,F em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Envio deve apresentar resultado compreensível. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** I,F
- **Exceção original:** Processamento assíncrono com estado rastreável. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FRM-008 (ver catálogo de cenários).

### NAV-001 — Usuário deve identificar o contexto atual de navegação.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Título, navegação ou mecanismo equivalente informa localização.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Usuário deve identificar o contexto atual de navegação. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,V,I
- **Exceção original:** Fluxo imersivo com contexto inequívoco. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-NAV-001 (ver catálogo de cenários).

### NAV-002 — Padrões de navegação devem ser consistentes entre telas equivalentes.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Posição e comportamento previsíveis.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Padrões de navegação devem ser consistentes entre telas equivalentes. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Fluxos de natureza distinta. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-NAV-002 (ver catálogo de cenários).

### NAV-003 — Modais devem gerenciar foco e fechamento adequadamente.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Foco inicial, contenção quando apropriada, retorno e teclado testados.
- **Observável/protocolo:** 1. Preparar contexto/estado. 2. Abrir modal por teclado, verificar foco inicial, ciclo de Tab, Escape quando apropriado, retorno do foco e fechamento sem perda de dados. 3. Registrar evidência por método e conclusão.
- **Métodos requeridos:** S,I
- **Exceção original:** Diálogo não modal segue padrão correspondente. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 2.1.1, 2.4.3
- **Caso manual:** TC-NAV-003 (ver catálogo de cenários).

### NAV-004 — Ações contextuais devem ficar próximas do objeto afetado.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Associação visual e semântica inequívoca.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Ações contextuais devem ficar próximas do objeto afetado. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Ação global com escopo explicitado. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-NAV-004 (ver catálogo de cenários).

### NAV-005 — Navegação não pode depender exclusivamente de hover ou gestos.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Funções essenciais acessíveis por alternativas.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Navegação não pode depender exclusivamente de hover ou gestos. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** I
- **Exceção original:** Sem exceção que comprometa acessibilidade. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-NAV-005 (ver catálogo de cenários).

### NAV-006 — Fluxos em etapas devem comunicar estado e progressão quando aplicável.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Etapa atual e próximas ações compreensíveis.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Fluxos em etapas devem comunicar estado e progressão quando aplicável. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Fluxo não linear com navegação própria. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-NAV-006 (ver catálogo de cenários).

### DAT-001 — Colunas devem usar alinhamento adequado ao tipo de dado.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Valores e textos alinhados consistentemente.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Colunas devem usar alinhamento adequado ao tipo de dado. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Apresentação especial justificada. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-DAT-001 (ver catálogo de cenários).

### DAT-002 — Busca e filtros devem se associar à listagem controlada.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Relação entre controles e resultados é clara.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Busca e filtros devem se associar à listagem controlada. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Filtro global identificado como tal. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-DAT-002 (ver catálogo de cenários).

### DAT-003 — Ações por registro devem identificar o registro afetado.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Nome/contexto da ação identifica o item.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Ações por registro devem identificar o registro afetado. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,I
- **Exceção original:** Sem exceção que crie ambiguidade. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-DAT-003 (ver catálogo de cenários).

### DAT-004 — Ações frequentes devem ser facilmente acessíveis.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Ações recorrentes sem navegação excessiva.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Identificar tarefa frequente no contexto do produto e contar interações necessárias para acessá-la; não impor limite universal. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Densidade ou segurança justifica menu. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-DAT-004 (ver catálogo de cenários).

### DAT-005 — Estados sem dados, erro e falta de permissão devem ser distinguíveis.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Mensagens e comportamentos representam causas distintas.
- **Observável/protocolo:** 1. Preparar contexto/estado. 2. Executar cenários com zero registros, erro de consulta e acesso negado; confirmar estados distintos sem revelar informação restrita. 3. Registrar evidência por método e conclusão.
- **Métodos requeridos:** V,I,F
- **Exceção original:** Detalhes internos sensíveis podem ser omitidos. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-DAT-005 (ver catálogo de cenários).

### DAT-006 — Indicadores devem conter contexto interpretativo suficiente.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Unidade, período e escopo presentes quando necessários.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,F em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Identificar unidade, período, população/escopo e origem necessários; apontar informação ausente que altera interpretação. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,F
- **Exceção original:** Contexto já explícito no agrupamento. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-DAT-006 (ver catálogo de cenários).

### RSP-001 — Conteúdo deve adaptar-se sem perda de funções essenciais.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Operações essenciais disponíveis nos tamanhos suportados.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Conteúdo deve adaptar-se sem perda de funções essenciais. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Sem exceção por preferência estética. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-RSP-001 (ver catálogo de cenários).

### RSP-002 — Breakpoints devem responder às necessidades do conteúdo.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Mudanças ocorrem antes de colisões ou ilegibilidade.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Breakpoints devem responder às necessidades do conteúdo. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Pontos existentes já atendem ao conteúdo. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-RSP-002 (ver catálogo de cenários).

### RSP-003 — Formulários devem priorizar uma coluna em telas estreitas.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Sequência linear compreensível.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Formulários devem priorizar uma coluna em telas estreitas. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Campos relacionados cabem sem prejuízo. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-RSP-003 (ver catálogo de cenários).

### RSP-004 — Alvos interativos devem atender critérios WCAG aplicáveis.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** WCAG 2.2 2.5.8 observada com exceções legítimas; 44×44 CSS px como recomendação interna para toque.
- **Observável/protocolo:** 1. Preparar contexto/estado. 2. Medir caixas de alvo e espaçamento em CSS px; avaliar exceções formais do SC 2.5.8. 44×44 CSS px é meta interna recomendada, não critério WCAG AA. 3. Registrar evidência por método e conclusão.
- **Métodos requeridos:** S,V,I
- **Exceção original:** Somente exceções previstas pelo critério aplicável. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 2.5.8
- **Caso manual:** TC-RSP-004 (ver catálogo de cenários).

### RSP-005 — Elementos fixos não podem ocultar conteúdo ou impedir interação.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Teclado, zoom e scroll não encobrem ações e campos essenciais.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Elementos fixos não podem ocultar conteúdo ou impedir interação. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Sem exceção que impeça uso. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-RSP-005 (ver catálogo de cenários).

### RSP-006 — Reflow deve preservar ordem de leitura e navegação.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** DOM e foco continuam coerentes após reorganização.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Reflow deve preservar ordem de leitura e navegação. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,I
- **Exceção original:** Sem exceção que quebre sequência. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 1.3.2, 2.4.3
- **Caso manual:** TC-RSP-006 (ver catálogo de cenários).

### RSP-007 — Tabelas devem preservar dados e operações essenciais na adaptação.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Scroll próprio ou apresentação alternativa mantém funções.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Tabelas devem preservar dados e operações essenciais na adaptação. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Colunas opcionais podem ser ocultadas com acesso alternativo. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-RSP-007 (ver catálogo de cenários).

### A11Y-001 — Elementos interativos devem ser operáveis por teclado.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Todas as funções aplicáveis alcançáveis e executáveis.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Elementos interativos devem ser operáveis por teclado. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** I
- **Exceção original:** Exceções previstas no critério WCAG aplicável. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 2.1.1, 2.1.2
- **Caso manual:** TC-A11Y-001 (ver catálogo de cenários).

### A11Y-002 — Foco deve permanecer visível.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Indicador de foco perceptível e não indevidamente ocultado.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Foco deve permanecer visível. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Conforme critérios WCAG aplicáveis. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 2.4.7, 2.4.11
- **Caso manual:** TC-A11Y-002 (ver catálogo de cenários).

### A11Y-003 — Controles devem ter nomes acessíveis apropriados.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Nome programático identifica propósito.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Controles devem ter nomes acessíveis apropriados. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,I
- **Exceção original:** Conforme critérios WCAG aplicáveis. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 4.1.2, 2.5.3
- **Caso manual:** TC-A11Y-003 (ver catálogo de cenários).

### A11Y-004 — Contraste deve atender critérios WCAG aplicáveis.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Contraste de texto e componentes testado nos estados relevantes.
- **Observável/protocolo:** 1. Preparar contexto/estado. 2. Medir contraste em estados normais, foco, desabilitado quando aplicável e erro; registrar razão e SC aplicável. Não concluir apenas por aparência. 3. Registrar evidência por método e conclusão.
- **Métodos requeridos:** S,V,I
- **Exceção original:** Exceções específicas WCAG quando aplicáveis. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 1.4.3, 1.4.11
- **Caso manual:** TC-A11Y-004 (ver catálogo de cenários).

### A11Y-005 — Informação não pode depender exclusivamente de cor.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Texto, forma ou outro sinal complementar disponível.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Informação não pode depender exclusivamente de cor. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Sem exceção fora dos critérios aplicáveis. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 1.4.1
- **Caso manual:** TC-A11Y-005 (ver catálogo de cenários).

### A11Y-006 — Semântica deve corresponder à função dos elementos.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Elementos nativos e ARIA adequados ao comportamento.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Semântica deve corresponder à função dos elementos. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,I
- **Exceção original:** Customização com equivalência acessível comprovada. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 1.3.1, 4.1.2
- **Caso manual:** TC-A11Y-006 (ver catálogo de cenários).

### A11Y-007 — Zoom e reflow devem preservar conteúdo e funções.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Testes conforme WCAG 1.4.4 e 1.4.10, quando aplicáveis.
- **Observável/protocolo:** 1. Preparar contexto/estado. 2. Testar zoom 200% e reflow equivalente a 320 CSS px conforme condições e exceções do SC aplicável; registrar configurações. 3. Registrar evidência por método e conclusão.
- **Métodos requeridos:** V,I
- **Exceção original:** Exceções previstas nos critérios aplicáveis. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** 1.4.4, 1.4.10
- **Caso manual:** TC-A11Y-007 (ver catálogo de cenários).

### FDB-001 — Operações relevantes devem apresentar processamento e resultado.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Estado durante e após operação é compreensível.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações I,F em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Simular operação rápida, lenta, sucesso e falha; registrar feedback observável em cada estado. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** I,F
- **Exceção original:** Operação instantânea com resultado imediatamente visível. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FDB-001 (ver catálogo de cenários).

### FDB-002 — Erros devem explicar problema e recuperação quando possível.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Mensagem compreensível e próximo passo quando viável.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Provocar erro reproduzível e verificar se mensagem identifica problema e ação de recuperação sem expor informação sensível. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V,I
- **Exceção original:** Detalhe técnico omitido por segurança. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FDB-002 (ver catálogo de cenários).

### FDB-003 — Estados vazios devem orientar próximo passo quando disponível.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Mensagem distingue ausência e orienta ação possível.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações V em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Estados vazios devem orientar próximo passo quando disponível. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** V
- **Exceção original:** Nenhuma ação possível no contexto. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FDB-003 (ver catálogo de cenários).

### FDB-004 — Sucesso não deve ser apresentado antes de confirmação efetiva.

- **Nível:** Obrigatória (interno; candidato)
- **Critério:** Feedback corresponde ao resultado confirmado.
- **Observável/protocolo:** 1. Preparar contexto/estado. 2. Simular resposta tardia e falha do servidor; confirmar que sucesso só aparece após confirmação da operação. 3. Registrar evidência por método e conclusão.
- **Métodos requeridos:** I,F
- **Exceção original:** Aceite assíncrono explicitamente rotulado como pendente. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FDB-004 (ver catálogo de cenários).

### FDB-005 — Mensagens transitórias não devem ser único meio de informação crítica.

- **Nível:** Convencional (interno; candidato)
- **Critério:** Informação crítica permanece recuperável.
- **Observável/protocolo:** 1. Identificar elemento e contexto da norma. 2. Executar verificações S,V,I em estados normal e relevante (erro, loading, mobile quando aplicável). 3. Inspecionar requisito específico: Mensagens transitórias não devem ser único meio de informação crítica. Registrar comportamento observado, não apenas impressão estética. 4. Anexar evidências por método e registrar limitações.
- **Métodos requeridos:** S,V,I
- **Exceção original:** Mensagem não crítica e dispensável. — interpretar segundo GOV-003, sem dispensa automática.
- **WCAG relacionada (mapeamento parcial):** não mapeada diretamente
- **Caso manual:** TC-FDB-005 (ver catálogo de cenários).

## 6. Cobertura de temas adicionais (AUD-07)

Não criar IDs novos nesta candidata. Aplicar avaliação de risco por fluxo e mapear: alterações não salvas (FRM-006, FDB-002, NAV-003), irreversibilidade (ACT-003), anúncios dinâmicos de erro (FRM-005, A11Y-003/006), paginação e ordenação (DAT-001/003, NAV-005, A11Y-001), permissões (DAT-005), operações em lote (ACT-003/004, DAT-003). Onde a norma existente não cobrir o comportamento, registrar **LACUNA_NORMATIVA** para deliberação do PO; não declarar conformidade integral.

## 7. Gate G1 (AUD-10)

**Entrada:** pacote v0.1.0, matriz e auditoria AUD-01…12; autorização de saneamento. **Saída documental mínima:** 53 IDs íntegros; cenários manuais com passos/resultado/evidência/N/A; baseline proposta e ressalva de cobertura; hierarquia de exceções; matriz baseline separada de execuções; modelo de evidência; changelog e mapa dos 12 achados; revisão documental e decisão expressa do PO. **Não exigido no G1:** executar testes em projetos reais, implementar skills, automação, integração Codex/Claude ou auditoria com leitor de tela; essas validações pertencem a gates posteriores. **Bloqueia homologação irrestrita:** conflitos normativos não resolvidos, referência faltante, critérios impossíveis de avaliar, ou baseline A11Y sem decisão do PO.

## 8. Contratos das skills (somente especificação, não implementação)

`ui-design`: recebe tarefa/escopo/projeto/versão normativa; produz proposta e/ou alterações somente se autorizadas, com decisões e verificações. `ui-audit`: recebe produto/fluxo/versão, produz achados com evidência, **read-only**. `ui-code-review`: recebe diff/contratos/versão, produz achados por arquivo, cobertura e limitações; não substitui validação visual/interativa. Todas devem rejeitar declaração de conformidade sem cobertura exigida e sinalizar conflito/lacuna.

## 9. Referências

- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/ARIA/apg/
- https://design-system.service.gov.uk/
- https://carbondesignsystem.com/
- https://m3.material.io/

Links são referências de consulta; este saneamento não executou validação externa completa dos critérios.