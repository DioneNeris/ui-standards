# PO — Registro aditivo de decisões G1/G2

**Data de registro:** 2026-11-18. **Autoridade declarada:** Product Owner, em conversa com ChatGPT. **Natureza:** transcrição resumida de decisões comunicadas fora do repositório; não é assinatura digital nem comprovação independente da identidade do decisor.

## Sequência das decisões

1. Após o parecer candidato de fechamento, o PO declarou expressamente: **“Homologo G1 da especificação normativa V0.1.1 com as ressalvas e pendências registradas.”** Essa manifestação é posterior ao documento histórico `G1-REGISTRO-DECISOES-FECHAMENTO-v0.1.1.md`, que permanece corretamente marcado como não homologado à época de sua emissão.
2. O PO autorizou o prosseguimento controlado do **G2 — discovery técnico e validação**, sem autorização geral para implementar skills ou alterar normas.
3. Em 2026-11-18, após receber as auditorias independentes Codex (`4321314`) e Claude Code (`c6ff988`), o PO respondeu **“sim”** à pergunta que propunha **homologar os dois relatórios como evidência de auditoria documental cruzada** e **autorizar saneamento documental controlado**, expressamente **sem implementação de skills e sem merge na `main`**.

## Alcance e limites

- A homologação documental G1 v0.1.1 mantém as 53 normas e 53 cenários, com ressalvas DEC-G1-001 a 003, incluindo WCAG 2.2 AA como **alvo**, não certificado.
- Homologar os relatórios significa aceitá-los como evidência da rodada de verificação documental, **não** declarar identidade do pacote-fonte, execução de cenários, conformidade WCAG, paridade operacional de skills ou encerramento G2.
- O saneamento pode atualizar documentação operacional, criar inventários, backlog e artefatos **derivados identificados**, e especificar contratos **propostos**. Não pode alterar originais candidatos, inventar arquivos ausentes, implementar skills ou fazer merge.
- A proveniência primária permanece na conversa do PO, não reproduzida integralmente no GitHub. Este registro fornece rastreabilidade secundária explícita, sem alegar prova independente.

## Evidências de auditoria

- `tests/reports/2026-11-18-auditoria-documental-g1.md` — Codex, commit `4321314a2be917fae455ee22591c02724ac1f07d`.
- `tests/reports/2026-11-18-auditoria-documental-g1-claude.md` — Claude Code, commit `c6ff988bf0069e73e8f6a11138d7c73f120a0b8f`.

**Gate G2:** aberto. **Implementação:** não autorizada. **Merge `main`:** não autorizado.
