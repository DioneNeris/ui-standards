# V1 piloto — instruções de avaliação

**Estado: trabalho em validação; não usar em projetos reais até revisão independente e conclusão dos critérios pendentes em `tests/reports/`.** A G1 é fonte normativa; o contrato V1 e a autorização do PO são registrados em `framework/contracts/G2-CONTRATO-V1-CANDIDATO.md` e `docs/decisions/2026-11-18-PO-V1-PILOTO.md`. Proveniência do ZIP externo não verificada; não inferir conformidade WCAG.

Pré-requisitos pretendidos: Python 3.11+ com `venv` e `pip`, Git e as dependências fixadas em `requirements-lock.txt`. Em ambiente autorizado, com acesso ao índice escolhido:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-lock.txt
.venv/bin/python -m unittest discover -s tests/contracts -v
.venv/bin/python scripts/validate.py baseline --package-root . --json
.venv/bin/python scripts/install.py --package-root . --project-root /caminho/projeto-descartavel --agents codex,claude --dry-run
.venv/bin/python scripts/install.py --package-root . --project-root /caminho/projeto-descartavel --agents codex,claude
```

O diretório alvo deve existir e a instalação requer autorização específica. O instalador não substitui arquivos existentes diferentes; reexecutá-lo com o mesmo pacote verifica idempotência. Para atualização, compare e remova manualmente apenas adaptadores gerados cuja substituição foi autorizada, depois instale novamente; não apague arquivos de terceiros. Mantenha disponível a cópia local do pacote apontada pelos adaptadores. O instalador verifica a baseline, mas ainda não fornece atestação criptográfica completa dos scripts/skills instalados nem atualização automática segura.

`schemas/v1/request.schema.json` e `result.schema.json` definem estrutura; o validador executa também verificações semânticas:

```sh
.venv/bin/python scripts/validate.py request --package-root . --file request.json
.venv/bin/python scripts/validate.py result --package-root . --file result.json --request request.json
.venv/bin/python scripts/report.py --package-root . --request request.json --result result.json
```

O relatório é impresso em stdout. Sua gravação em arquivo requer autorização explícita e verificação do destino pelo operador. A referência `request_ref` é SHA-256 dos bytes exatos do arquivo request. Os fixtures em `tests/contracts/fixtures.py` demonstram objetos parciais; são dados sintéticos, não evidência de produto. JSON Schema e hashes não avaliam automaticamente a suficiência substantiva de uma observação: o avaliador deve justificá-la. Uma string de autorização não impõe sandbox; somente executar uma auditoria quando o ambiente realmente impedir escrita no produto e em dados. `ui-design` em modo de implementação precisa de autorização específica para o produto e caminhos. O instalador usa caminhos de projeto `.agents/skills` e `.claude/skills`; reinicie a sessão e confira a descoberta no agente. A leitura do pacote pelo agente precisa estar permitida pelo ambiente. Testes de descoberta não equivalem a uma avaliação de interface.
