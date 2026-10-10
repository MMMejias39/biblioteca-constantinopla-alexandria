# BABEL v0.10b — Backlog de Desenvolvimento

**Data:** 2026-10-10 | **Status:** Em Execução | **Versão:** 0.10b

---

## 📊 Quadro de Prioridades

### 🔴 CRÍTICO (Semana 1-2)

#### 1. Publicação Final Zenodo
- **Status:** Bloqueado por validação
- **Esforço:** 1-2 horas
- **Descrição:** Submeter upload Zenodo de rascunho para publicação final
- **Tarefas:**
  - [ ] Preencher campo "Dates" obrigatório (se necessário)
  - [ ] Clicar "Submit for review"
  - [ ] Aguardar aprovação Zenodo (24-48h)
  - [ ] Publicar e obter URL permanente
  - [ ] Atualizar `veracidade/carimbo.txt` com data de publicação
- **Dependências:** Zenodo upload com metadados (✅ concluído)

#### 2. Divulgação Anônima — Fase 1
- **Status:** Pronto para execução
- **Esforço:** 2-3 horas
- **Descrição:** Iniciar espalhamento viral de BABEL
- **Tarefas:**
  - [ ] Email anônimo (ProtonMail) para 10 educadores/ONGs
  - [ ] Posts Reddit em 5 subreddits (r/opensource, r/decentralized, etc)
  - [ ] Tweet anônimo em 3 contas (Twitter + Mastodon)
  - [ ] Contato boca-a-boca com 3-5 pessoas-chave
  - [ ] Documentar feedback em `DIVULGACAO-ANONIMA.md`
- **Dependências:** Link permanente Zenodo + GitHub URL

#### 3. Registrar Codeberg como Espelho
- **Status:** Aguardando token HTTPS
- **Esforço:** 30 minutos
- **Descrição:** Ativar replicação em Codeberg
- **Tarefas:**
  - [ ] Gerar token HTTPS em https://codeberg.org/user/settings/applications
  - [ ] Executar `espelhar.sh` com credencial Codeberg
  - [ ] Verificar replicação bem-sucedida
  - [ ] Atualizar README com link Codeberg
- **Dependências:** Credencial Codeberg

---

### 🟠 ALTO (Semana 2-3)

#### 4. Dashboard Monitor Zenodo
- **Status:** Arquitetura pronta
- **Esforço:** 4-6 horas
- **Descrição:** Integrar métricas Zenodo ao babel-monitor
- **Tarefas:**
  - [ ] Adicionar API Zenodo ao monitor Rust
  - [ ] Coletar: downloads, views, citações
  - [ ] Exibir em dashboard localhost:3000
  - [ ] Gráficos de crescimento (7d, 30d, YTD)
  - [ ] Testar com dados Zenodo reais
- **Dependências:** Publicação Zenodo, Rust 1.70+

#### 5. Validação Visena (IA-IA)
- **Status:** Estrutura pronta
- **Esforço:** 6-8 horas
- **Descrição:** Implementar auditoria automática via Visena
- **Tarefas:**
  - [ ] Executar `veracidade/auditoria-ia/src/main.rs`
  - [ ] Validar semântica de todos os .md em Visena
  - [ ] Gerar relatório de conformidade
  - [ ] Registrar assinatura criptográfica em carimbo.txt
  - [ ] Documentar protocolo em `COMO-AUDITAR-IA.md`
- **Dependências:** Arquivo Visena completo

#### 6. Replicação IPFS — Fase 2
- **Status:** CID registrado (QmYMWe...)
- **Esforço:** 3-4 horas
- **Descrição:** Pinnar permanentemente e divulgar
- **Tarefas:**
  - [ ] Conectar a 5+ nós públicos (Pinata, Web3.Storage, etc)
  - [ ] Registrar CID em `veracidade/ipfs-cid.txt`
  - [ ] Publicar em comunidades IPFS (blog, Twitter)
  - [ ] Medir peers conectados via `ipfs dht findprovs <CID>`
  - [ ] Documentar em `REPLICACAO-UNIVERSAL.md`
- **Dependências:** IPFS Kubo rodando

#### 7. Tradução Colaborativa — Fase 1
- **Status:** Estrutura em 8 idiomas pronta
- **Esforço:** 8-10 horas (distribuído)
- **Descrição:** Revisar e completar traduções
- **Tarefas:**
  - [ ] Revisar README em 8 idiomas
  - [ ] Completar PRIMEIRO-USO em idiomas que faltam
  - [ ] Validar gramatica Visena em cada idioma
  - [ ] Criar guia de contribuição para tradutores
  - [ ] Testar renderização em idiomas RTL (árabe, hebraico)
- **Dependências:** Visena grammar stable

---

### 🟡 MÉDIO (Semana 3-4)

#### 8. Fria Edition (Papel)
- **Status:** Script gerado (`fria.sh`)
- **Esforço:** 2-3 horas
- **Descrição:** Preparar edição para impressão de 300+ anos
- **Tarefas:**
  - [ ] Executar `fria.sh` e gerar PDF otimizado
  - [ ] Validar compatibilidade com impressoras offset
  - [ ] Testar durabilidade: papel de arquivo, tinta neutra
  - [ ] Orçar impressão de 100 cópias
  - [ ] Distribuir em 5-10 arquivos públicos (universidades, museus)
- **Dependências:** Arquivo estável, PDF gerado

#### 9. Carimbo Criptográfico — Assinatura Blockchain
- **Status:** SHA256 em carimbo.txt
- **Esforço:** 4-6 horas
- **Descrição:** Registrar hash em blockchain público
- **Tarefas:**
  - [ ] Estudar Ethereum/Bitcoin/IPFS timestamp services
  - [ ] Escolher blockchain (recomendação: Arweave para permanência)
  - [ ] Registrar `MANIFESTO.sha256` + Zenodo DOI
  - [ ] Gerar certificado de timestamp imutável
  - [ ] Adicionar endereço em `veracidade/carimbo.txt`
- **Dependências:** Carimbo SHA256 + DOI Zenodo

#### 10. Comunidades Indígenas — Parceria CARE
- **Status:** Framework documentado
- **Esforço:** 6-8 horas (pesquisa + contato)
- **Descrição:** Contatar guardiões de conhecimento indígena
- **Tarefas:**
  - [ ] Mapear 10 organizações indígenas (Brasil, América Latina)
  - [ ] Enviar proposta de colaboração respeitosa
  - [ ] Integrar saberes locais em seção dedicada
  - [ ] Registrar atribuição segundo CARE principles
  - [ ] Criar protocolo de consentimento prévio informado
- **Dependências:** Lista de contatos, DIVULGACAO-COMUNITARIA.md

#### 11. Governança Distribuída — Quórum 1
- **Status:** Framework pronto
- **Esforço:** 5-6 horas
- **Descrição:** Recrutamento de 4 guardiões iniciais
- **Tarefas:**
  - [ ] Publicar chamada para guardiões (email, redes)
  - [ ] Avaliar candidatos com critério de diversidade
  - [ ] Realizar 1º voto: estrutura de decisão
  - [ ] Publicar atas em `veracidade/dossie-quorum-v0.1.md`
  - [ ] Estabelecer cadência (trimestral)
- **Dependências:** Zenodo publicado, comunidade inicial

---

### 🟢 BAIXO (Semana 4+)

#### 12. Monitor — Integração GitHub Stats
- **Status:** Conceito aprovado
- **Esforço:** 3-4 horas
- **Descrição:** Adicionar stars/forks/clones do GitHub
- **Tarefas:**
  - [ ] API GitHub (public access)
  - [ ] Integrar em babel-monitor
  - [ ] Mostrar comparativo: GitHub vs Zenodo vs IPFS
  - [ ] Gráficos de crescimento combinado
- **Dependências:** Monitor Zenodo (item 4)

#### 13. Versão Mobile (Aplicativo)
- **Status:** Exploração
- **Esforço:** 12-20 horas
- **Descrição:** App móvel para acesso offline
- **Tarefas:**
  - [ ] Escolher stack: React Native ou Flutter
  - [ ] Prototipar leitura de metadados IPFS
  - [ ] Implementar busca local com ElasticSearch
  - [ ] Publicar em F-Droid (Android)
- **Dependências:** BABEL v1.0 estável

#### 14. Educação — Currículo Aberto
- **Status:** Estrutura em `catalogo/`
- **Esforço:** 10-15 horas
- **Descrição:** Transformar em módulo educacional
- **Tarefas:**
  - [ ] Criar plano de aula (ensino médio + universidade)
  - [ ] Elaborar exercícios: filtragem, busca, tradução
  - [ ] Registrar em plataformas (Moodle, Canvas, etc)
  - [ ] Parcerias com 3 escolas para teste
- **Dependências:** Visena estável

#### 15. Monitoramento Longo Prazo
- **Status:** Métricas base estabelecidas
- **Esforço:** 2-3 horas (setup), contínuo (manutenção)
- **Descrição:** Dashboard de saúde de BABEL
- **Tarefas:**
  - [ ] Configurar CloudFlare Analytics para GitHub Pages
  - [ ] Alertas: IPFS peers < 5, Zenodo downloads/semana
  - [ ] Relatório mensal: crescimento, comunidade, novos idiomas
  - [ ] Publicar em `MONITORAMENTO-BABEL.md`
- **Dependências:** Toda infraestrutura ativa

---

## 🎯 Marcos (Milestones)

| Fase | Data | Objetivo | Métricas |
|------|------|---------|----------|
| **v0.10b (Atual)** | 2026-10-10 | Zenodo + Divulgação iniciada | 35 arquivos, DOI público |
| **v0.11** | 2026-10-31 | 3 espelhos ativos + 100 cópias Fria | 100+ stars GitHub, 1000+ peers IPFS |
| **v0.20** | 2026-12-15 | 4 guardiões + 5 idiomas completados | 5K downloads Zenodo, 10K stars |
| **v1.0** | 2027-03-01 | Produção estável + Educação | 50K usuários, 100+ comunidades |

---

## 📋 Checklist Semanal

### Semana de 2026-10-10 a 2026-10-17 (ATUAL)
- [ ] Publicar Zenodo
- [ ] Iniciar divulgação (email + Reddit)
- [ ] Configurar Codeberg
- [ ] Executar auditoria Visena
- [ ] Medir crescimento GitHub

### Semana de 2026-10-17 a 2026-10-24
- [ ] Integrar Dashboard Zenodo
- [ ] Pinnar em 3 serviços IPFS
- [ ] Revisar traduções (português + inglês)
- [ ] Contatar 5 educadores
- [ ] Recrutar guardiões

---

## 🚀 Call to Action

**Próxima reunião de quórum:** 2026-10-15 (decisão sobre prioridades)

**Responsáveis atuais:**
- Marcelo Moreira Mejias (coordenação geral, validação IA)
- Comunidade (tradução, divulgação, educação)

**Como contribuir:**
1. Escolher uma tarefa do backlog
2. Criar issue em GitHub com `[BACKLOG]` prefix
3. Submeter PR quando pronta
4. Registrar em `MONITORAMENTO-ATUAL.md`

---

**Última atualização:** 2026-10-10 23:45 UTC | **Versão:** 1.0
