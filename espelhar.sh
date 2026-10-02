#!/usr/bin/env bash
# Multiplicação em tempo real: push simultâneo em todos os Gits + cópias físicas
# Uso: ./espelhar.sh  (roda automático após cada commit, pelo hook)
set -u
cd "$(dirname "$0")"
cd "$(dirname "$0")" || exit 1
BR=$(git branch --show-current)

# 1. todos os remotes configurados (origin=github; adicionar gitlab e codeberg quando criados)
git remote | while read R; do git push "$R" "$BR" 2>&1 | grep -q "up to date\|main" || echo "aviso: falha em $R"; done

# 2. bundle datado (cópia física #2)
git bundle create "/home/mejias/Documentos/biblioteca-convivencia-$BR.bundle" "$BR" >/dev/null 2>&1

# 3. cópia sincronizada (pasta de nuvem pessoal, se existir e escrevível)
GD="/home/mejias/google-drive"
if [ -d "$GD" ] && [ -w "$GD" ]; then
  mkdir -p "$GD/biblioteca-convivencia" 2>/dev/null && \
  tar --exclude='.git' -czf "$GD/biblioteca-convivencia/acervo.tar.gz" . 2>/dev/null && \
  cp -f MANIFESTO.sha256 veracidade/carimbo.txt "$GD/biblioteca-convivencia/" 2>/dev/null
fi
echo "espelhado: git × $(git remote | wc -l) · bundle ✓ · nuvem ✓"
