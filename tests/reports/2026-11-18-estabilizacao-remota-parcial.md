# Estabilização remota V1 — alterações iniciais (2026-11-18)

**Estado: IMPLEMENTAÇÃO PARCIAL; TESTES NÃO EXECUTADOS NESTE AMBIENTE.** Branch `g2/bootstrap-framework`. Autorização do PO para correções A1–A4 e testes controlados. Nenhuma homologação de V1 ou liberação para projetos reais.

## Mudanças realizadas

- **A1:** `uistandards/validation.py` passa a aceitar diagnóstico `BLOQUEADA` com `rules=[]` quando a baseline era inacessível ao executor, mesmo se o checkout do validador está íntegro. Requer erros e limitações, identidade do request e baseline, ausência de findings/evidence/changed_files. Não cria resultado de conformidade. Acrescentados testes de regressão positivos e negativos em `tests/contracts/test_validation.py`.
- **A2:** documentação compartilhada e texto gerado por `scripts/install.py` esclarecem que `baseline-commit` é identidade histórica da fonte e HEAD mais recente não é conflito.
- **A3:** `scripts/validate.py` aceita `--file -` para stdin (request/result) e `--request -` para request por stdin, recusando ambos simultaneamente. Hash de request continua calculado sobre bytes recebidos.
- **A4:** documentação instrui comandos individuais, caminhos preaprovados e nenhuma expansão automática da allowlist. Não foi alterada a política efetiva de sandbox.

## Evidências e limitações

Os arquivos foram atualizados diretamente pela API de conteúdo do GitHub. O ambiente de execução disponível não conseguiu clonar o repositório (`Could not resolve host: github.com`); **nenhum teste automatizado, teste CLI, ensaio adversarial, ensaio de agentes ou instalação via pip foi executado nesta rodada**. O sucesso das operações de commit não prova funcionamento do código. As alterações devem ser submetidas a testes e revisão antes de aceite.

**Pendências:** executar regressões e CLI com stdin; verificar diagnóstico bloqueado usando fixture real do Claude; ensaiar `ui-design`, isolamento read-only e instalação venv/pip/lock; comparar resultados de agentes. A documentação de stdin não garante que um agente sem ferramenta de escrita consiga encaminhar bytes inline ao processo em todos os ambientes. A integridade da baseline G1 original não foi revalidada nesta sessão, embora os commits realizados não tenham editado seus caminhos.

## Reprodução pendente

```sh
python3 -m unittest discover -s tests/contracts -v
python3 scripts/validate.py baseline --package-root . --json
python3 scripts/validate.py request --package-root . --file request.json
python3 scripts/validate.py result --package-root . --file - --request request.json < result.json
```

**Veredito:** correções iniciais publicadas, validação técnica **NAO_VERIFICADA**. Não usar em projeto real.
