# Auditoria documental independente — G1 v0.1.1 (Claude Code)

**Data:** 2026-11-18
**Executor:** Claude Code (modelo Claude Opus 5.5), agente local em WSL
**Natureza:** auditoria documental **read-only**. Não houve teste de interface, execução de cenários nem implementação de skills.

## 1. Objetivo

Verificar a integridade documental do G1 v0.1.1 no repositório:
- as 53 normas e os 53 cenários;
- a rastreabilidade entre especificação, matriz e catálogo;
- a governança (homologação, decisões e ressalvas);
- as pendências para integração com Codex e Claude Code.

## 2. Escopo e autorização

- **Autorizado:** leitura do repositório e criação **exclusiva** deste arquivo, com commit e push na branch `g2/bootstrap-framework`.
- **Não autorizado e não realizado:** alterar documentos normativos, código, dependências ou estrutura; implementar skills; executar testes de interface; fazer merge na `main`.
- **Independência:** o relatório anterior do Codex (`tests/reports/2026-11-18-auditoria-documental-g1.md`) **não foi aberto**. Dele foram vistos apenas o nome, o tamanho (8949 bytes) e a mensagem do commit `4321314` ("docs: audit G1 baseline and traceability").

## 3. Estado de origem

| Item | Valor |
|---|---|
| Branch | `g2/bootstrap-framework` |
| HEAD local no início | `4321314a2be917fae455ee22591c02724ac1f07d` |
| `origin/g2/bootstrap-framework` após `git fetch` | `4321314a2be917fae455ee22591c02724ac1f07d` (igual ao HEAD local) |
| Working tree no início | limpo (`git status --porcelain` vazio) |
| `origin/main` | `dbc4e72` (somente o bootstrap do README) |
| Versão normativa auditada | G1 v0.1.1 CANDIDATA SANEADA (cópia commitada) |

## 4. Ambiente e ferramentas

- Linux (WSL2), git 2.53.0 e Python 3.14.4 (somente biblioteca padrão: `re`, `csv`, `collections`).
- Ferramentas de shell: `sha256sum`, `grep`, `od`, `file`, `wc`.
- Nenhuma ferramenta foi instalada e nenhum acesso de rede foi feito além de `git fetch`.
- As fontes WCAG não foram consultadas online.

## 5. Vocabulário deste relatório

Os status do GOV-004 (CONFORME, NAO_CONFORME etc.) servem para avaliar produtos e **não são atribuídos aqui**. Este relatório usa um vocabulário próprio:

- **COMPROVADO**: inconsistência ou lacuna demonstrada por evidência citada no repositório.
- **SEM DIVERGÊNCIA**: verificação executada sem nenhuma discrepância encontrada.
- **OBSERVAÇÃO**: ponto que merece decisão ou esclarecimento, sem afirmação de erro.
- **NÃO VERIFICADO**: não foi possível verificar com os meios e o escopo disponíveis.

## 6. Verificações executadas (somente documentais)

| # | Verificação | Método | Resultado |
|---|---|---|---|
| V1 | Inventário de arquivos e SHA-256 | `git ls-files`, `sha256sum` | Executada (§7) |
| V2 | Proveniência git de cada arquivo | `git show --stat` por commit | SEM DIVERGÊNCIA: cada original foi adicionado uma única vez e nunca mais modificado |
| V3 | Contagem e unicidade dos IDs na especificação | script (Apêndice A) | SEM DIVERGÊNCIA: 53 IDs únicos |
| V4 | Contagem e unicidade dos IDs na matriz CSV | script | SEM DIVERGÊNCIA: 53 linhas e 53 IDs únicos. O CSV tem um problema de formato (ver A-01) |
| V5 | Contagem dos cenários e mapeamento TC↔norma | script | SEM DIVERGÊNCIA: 53 TCs, bijeção `TC-<ID>` ↔ `<ID>` |
| V6 | Distribuição por domínio comparada ao AGENTS.md | script | SEM DIVERGÊNCIA: LAY 6, ACT 8, FRM 8, NAV 6, DAT 6, RSP 7, A11Y 7, FDB 5 |
| V7 | Igualdade campo a campo entre spec, CSV e catálogo | script | SEM DIVERGÊNCIA (detalhes em §8) |
| V8 | Coerência da governança entre AGENTS, STATUS, INVENTORY, REGISTRO e PARECER | leitura e `grep -n` | Achados A-03 e A-04 |
| V9 | Artefatos referenciados e ausentes | leitura e `grep` | Achados A-02 e A-05 |
| V10 | Prontidão para integração com Codex e Claude Code | listagem da estrutura e leitura do §8 da spec | Observações O-05 e O-06 |
| V11 | Codificação e formato dos arquivos | `file`, `od`, `grep -c $'\r'` | UTF-8 sem BOM e sem CR. Preâmbulo no CSV (A-01) |

**Não executado:** cenários em produto, testes visuais, interativos ou funcionais, validação WCAG contra a fonte oficial, ensaio de repetibilidade e descoberta ou execução de skills.

## 7. Inventário e hashes da cópia commitada (base `4321314`)

| Arquivo | Commit de entrada | SHA-256 |
|---|---|---|
| `framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md` | 80b51f6 | `4b5f2c33f8545c9a1bb8d3fa627fe1a2c76ebab4f964b96153099f64590ab39a` |
| `tests/scenarios/G1-CATALOGO-CENARIOS-v0.1.1.md` | 6d65f52 | `37c6d84ef09e534043e78be29383fce234186bdd332163535b273af5bd604be3` |
| `framework/traceability/G1-MATRIZ-BASELINE-v0.1.1.csv` | fd9132e | `0a1042c7eb6f1526b78449a747c5317ae8d4829ed7b0844f68c85d8b852ca101` |
| `docs/decisions/G1-REGISTRO-DECISOES-FECHAMENTO-v0.1.1.md` | 620f762 | `62df207bd91c8edfbb978fe24d74eb1557fab6d09ae65a41afbbf52c8a7ce87d` |
| `docs/decisions/G1-MAPA-SANEAMENTO-AUDITORIA-v0.1.1.md` | 7fa8c1e | `07a119e89db165ea4dedec5d1fc6971a4e7c990633a621d209213df1189a122e` |
| `docs/decisions/G1-PARECER-FECHAMENTO-v0.1.1-READONLY.md` | b0b85d3 | `dd036b38cd2db12971e827ab5a65cc477a67af488dc79ecc83f2e81fd2515510` |
| `framework/SOURCE-INVENTORY.md` | 92c5717 | `70c069dd0df25f17ed8cbe5d4935d347ce7ed7f20d07955c7cf250fbfe94437f` |
| `AGENTS.md` | e522a9a | `8bbba1261376429fc4a48f8ac2508a355d03b1311b7a569a93ecba9cbf87ed6e` |
| `docs/WORKFLOW.md` | fb1de86 | `6ffbd093a68b76d225bb8a8fe244107fb1f37d7c6b4486983e88c6836aa05671` |
| `docs/PROJECT-STATUS.md` | 71bfe07 | `ea942bf25aeb0b94b5755fa87b057e747f516036571eb5dd12615c7fcf0b8053` |
| `README.md` | dbc4e72 | `8df4a5f79aeeecffde54a55372ef9e0c93e8ae6f13358faeca4397015cd13976` |

Esses hashes servem **apenas como linha de base da cópia commitada**. Eles **não comprovam identidade com o pacote-fonte** `UI-UX-Standards-G1-v0.1.1-CANDIDATA-SANEADA.zip`, citado em `G1-PARECER-FECHAMENTO-v0.1.1-READONLY.md:4`. O zip não está no repositório e nenhum hash de referência foi fornecido. A comparação fica NÃO VERIFICADA.

## 8. Resultados da rastreabilidade (SEM DIVERGÊNCIA)

O script do Apêndice A extraiu cada bloco `### <ID>` da especificação, cada linha do CSV e cada bloco `## TC-<ID>` do catálogo. Resultados:

- **Conjuntos e ordem:** os IDs da spec e do CSV são iguais e estão na mesma ordem. O `index` do CSV é contínuo de 0 a 52. Todo TC aponta para uma norma existente, e toda norma tem exatamente um TC.
- **Igualdade campo a campo, nas 53 normas, sem nenhuma divergência:**
  - título da spec = `requisito` do CSV;
  - `Critério` da spec = `criterio_aceitacao` do CSV = `Resultado esperado` do TC;
  - `Métodos requeridos` da spec = `metodos_requeridos` do CSV = `Métodos` do TC;
  - `Nível` = `nivel`;
  - `Exceção original` = `excecoes`;
  - `WCAG relacionada` = `wcag_relacionada`;
  - `Caso manual` = `caso_teste` = `TC-<ID>`;
  - `Observável/protocolo` da spec = `Passos` do TC.
- **Níveis:** 30 Obrigatória e 23 Convencional. O `status_normativo` é `CANDIDATA` em todas as 53 linhas, coerente com a preservação do original candidato.
- **Mapeamento WCAG:** 12 normas mapeadas e 41 marcadas como "não mapeada diretamente". Os 18 SC distintos citados são: 1.3.1, 1.3.2, 1.4.1, 1.4.3, 1.4.4, 1.4.10, 1.4.11, 2.1.1, 2.1.2, 2.4.3, 2.4.7, 2.4.11, 2.5.3, 2.5.8, 3.3.1, 3.3.2, 3.3.3 e 4.1.2. A spec declara que o mapeamento é parcial (`spec:19`).
- **Execução:** o catálogo declara "53 cenários especificados, 0 executados" (`G1-CATALOGO-CENARIOS-v0.1.1.md:2`). Nenhum resultado de execução aparece no CSV.
- **Campos fixos:** Pré-condição, Evidência mínima e N/A estão presentes nos 53 TCs, com texto idêntico.
- **Nota (não é achado):** 44 TCs usam o passo genérico "Executar verificações <métodos>". Os outros 9 têm passos específicos: ACT-002, ACT-006, FRM-006, NAV-003, DAT-005, RSP-004, A11Y-004, A11Y-007 e FDB-004. Mesmo nesses 9, o campo `Métodos` confere com a spec e o CSV.

## 9. Achados comprovados

### A-01 — A matriz CSV não está em formato CSV válido
- **Evidência:** as linhas 1 e 2 de `framework/traceability/G1-MATRIZ-BASELINE-v0.1.1.csv` são `<PARSED TEXT FOR SHEET: 1 / 1 TABS` e `TAB NAME: G1-MATRIZ-BASELINE-v0.1.1.csv>`. O cabeçalho real (`index,id,dominio,...`) só aparece na linha 3. O arquivo tem 56 linhas (2 de preâmbulo, 1 de cabeçalho e 53 de dados) e não termina com quebra de linha.
- **Impacto:** quem ler o arquivo diretamente como CSV, por exemplo uma futura skill, recebe um cabeçalho errado. Os dados só foram validados neste relatório porque o script descartou as 2 primeiras linhas.
- **Não verificado:** a origem do preâmbulo e se o arquivo do pacote-fonte o contém. Nada foi corrigido, porque isso cabe a uma decisão do PO.

### A-02 — A lista de artefatos ausentes no `SOURCE-INVENTORY.md` está incompleta
- **Evidência:** `G1-PARECER-FECHAMENTO-v0.1.1-READONLY.md:9` declara que foram examinados "catálogo CSV/Markdown, ... esquema de evidência, changelog e README". Já `framework/SOURCE-INVENTORY.md:13-14` lista como não recuperados apenas o esquema de evidência, o README e o changelog.
- **Lacuna:** o **catálogo de cenários em CSV** também falta no repositório e não está registrado como ausente.

### A-03 — A homologação do G1 e a autorização do G2 não têm registro primário no repositório
- **Evidência:**
  - `AGENTS.md:10` diz que o G1 "was homologated with controlled caveats by the PO" e manda "record the later PO decision separately".
  - `AGENTS.md:11` diz que "G2 technical discovery is authorized".
  - `docs/PROJECT-STATUS.md:6` repete a homologação.
  - `framework/SOURCE-INVENTORY.md:3` remete a homologação a `G1-REGISTRO-DECISOES-FECHAMENTO-v0.1.1.md`. Esse registro, porém, diz o contrário: "NÃO HOMOLOGADO" (linha 5), "G2 não autorizado" (linha 6) e "a presente deliberação não é homologação" (linha 35).
- **Lacuna:** não existe no repositório um registro aditivo da decisão posterior do PO, com data, escopo e ressalvas aceitas, como o próprio `AGENTS.md:10` exige. A remissão do `SOURCE-INVENTORY.md:3` aponta para um documento que não contém essa decisão.
- **Não verificado:** a decisão em si, que segundo o `AGENTS.md` ocorreu "in the conversation", fora do repositório.

### A-04 — O `PROJECT-STATUS.md` e o `README.md` estão desatualizados
- **Evidência:**
  - `docs/PROJECT-STATUS.md:13` diz "Normative G1 source package not yet committed/verified here", mas os originais foram commitados entre `80b51f6` e `92c5717`.
  - `README.md:5` diz que a baseline "will be incorporated".
  - A pendência 1 (`PROJECT-STATUS.md:17`) continua parcialmente aberta, porque o esquema de evidência e a proveniência (hashes do pacote) não foram commitados.
- **Ressalva:** como a integridade contra a fonte não foi verificada (§7), a frase "not verified" continua correta. A parte "not committed" está desatualizada.

### A-05 — A saída mínima do Gate G1 não está completa no repositório
- **Evidência:** `spec:569` exige, entre outros itens, "modelo de evidência; changelog e mapa dos 12 achados".
  - O mapa está presente (`G1-MAPA-SANEAMENTO-AUDITORIA-v0.1.1.md`).
  - O **changelog está ausente**.
  - O modelo de evidência existe **apenas como prosa** no §3 da spec (`spec:23`). O esquema separado citado no PARECER:9 não está no repositório.
- **Consequência:** a classificação `SANEADO_DOCUMENTALMENTE` de AUD-05 e AUD-09 (`G1-MAPA-SANEAMENTO-AUDITORIA-v0.1.1.md:9,13`) só pode ser verificada parcialmente a partir do repositório.

## 10. Observações (sem afirmação de erro)

- **O-01 — Terminologia dos tipos de exceção.**
  - O GOV-003 (`spec:11`) define quatro tipos: não aplicabilidade, alternativa equivalente, waiver de convenção e conflito bloqueante.
  - A coluna `tipo_excecao` do CSV usa só dois valores, `ALTERNATIVA_EQUIVALENTE_OU_NA` (30) e `CONVENCAO_LOCAL` (23), e eles se derivam 1:1 do `nivel`.
  - Não há glossário que relacione os dois vocabulários. O PO deve esclarecer antes que skills consumam essa coluna.
- **O-02 — A "Evidência mínima" dos TCs é menor que o registro de execução do §3.** O texto comum aos 53 TCs omite campos que o §3 da spec exige: `run_id`, commit/versão, versão normativa, viewport/zoom, executor e data. É uma possível ambiguidade sobre qual dos dois prevalece num relatório de execução.
- **O-03 — Ausência de LICENSE.** O `README.md:3` diz "Open-source framework", mas o repositório não tem arquivo de licença. Isso é relevante para uma futura publicação, que depende de decisão do PO.
- **O-04 — Commits sem assinatura.** Todos os commits aparecem com `%G? = N`. A autoria só se apoia na configuração do git.
- **O-05 — Integração com Codex e Claude Code.**
  - Não existem `CLAUDE.md`, `.claude/`, `.codex/`, diretório de skills, manifests, esquema de evidência legível por máquina (JSON/YAML), template de registro de execução nem scripts de validação.
  - Os contratos de `ui-design`, `ui-audit` e `ui-code-review` existem apenas como prosa (`spec:573`). Não definem esquema de entrada e saída, códigos de erro, formato de achado nem versionamento.
  - Nesta sessão, o conteúdo do `AGENTS.md` foi entregue ao Claude Code pelo ambiente. Isso é **observação de sessão, não teste de descoberta**. A descoberta pelo Codex e por outras configurações do Claude Code fica NÃO VERIFICADA.
- **O-06 — Backlog e ressalvas sem artefato de acompanhamento.**
  - DEC-G1-002 manda registrar um "backlog versionado" de alterações não salvas, operações em lote e paginação.
  - DEC-G1-003 exige "evidência, responsável e decisão de aceite" para cada ressalva transferida.
  - Nenhum arquivo de backlog ou de acompanhamento dessas ressalvas existe no repositório. Até aqui, elas só aparecem como menção no `AGENTS.md:37` e no `PROJECT-STATUS.md:26`.

## 11. Itens NÃO VERIFICADOS

1. Identidade dos arquivos commitados com o pacote-fonte (zip ausente e sem hashes de referência).
2. Conteúdo dos artefatos ausentes: esquema de evidência, README do pacote, changelog e catálogo CSV.
3. A decisão de homologação do PO e a autorização do G2 (ambas fora do repositório).
4. Correção e suficiência dos 18 SC WCAG 2.2 citados, contra a fonte oficial W3C (transferida pela DEC-G1-003(d)).
5. Repetibilidade dos protocolos entre avaliadores ou agentes (FEC-02).
6. Execução de qualquer um dos 53 cenários e qualquer conformidade de produto.
7. Descoberta e funcionamento de skills ou adapters no Codex e no Claude Code.

## 12. Limitações

- A análise cobre só o conteúdo do repositório no commit `4321314`. Nenhuma fonte externa foi consultada.
- A extração por expressões regulares depende da formatação Markdown atual. Blocos fora do padrão `### <ID> — ` e `## TC-<ID> — <ID>` não seriam capturados. A contagem de 53 de cada lado e a bijeção reduzem esse risco, mas não o eliminam.
- O CSV foi lido descartando as 2 primeiras linhas (A-01).
- Não houve julgamento de mérito sobre o conteúdo normativo das regras.

## 13. Pendências recomendadas (para decisão do PO, sem execução aqui)

1. Fornecer o pacote-fonte, ou ao menos seus hashes, para fechar a integridade (§7, A-01, A-02).
2. Registrar num documento aditivo em `docs/decisions/` a homologação com ressalvas e a autorização do G2 (A-03).
3. Decidir sobre o preâmbulo do CSV: manter o arquivo como cópia recebida e criar à parte um CSV normalizado e derivado, ou recuperar o original (A-01).
4. Recuperar ou registrar como ausentes o changelog, o esquema de evidência e o catálogo CSV (A-02, A-05).
5. Atualizar o `PROJECT-STATUS.md` e o `README.md` (A-04).
6. Antes de implementar skills, definir esquemas formais para os contratos, o registro de execução e o glossário de `tipo_excecao` (O-01, O-02, O-05).

## 14. Arquivos alterados

- Criado: `tests/reports/2026-11-18-auditoria-documental-g1-claude.md` (este arquivo). Nenhum outro arquivo foi alterado.
- **Commit e push:** branch `g2/bootstrap-framework`, com base em `4321314`. O SHA do commit que contém este relatório não pode constar dele próprio; ele é informado na resposta de entrega.

## Apêndice A — Reprodução

Comandos de estado e inventário:

```bash
git rev-parse HEAD; git status --porcelain; git fetch origin; git rev-parse origin/g2/bootstrap-framework
sha256sum $(git ls-files | grep -v tests/reports)
for c in $(git rev-list --reverse HEAD); do git show --stat --format='%h %s' $c; done
git log --format='%h %G? %s'
head -c 200 framework/traceability/G1-MATRIZ-BASELINE-v0.1.1.csv | od -c
```

Script de verificação cruzada (`python3 -I xcheck.py <raiz-do-repo>`), mantido fora do repositório. Abaixo vai uma versão condensada, com a mesma lógica de extração e comparação; foram retiradas apenas algumas impressões de diagnóstico e de distribuição:

```python
import re, csv, io, sys, collections
root=sys.argv[1]
spec=open(root+'/framework/specification/UI-UX-FRAMEWORK-SPEC-v0.1.1-CANDIDATA.md',encoding='utf-8').read()
scen=open(root+'/tests/scenarios/G1-CATALOGO-CENARIOS-v0.1.1.md',encoding='utf-8').read()
raw=open(root+'/framework/traceability/G1-MATRIZ-BASELINE-v0.1.1.csv',encoding='utf-8').read()
lines=raw.split('\n')
print('CSV preamble lines:',lines[:2])
rows=list(csv.DictReader(io.StringIO('\n'.join(lines[2:]))))
print('CSV header:',list(rows[0].keys()))
print('CSV data rows:',len(rows))
for i,r in enumerate(rows):
    if None in r or any(v is None for v in r.values()): print('BAD FIELD COUNT row',i,r)
blocks=re.split(r'\n(?=### )',spec)
S={}
for b in blocks:
    m=re.match(r'### ([A-Z0-9]+-\d{3}) — (.+)',b)
    if not m: continue
    id_=m.group(1); d={'title':m.group(2).strip()}
    for k,lab in [('nivel','Nível'),('crit','Critério'),('met','Métodos requeridos'),('exc','Exceção original'),('wcag','WCAG relacionada \\(mapeamento parcial\\)'),('caso','Caso manual'),('prot','Observável/protocolo')]:
        mm=re.search(r'- \*\*'+lab+r':\*\* (.+)',b); d[k]=mm.group(1).strip() if mm else None
    if id_ in S: print('DUP spec',id_)
    S[id_]=d
print('spec IDs',len(S), collections.Counter(k.split('-')[0] for k in S))
T={}
for b in re.split(r'\n(?=## )',scen):
    m=re.match(r'## (TC-[A-Z0-9]+-\d{3}) — ([A-Z0-9]+-\d{3})',b)
    if not m: continue
    d={'rule':m.group(2)}
    for k,lab in [('pre','Pré-condição'),('steps','Passos'),('exp','Resultado esperado'),('met','Métodos'),('ev','Evidência mínima'),('na','N/A')]:
        mm=re.search(r'\*\*'+lab+r':\*\* (.+)',b); d[k]=mm.group(1).strip() if mm else None
    if m.group(1) in T: print('DUP TC',m.group(1))
    T[m.group(1)]=d
print('TC count',len(T))
C={r['id']:r for r in rows}
print('CSV unique ids',len(C), collections.Counter(k.split('-')[0] for k in C))
print('index seq ok:',[int(r['index']) for r in rows]==list(range(len(rows))))
print('sets equal spec/csv:',set(S)==set(C),set(S)-set(C),set(C)-set(S))
print('order equal spec/csv:',list(S)==[r['id'] for r in rows])
tcrules={v['rule'] for v in T.values()}
print('TC->rules equal spec:',tcrules==set(S), set(S)-tcrules, tcrules-set(S))
for tc,v in T.items():
    if tc!='TC-'+v['rule']: print('TC name/rule mismatch',tc,v['rule'])
def norm(x): return (x or '').replace(' ','').strip()
diff=collections.defaultdict(list)
for id_,s in S.items():
    c=C.get(id_,{}); t=T.get('TC-'+id_,{})
    if s['caso']!=f"TC-{id_} (ver catálogo de cenários).": diff['spec caso'].append((id_,s['caso']))
    if c.get('caso_teste')!='TC-'+id_: diff['csv caso'].append((id_,c.get('caso_teste')))
    if norm(s['met'])!=norm(c.get('metodos_requeridos')): diff['met spec/csv'].append((id_,s['met'],c.get('metodos_requeridos')))
    if norm(s['met'])!=norm(t.get('met')): diff['met spec/tc'].append((id_,s['met'],t.get('met')))
    if s['title'].rstrip('.')!=c.get('requisito','').rstrip('.'): diff['title/requisito'].append((id_,s['title'],c.get('requisito')))
    if s['crit']!=c.get('criterio_aceitacao'): diff['crit spec/csv'].append((id_,))
    if s['crit']!=t.get('exp'): diff['crit spec/tc'].append((id_,))
    if s['prot']!=t.get('steps'): diff['prot/steps'].append((id_,))
    if s['nivel'].split(' (')[0]!=c.get('nivel'): diff['nivel'].append((id_,s['nivel'],c.get('nivel')))
    if s['exc'].split(' — interpretar')[0]!=c.get('excecoes'): diff['exc'].append((id_,))
    w=s['wcag']; cw=c.get('wcag_relacionada')
    if not ((w=='não mapeada diretamente' and cw=='') or w==cw): diff['wcag'].append((id_,w,cw))
    for k in ('pre','steps','exp','met','ev','na'):
        if not t.get(k): diff['tc missing '+k].append(id_)
    mm=re.search(r'Executar verificações ([SVIF,]+) ',t.get('steps') or '')
    if mm and norm(mm.group(1))!=norm(t.get('met')): diff['steps vs met'].append((id_,mm.group(1),t.get('met')))
    if not mm: diff['steps no method mention'].append(id_)
for k,v in diff.items():
    print(f'\n### {k}: {len(v)}')
    for x in v: print('  ',x)
print('status_normativo',collections.Counter(r['status_normativo'] for r in rows))
print('nivel x tipo',collections.Counter((r['nivel'],r['tipo_excecao']) for r in rows))
```

Saída relevante obtida: 53 IDs na spec, 53 linhas no CSV e 53 TCs. Os conjuntos e a ordem são iguais. A única categoria de diferença listada foi `steps no method mention: 9` (nota em §8). As contagens são `CANDIDATA: 53`, `(Obrigatória, ALTERNATIVA_EQUIVALENTE_OU_NA): 30` e `(Convencional, CONVENCAO_LOCAL): 23`.
