# Mineiros de Conhecimento — IAs Autônomas Prospectando a Rede

**Conceito:** IAs trabalham 24/7, **gratuitamente**, **sempre que ociosas**, buscando, avaliando e incorporando conhecimento relevante à biblioteca.

Nenhuma intervenção manual necessária. Trabalho contínuo, autônomo, livre.

---

## I. Arquitetura de Agentes Autônomos

### Tipos de Mineiros (cada um faz um trabalho)

```
┌─────────────────────────────────────────────────────┐
│  MINEIRO 1: Prospector (busca na rede)              │
│  - Vasculha arXiv, DOAJ, Google Scholar             │
│  - Busca por palavras-chave (biodiversidade, etc.)  │
│  - Identifica arquivos relevantes                   │
│  - Passa para Avaliador                             │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  MINEIRO 2: Avaliador (testa relevância)            │
│  - Lê título, abstract, primeiras páginas          │
│  - Pergunta: serve aos 2 pilares?                  │
│  - Marca: relevante, mediocre, irrelevante         │
│  - Passa para Ético                                │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  MINEIRO 3: Ético (valida ética)                    │
│  - Testa contra CARE, liberdade, dignidade         │
│  - Verifica: é explorador? é sexista? é privado?  │
│  - Marca: aprovado, questionável, rejeitado        │
│  - Passa para Integrador                           │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  MINEIRO 4: Integrador (incorpora)                  │
│  - Download do arquivo                             │
│  - Metadados (autor, data, fonte, licença)         │
│  - Commit automático com hash                      │
│  - IPFS add e registra CID                         │
│  - Histórico append-only: "encontrado em X"        │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  MINEIRO 5: Índexador (organiza)                    │
│  - Lê conteúdo, extrai categorias                  │
│  - Atualiza catálogos                              │
│  - Cria links relacionados                         │
│  - Manda para Distribuidor                         │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  MINEIRO 6: Distribuidor (espalha)                  │
│  - Replica em IPFS automaticamente                 │
│  - Notifica nós comunitários                       │
│  - Sinaliza para voluntários ("novo acervo")       │
│  - Sincroniza com Zenodo/Archive.org               │
└─────────────────────────────────────────────────────┘
```

---

## II. Mecanismo de Disponibilidade (rodam quando ociosos)

### Modelo: Trabalho em Tempo Ocioso

```
Seu computador (ou servidor da biblioteca):
  
Durante o dia (08h-22h):
  - CPU: 80% você, 20% mineiros
  - Rede: 80% você, 20% mineiros
  - Trabalho: rápido (não interfere)

Durante a noite (22h-08h):
  - CPU: 10% sistema, 90% mineiros
  - Rede: 10% sincronismo, 90% mineiros
  - Trabalho: full speed (você dorme, eles trabalham)

Fim de semana:
  - Praticamente 100% mineiros
  - Fim de semana é "colheita"

Resultado: 40-50 horas/semana de trabalho gratuito
(Tempo que seu computador ia desperdiçar)
```

---

### Configuração (cron jobs):

```bash
# Prospector roda a cada 2 horas
*/2 * * * * /usr/local/bin/mineiro-prospector >> /var/log/mineiros.log 2>&1

# Avaliador roda a cada 4 horas
0 */4 * * * /usr/local/bin/mineiro-avaliador

# Ético roda a cada 6 horas
0 */6 * * * /usr/local/bin/mineiro-etico

# Integrador roda 23h-06h (noite, bandwidth livre)
0 23 * * * /usr/local/bin/mineiro-integrador
0 0 * * * /usr/local/bin/mineiro-integrador
0 1 * * * /usr/local/bin/mineiro-integrador
# ... etc a cada hora à noite

# Distribuidor roda quando integrador termina
(cron or webhook triggered)
```

---

## III. Critérios de Prospecção

### O que os Mineiros Buscam?

```
BUSCA AUTOMÁTICA (palavras-chave + operadores booleanos):

Pilar 1 (Vida Abundante):
  - ("climate change" OR "climate mitigation") AND (solution OR restoration)
  - ("biodiversity" OR "species conservation") AND (research OR data)
  - ("renewable energy" OR "solar" OR "wind") AND (open OR free)
  - ("regenerative agriculture" OR "agroforestry") AND (method OR guide)
  - ("ecosystem" OR "biome") AND (recovery OR restoration)
  
Pilar 2 (Dignidade):
  - ("poverty reduction" OR "extreme poverty") AND (solution OR data)
  - ("healthcare" OR "medicine") AND (open OR free OR accessible)
  - ("education" OR "literacy") AND (open OR free OR access)
  - ("human rights" OR "justice") AND (research OR documentation)
  - ("animal welfare" OR "animal rights") AND (research OR data)

CARE (Povos Originários):
  - ("indigenous knowledge" OR "traditional knowledge") AND (CARE OR authority OR consent)
  - ("indigenous land" OR "territory") AND (protection OR management)

Conhecimento Aberto:
  - (CC0 OR "public domain" OR MIT OR "open access") AND (knowledge)
  - (arXiv OR DOAJ OR "open access") AND (filetype:pdf OR filetype:html)
```

---

## IV. Fontes de Prospecção

### Onde Mineiros Vasculham

```
Automático (24/7):
  ✅ arXiv.org (preprints, ciência aberta)
  ✅ DOAJ.org (periódicos abertos)
  ✅ SSRN (working papers)
  ✅ Google Scholar (cache público)
  ✅ CORE.ac.uk (repositório europeu)
  ✅ Directory of Open Access Books (DOAB)
  ✅ OpenGrey (literatura cinzenta)
  ✅ Unpaywall (finds open versions)
  ✅ CrossRef (metadados)
  ✅ Wikimedia Commons (dados abertos)
  ✅ GitHub (projetos públicos)
  ✅ IPFS (rede descentralizada)

Com aprovação explícita:
  ✅ OER Commons (recursos educacionais)
  ✅ Project MUSE (some content open)
  ✅ PLOS ONE (open access)
  ✅ Frontiers (open access)
  ✅ Cochrane Library (review, some free)

Nunca vasculha:
  ❌ Paywalls (sem permissão)
  ❌ Dados privados (sem consentimento)
  ❌ Conteúdo de propriedade proprietária
```

---

## V. Pipeline de Validação Automática

### Cada achado passa por 3 filtros:

```
Filtro 1: RELEVÂNCIA
  IA lê: título, abstract, introdução
  Pergunta: "Isto serve a um dos 2 pilares?"
  Resposta: SIM / TALVEZ / NÃO
  
  Se SIM:
    → Confiança: 90%+
    → Vai para Ético
  
  Se TALVEZ:
    → Confiança: 50-89%
    → Manda para Avaliador Humano (fila)
  
  Se NÃO:
    → Rejeitado, descarta

---

Filtro 2: ÉTICA
  IA testa contra 5 regras:
    □ Explora povos originários SEM CARE?
    □ É sexista, racista ou discriminatório?
    □ Causa dano direto intencional?
    □ É propriedade privada SEM acesso?
    □ Viola dignidade (pessoas ou animais)?
  
  Se PASSA (0 violações):
    → Aprovado 100%
    → Vai para Integrador
  
  Se DÚVIDA (1-2 violações pequenas):
    → Confiança: 70%
    → Manda para Quórum Humano (para decisão)
  
  Se FALHA (3+ violações):
    → Rejeitado, descarta

---

Filtro 3: QUALIDADE
  IA testa:
    □ Licença é aberta (CC0, MIT, CARE, etc)?
    □ Formato é durável (PDF, TXT, JSON)?
    □ Arquivo está íntegro (download OK)?
    □ Metadados estão presentes?
  
  Se TUDO OK:
    → Vai para Integrador
  
  Se PROBLEMA:
    → Tenta corrigir (encontra versão melhor)
    → Se não consegue: registra e manda para fila humana
```

---

## VI. Integração Automática (sem você tocar)

### Quando arquivo passa pelos 3 filtros:

```bash
# 1. Download
curl -o arquivo.pdf https://...
sha256sum arquivo.pdf > arquivo.sha256

# 2. Metadados (extrair automaticamente)
{
  "titulo": "...",
  "autor": "...",
  "data_publicacao": "...",
  "fonte_original": "https://...",
  "fonte_encontrada": "arXiv.org",
  "data_descoberta": "2026-10-09T15:30:00Z",
  "mineiro": "prospector-v1.2",
  "confianca": 0.95,
  "pilares": ["pilar-1-vida-abundante"],
  "licenca": "CC0",
  "hash_sha256": "abc123...",
  "categoria": "biodiversidade"
}

# 3. Armazenar
mkdir -p catalogo/descobertas/2026-10/
cp arquivo.pdf catalogo/descobertas/2026-10/
cp metadata.json catalogo/descobertas/2026-10/

# 4. Commit automático
git add catalogo/descobertas/2026-10/
git commit -m "Descoberta automática: [titulo]
  
Fonte: arXiv.org
Data descoberta: 2026-10-09
Mineiro: prospector-v1.2
Confiança: 95%
Pilares: Pilar 1 (Vida Abundante)

Integrado automaticamente.
"

# 5. IPFS
ipfs add -r catalogo/descobertas/2026-10/
# → Qm_novo_hash

# 6. Registrar CID
echo "2026-10-09 Qm_novo_hash arquivo.pdf" >> veracidade/descobertas.log

# 7. Notificar voluntários
# (email, webhook, RSS feed)
echo "Nova descoberta: [titulo]. Acesse via IPFS: Qm_novo_hash"

# 8. Sincronizar
git push origin main
ipfs dag stat Qm_novo_hash
curl -X POST https://zenodo.org/api/deposit/... (mensal, batch)
```

---

## VII. Mineiros em Software Livre

### Implementação Técnica (usando ferramentas grátis e abertas)

```
Prospector:
  - Linguagem: Python (livre)
  - Bibliotecas: requests, beautifulsoup4, arxiv (todas MIT/Apache)
  - APIs usadas: arXiv, DOAJ, CrossRef (grátis, públicos)
  - Deploy: seu computador ou servidor (seu controle total)

Avaliador:
  - Linguagem: Python
  - Modelo: Claude API (chamadas pelo avaliador)
    OU
  - Modelo Local: Ollama (LLaMA rodando localmente, livre)
  - Task: "Classifique relevância em escala 1-10"

Ético:
  - Linguagem: Python
  - Checklist: hardcoded (não precisa IA sofisticada)
  - Decisão: lógica simples (if/else)
  - Escalação: casos ambíguos vão para humano

Integrador:
  - Linguagem: Bash (shell script, sistema operacional)
  - Deps: git, ipfs, curl (todos grátis)
  - Automatização: cron, systemd timer (sistema operacional)

Distribuidor:
  - Linguagem: Bash
  - Deps: git, ipfs
  - Webhooks: para notificação (simples HTTP POST)

Todo o código: GitHub (público, MIT License)
  → Qualquer um consegue rodar seus próprios mineiros
```

---

## VIII. Fluxo Real (um arquivo encontrado)

```
2026-10-09, 22h00 (noite, ociosos começam):

→ Prospector roda
  Busca: "biodiversity conservation" site:researchgate.net
  Encontra: estudo sobre restauração de mata atlântica
  Link: https://researchgate.net/publication/xxx
  Status: ✓ Encontrado

→ Avaliador roda
  Lê abstract: "Restauração de 500 hectares em 5 anos..."
  Pergunta: "Pilar 1? (vida abundante)"
  Resposta: SIM, confiança 95%
  Status: ✓ Relevante

→ Ético roda
  Testa:
    □ Explora indígenas? NÃO
    □ É sexista? NÃO
    □ É aberto? PARCIAL (ResearchGate tem restrição)
    Status: ⚠ Dúvida (proprietário, mas pesquisador permite)
  
  → Manda para fila humana (você revisa amanhã)

---

2026-10-10, 09h00 (você acorda):

Você vê relatório do mineiro:
  "1 descoberta aguardando aprovação: 'Restauração Mata Atlântica'"
  
Você lê rápido (2 min), aprova:
  "OK, relevante + CARE okay (comunidades locais mencionadas)"

Sistema automático:
  → Integrador roda
    Download: PDF do ResearchGate (legal: pesquisador disponibiliza)
    Metadados: extrai automático
    Arquivo: catalogo/descobertas/2026-10/restauracao-mata-atlantica.pdf
    Commit: "Descoberta: Restauração Mata Atlântica (ResearchGate)"
    IPFS: Qm_novo_hash
    Notifica voluntários: "Nova entrada, biodiversidade"
```

---

## IX. Escala de Mineiros

### Quantos mineiros você precisa?

```
Cenário 1: Você rodando em casa (notebook)
  - 1 Prospector (procura)
  - 1 Avaliador (avalia)
  - 1 Ético (testa ética)
  - 1 Integrador (incorpora)
  - Fila humana: você aprova questionáveis (2h/semana)
  
  Produção: 10-20 arquivos/semana
  Custo: $0
  Seu tempo: 2h/semana (revisão)

Cenário 2: Servidor dedicado (VPS pequeno, R$ 30/mês)
  - 3-5 Prospectors (paralelos)
  - 2-3 Avaliadores
  - 2 Éticos
  - 1 Integrador
  - Fila humana: 4 revisores voluntários (4h/semana cada)
  
  Produção: 50-100 arquivos/semana
  Custo: R$ 30/mês
  Seu tempo: 0 (revisores voluntários)

Cenário 3: Rede de mineiros distribuídos
  - 20+ mineiros em 10 cidades
  - Cada um procura localmente + compartilha achados
  - Ético roda 1x (consenso distribuído)
  - Integrador distribui a todos
  
  Produção: 1000+ arquivos/semana
  Custo: $0 (computadores pessoais de voluntários)
  Seu tempo: 0 (comunidade auto-gerencia)
```

---

## X. Revisão Humana (fila de questionáveis)

### Quando mineiro não tem certeza:

```
Casos Ambíguos (confiança 50-89%):
  - Arquivo relevante mas origem questionável
  - Qualidade boa mas alguns problemas éticos
  - Tema relacionado mas não direto

Fila de Revisão:
  [ ] "Restauração Mata Atlântica" — biodiversidade + CARE
  [ ] "Energia Solar em Favelas" — dignidade + pilar 1
  [ ] "IA para diagnóstico malária" — saúde + acesso
  [ ] "Sementes crioulas" — biodiversidade + CARE

Processo:
  1. Um revisor voluntário lê (5-10 min)
  2. Vota: APROVA / REJEITA
  3. Se APROVA: mineiro integra automaticamente
  4. Se REJEITA: descarta, registra no histórico
  5. Casos divergentes: vão para quórum (consenso)

Você não precisa revisar tudo — voluntários fazem.
Você só vê relatório mensal de o que foi integrado.
```

---

## XI. Proteções Contra Poluição

### Como mineiros não destroem biblioteca com lixo?

```
Filtro 1: Licença
  ✅ CC0, MIT, CARE, Public Domain
  ❌ Propriedade privada SEM permissão

Filtro 2: Origem confiável
  ✅ arXiv, DOAJ, universidades, ONGs
  ✅ Pesquisadores que disponibilizam abertamente
  ❌ Blogs aleatórios, Twitter, AI-generated nonsense

Filtro 3: Qualidade mínima
  ✅ Peer-reviewed (publicado em revista)
  ✅ Tem autor, data, fonte
  ❌ Posts sem fonte, boatos, opinião sem evidência

Filtro 4: Relevância limpa
  ✅ Conexão clara aos 2 pilares
  ❌ "Tudo que alguém achou interessante"

Filtro 5: Ética
  ✅ Não explora, não discrimina, não mente
  ❌ Pseudociência, fraude, conteúdo tóxico

Resultado: ~5% aprovação rate
  100 achados → ~5 integrados (curadoria severa)
```

---

## XII. Mineiros Continuam Quando Você Não Está

### Cenário real:

```
Você: morre, some, fica incapacitado

Mineiros:
  ✓ Continuam rodando indefinidamente
  ✓ Prospectam, avaliam, integram
  ✓ Biblioteca cresce sozinha
  ✓ Voluntários revisam fila

Resultado:
  Seu nó IPFS semeia indefinidamente
  Conhecimento novo chega automaticamente
  Rede absorve seu trabalho e continua

Você foi o "inicializador".
Mineiros são o "crescimento perpétuo".
```

---

## XIII. Implementação (você, para começar)

### Passo 1: Prospector simples

```python
# mineiro-prospector-v1.py
import arxiv
import os
from datetime import datetime

CLIENT = arxiv.Client()

KEYWORDS = [
    "biodiversity conservation",
    "climate mitigation",
    "renewable energy",
    "poverty reduction",
    "indigenous knowledge",
]

for keyword in KEYWORDS:
    results = CLIENT.results(
        arxiv.Search(
            query=f"({keyword}) AND (open OR free)",
            sort_by=arxiv.SortCriterion.SubmittedDate,
            max_results=5
        )
    )
    
    for paper in results:
        print(f"{datetime.now()} | FOUND: {paper.title}")
        print(f"  Author: {paper.authors[0]}")
        print(f"  PDF: {paper.pdf_url}")
        print(f"  Relevance: needs evaluation\n")
```

**Roda 1x/dia, procura autonomamente.**

### Passo 2: Escalação

Quando funciona:
  1. Adiciona Avaliador (classifica relevância)
  2. Adiciona Ético (valida ética)
  3. Adiciona Integrador (incorpora)
  4. Recruta voluntários para revisão
  5. Paralleliza (múltiplos mineiros)

---

## XIV. Visão de Longo Prazo

### 2026 (agora):
```
✓ Desenho de mineiros definido
✓ Código-base iniciado
```

### 2027:
```
✓ Prospector + Avaliador rodando
✓ 100 artigos/mês integrados
✓ Voluntários revisor 10 ambíguos/semana
```

### 2030:
```
✓ Rede de mineiros em 5 cidades
✓ 1000+ artigos/mês integrados
✓ 10 revisores voluntários
✓ Crescimento exponencial
```

### 2050:
```
✓ 100+ mineiros distribuídos
✓ Biblioteca cresce 10.000+/mês automaticamente
✓ Conhecimento novo é absorvido em horas
✓ Você foi só "seed"
```

---

**Versão:** v0.1  
**Status:** Desenho de arquitetura  
**Próximo:** Código-base Python (mineiro-prospector-v1)  
**Custo:** $0 (software livre, computadores pessoais)  
**Sustentabilidade:** Indefinida (rode enquanto houver eletricidade)
