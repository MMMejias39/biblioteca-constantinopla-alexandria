# 📊 BABEL Monitor v1.0 — Aplicativo Rust

Dashboard em tempo real para monitorar o crescimento de BABEL.

## 🚀 Quick Start

### Pré-requisitos

- Rust 1.70+ (https://rustup.rs/)
- Cargo (incluso no Rust)

### Instalação e Execução

```bash
# 1. Navegue até o diretório
cd /home/mejias/biblioteca-constantinopla-alexandria/babel-monitor

# 2. Compile e execute
cargo run --release

# 3. Abra no navegador
http://localhost:3000
```

**Tempo de compilação:** ~2-3 minutos (primeira vez)

---

## 📊 Dashboard — O Que Você Verá

### Seções Principais

| Seção | Métrica | Descrição |
|-------|---------|-----------|
| **GitHub** | Stars, Forks, Issues, PRs | Crescimento no repositório |
| **Rede** | IPFS Peers, Clones, Alcance | Replicação descentralizada |
| **Crescimento** | Gráfico 7 dias | Tendência de crescimento |
| **Multilingualismo** | 20 idiomas | Status de tradução |
| **Replicação** | GitHub, IPFS, Sociais | Distribuição em rede |

---

## 🔄 Como Atualizar Métricas

### Opção 1: Via cURL (Manual)

```bash
# Simular 10 GitHub stars
curl -X POST http://localhost:3000/api/metrics/update \
  -H "Content-Type: application/json" \
  -d '{"github_stars": 10}'

# Simular IPFS peers
curl -X POST http://localhost:3000/api/metrics/update \
  -H "Content-Type: application/json" \
  -d '{"ipfs_peers": 5}'

# Atualizar múltiplas métricas
curl -X POST http://localhost:3000/api/metrics/update \
  -H "Content-Type: application/json" \
  -d '{
    "github_stars": 25,
    "github_forks": 3,
    "github_issues": 2,
    "github_prs": 1,
    "ipfs_peers": 8,
    "github_clones": 50,
    "total_reach": 500
  }'
```

### Opção 2: Via JavaScript (No Console do Navegador)

```javascript
// Atualizar stars
fetch('/api/metrics/update', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ github_stars: 10 })
}).then(r => r.json()).then(console.log);

// Atualizar tudo
fetch('/api/metrics/update', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    github_stars: 25,
    ipfs_peers: 8,
    github_clones: 50,
    total_reach: 500
  })
}).then(r => r.json()).then(console.log);
```

---

## 📈 Cenários de Teste

### Cenário 1: Dia 1 (Baseado)

```bash
# Nenhuma ação (0 crescimento)
```

Dashboard mostra: 0 stars, 0 IPFS peers, 1 pessoa alcançada

### Cenário 2: Após Divulgação (Dia 2-3)

```bash
# Simular descoberta inicial
curl -X POST http://localhost:3000/api/metrics/update \
  -H "Content-Type: application/json" \
  -d '{
    "github_stars": 5,
    "github_clones": 20,
    "total_reach": 50
  }'
```

Dashboard mostra: Crescimento inicial

### Cenário 3: Crescimento Viral (Semana 1)

```bash
# Simular crescimento exponencial
curl -X POST http://localhost:3000/api/metrics/update \
  -H "Content-Type: application/json" \
  -d '{
    "github_stars": 45,
    "github_forks": 8,
    "github_issues": 5,
    "github_prs": 3,
    "ipfs_peers": 12,
    "github_clones": 200,
    "total_reach": 800
  }'
```

Dashboard mostra: Replicação em múltiplas jurisdições

---

## 🔗 API Endpoints

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/` | GET | HTML do dashboard |
| `/api/metrics` | GET | Todas as métricas atuais |
| `/api/metrics/update` | POST | Atualizar métricas |
| `/api/github` | GET | Apenas métricas GitHub |
| `/api/network` | GET | Apenas métricas de rede |
| `/api/languages` | GET | Status de idiomas |

### Exemplo de Resposta

```json
{
  "timestamp": "2026-10-09T23:14:46.123Z",
  "github": {
    "stars": 25,
    "forks": 3,
    "issues": 2,
    "prs": 1,
    "commits_total": 40
  },
  "network": {
    "github_clones": 50,
    "ipfs_peers": 5,
    "countries": ["BR", "US"],
    "total_reach": 500
  },
  "languages": [
    {
      "language": "Português",
      "code": "pt",
      "files": 3,
      "completeness": 1.0
    },
    ...
  ],
  "status": "🟢 OPERACIONAL",
  "growth_rate": 2.5
}
```

---

## 🎨 Visualização

### Dashboard Mostra Em Tempo Real:

- **GitHub Stats:** Stars subindo conforme divulgação
- **IPFS Peers:** Replicação descentralizada
- **Gráfico 7 dias:** Tendência exponencial
- **Idiomas:** Barras de progresso para cada língua
- **Rede:** Visualização de distribuição geográfica

### Auto-Atualiza:
- A cada 10 segundos (via JavaScript fetch)
- Via botão "🔄 Atualizar" (manual)

---

## 🛠️ Desenvolvimento

### Estrutura do Projeto

```
babel-monitor/
├── Cargo.toml          # Dependências Rust
├── Cargo.lock          # Lock de versões
├── README.md           # Este arquivo
├── src/
│   └── main.rs         # Servidor Axum
└── static/
    └── index.html      # Dashboard HTML/CSS/JS
```

### Stack Técnico

- **Backend:** Axum (web framework moderno)
- **Async:** Tokio (runtime async/await)
- **Serialização:** Serde (JSON)
- **Frontend:** HTML5 + CSS3 + Vanilla JS

### Build Release (Otimizado)

```bash
cargo build --release
# Executável: ./target/release/babel-monitor
```

---

## 📊 Monitoramento Contínuo

### Para Automatizar Coleta de Dados

```bash
#!/bin/bash
# script-monitor.sh

while true; do
  # Coletar stars do GitHub (via API)
  STARS=$(curl -s https://api.github.com/repos/MMMejias39/biblioteca-constantinopla-alexandria | jq '.stargazers_count')
  
  # Atualizar dashboard
  curl -X POST http://localhost:3000/api/metrics/update \
    -H "Content-Type: application/json" \
    -d "{\"github_stars\": $STARS}"
  
  # Aguardar 1 hora
  sleep 3600
done
```

---

## 🌐 Exposição em Produção

### Para Expor Além de Localhost

Edite `src/main.rs`:

```rust
// De:
let listener = tokio::net::TcpListener::bind("127.0.0.1:3000").await.unwrap();

// Para:
let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
```

Depois:
```bash
cargo run --release
# Acessível de: http://<sua-ip>:3000
```

---

## 🔒 Segurança

O dashboard não tem autenticação (assumindo localhost/rede local).

Para produção, adicione:

```rust
// Use middleware de autenticação
.layer(middleware::from_fn(auth_middleware))
```

---

## 📱 Responsividade

Dashboard é responsivo e funciona em:
- Desktop (full view)
- Tablet (grid adaptado)
- Mobile (stack vertical)

---

## 🐛 Troubleshooting

### "Error: Address already in use"

```bash
# Mude a porta em src/main.rs
let listener = tokio::net::TcpListener::bind("127.0.0.1:3001").await.unwrap();
```

### "Cargo compilation failed"

```bash
# Update Rust
rustup update

# Clean build
cargo clean
cargo build --release
```

### "Dashboard não atualiza"

1. Verifique se servidor está rodando (`cargo run`)
2. Verifique console do navegador (F12)
3. Verifique se fetch está funcionando (Network tab)

---

## 🎯 Casos de Uso

### 1. Monitoramento em Tempo Real
```bash
cargo run --release
# Acesse http://localhost:3000
# Veja crescimento conforme acontece
```

### 2. Teste de Carga
```bash
# Simule crescimento rápido
for i in {1..100}; do
  curl -X POST http://localhost:3000/api/metrics/update \
    -H "Content-Type: application/json" \
    -d "{\"github_stars\": $i}"
  sleep 1
done
```

### 3. Integração com Scripts
```python
import requests
import time

while True:
    # Coleta de dados (sua lógica)
    stars = get_github_stars()  # Sua função
    
    # Atualiza dashboard
    requests.post('http://localhost:3000/api/metrics/update', json={
        'github_stars': stars
    })
    
    time.sleep(3600)  # A cada hora
```

---

## 📞 Suporte

Se tiver problemas:

1. Verifique se Rust está instalado: `rustc --version`
2. Verifique porta 3000: `lsof -i :3000`
3. Limpe cache: `cargo clean && cargo build --release`

---

**Versão:** 1.0  
**Data:** 2026-10-09  
**Status:** ✅ Pronto para Monitoramento

🚀 Execute e comece a monitorar BABEL em tempo real!
