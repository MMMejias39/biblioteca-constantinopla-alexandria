# Início Rápido — IPFS (5 minutos)

**Objetivo:** você hospeda a biblioteca em IPFS descentralizado, zero-cost.

---

## 1. Instalar IPFS (escolha sua plataforma)

### Linux/macOS
```bash
# Baixe o binário
curl -L https://dist.ipfs.tech/go-ipfs/v0.20.0/go-ipfs_v0.20.0_linux-amd64.tar.gz | tar xz

# Instale
cd go-ipfs
sudo ./install.sh

# Confirme
ipfs --version
# → go-ipfs version 0.20.0
```

### Windows
1. Acesse https://dist.ipfs.tech/
2. Baixe `go-ipfs_vX.X.X_windows-amd64.zip`
3. Extraia para `C:\Program Files\ipfs`
4. Abra Terminal: `ipfs --version`

### macOS (Homebrew)
```bash
brew install ipfs
```

---

## 2. Inicializar seu Nó IPFS

```bash
# Cria ~/.ipfs/ com configurações
ipfs init

# Saída:
# initializing ipfs node at /home/seu-usuario/.ipfs
# generating 2048-bit RSA keypair... done
# peer identity: Qm8a7b9c... (seu node ID único)
```

---

## 3. Adicionar a Biblioteca ao IPFS

```bash
# Vá para o repositório
cd ~/seu-caminho/biblioteca-constantinopla-alexandria

# Adicione com progresso
ipfs add -r --progress .

# Saída (última linha é o que interessa):
# added 1234 objects
# Qm8a7b9c1d2e3f4g5h6i7j8k9l0m1n2o3p4q5r6s7t8u9v0w1x2y3z [root dir]
```

**Anote este CID:** `Qm8a7b9c...` — é a identidade permanente da sua biblioteca.

---

## 4. Começar a Hospedar (Daemon)

```bash
# Rode o daemon (sempre replicando)
ipfs daemon

# Saída:
# Initializing daemon...
# go-ipfs version: v0.20.0
# Peer identity: Qm8a7b9c...
# API server listening on /ip4/127.0.0.1/tcp/5001
# HTTP server listening on /ip4/127.0.0.1/tcp/8080
# Gateway (readonly) server listening on /ip4/127.0.0.1/tcp/8080

# (Deixe rodando. Abra outro terminal para continuar.)
```

---

## 5. Acessar a Biblioteca

### Localmente (seu computador)
```bash
# No browser:
open http://localhost:8080/ipfs/Qm8a7b9c1d2e3f4g5h6i7j8k9l0m1n2o3p4q5r6s7t8u9v0w1x2y3z
```

### Via Internet (sem seu computador rodando)
```bash
# Se houver outro nó replicando:
open https://ipfs.io/ipfs/Qm8a7b9c1d2e3f4g5h6i7j8k9l0m1n2o3p4q5r6s7t8u9v0w1x2y3z

# Ou via Cloudflare (melhor performance):
open https://cloudflare-ipfs.com/ipfs/Qm8a7b9c1d2e3f4g5h6i7j8k9l0m1n2o3p4q5r6s7t8u9v0w1x2y3z
```

---

## 6. Registrar o CID Permanentemente

```bash
# Adicione ao manifesto de veracidade
echo "CID: Qm8a7b9c1d2e3f4g5h6i7j8k9l0m1n2o3p4q5r6s7t8u9v0w1x2y3z" >> veracidade/carimbo.txt
echo "Data: $(date -u +'%Y-%m-%dT%H:%M:%SZ')" >> veracidade/carimbo.txt

# Commit
git add veracidade/carimbo.txt
git commit -m "IPFS CID registrado (v0.10)"
git push origin main
```

---

## 7. Automatizar Sincronização (Cron Job, opcional)

```bash
# Edite crontab
crontab -e

# Adicione esta linha (roda a cada 6 horas):
0 */6 * * * cd ~/biblioteca-constantinopla-alexandria && git pull origin main && ipfs add -r . --progress >> /tmp/ipfs-sync.log 2>&1

# Salve e saia (Ctrl+X, depois Y, Enter)
```

---

## 8. Verificar Saúde do Nó

```bash
# Em outro terminal (enquanto daemon roda):

# Veja seu peer ID
ipfs id

# Veja quantos pares está conectado
ipfs swarm peers | wc -l

# Teste conectividade
ipfs ping Qm8a7b9c1d2e3f4g5h6i7j8k9l0m1n2o3p4q5r6s7t8u9v0w1x2y3z
```

---

## 9. Parar o Daemon (quando necessário)

```bash
# Pressione Ctrl+C no terminal onde está rodando

# Ou, de outro terminal:
pkill -f "ipfs daemon"
```

---

## 10. Próximos Passos

✅ **Feito:** você está hospedando a biblioteca descentralizadamente

⏳ **Próximo:** divulgue o CID para comunidades
```
"Baixe via IPFS: ipfs get Qm8a7b9c1d2e3f4g5h6i7j8k9l0m1n2o3p4q5r6s7t8u9v0w1x2y3z"
```

⏳ **Depois:** recrute mais "nós bibliotecários" (voluntários em outras cidades)

⏳ **Futuro:** biblioteca que não morre com GitHub, com você, ou com qualquer servidor

---

## Dúvidas?

- **Meu daemon/nó está consumindo muita banda?**  
  → Defina limites em `~/.ipfs/config` (consulte docs IPFS)

- **Quero desligar o daemon mas manter a biblioteca?**  
  → Só não rodará o daemon; sua cópia local continua intacta

- **Alguém consegue deletar meus dados?**  
  → Não. São seus dados no seu disco. Ninguém pode apagar.

- **Posso fazer backup?**  
  → Sim. Comprima `~/.ipfs/blocks/` (é toda a replicação)

- **Qual é o custo de bandwidth?**  
  → Zero. Você hospeda; outros baixam. Seu ISP cobra se houver limite.

---

**Tempo total:** ~5 minutos para setup + 1 hora primeira sincronização.

**Depois:** automático, indefinido, zero-cost. Sua biblioteca vive enquanto você hospedá-la.
