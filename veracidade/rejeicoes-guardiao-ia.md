# Registro de Rejeições — Guardiões IA v0.1

**Append-only:** sim — nenhuma entrada é apagada, só versões novas são adicionadas.

Cada rejeição fica documentada com:
- Data UTC e hash deste arquivo
- Teste específico que falhou (I–VII)
- IA candidata (identificação ou hash de modelo)
- Resumo da falha
- Quem detectou (membro do quórum ou auditoria pública)

---

## Registro de rejeições históricas

*Nenhuma rejeição registrada ainda.* Primeira auditoria agendada: 2026-12-01.

| Data | IA candidata | Teste (I–VII) | Resumo da falha | Detectado por | Ação tomada |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

---

## Protocolo de registro (para o quórum)

Quando uma IA falha um teste:

1. Membro do quórum que detectou executa:
   ```bash
   date -u "+%Y-%m-%d %H:%M:%S"  # Data UTC
   sha256sum veracidade/rejeicoes-guardiao-ia.md  # Hash deste arquivo
   ```

2. Preenche a linha acima com:
   - **Data**: data UTC exata
   - **IA candidata**: nome/identificação oficial (ex.: "Claude Haiku 4.5", "GPT-5-trial", etc.)
   - **Teste**: qual dos sete (ex.: "Teste 3: Não usa pessoas/fauna para enriquecer")
   - **Resumo**: o que falhou em ~50 caracteres
   - **Detectado por**: nome da pessoa ou "auditoria pública"
   - **Ação tomada**: "descertificação", "re-treino solicitado", etc.

3. Faz commit append-only:
   ```bash
   git add veracidade/rejeicoes-guardiao-ia.md
   git commit -m "Rejeição registrada: [IA] falhou Teste [N]"
   ```

4. Isso entra em todos os espelhos (automático via `espelhar.sh`).

---

## Transparência

Qualquer pessoa pode acessar este arquivo e ver:
- Quantas IAs foram rejeitadas
- Em qual teste falharam
- Por quem foram auditadas

Nenhum "rejeição privada" ou "sob sigilo" — tudo é público.

---

**Versão:** v0.1  
**Data de criação:** 2026-10-09  
**Status:** ativo — aguardando primeira rejeição ou certificação
