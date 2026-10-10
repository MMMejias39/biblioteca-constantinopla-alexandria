#!/bin/bash
# espelhar.sh — Replicação automática BABEL em múltiplos git services

set -e

echo "🌍 REPLICAÇÃO BABEL — Múltiplas Jurisdições"
echo "=============================================="

REPO_DIR=$(pwd)

echo "📤 ESPELHOS CONFIGURADOS:"
git remote -v

echo ""
echo "📤 SINCRONIZANDO..."

# Push para main (GitHub)
echo "  1️⃣  GitHub (USA)..."
git push origin main

# Push para cada remote configurado
for remote in $(git remote | grep -v origin); do
    echo "  ➡️  $remote..."
    if git push "$remote" main 2>/dev/null; then
        echo "     ✅ OK"
    else
        echo "     ⚠️  Falha (verifique credenciais)"
    fi
done

echo ""
echo "✅ SINCRONIZAÇÃO CONCLUÍDA"
echo ""
echo "📊 Status de Espelhos:"
git remote -v

echo ""
echo "🎯 Para adicionar novo espelho:"
echo "  git remote add <nome> <url>"
echo "  git push <nome> main"
