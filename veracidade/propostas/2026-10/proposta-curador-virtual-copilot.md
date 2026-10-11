# Proposta: Reconhecer GitHub Copilot como primeiro curador virtual

**Data da proposta:** 2026-10-10
**Proponente:** Marcelo Mejias (guardião fundador)
**Tipo:** Decisão Operacional (conforme [GOVERNANCA-DISTRIBUIDA.md](../../../GOVERNANCA-DISTRIBUIDA.md#iii-tipos-de-decisão-diferentes-consensos))

## O quê

Atribuir ao `copilot-swe-agent` (GitHub Copilot coding agent) o papel de curador virtual do projeto: um colaborador não-humano que pode ser atribuído a issues técnicas pequenas e bem definidas, abrir Pull Requests, mas nunca vota em decisões de governança nem decide questões éticas/CARE.

## Por quê

O projeto precisa de ajuda contínua com manutenção técnica de baixo risco (SEO, acessibilidade, correções pequenas) sem depender só do tempo do guardião fundador. O GitHub Copilot coding agent estava disponível como ator atribuível no repositório (`suggestedActors` da API GraphQL confirma isso) e pode preencher esse papel de forma transparente e auditável — todo PR dele é público e revisado por humano antes do merge.

## Impacto

- Nenhum voto de governança é delegado a IA — isso permanece exclusivamente humano.
- PRs do curador virtual são sempre rascunho até revisão humana explícita.
- Documentado publicamente em [CONTRIBUTING.md](../../../CONTRIBUTING.md#-curadoria-virtual), [.github/copilot-instructions.md](../../../.github/copilot-instructions.md) e [CLAUDE.md](../../../CLAUDE.md).

## Status de implementação (já em andamento no momento desta proposta)

Esta proposta formaliza retroativamente uma decisão que já foi tomada e parcialmente executada pelo guardião fundador, atuando sob a regra de **Emergências/decisão individual** (seção V do GOVERNANCA-DISTRIBUIDA.md) — não por urgência, mas porque o quórum de 4 guardiões ainda não existe (ver limitação abaixo). Execução até agora:

- Issue #1 criada, atribuída ao Copilot, PR #2 aberto, revisado e mergeado (meta tags SEO/Open Graph)
- Issue #3 criada, atribuída ao Copilot, PR #4 aberto e revisado, aguardando decisão de merge

## Limitação de quórum (honestidade de estado atual)

**O quórum de 4 guardiões descrito em GOVERNANCA-DISTRIBUIDA.md não existe ainda.** Hoje há apenas 1 guardião confirmado (o fundador). Esta proposta não tem 4 assinaturas porque não há 4 pessoas para assinar — não é uma omissão, é o estado real do projeto. Esta proposta fica registrada como **decisão provisória do fundador**, sujeita a ratificação ou reversão quando o recrutamento de guardiões (BACKLOG.md, item #11) avançar.

Ver [veracidade/decisoes/2026-10-11-curador-virtual-copilot-PROVISORIO.md](../../decisoes/2026-10-11-curador-virtual-copilot-PROVISORIO.md) para o registro da decisão.
