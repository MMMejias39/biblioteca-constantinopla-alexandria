# Visena — Processo vivo v0.1

1. **Versão**: como software — v0.1 hoje; mudanças registradas e datadas; nada é alterado retroativamente sem aviso.
2. **Corpus**: toda frase oficial da biblioteca é bilingue (português — Visena) e entra no acervo.
3. **Distribuição**: pacote offline Kiwix (`.zim`) com léxico, gramática e frases — a língua viaja pelo protocolo de preservação.
4. **Revisão por pares com linguista-par**: cada nova raiz precisa de (a) raiz internacional reconhecível, (b) teste das sete regras ecológicas, (c) registro de quem propõe e de quem valida.
5. **Uso em ato**: uma frase nova por encontro comunitário — língua se aprende conviver, não memarizando.

## Registro de mudanças
- **2026-10-02 (v0.2)**: proposta de raiz **es** (ensinar-aprender recíproco) e composição **luse** (despertar da consciência); regras 8–9 (poder testemunhado; posição ≠ posse). Origem: carta-da-convivencia.md (guardião do poder; educação-libertação). Testadas nas 7 regras ecológicas: sem violação. Validação por línguista-par: **pendente**.
- **2026-10-02 (v0.3)**: regra 10 (proibição de poder anônimo em nome de "a comunidade" — contra seita, fascismo e nacionalismos étnicos). Origem: carta (O limite da comunidade). Sem violação das regras ecológicas. Validação por línguista-par: **pendente**.
- **2026-10-02 (v0.4)**: frase `Ve; ne mi; ne nu.` (regra de perpetuação de definições; axioma: verdade independente de tempo ou pessoa). Nenhuma raiz nova. Validação por línguista-par: **pendente**.
- **2026-10-03 (HMF)**: `schema/alp-config.yaml` + `schema/pos_decodificar.py` — config alp-data (v1.10.0, MIT, verificação 2026-10-03) + hook pós-decodificação: evidencial pela origem do rótulo (ve/so/ao/su — `si` nunca por máquina), `confianca` automática pelo score (≥ 0,80 = gran), distress generoso (prioridade alta sempre), atuação proibida (confinar/capturar/…) recusada e registrada. Sem raiz nova. Validação por línguista-par: **pendente**.
- **2026-10-11 (v0.5)**: três correções e uma decisão de desenho, ao escrever `manual.md` (pedagogia expõe o que a referência dispersa deixava passar):
  - `gramatica.md` regra 3 passa a listar **su** como evidencial (já estava em `lexico.md`, `hmf.md` e `validar.py`; a gramática estava desatualizada em relação ao próprio schema).
  - **Decisão de desenho (provisória)**: regra 3 (evidencial obrigatório) se aplica a **afirmações factuais sobre o mundo** — saudações, convites (`va`), perguntas (`ki`), recusas (`ne`) e lemas ficam isentos, por não serem afirmações factuais. Motivo: o corpus de `frases.md` já seguia essa leitura na prática (`Mi grat.`, `Ni ku ona.`, `Dig per ona.` nunca tiveram evidencial) sem a regra escrita dizer isso — a regra estava mais estreita que o uso real. Nenhuma raiz nova. Validação por línguista-par: **pendente**.
  - Correção de erro de digitação em `frases.md`: `Te pos gra be ao.` → `Te pos gra**n** be ao.` (gloss "abundante" = **gran**, não existe raiz "gra").
  - Limpeza de nota de rascunho não resolvida em `lexico.md` (`an-pe pessoa de outro tipo? não: pe já cobre`) e de seta de edição esquecida em `frases.md` (`Tu si si-ne? → Tu si be?`), ambas substituídas pela forma final única.
