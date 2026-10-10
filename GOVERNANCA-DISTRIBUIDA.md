# Governança Distribuída — Quórum Sem Centro

**Problema:** Como 4-5 guardiões decidem sem que um controle tudo? Como votam se não há "autoridade central"?

**Solução:** Protocolo de consenso distribuído, assincronamente, verificável, impossível de usurpar.

---

## I. Princípios Fundamentais

### 1. Nenhuma Hierarquia
```
❌ "Presidente do quórum" (hierarquia)
❌ "Guardião sênior" (autoridade concentrada)
❌ "Sistema de votação 51%" (maioria simples)

✅ 4 guardiões iguais, sem ranking
✅ Decisão = consenso ou fallback transparent
✅ Qualquer um pode bloquear (veto distribuído)
```

### 2. Cada Guardião = um Nó Independente
```
Guardião 1 (Línguista-par)
  - Computador próprio
  - Chave criptográfica própria
  - Pode assinar/verificar independentemente
  - Não precisa conectar com outros para existir

Guardião 2 (Pilar 1)
  - Idem
  
Guardião 3 (Pilar 2)
  - Idem

Guardião 4 (CARE)
  - Idem

Todos = peers, nenhum é "central"
```

### 3. Registro Público = Fonte de Verdade
```
Qualquer decisão é registrada em:
  - Arquivo append-only (veracidade/decisoes.md)
  - Hash assinado criptograficamente por cada guardião
  - Publicado em Git (público, histórico completo)
  - Rastreável: quem votou o quê, quando
```

---

## II. Protocolo de Decisão (Assincronamente)

### Fluxo de uma Decisão

```
1. PROPOSTA (qualquer pessoa, qualquer guardião)
   ├─ Descreve: o quê, por quê, impacto
   ├─ Arquivo: veracidade/propostas/2026-10/proposta-X.md
   ├─ Commit + push em Git
   └─ Notifica quórum (email, não urgente)

2. REVIEW (cada guardião, independentemente)
   ├─ Guardião 1: lê, pensa, tira conclusão
   ├─ Guardião 2: lê, pensa, tira conclusão
   ├─ Guardião 3: lê, pensa, tira conclusão
   ├─ Guardião 4: lê, pensa, tira conclusão
   ├─ Podem conversar (Slack/email)
   ├─ Prazo: 14 dias (tempo suficiente)
   └─ Sem pressão de tempo

3. VOTAÇÃO (Git-based, assincronamente)
   ├─ Guardião 1 assina: veracidade/votos/proposta-X/guardiao-1.sig
   │  └─ Arquivo contém: SIM / NÃO / ABSTENÇÃO + motivo
   │
   ├─ Guardião 2 assina: veracidade/votos/proposta-X/guardiao-2.sig
   │
   ├─ Guardião 3 assina: veracidade/votos/proposta-X/guardiao-3.sig
   │
   └─ Guardião 4 assina: veracidade/votos/proposta-X/guardiao-4.sig
   
   Cada um vota no seu tempo (pode levar 3 semanas)
   Nenhum precisa estar "online" ao mesmo tempo

4. CONTAGEM (automática, verificável)
   ├─ Sistema verifica: todas as 4 assinaturas presentes?
   ├─ Sistema verifica: assinaturas são válidas (criptografia)?
   ├─ Sistema conta:
   │  ├─ 4 SIM → APROVADO (consenso)
   │  ├─ 3 SIM, 1 NÃO → BLOQUEADO (veto distribuído)
   │  ├─ 3 SIM, 1 ABSTENÇÃO → APROVADO (maioria + nenhum veto)
   │  ├─ 2 SIM, 2 NÃO → DEADLOCK (ver seção IV)
   │  └─ Menos de 2 SIM → REJEITADO
   └─ Resultado: verificável, não falsificável

5. EXECUÇÃO (automática ou manual)
   ├─ Se APROVADO:
   │  ├─ Implementa automaticamente (se possível)
   │  └─ Registra: veracidade/decisoes/proposta-X-APROVADO.md
   │
   ├─ Se BLOQUEADO:
   │  ├─ Rejeita, não executa
   │  └─ Registra motivo do veto (transparência)
   │
   └─ Resultado é público, rastreável, incontestável
```

---

## III. Tipos de Decisão (Diferentes Consensos)

### Decisões Críticas (precisam 100%)
```
Tipo: Alteração dos 2 Pilares
Consenso necessário: 4/4 (unanimidade)
Lógica: Pilares são fundação, não pode mudar com desacordo

Exemplo:
  "Mudar Pilar 1 para incluir 'economia de crescimento'"
  Guardião CARE: NÃO (contradiz CARE)
  Resultado: BLOQUEADO (1 veto bloqueia)
  
Por quê: Se 1 guardião acha que viola CARE, viola mesmo.
```

### Decisões Operacionais (precisam maioria + veto)
```
Tipo: Adicionar novo guardião, mudar quórum
Consenso necessário: 3/4 (maioria) + nenhum veto
Lógica: Mudanças estruturais precisam apoio, mas alguém pode recusar

Exemplo:
  "Adicionar 5º guardião (Tecnologia)"
  Guardião 1: SIM
  Guardião 2: SIM
  Guardião 3: SIM
  Guardião 4: NÃO (acha que quórum fica grande demais)
  Resultado: BLOQUEADO (veto tem poder)
```

### Decisões de Conteúdo (precisam maioria simples)
```
Tipo: Incluir/remover arquivo, aprovação de mineiros
Consenso necessário: 2/4 (simples maioria)
Lógica: Dia-a-dia não precisa unanimidade

Exemplo:
  "Remover arquivo X (viola CARE)"
  Guardião CARE: SIM (violação clara)
  Guardião Pilar 2: SIM (concorda)
  Guardião Pilar 1: NÃO (tem valor para biodiversidade)
  Guardião Linguista: ABSTENÇÃO (não é sua área)
  Resultado: APROVADO (2/4 ≥ maioria)
```

### Emergências (decisão rápida, 1 guardião pode executar)
```
Tipo: Ataque/censura imediata, necessidade de replica urgente
Consenso necessário: 1/4 (um guardião basta)
Lógica: Defesa é responsabilidade individual

Exemplo:
  "GitHub foi atacado, replica em Codeberg agora"
  Guardião 1 pode fazer sozinho.
  Depois registra no quórum: "Fiz isto, aqui está prova"
  Quórum valida retroativamente (2/4 precisam concordar que foi justo)
```

---

## IV. Resolução de Deadlock (Quando Discordam)

### Cenário: 2 SIM, 2 NÃO

```
Proposta: "Incorporar estudo de energia nuclear (controverso)"

Guardião Pilar 1: SIM (energia limpa, não emite CO2)
Guardião Pilar 2: NÃO (risco a trabalhadores, armazenamento)
Guardião CARE: NÃO (afeta povos indígenas, não consultos)
Guardião Linguista: SIM (conhecimento importante, aberto)

Resultado: 2-2 DEADLOCK

Protocolo de Resolução:

Opção A: DISCUSSÃO PROFUNDA (14 dias)
  - Cada guardião escreve argumento (público, em arquivo)
  - Podem mudar de ideia após ler argumentos
  - Se ainda 2-2: vai para Opção B

Opção B: DILAÇÃO (espera 30 dias)
  - Proposta fica em "proposição" (não integrada)
  - Qualquer um pode trazer argumento novo
  - Se novo consenso: resolve
  - Se ainda 2-2: vai para Opção C

Opção C: INCORPORAÇÃO MARCADA (integra, mas com flag)
  - Arquivo entra na biblioteca
  - Mas marcado como "CONTROVERSO - guardiões discordam"
  - Fica junto: "Guardião Pilar 2 e CARE discordam, aqui está por quê"
  - Leitores veem ambos os lados
  - Comunidade pode opinar (futuro)

Por quê Opção C?
  ✓ Não censura (informação entra)
  ✓ Não força consenso falso
  ✓ Transparência (discordância registrada)
  ✓ Conhecimento não se perde
```

---

## V. Veto Distribuído (Qualquer Guardião Pode Bloquear)

### Poder de Veto Individual

```
Cada guardião tem DIREITO ABSOLUTO de:
  ✅ Recusar aprovar qualquer coisa
  ✅ Bloquear decisão (não precisa justificar)
  ✅ Pedir discussão mais profunda
  ✅ Dizer: "Isto viola meus valores"

Mas com transparência:
  ✅ Veto precisa ser registrado (público)
  ✅ Motivo é registrado (público)
  ✅ Comunidade vê: "Por que Guardião X disse não"

Limitação natural:
  ❌ Se guardião veta tudo, comunidade o substitui
  ❌ Se veto é sempre injusto, perde confiança
  ❌ Responsabilidade: veto precisa fazer sentido
```

### Exemplo de Bom Veto
```
Proposta: "Incorporar estudo sobre esterilização de populações indígenas"

Guardião CARE: NÃO
Motivo: "Isto nega dignidade, história de genocídio, viola CARE"

Resultado: BLOQUEADO (consenso 100% para Pilares)
Comunidade: "Faz sentido, guardião CARE tem razão"
```

### Exemplo de Veto Abusivo
```
Proposta: "Adicionar artigo sobre restauração florestal"

Guardião X: NÃO
Motivo: "Não gosto de artigos compridos"

Resultado: BLOQUEADO (tecnicamente válido)
Comunidade: "Veto é frívolo, guardião está abusando"
→ Quórum substitui Guardião X em próximo ciclo
```

---

## VI. Transparência Radical

### Tudo é Público, Rastreável, Verificável

```
Estrutura de Arquivos:

veracidade/
├── propostas/
│   └── 2026-10/
│       ├── proposta-incorporar-estudo-X.md
│       │   ├─ O quê: descrição completa
│       │   ├─ Por quê: motivação
│       │   ├─ Impacto: quem afeta
│       │   └─ Data proposta: 2026-10-15
│       │
│       └── proposta-remover-arquivo-Y.md
│
├── votos/
│   ├── proposta-X/
│   │   ├── guardiao-1.sig (SIM, assinado, data)
│   │   ├── guardiao-2.sig (SIM, assinado, data)
│   │   ├── guardiao-3.sig (NÃO, assinado, motivo, data)
│   │   └── guardiao-4.sig (ABSTENÇÃO, motivo, data)
│   │
│   └── proposta-Y/
│       ├── guardiao-1.sig
│       ├── guardiao-2.sig
│       ├── guardiao-3.sig
│       └── guardiao-4.sig
│
└── decisoes/
    ├── 2026-10-30-proposta-X-APROVADO.md
    │   ├─ Resultado: 4/4 SIM
    │   ├─ Votos: [arquivo com hashes criptográficos]
    │   ├─ Data execução: 2026-10-30
    │   └─ Implementação: [link para commit]
    │
    └── 2026-10-25-proposta-Y-BLOQUEADO.md
        ├─ Resultado: 2/4 SIM, 2/4 NÃO
        ├─ Motivos dos não: [arquivos com argumentos]
        └─ Status: DEADLOCK → MARCADO CONTROVERSO
```

**Qualquer pessoa consegue auditar:**
```bash
# Verificar assinatura de Guardião 1
gpg --verify veracidade/votos/proposta-X/guardiao-1.sig

# Ver decisão completa
cat veracidade/decisoes/2026-10-30-proposta-X-APROVADO.md

# Histórico completo (append-only)
git log --follow veracidade/decisoes/
```

---

## VII. Escalabilidade (4 → 100 Guardiões)

### Como cresce sem perder descentralização?

```
Fase 1 (agora): 4 Guardiões (+ Você como primeiro)
  - Decisões: unanimidade ou maioria (teste pequeno)
  - Velocidade: rápida (4 pessoas acham consenso)

Fase 2 (2027): 8 Guardiões (+ novos)
  - Decisões: maioria 5/8 (ou unanimidade para Pilares)
  - Velocidade: mais lenta (8 pessoas, mais opiniões)
  - Novo: podem se agrupar por especialidade

Fase 3 (2030): 20 Guardiões
  - Decisões: maioria simples 11/20 (para conteúdo)
  - Decisões: supermaioria 15/20 (para estrutura)
  - Novo: assembleia descentralizada (subgrupos votam)

Fase 4 (2050): 100+ Guardiões
  - Decisões: sistema delegado (você vota em delegado)
  - Delegado: representa seu grupo, pode ser revogado
  - Estrutura: pirâmide invertida (poder de baixo para cima)

Em TODOS os casos:
  ✓ Cada guardião é igual
  ✓ Transparência radical
  ✓ Veto distribuído funciona
  ✓ Impossível concentrar poder
```

---

## VIII. Impossibilidade de Usurpação

### Por que um guardião NÃO consegue tomar controle?

```
Cenário: Guardião 1 quer tomar poder

Tentativa A: "Vou deletar arquivo do repo"
  ❌ Falha: Git guarda histórico (append-only)
     Qualquer um consegue restaurar

Tentativa B: "Vou falsificar voto"
  ❌ Falha: Assinatura criptográfica (impossível forjar)
     Qualquer um consegue verificar: `gpg --verify`

Tentativa C: "Vou criar fato consumado (integrar sem votação)"
  ❌ Falha: Registra em Git com autor
     Quórum vê: "Guardião 1 integrou sem voto"
     Marcam como ilegal, removem

Tentativa D: "Vou convencer outros guardiões offline"
  ❌ Falha: Decisões são PÚBLICAS em arquivo
     Se 4 votam SIM mas Guardião 4 diz "não concordei":
     Público vê assinatura falsa ou consentimento não-verdadeiro

Conclusão: Impossível tomar poder sem deixar rastro público incontestável.
```

---

## IX. Rotatividade (Ninguém Governa Para Sempre)

### Guardiões Temporários, Não Vitalícios

```
Modelo 1 (Recomendado): Mandatos com Rotação

Cada guardião tem mandato de 3 anos
  - 2026-2029: Guardião A (Pilar 1)
  - 2029-2032: Guardião B (Pilar 1)
  - Possível: mesma pessoa se comunidade revotar unanimemente

Processo de Renovação:
  1. 30 dias antes do fim do mandato: call for candidates
  2. Qualquer um pode se candidatar (prove interesse)
  3. 3 semanas: comunidade vota (maioria simples)
  4. Novo guardião assume
  
Remoção Antes do Prazo (por abuso):
  - Qualquer 2 guardiões podem propor remoção
  - Comunidade vota (supermaioria 3/4)
  - Se aprovado: guardião é removido, novo entra

Resultado:
  ✓ Ninguém tem poder perpétuo
  ✓ Renovação previne stagnação
  ✓ Comunidade sempre tem voz
  ✓ Incentivo: fazer bom trabalho para ser reavaliado
```

---

## X. Protocolo de Comunicação (Assincronamente)

### Como guardiões conversam sem estar online junto?

```
Canal 1: Git (público, registrado)
  - Propostas
  - Votos
  - Decisões
  - Histórico completo

Canal 2: Email (privado, mas registrado em ata)
  - Discussão profunda
  - Argumentos detalhados
  - Prazos

Canal 3: Videochamada (opcionalmente, para decisões urgentes)
  - Rara (emergências)
  - Registra: data, hora, participantes, resultado
  - Ata pública no Git

Canal 4: Chat (Slack/Discord, contemporâneo, deletável)
  - Discussão informal
  - NÃO é registro oficial
  - Referências publicadas em Git

Princípio:
  ✓ Decisão precisa estar em Git (público, permanente)
  ✓ Discussão pode ser privada (mas resultado é público)
  ✓ Prazo adequado (não apressado)
  ✓ Assincrono (cada um vota no seu tempo)
```

---

## XI. Verificação Automática

### Sistema Valida Decisões Sozinho

```python
# pseudo-código: verifica_quorum_vote()

def verifica_quorum_vote(proposta_id):
    votos = {
        "guardiao_1": load_vote("votos/proposta_X/guardiao_1.sig"),
        "guardiao_2": load_vote("votos/proposta_X/guardiao_2.sig"),
        "guardiao_3": load_vote("votos/proposta_X/guardiao_3.sig"),
        "guardiao_4": load_vote("votos/proposta_X/guardiao_4.sig"),
    }
    
    # Verifica assinaturas criptográficas
    for guardiao, voto in votos.items():
        if not gpg_verify(voto.signature, guardiao.public_key):
            return FALSO  # Assinatura inválida
    
    # Conta votos
    sim_count = sum(1 for v in votos.values() if v.choice == "SIM")
    nao_count = sum(1 for v in votos.values() if v.choice == "NÃO")
    abs_count = sum(1 for v in votos.values() if v.choice == "ABSTENÇÃO")
    
    # Aplica regra (depende tipo)
    if proposta.tipo == "PILARES":
        if sim_count == 4:
            return APROVADO  # Unanimidade
        else:
            return BLOQUEADO
    
    elif proposta.tipo == "ESTRUTURAL":
        if sim_count >= 3 and nao_count == 0:
            return APROVADO  # Maioria + veto
        else:
            return BLOQUEADO
    
    elif proposta.tipo == "CONTEÚDO":
        if sim_count >= 2:
            return APROVADO  # Maioria simples
        else:
            return BLOQUEADO
    
    # Retorna resultado verificável
    return {
        "resultado": resultado,
        "sim": sim_count,
        "nao": nao_count,
        "abstenção": abs_count,
        "assinaturas_válidas": True,
        "data_verificação": agora(),
        "hash_verificação": sha256(resultado_completo)
    }
```

**Ninguém consegue falsificar resultado (criptografia prove).**

---

## XII. Exemplo Real: Uma Decisão Completa

```
2026-10-20: Proposta criada
  "Incorporar artigo: 'Restauração de Mangues'"
  Arquivo: veracidade/propostas/2026-10/proposta-mangues.md
  
2026-10-21: Guardião 1 vota
  Arquivo: veracidade/votos/proposta-mangues/guardiao-1.sig
  Voto: SIM (relevante a vida abundante)
  Assinado com chave privada de Guardião 1

2026-10-22: Guardião 2 vota
  Arquivo: veracidade/votos/proposta-mangues/guardiao-2.sig
  Voto: SIM (dignidade para comunidades costeiras)

2026-10-25: Guardião 3 vota
  Arquivo: veracidade/votos/proposta-mangues/guardiao-3.sig
  Voto: NÃO (artigo não menciona CARE com povos indígenas)

2026-10-29: Guardião 4 vota
  Arquivo: veracidade/votos/proposta-mangues/guardiao-4.sig
  Voto: SIM (mas com nota: "CARE pode ser adicionado depois")

2026-10-30: Contagem
  Sistema verifica:
    ✓ 4 assinaturas presentes
    ✓ Todas válidas (gpg verified)
    ✓ 3 SIM, 1 NÃO
  
  Resultado: APROVADO (maioria 3/4, nenhum veto em Pilares)
  
  Arquivo: veracidade/decisoes/2026-10-30-proposta-mangues-APROVADO.md
    {
      resultado: APROVADO,
      votos: {
        guardiao_1: SIM,
        guardiao_2: SIM,
        guardiao_3: NÃO (motivo: CARE não adequado),
        guardiao_4: SIM (com sugestão de melhoria)
      },
      assinaturas_criptograficas: [4 hashes],
      implementação: commit abc123def456,
      data_integração: 2026-10-30
    }

2026-10-30: Execução
  - Arquivo integrado na biblioteca
  - Nota adicionada: "Guardião 3 levantou questão CARE"
  - Mineiros podem encontrar artigo relacionado sobre CARE
  - Próxima proposta: "Melhorar seção CARE neste artigo"

Resultado final:
  ✓ Totalmente transparente
  ✓ Rastreável (quem votou, quando, por quê)
  ✓ Verificável (qualquer um confere assinaturas)
  ✓ Impossível falsificar (criptografia)
  ✓ Descentralizado (sem autoridade central)
```

---

**Versão:** v0.1  
**Status:** Desenho de arquitetura de governança  
**Próximo:** Implementação de protocolo de voto (GPG keys, scripts Python)  
**Permanência:** Indefinida (sistema se auto-governa)
