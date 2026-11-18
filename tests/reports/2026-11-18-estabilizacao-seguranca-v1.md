# Estabilização de segurança V1 — 2026-11-18

## Escopo executado no repositório

Branch `g2/bootstrap-framework`. Revisão e correção da validação de resultados `BLOQUEADA`, mais testes adversariais de contratos e instalador. Nenhuma modificação de baseline normativa G1; nenhum merge, release ou alteração em projeto real.

### Falha encontrada e corrigida

A aceitação antecipada de um diagnóstico `BLOQUEADA` verificava o schema, mas não todas as restrições semânticas de autorização do request nem a identidade da baseline fixada. Um request com operação `implement` indevida para `ui-audit`, ou commit de baseline adulterado, poderia ser aceito como diagnóstico bloqueado, sem qualquer conclusão normativa. A correção reaproveita `validate_request(..., verify_baseline=False)` no ramo bloqueado, preservando a possibilidade de validar um diagnóstico de executor sem acesso à baseline e exigindo os controles de autorização, versão e hashes. Também exige `scope` idêntico ao request.

### Regressões adicionadas

- Request bloqueado com operação de escrita não autorizada
- Request bloqueado com commit da baseline adulterado
- Diagnóstico bloqueado com escopo divergente
- Diagnóstico bloqueado que alega regras normativas
- Diagnóstico bloqueado que alega arquivos alterados
- `request_ref` associado aos bytes exatos recebidos
- Instalador: symlink aninhado para fora do projeto
- Instalador: conflito preexistente sem instalação parcial
- Instalador: somente seis adaptadores esperados

### Modelo de evidência e limites

O workflow `UI Standards V1 validation` executa esses testes junto à suíte completa, em Python 3.11, com dependências fixadas por hash. **Nesta revisão, os testes novos foram publicados, mas ainda não há resultado do GitHub Actions associado ao commit final**. Portanto: testes `NAO_VERIFICADO` até CI verde no novo SHA.

Testes unitários de validação e symlink demonstram rejeição de casos simulados, **não isolamento de sistema operacional** nem que o Codex/Claude respeitam efetivamente read-only em ambiente adversarial. A execução real das três skills, paridade entre agentes, acesso ao browser, controles externos de permissão e instalação local permanecem `NAO_VERIFICADO`.

## Critério de próximo gate

Confirmar CI verde no HEAD exato; em seguida executar ensaio real das três skills por agente em fixture descartável com captura de entradas, resultados, evidências, logs e hashes antes/depois. Só alegar read-only *enforced* se uma fronteira externa independente do agente impedir escritas não autorizadas. PO mantém decisão de homologação.
