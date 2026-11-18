# Contrato V1 candidato — ui-design, ui-audit e ui-code-review

**Estado:** CANDIDATO PARA ACEITE DO PO; não implementado. **Versão proposta:** contrato `1.0.0`, formato de resultado `1.0.0`; baseline declarada `G1-0.1.1`. **Fonte documental examinada:** commit `a64a3a5845a3a140aee7535dcbdf0f1f3118a9f0`, branch `g2/bootstrap-framework`. Esta proposta não altera a G1, não fecha G2 e não autoriza implementação, instalação, uso em produto, publicação ou merge. A execução e a implantação do piloto exigem autorização específica posterior.

## 1. Autoridade e arquitetura

A especificação `framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md`, GOV-001 a GOV-005 e decisões posteriores são autoridade normativa; a matriz e o catálogo são instrumentos de consulta, não substitutos da especificação. O registro `docs/decisions/2026-11-18-PO-G1-G2-AUDITORIAS.md` documenta separadamente homologação posterior com ressalvas e G2 aberto; sua fonte primária não foi verificada independentemente. WCAG 2.2 AA é alvo, não certificado. Backlog DEC-G1-002 não cria IDs adicionais.

**Escolha candidata:** pacote local versionado, três instruções de skill comuns e adaptadores finos para descoberta por agente. O carregador lê os originais preservados, o CSV derivado e o catálogo; não copia normas para os adaptadores. Validador local determina estrutura, referências e agregação; o agente coleta e avalia evidência, sempre dentro de autorização. Artefatos são JSON UTF-8 e relatório Markdown renderizado a partir do mesmo resultado. Sem serviço, API ou banco. Opção alternativa de embutir a baseline nos seis adaptadores foi descartada por risco de divergência; um serviço central não é necessário para o piloto. Um único runtime portátil Python 3.11+ e `jsonschema` fixado na implementação são propostos para validação Draft 2020-12; sem dependências de produção adicionais. A instalação de dependências somente ocorrerá em tarefa autorizada posterior.

Estrutura **proposta, ainda inexistente** no pacote `ui-standards`:

```text
framework/                        # fonte G1 existente e única
  specification/…                # original preservado
  traceability/…                 # original e derivado existente
  contracts/G2-CONTRATO-V1-CANDIDATO.md
skills/
  ui-design/SKILL.md             # instruções comuns por skill
  ui-audit/SKILL.md
  ui-code-review/SKILL.md
  shared/CONTRACT.md             # instruções comuns, referência a este contrato e fontes
schemas/v1/{request,result}.schema.json
scripts/{install.py,validate.py} # interfaces abaixo, a implementar
tests/contracts/                 # fixtures e testes determinísticos
```

`SKILL.md` deve incluir frontmatter `name` e `description`, declarar limites e indicar leitura do contrato e caminhos do pacote; instruções comuns podem referenciar `skills/shared/CONTRACT.md`. `install.py` gera adaptadores pequenos sob `.agents/skills/<nome>/SKILL.md` e `.claude/skills/<nome>/SKILL.md` no projeto alvo, apontando para a mesma cópia local fixada do pacote; apenas adaptadores são duplicados. Os caminhos compartilhados resolvem-se pela raiz absoluta do pacote registrada no adaptador e validada contra commit/hash; não se supõe que links relativos sobrevivam à instalação. Evitar symlinks como requisito, para portabilidade. Nenhum adaptador contém texto de regras. Nunca copiar ou sobrescrever silenciosamente arquivo existente; reinstalação idempotente só substitui arquivos marcados como gerados pelo instalador com conteúdo esperado, e falha em conflito. O projeto precisa preservar acesso à cópia fixada; ao mudar o pacote, reinstalar/validar explicitamente. Diretórios de saída não são fontes de normas.

## 2. Carregamento e confiança

Entrada obrigatória fixa `baseline.repository`, `baseline.commit` (SHA Git completo), `baseline.version=G1-0.1.1` e hashes SHA-256 de spec, CSV derivado e catálogo. SHA identifica bytes, não autoria. O executor lê arquivos do checkout correspondente, verifica commit e conteúdo limpo dos arquivos normativos comparando bytes com blobs desse commit, confere hashes declarados, matriz derivada contra matriz original (remover exatamente as duas linhas iniciais, acrescentar LF final se ausente), cabeçalho de 12 campos e CSV estrito, 53 IDs distintos nas 8 famílias (6/8/8/6/6/7/7/5), métodos somente S/V/I/F, nomes `TC-<ID>` e bijeção com os 53 cabeçalhos do catálogo e da spec. Valida nível, requisito, critério, métodos e caso contra a especificação e cenários, sem modificar fontes. Um manifesto de hashes versionado deve ser produzido na implementação e vinculado ao commit auditado; não usar `status_normativo=CANDIDATA` como resultado de execução. O carregador devolve lista ordenada de objetos com ID, requisitos, critério, métodos, exceção e vínculo ao cenário, apontando para os caminhos de origem e linhas.

Distinguir: (a) **integridade do checkout**: bytes/hashes e vínculos verificáveis localmente; (b) **proveniência original**: comparação externa com ZIP/fonte independente, hoje `NAO_VERIFICADA`; (c) **homologação**: informada pelo registro aditivo, distinta de (a) e (b). Esses estados são campos separados. O contrato não afirma baseline instalada ou pacote original íntegro enquanto (b) não for comprovado.

**Política proposta para aceite do PO:** com (a) íntegra e (b) pendente, permitir análise documental limitada e, após autorização específica do PO para o piloto, avaliações de produto e implementação de UI explicitamente autorizadas usando cópia identificada e ressalva obrigatória em cada resultado. Nenhuma afirmação de proveniência completa, homologação de aplicação ou conformidade WCAG decorre disso. Divergência de hash, fonte ausente, CSV inválido, ID duplicado ou conflito normativo bloqueia resultados normativos e mudanças dependentes; permite apenas diagnóstico documental sem status de conformidade e sem substituir dados. Ausência apenas do ZIP externo não se confunde com corrupção local. Conflito entre obrigação externa e funcional é registrado e escalado conforme GOV-002, sem decisão unilateral; divergências entre spec, matriz e catálogo bloqueiam a regra afetada e, se conjunto/identidade não puder ser determinado, toda avaliação normativa.

## 3. Contrato comum de dados

Os arquivos de esquema são entregáveis da implementação posterior, não criados agora. Os tipos abaixo são requisitos implementáveis para `request.schema.json` e `result.schema.json`; JSON Schema valida estrutura e o validador adicional verifica regras semânticas e referências. Em ambos, `additionalProperties: false` por objeto, exceto `extensions`, objeto opcional com chaves prefixadas `x-`; strings obrigatórias não vazias, arrays de IDs únicos. `null` só é admitido onde indicado; omissão nunca representa verificação bem-sucedida. V1 rejeita versão major desconhecida; minor/patch maiores são aceitos apenas quando o produtor declara compatibilidade retroativa e usa `extensions`, caso contrário rejeitar. Envelopes inválidos geram erro estruturado, sem resultado normativo válido.

### 3.1 Entrada `request`

| Campo obrigatório | Tipo e regra |
|---|---|
| `contract_version` | string semver `1.0.0` |
| `skill` | `ui-design`, `ui-audit`, `ui-code-review` |
| `mode` | `plan` ou `implement` para design; `audit` para auditoria; `review` para revisão |
| `baseline` | `{repository, commit, version, hashes}`: strings; commit hexadecimal completo; `hashes` contém `spec`, `matrix_derived`, `scenarios` com SHA-256 hex de 64 caracteres |
| `target` | `{project, repository, revision, scope, flows}`: identificação do projeto/repositório, commit/revisão ou identificador do estado; `scope` texto; `flows` array não vazio de referências de tela/fluxo |
| `environment` | `{os, agent, agent_version, browser, device, viewport, zoom}`; `browser`, `device`, `viewport`, `zoom` são string ou null com `environment_limitations` explicando desconhecimento/não pertinência |
| `authorization` | `{reference, operations, writable_paths, methods}`; referência verificável da autorização no contexto, operações explícitas, caminhos autorizados e subconjunto S/V/I/F. Referência não é credencial e não substitui avaliação humana de autoridade |
| `output` | `{delivery, path}`: `delivery` = `inline` ou `file`; `path` null para inline, caminho autorizado para file |
| `task` | texto da tarefa; para review incluir `review: {base, head, diff_scope}`; para design incluir `design: {artifacts, constraints}` com arrays; campos condicionais obrigatórios conforme skill |
| `environment_limitations` | array de justificativas; vazio permitido se todos os campos pertinentes são conhecidos |

`ui-audit` e `ui-code-review`: `operations` não inclui mudanças em produto; `writable_paths` vazio exceto destino do relatório quando explicitamente autorizado. `plan` não modifica produto. `implement` exige autorização específica e caminhos explícitos, além da política de piloto acima; verificar caminhos reais após resolver links, negar fora do escopo e não alterar normas, negócio, segurança, dependências ou infraestrutura sem autorização independente. Operações destrutivas, chamadas remotas ou ações que alterem dados não são implicitamente autorizadas por métodos I/F. Se o ambiente não puder impor os limites, a skill suspende a ação e registra limitação; instrução de linguagem natural sozinha não garante sandbox.

### 3.2 Saída `result`

Envelope obrigatório: `contract_version`, `result_version`, `run_id` (UUID único), `skill`, `mode`, `execution_state` (`COMPLETA`, `PARCIAL`, `BLOQUEADA`), `started_at`, `finished_at` (RFC 3339 UTC), `executor`, `request_ref` (hash SHA-256 do JSON de entrada), `baseline` (identificadores, hashes efetivos, `repository_integrity`, `source_provenance`, `approval_state` independentes), `target`, `environment`, `scope`, `authorization_ref`, `rules`, `findings`, `evidence`, `limitations`, `errors`, `artifacts`, `changed_files`. `repository_integrity` = `VERIFICADA|FALHOU|NAO_VERIFICADA`; `source_provenance` = `VERIFICADA|NAO_VERIFICADA|DIVERGENTE`; `approval_state` = `HOMOLOGADA_COM_RESSALVAS|NAO_VERIFICADA`, com referência ao registro, não derivado da coluna candidata. `findings`, `evidence`, `limitations`, `errors`, `artifacts`, `changed_files` são arrays, possivelmente vazios; erro inclui `code`, `message`, `affected_ids`, `action`.

Cada entrada de `rules` inclui `id`, `scenario_id`, `applicability` (`APLICAVEL|NAO_APLICAVEL|INDETERMINADA`), `required_methods` conforme baseline, `method_results`, `status` GOV-004, `exceptions`, `limitations`. Em auditoria completa de escopo, emitir exatamente 53 entradas: cada ID fora do escopo é `NAO_VERIFICADO` com motivo, nunca N/A automático. Inspeção parcial também emite as 53 entradas quando a baseline íntegra está disponível; se indisponível, `rules=[]`, estado BLOQUEADA e erro sem conclusões normativas. Por método requerido, uma entrada única `{method, applicability, status, evidence_ids, reason}`; status do método usa os quatro valores GOV-004. Métodos adicionais podem constar com `additional=true` e não substituem os requeridos. `findings` contém `{id, rule_id, method, observation, impact, evidence_ids}` e não representa evidência por si só.

### 3.3 Evidência e registro completo

`evidence` é array obrigatório de objetos `{id, rule_id, method, flow, element, state, steps, observation, artifact, captured_at, executor, method_result, sufficiency, sufficiency_reason, assessor, limitations}`. `sufficiency` é `SUFICIENTE|INSUFICIENTE|INDETERMINADA`; `sufficiency_reason` e `assessor` são strings não vazias. `steps` é array ordenado de strings; `artifact` contém `{uri, sha256, media_type}` com URI/caminho acessível e hash quando artefato digital existe; ausência exige `artifact=null` e justificativa em limitações, e não pode isoladamente sustentar CONFORME ou N/A. URI não deve conter segredos ou dados pessoais. Uma evidência pode referenciar um método e regra; evidência comum é referenciada em entradas separadas com o mesmo artefato. Registrar no envelope `run_id`, projeto, repositório/revisão, tela/fluxo, baseline, ambiente, browser/SO/dispositivo quando relevantes, viewport/zoom, data e executor; em cada evidência estado de dados/permissão, passos, método, observação, achado, artefato, resultado e limitações. Conclusão por regra e por método está em `rules`; referências de `findings`/evidências precisam resolver dentro do resultado. Isto implementa o registro completo da §3; evidência mínima do cenário complementa, nunca reduz esses campos.

**Suficiência:** validação estrutural e existência/hash de artefato são necessárias, não suficientes para afirmar que prova o critério. Executor registra observação, contexto, passo e vínculo ao critério; faz julgamento fundamentado e rastreável de suficiência por método. O validador rejeita CONFORME se qualquer evidência exigida estiver ausente, inválida ou não marcada `sufficiency=SUFICIENTE` com `sufficiency_reason` e `assessor`. Este julgamento não substitui revisão humana nem valida critérios subjetivos automaticamente. A avaliação de N/A também precisa de evidência verificável de ausência/inaplicabilidade e justificativa específica; não basta campo vazio.

## 4. GOV-004 e GOV-003

Agregação determinística por regra, sem dispensar avaliação humana de suficiência:

1. Se existir método com violação comprovada e evidência válida: `NAO_CONFORME`, inclusive se outros métodos estiverem ausentes.
2. Senão, se a regra inteira for comprovadamente inaplicável: `NAO_APLICAVEL`, com justificativa e evidência de escopo. Uma regra não é N/A apenas porque um método não foi executado.
3. Senão, se aplicabilidade indeterminada, qualquer método requerido aplicável estiver ausente, incompleto ou sem evidência suficiente, ou N/A por método sem justificativa verificável: `NAO_VERIFICADO`.
4. Senão, `CONFORME` somente quando todos os métodos requeridos aplicáveis estiverem `CONFORME` com evidência suficiente; métodos efetivamente não aplicáveis exigem justificativa verificável. Se nenhum método for aplicável, não gerar conformidade por verdade vazia; reavaliar a aplicabilidade da regra ou manter `NAO_VERIFICADO`.

Método `NAO_CONFORME` também exige evidência de violação; resultado afirmado sem evidência válida é rejeitado, não convertido silenciosamente. A não aplicabilidade não elimina violação comprovada. Quando o avaliador não consegue determinar suficiência ou aplicabilidade, registra `NAO_VERIFICADO` e limitação. Um resultado parcial ou fora de escopo não autoriza conclusão global de produto.

Exceções têm `{rule_id, type, context, justification, evidence_ids, approver, validity, review_at, impact}`; `type` enum `NAO_APLICABILIDADE`, `ALTERNATIVA_EQUIVALENTE`, `WAIVER_CONVENCAO`, `CONFLITO_BLOQUEANTE`. Aprovação, responsável, validade, revisão e impacto devem ser registrados conforme GOV-003; em solicitação ainda não aprovada, `approver`, `validity`, `review_at` podem ser null acompanhados de `approval_state=PENDENTE` e justificativa, sem aplicar a exceção. Alternativa equivalente exige teste de equivalência e aprovação técnica/PO; waiver não dispensa obrigações externas; conflito bloqueante é escalado. Campo CSV `tipo_excecao` é metadado de origem, não é decisão: `ALTERNATIVA_EQUIVALENTE_OU_NA` e `CONVENCAO_LOCAL` não são mapeados automaticamente aos quatro tipos GOV-003. A proposta é seleção explícita contextual pelo avaliador, com evidência e aprovação pertinentes; sem equivalência normativa nova. Critérios para dispensa individual de método e interpretação detalhada desse metadado seguem para aceite PO.

## 5. Comportamento das skills

- **ui-design:** `plan` identifica tarefa, normas aplicáveis, decisões propostas, conflitos e verificações; não altera produto. `implement` somente com autorização de implementação para escopo/caminhos, aprovação da política de fonte e direitos efetivos do ambiente. Saída inclui plano, `changed_files` com antes/depois ou diff, verificações realmente executadas e cobertura por norma. Não inferir licença para alteração de negócio, dependência ou norma. Design pode relatar `NAO_VERIFICADO` antes de ter UI ou métodos executáveis.
- **ui-audit:** lê alvo e evidências; não modifica produto, ambiente, dados, infraestrutura ou baseline. Métodos I/F somente quando ação autorizada e não altera estado; se o fluxo exigir mutação, registra `NAO_VERIFICADO` e pede autorização específica fora do escopo read-only. `output=file` apenas com autorização expressa para esse caminho; senão entrega inline. Resultado por regra/método e achados rastreáveis.
- **ui-code-review:** lê base/head e diff; S é análise estática, não comprova V/I/F. Mesmo se S conforme, métodos não executados mantêm regra `NAO_VERIFICADO`, salvo violação comprovada. Resultados fora do diff e limitações de contexto são explícitos; relatório segue regra read-only. Evidências de execução preexistentes podem ser consideradas somente se atribuíveis à mesma revisão, escopo, estado e método e estiverem disponíveis para verificação.

## 6. Falhas, instalação e operação previstas

Códigos comuns: `INVALID_REQUEST`, `UNSUPPORTED_VERSION`, `BASELINE_MISSING`, `BASELINE_HASH_MISMATCH`, `BASELINE_CONFLICT`, `SOURCE_PROVENANCE_UNVERIFIED`, `AUTHORIZATION_MISSING`, `READ_ONLY_UNENFORCEABLE`, `EVIDENCE_INSUFFICIENT`, `EXCEPTION_UNAPPROVED`, `OUTPUT_UNAUTHORIZED`, `INSTALL_CONFLICT`. Eventos recuperáveis tornam execução PARCIAL e mantêm regras afetadas não verificadas; erros de identidade da baseline, escopo/autorização ou entrada bloqueiam ação dependente. `SOURCE_PROVENANCE_UNVERIFIED` é limitação, não corrupção; a política do §2 depende de aceite PO. Erro inclui ação possível, sem dados sensíveis. Não rebaixar violação estabelecida; não gerar relatório de sucesso em falha.

CLI **proposta para implementação futura**, executada a partir de uma cópia local fixada do pacote, sem acesso de rede durante execução:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/validate.py baseline --package-root .
.venv/bin/python scripts/validate.py request --file request.json --package-root .
.venv/bin/python scripts/validate.py result --file result.json --request request.json --package-root .
.venv/bin/python scripts/install.py --package-root . --project-root /caminho/do/projeto --agents codex,claude --dry-run
.venv/bin/python scripts/install.py --package-root . --project-root /caminho/do/projeto --agents codex,claude
```

A instalação posterior requer autorização no projeto alvo; dry-run não escreve. Comandos `validate` retornam 0 válido, 2 entrada/esquema inválido, 3 baseline inválida, 4 erro de ambiente; `install` retorna 0, 2 argumentos inválidos, 3 pacote inválido, 4 conflito/permissão; erros em stderr e saída legível por máquina com `--json` opcional. Fixar versão exata de `jsonschema` e transitivas em `requirements-lock.txt` na implementação, com hashes e verificação offline após instalação. Revalidar package-root/commit/hash em cada invocação. Nenhum desses comandos ou arquivos de implementação existe nesta entrega.

Codex descobre `.agents/skills/<nome>/SKILL.md`, invocação explícita `$ui-design`, `$ui-audit`, `$ui-code-review`; Claude Code descobre `.claude/skills/<nome>/SKILL.md`, invocação explícita `/ui-design`, `/ui-audit`, `/ui-code-review`. Instalação prevê adaptadores com frontmatter `name`/`description` e texto para localizar o pacote comum; usar diretórios de projeto, não presumir instalação global. Reiniciar/recarregar sessão conforme agente, verificar catálogo e invocar cada skill em ambiente controlado. Versões reais e resultados devem ser registrados; configuração, precedência e suporte podem variar. Referências técnicas consultadas: [Codex carregamento e roots](https://github.com/openai/codex/blob/main/codex-rs/ext/skills/src/host_roots.rs), [Codex nomes e symlinks](https://github.com/openai/codex/blob/main/codex-rs/ext/skills/src/loader/host.rs), [Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), [JSON Schema 2020-12](https://json-schema.org/draft/2020-12). Sem garantia de paridade antes dos ensaios. O núcleo não depende do fornecedor; compatibilidade de adaptador depende do agente e versão testados.

## 7. Entrega futura coesa e aceite

Após aceite deste contrato e autorização específica, implementar em uma entrega: (1) fixar manifesto e dependência; (2) schemas com todos os campos acima e validação semântica/aggregação; (3) três instruções comuns e instalador com adaptadores; (4) fixtures e testes; (5) ensaios em ambos os agentes e relatório versionado. Nenhuma mudança em originais. Validar com JSON Schema Draft 2020-12; ativar validação de `format` explicitamente e verificar datas/hash/URI também na camada semântica, pois `format` não é necessariamente assertion. Objetos condicionais e referências cruzadas são verificados por código, não apenas por schema.

| Classe | Critério objetivo de aceite, executado depois da implementação |
|---|---|
| Contrato automatizado | Baseline íntegra retorna 53 IDs, distribuição esperada e 53 pares TC únicos; erro em hash, duplicate, cenário ausente, método desconhecido ou CSV alterado bloqueia; comparação byte a byte da transformação verifica LF final. |
| Contrato automatizado | Request/result válidos para três skills aceitos; ausência de campo, versão incompatível, método inválido, referência órfã, UUID/data inválidos ou saída não autorizada rejeitados com código. Cobrir cada ramo condicional, incluindo nullable justificado. |
| Contrato automatizado | Fixture de todos métodos conformes com evidência suficiente → CONFORME; evidência insuficiente/método ausente → NAO_VERIFICADO; violação comprovada + método ausente → NAO_CONFORME; N/A sem justificativa/evidência rejeitado; N/A integral comprovado → NAO_APLICAVEL; nenhum método aplicável não produz CONFORME. |
| Contrato automatizado | Códigos CSV não criam exceção; exceção não aprovada não é aplicada; artefato/hash alterado rejeita suficiência; estados `CANDIDATA`, aprovação e execução não se misturam. Fixtures verificam registro completo §3 e referências. |
| Integração controlada | Em projeto descartável e sob sandbox com produto read-only, validar que `ui-audit` e `ui-code-review` não alteram arquivos/dados; comparar hashes antes/depois e monitorar operações, inclusive falhas e links simbólicos; escrita de relatório só no caminho explicitamente autorizado. Ações de UI que modifiquem dados ficam fora do teste read-only. |
| Integração agentes | Após instalação autorizada, registrar versões e ambiente; verificar descoberta explícita e execução das três skills em Codex e Claude Code (6 combinações), incluindo chamada com fixture idêntica, saída válida e referências à mesma baseline; comparar resultados determinísticos do validador e documentar divergências de julgamento dos agentes. Falha ou ausência de agente mantém combinação não verificada. |
| Rastreabilidade | Para cada ensaio gerar JSON validado e Markdown coerente com mesmo `run_id`, revisão, hashes, escopo, métodos, evidências, exceções e limitações; reproduzir validação a partir dos arquivos, sem alegar que a presença do catálogo executou cenários. |
| Posterior em UI real | Com autorização e escopo próprios, executar os 53 cenários de piloto com evidência por método e comparar avaliadores; validar WCAG aplicável contra fonte oficial e produzir exemplos positivos/negativos. Isso é gate separado, não consequência de testes de contrato nem garantia de conformidade WCAG. |

## 8. Decisões, bloqueios e limitações

**Para aceite do PO antes de implementar:** (P1) aprovação deste contrato e autorização explícita de implementação e ensaios; (P2) política de uso piloto com pacote original não recuperado (§2), incluindo limites de afirmação; (P3) proposta de seleção contextual dos tipos GOV-003 sem mapear CSV e tratamento de método individualmente inaplicável (§4). Se qualquer ponto for recusado, ajustar proposta; nenhuma decisão é presumida. Aprovação deste texto não equivale a autorização de alterações em produtos ou merge.

**Bloqueantes técnicos para execução normativa:** falha local de integridade/identidade, conflito de fonte sem resolução, ausência de autorização apropriada, schema/validador inexistente ou incapacidade de impor read-only. Descoberta/execução de cada agente bloqueia aceite daquela combinação, não pode ser declarada aprovada por outra. **Não bloqueantes sob política P2, se aceita:** recuperação do ZIP/schema/README/changelog/catálogo CSV, exemplos completos, validação externa WCAG e repetibilidade em piloto permanecem rastreados; não se tornam verificados pela V1. Licença é decisão antes da publicação, não licença implícita do projeto. Alterações não salvas, operações em lote e paginação continuam backlog normativo.

Fontes consultadas: `AGENTS.md`, `docs/WORKFLOW.md`, `docs/PROJECT-STATUS.md`, `framework/SOURCE-INVENTORY.md`, spec G1 §§1–9, matriz derivada, catálogo de 53 cenários, registro aditivo, `docs/BACKLOG-G2-G3.md`, contratos propostos e três relatórios em `tests/reports/` (incluindo `a64a3a5`). Sem execução de produto, skills, testes visuais, ou validação de WCAG nesta etapa.
