# Infraestrutura de desenvolvimento

> Documento para agentes de IA e pessoas que trabalham neste projeto. Conferido em 22/11/2026. Visão geral da infraestrutura: repositório privado **DioneNeris/devbox-oci** (na VPS: `~/devbox-oci`).

## Onde este projeto está

| Item | Valor |
|---|---|
| Pasta na VPS de dev | `~/projects/ui-standards` |
| Repositório | `DioneNeris/ui-standards` (privado) |
| Branch de trabalho | `g2/bootstrap-framework` |
| Tipo | framework/biblioteca Python (padrões de UI, validadores, skills). **Não é um app publicado**: não tem ambiente de teste no Easypanel nem produção |

## Ambiente

O desenvolvimento acontece na **VPS de dev da Oracle** (host `oracle-dev`, Ubuntu 24.04 ARM64). O antigo WSL foi desativado. **Onde o `AGENTS.md` disser "WSL", leia "VPS de dev"** (`~/projects/ui-standards`).

Disponível: Python 3 (+ `python3 -m venv`), Git, GitHub CLI autenticado e os agentes Claude Code, Codex e Antigravity.

```bash
cd ~/projects/ui-standards
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements-lock.txt
python scripts/validate.py --help     # validadores do framework
```

## Regras

- Siga o fluxo de revisão do `AGENTS.md`: trabalho em branch de revisão, sem merge na `main`, sem tag e sem force-push sem autorização explícita.
- Infraestrutura com problema: rode `devbox-check` e veja `~/devbox-oci/06-recuperar-conexoes.md`.
