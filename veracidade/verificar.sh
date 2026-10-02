#!/usr/bin/env bash
# Carimbo de Veracidade — marca intransferível de cada versão
# Uso: ./veracidade/verificar.sh   (roda após cada commit)
set -u
cd "$(dirname "$0")/.."
MAN="MANIFESTO.sha256"
CAR="veracidade/carimbo.txt"

# 1. regenera manifesto (todos os arquivos rastreados, exceto o manifesto e carimbo)
git ls-files | grep -vE "^($MAN$|veracidade/carimbo\.txt$)" | tr '\n' '\0' \
  | xargs -0 sha256sum > "$MAN"

# 2. carimbo = hash do manifesto + versão + data
HASH=$(sha256sum "$MAN" | cut -d' ' -f1)
DATA=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
VER=$1
echo "$VER $HASH $DATA" >> "$CAR"
echo "CARIMBO: versão=$VER hash=$HASH data=$DATA"
echo "  → cite assim: «$VER/$HASH»"

# 3. auto-verificação integral da cópia atual
echo "verificação: $(sha256sum -c "$MAN" 2>/dev/null | grep -c OK) arquivos OK"
