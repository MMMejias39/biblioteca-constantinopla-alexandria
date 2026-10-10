#!/bin/bash
# Replicar BABEL em IPFS descentralizado

set -e

echo "🌐 REPLICAÇÃO BABEL — IPFS"
echo "=========================="

# Verificar IPFS instalado
if ! command -v ipfs &> /dev/null; then
    echo "❌ IPFS não encontrado"
    echo "Instale em: https://dist.ipfs.tech/"
    exit 1
fi

REPO_DIR="/home/mejias/biblioteca-constantinopla-alexandria"
cd "$REPO_DIR"

echo ""
echo "1️⃣  Status IPFS:"
ipfs --version
echo ""

# Verificar se daemon está rodando
if ! ipfs id > /dev/null 2>&1; then
    echo "⚠️  Daemon não está rodando"
    echo "   Inicie em outro terminal: ipfs daemon"
    exit 1
fi

PEER_ID=$(ipfs id -f "<ID>")
echo "   Peer ID: $PEER_ID"
echo ""

echo "2️⃣  Adicionando BABEL ao IPFS..."
echo "   (isso pode levar alguns minutos)"
echo ""

# Adicionar com progresso
CID=$(ipfs add -r --progress . \
    --exclude babel-venv \
    --exclude .git \
    --exclude target \
    --exclude "*.zip" \
    2>&1 | tail -1 | awk '{print $2}')

if [ -z "$CID" ]; then
    echo "❌ Erro ao adicionar a IPFS"
    exit 1
fi

echo ""
echo "✅ ADICIONADO COM SUCESSO!"
echo ""
echo "3️⃣  Informações do CID:"
echo "   CID: $CID"
echo ""
echo "4️⃣  Acessar BABEL via IPFS:"
echo "   Local:      http://localhost:8080/ipfs/$CID"
echo "   IPFS.io:    https://ipfs.io/ipfs/$CID"
echo "   Cloudflare: https://cloudflare-ipfs.com/ipfs/$CID"
echo ""

echo "5️⃣  Pinnar para persistência:"
echo "   ipfs pin add --recursive $CID"
echo ""

echo "6️⃣  Registrar CID:"
echo "$CID" > veracidade/ipfs-cid.txt
echo "   Salvo em: veracidade/ipfs-cid.txt"
echo ""

echo "7️⃣  Compartilhar CID:"
echo "   Tweet: BABEL está em IPFS: ipfs://$CID"
echo "   Email: https://ipfs.io/ipfs/$CID"
echo "   Chat:  https://gateway.pinata.cloud/ipfs/$CID"
echo ""

echo "✨ REPLICAÇÃO COMPLETA"
echo "   BABEL agora é parte da rede descentralizada"
echo "   Quanto mais pessoas pinnam, mais resiliente fica"

