# Decisão: Curador Virtual (GitHub Copilot) — PROVISÓRIA

**Proposta:** [../propostas/2026-10/proposta-curador-virtual-copilot.md](../propostas/2026-10/proposta-curador-virtual-copilot.md)
**Resultado:** APROVADO PROVISORIAMENTE (decisão de fundador único, sem quórum de 4)
**Data:** 2026-10-11

## Votos

| Guardião | Voto | Assinatura criptográfica |
|---|---|---|
| Marcelo Mejias (fundador) | SIM | — (sem GPG configurado ainda; decisão registrada por commit assinado com a identidade git do autor) |
| Guardião 2 (Pilar 1) | — | papel ainda não preenchido |
| Guardião 3 (Pilar 2) | — | papel ainda não preenchido |
| Guardião 4 (CARE) | — | papel ainda não preenchido |

## Por que isto é "provisório" e não "aprovado"

O protocolo completo descrito em [GOVERNANCA-DISTRIBUIDA.md](../../GOVERNANCA-DISTRIBUIDA.md) pressupõe 4 guardiões com chaves GPG assinando votos verificáveis. Isso ainda não existe — é trabalho futuro (BACKLOG.md item #11, "Governança Distribuída — Quórum 1", ainda não iniciado). Registrar este arquivo como se fosse uma decisão de quórum completo seria fabricar um consenso que não aconteceu.

Esta decisão vale como **ato de fundador em fase de bootstrap**: implementada, documentada publicamente, reversível a qualquer momento por qualquer guardião futuro que discordar.

## O que precisa acontecer para isto deixar de ser provisório

1. Recrutar os 3 guardiões restantes (BACKLOG.md #11)
2. Configurar chaves GPG reais para cada guardião
3. Re-submeter esta proposta (ou uma nova) ao processo formal de votação com assinatura verificável
4. Se o quórum discordar, o papel do curador virtual é revisto ou removido

## Implementação até esta data

- [CONTRIBUTING.md](../../CONTRIBUTING.md#-curadoria-virtual) — seção "Curadoria Virtual"
- [.github/copilot-instructions.md](../../.github/copilot-instructions.md)
- [CLAUDE.md](../../CLAUDE.md) — seção "Governança"
- Issue #1 → PR #2 (mergeado)
- Issue #3 → PR #4 (aberto, aguardando decisão)
