# Distribuição Descentralizada — Zero Custos, Múltiplas Jurisdições

**Problema:** nenhuma biblioteca depende de um servidor único, uma empresa, ou um país.  
**Solução:** rede de replicação descentralizada, offline-first, sem ponto de falha.

---

## 1. Camadas de Distribuição (da mais rápida à mais durável)

```
┌─────────────────────────────────────────────────────────────┐
│  CAMADA 0: Git (você aqui)                                   │
│  Local disk + GitHub + Codeberg + Forgejo próprio            │
│  Rápido, auditável, versionado                               │
└─────────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────────┐
│  CAMADA 1: IPFS (rede descentralizada)                        │
│  `ipfs add -r .` → CID único                                 │
│  Replicável por qualquer nó; sem servidor central            │
│  Custo: 0 (você hospeda um nó, ou pinning service grátis)    │
└─────────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────────┐
│  CAMADA 2: Preservação Acadêmica (grátis)                    │
│  Zenodo (CERN, UE) → DOI citável                             │
│  Internet Archive → Wayback + acervo histórico               │
│  Custo: 0 (serviços públicos)                                │
└─────────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────────┐
│  CAMADA 3: Offline-First (Kiwix .zim)                        │
│  Wikipédia-like, roda sem internet                           │
│  USB/SD card → distribuído em escolas, comunidades           │
│  Custo: ~$0.50/unidade (pendrive descartável)                │
└─────────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────────┐
│  CAMADA 4: Papel (Fria anual)                                │
│  Impressão de manifesto + carimbo + assinaturas do quórum    │
│  Durável 300+ anos; distribuído via assinantes              │
│  Custo: ~$5/cópia (tinta + papel archival)                   │
└─────────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────────┐
│  CAMADA 5: Rede Comunitária (P2P BitTorrent)                │
│  Comunidades replicam localmente em HD/cloud pessoal         │
│  Sem tracker central; cada cópia é seed                      │
│  Custo: 0 (hospedagem local)                                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Mapa de Jurisdições (redundância geográfica)

| # | Plataforma | Jurisdição | Custo | Status | CID/DOI |
|---|---|---|---|---|---|
| 1 | **GitHub** | EUA (Microsoft) | Grátis (público) | ✓ Ativa | git: main |
| 2 | **Codeberg** | Alemanha (não-profit) | Grátis | ⏳ Pendente (seu token HTTPS) | git: main |
| 3 | **Forgejo próprio** (opcional) | Você define | $0–50/ano | ⏳ Opcional | git: main |
| 4 | **IPFS** | Nenhuma (rede P2P) | Grátis (nó próprio) | ⏳ Preparar | CID: Qm... |
| 5 | **Pinata** (IPFS) | EUA | Grátis (1GB) | ⏳ Opcional | CID: Qm... |
| 6 | **Zenodo** | UE (CERN, Suíça) | Grátis | ⏳ Token + upload | DOI: 10.5281/... |
| 7 | **Internet Archive** | EUA | Grátis | ⏳ Preparado | IA ID: bc-alexandria |
| 8 | **Kiwix Hub** | Nenhuma | Grátis | ⏳ Zim builder | Local download |
| 9 | **Papel/Impressão** | Você + assinantes | ~$5/cópia | ⏳ fria.sh | Carimbo |
| 10 | **Comunidades** | Global | Grátis | ⏳ Recrutar | Local HD |

---

## 3. Fluxo de Replicação (como a informação viaja)

### 3.1 — Você commita algo novo

```bash
# Seu fluxo local
git add novo-arquivo.md
git commit -m "Nova entrada"
git push origin main          # GitHub (automático via hook)
```

### 3.2 — Hook automático: replicação em cascata

```bash
# 1. Push para múltiplos espelhos Git
git push codeberg main
git push forgejo main

# 2. Gera IPFS
ipfs add -r . --progress
# → Qm8a7b9c... (novo CID)

# 3. Registra CID + hash em veracidade/carimbo.txt
echo "Qm8a7b9c 2026-10-10T15:30:00Z SHA256:abc123..." >> carimbo.txt

# 4. Opcional: notifica Zenodo/IA para re-harvest
curl -X POST https://zenodo.org/api/harvest/github/...
curl -s "https://archive.org/services/check_identifier.php?identifier=bc-alexandria"
```

### 3.3 — Usuários replicam de qualquer ponto

```bash
# Opção A: Git (rápido, versionado)
git clone https://github.com/[user]/biblioteca-constantinopla-alexandria.git
# ou
git clone https://codeberg.org/[user]/biblioteca-constantinopla-alexandria.git

# Opção B: IPFS (descentralizado, sem intermediário)
ipfs get Qm8a7b9c [--output=biblioteca/]
# Roda offline se você tiver o nó

# Opção C: Zenodo (citável, para pesquisadores)
curl https://zenodo.org/api/records/[record-id]/files

# Opção D: Internet Archive (histórico, Wayback)
# https://archive.org/details/bc-alexandria/

# Opção E: Kiwix (sem internet, offline)
# Baixe biblioteca.zim (~500 MB) e abra no Kiwix

# Opção F: BitTorrent (P2P, velocidade)
# arquivo.iso.torrent (GitHub Releases)

# Opção G: Papel (impressão anual)
# Pida referência de quem tem cópia impressa
```

---

## 4. Implementação por Fase

### **Fase 1 (agora)** — Git + IPFS + Papel
- ✅ GitHub (já existe)
- ⏳ Codeberg (aguarda seu HTTPS token)
- ⏳ IPFS local (instale `ipfs`, rode nó)
- ⏳ Fria.sh (gera impressão anual)

**Custo:** 0 + seu tempo

### **Fase 2 (nov 2026)** — Preservação + Offline
- ⏳ Zenodo (upload via API, 1 DOI/versão)
- ⏳ Internet Archive (S3 keys, 1 upload/versão)
- ⏳ Kiwix .zim (zimwriterfs, conversor HTML)

**Custo:** 0 (serviços públicos)

### **Fase 3 (2027)** — Distribuição Física + Comunitária
- ⏳ USB bootável (ISO com Kiwix + Git)
- ⏳ BitTorrent (GitHub Releases, magnet link)
- ⏳ Recrutar 10–20 "bibliotecários comunitários" (voluntários com HD local)

**Custo:** ~$0.50/USB (se queimar 100 unidades)

---

## 5. Estrutura de Arquivos Publicáveis

```
biblioteca-constantinopla-alexandria/

# Git (versionado)
.git/                    → Histórico completo
.gitignore

# IPFS (hash-identificado)
MANIFESTO.sha256         → Todos os arquivos da versão
carimbo.txt             → Versão + CID + data

# Construtos para distribuição
fria.sh                 → Gera PDF/impressão anual
kiwix-builder.sh        → Gera .zim (offline)
torrent-generator.sh    → Cria arquivo.iso.torrent

# Metadados para preservação
.zenodo.json            → Campos da API Zenodo
.ia-metadata.txt        → Campos Internet Archive
.ipfs-pin.json          → Instruções de pinning
```

---

## 6. Arquitetura de Nó IPFS Pessoal (zero-cost)

### 6.1 — Setup local (seu computador)

```bash
# 1. Instale IPFS
curl https://dist.ipfs.tech/go-ipfs/v0.20.0/go-ipfs_v0.20.0_linux-amd64.tar.gz | tar xz
sudo mv go-ipfs/ipfs /usr/local/bin

# 2. Inicialize (cria ~/.ipfs/)
ipfs init

# 3. Adicione a biblioteca
ipfs add -r --progress biblioteca-constantinopla-alexandria/
# → Qm8a7b9c (raiz)

# 4. Lance o daemon (sempre rodando, opcional)
ipfs daemon &
# Localhost:5001 (API), :8080 (gateway HTTP)

# 5. Seu nó agora hospeda a biblioteca (seeding)
# Qualquer pessoa com IPFS consegue: ipfs get Qm8a7b9c
```

### 6.2 — Gateway público (se quiser HTML via browser)

```bash
# Seu nó já oferece gateway local
open http://localhost:8080/ipfs/Qm8a7b9c

# Acesse de fora (via público Infura/Cloudflare)
open https://ipfs.io/ipfs/Qm8a7b9c
# (Infura é free, mantido pela comunidade)
```

---

## 7. Recrutamento de Bibliotecários Comunitários

### 7.1 — Quem pode replicar?

Qualquer pessoa/grupo com:
- HD ou NAS (espaço: ~5 GB/versão anual)
- Internet (passiva; replicam 1x, seedam sempre)
- Compromisso documentado (assinatura)

### 7.2 — Estrutura mínima

```
Ser bibliotecário comunitário (voluntário):

1. Mantenha cópia sincronizada:
   git clone https://...
   cd biblioteca-constantinopla-alexandria
   git pull                    # A cada commit novo

2. Hospede IPFS (opcional):
   ipfs add -r --progress .
   ipfs daemon &              # Seu nó seeds

3. Registre-se publicamente:
   echo "Seu Nome (Cidade) — $(date)" >> BIBLIOTECARIOS.md
   git push origin main

4. Replicadores conhecidos:
   - Caso falhe GitHub → comunidade consulta você
   - Caso falhe Codeberg → comunidade consulta você
```

### 7.3 — Incentivos

- **Nenhum dinheiro** (tudo é voluntário)
- **Visibilidade** (seu nome em BIBLIOTECARIOS.md)
- **Autonomia** (você hospeda, ninguém controla)
- **Durabilidade** (biblioteca sobrevive com você)

---

## 8. Exemplo: Replicação de Emergência

Se GitHub cai amanhã:

```
Usuario A descobriu: GitHub offline
  ↓
Git: copia local + Codeberg ainda funciona → sync
  ↓
IPFS: pede Qm8a7b9c a qualquer nó → restaura
  ↓
Internet Archive: wayback.archive.org tem versão 2026-10-01
  ↓
Bibliotecário em São Paulo: "Tenho cópia local, faço mirror"
  ↓
Zenodo DOI: "Eu tenho versão cientificamente citável"
  ↓
Kiwix: "Posso rodar offline no USB"
  ↓
Papel: "Tenho impressão assinada de 2026"
  ↓
RESULTADO: GitHub desaparece, biblioteca não morre.
```

---

## 9. Checklist de Implementação (você, agora até 2026-12-31)

### **Immediate (2026-10-09 → 2026-10-31)**
- [ ] Codeberg: criar repo, pushear via HTTPS
- [ ] IPFS: instalar nó, `ipfs add -r .` → registrar CID
- [ ] Carimbo: criar `veracidade/carimbo.txt` com CID + SHA256

### **Short-term (2026-11-01 → 2026-11-30)**
- [ ] Zenodo: conta, gerar token, 1º upload
- [ ] Internet Archive: conta, gerar S3 keys, 1º upload
- [ ] Fria.sh: testar, gerar PDF/impressão

### **Medium-term (2026-12-01 → 2027-01-31)**
- [ ] Kiwix: builder HTML → .zim
- [ ] BitTorrent: GitHub Releases, arquivo.iso.torrent
- [ ] BIBLIOTECARIOS.md: recrutar 5–10 voluntários

### **Long-term (2027+)**
- [ ] USB/DVD física distribuição (conferências, eventos)
- [ ] Fria anual (impressão + assinaturas)
- [ ] Auditoria: validar todas as cópias com `validador-manifesto`

---

## 10. Diagrama de Fluxo Visual

```
        ┌──────────────────────────────────────┐
        │  Você commita algo novo              │
        │  (em seu computador)                 │
        └──────────────────┬───────────────────┘
                           │
        ┌──────────────────▼───────────────────┐
        │  Hook git: replicação automática      │
        │  push → GitHub, Codeberg, Forgejo    │
        └──────────────────┬───────────────────┘
                           │
        ┌──────────────────▼───────────────────┐
        │  IPFS hash + carimbo registrado      │
        │  (determinístico, validável)         │
        └──────────────────┬───────────────────┘
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼
  ┌─────────┐        ┌──────────┐        ┌──────────────┐
  │   Git   │        │  IPFS    │        │  Preservação │
  │ (vivo)  │        │ (P2P)    │        │  (histórico) │
  │         │        │          │        │              │
  │ GitHub  │        │ Seu nó   │        │ Zenodo/IA    │
  │ Codeberg│        │ + Pinata │        │              │
  │ Forgejo │        │ (livre)  │        │              │
  └─────────┘        └──────────┘        └──────────────┘
      │                    │                    │
      └────────────────────┼────────────────────┘
                           │
              ┌────────────▼────────────┐
              │  Distribuição Offline   │
              │                         │
              │  Kiwix (.zim) → USB    │
              │  BitTorrent (.iso)      │
              │  Papel (fria.sh)        │
              │                         │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │ Bibliotecários Comunitári│
              │ (voluntários, múltiplas  │
              │  jurisdições, IPs)       │
              │                          │
              │ São Paulo → local HD     │
              │ Berlin → NAS             │
              │ Tokyo → cloud pessoal    │
              │                          │
              └──────────────────────────┘
```

---

## 11. Custo Total de Propriedade (TCO)

| Camada | Custo Anual | Nota |
|---|---|---|
| Git (GitHub + Codeberg) | $0 | Grátis indefinidamente |
| IPFS (seu nó) | $0 | Eletricidade já paga |
| Zenodo/IA | $0 | Públicos, não-profit |
| Kiwix .zim | $0 | Software livre |
| USB (1000 un.) | $500 | Opcional; ~$0.50/un. |
| Papel anual | $100–200 | 20–40 cópias |
| Hospedagem Forgejo | $0–50 | Opcional |
| Pinning IPFS (upgrade) | $0–10 | Grátis até 1GB |
| **TOTAL** | **$0–750/ano** | **Zero obrigatório** |

---

## 12. Próximas Ações (você)

1. **Assine protocolo** (protocolo-certificacao-guardiao-ia.md)
2. **Setup IPFS** (`ipfs init && ipfs daemon`)
3. **Registre CID** (próxima versão, carimbo.txt)
4. **Recrute bibliotecários** (BIBLIOTECARIOS.md)
5. **Teste restauração** (delete local, recupere de IPFS/IA)

---

**Resultado:** biblioteca que não morre quando GitHub cai, quando uma jurisdição bloqueia, quando uma plataforma é capturada, ou quando você não está mais aqui.

**Durabilidade:** indefinida (enquanto houver 1 pessoa com cópia + IPFS).
