#!/usr/bin/env bash
# Biblioteca fria — a edição anual em papel (verificação humana como checksum)
# Gera texto simples (sem formatos proprietários) + carimbo + manifesto no final.
# Saída: biblioteca-fria/ (ignorada pelo Git — a mídia é papel, não o repo)
set -euo pipefail
cd "$(dirname "$0")"
ANO=$(date -u +"%Y")
CAR=$(tail -1 veracidade/carimbo.txt)
HASH=$(echo "$CAR" | cut -d' ' -f2 | head -c 12)
OUT="biblioteca-fria/biblioteca-fria-$ANO-$HASH.txt"
mkdir -p biblioteca-fria
{
printf '%s\n' \
"════════════════════════════════════════════════════════════════" \
" BIBLIOTECA CONSTANTINOPLA–ALEXANDRIA — EDIÇÃO FRIA $ANO" \
" Ninguém é dono de nada. Quem mantém, kuro (cuida)." \
" Ordem dos pilares: 1) vida abundante na Terra · 2) dignidade para" \
" pessoas e outros animais. CARE antes de FAIR." \
"════════════════════════════════════════════════════════════════" \
"" "— Carimbo desta edição —" "$CAR" "" \
"— Prova da cópia — sha256sum -c MANIFESTO.sha256 (rodar contra o manifesto impresso ao final)" ""
for f in carta-da-convivencia.md consenso-global.md permanencia.md preservacao.md \
         README.md catalogo/*.md veracidade/README.md \
         idioma/README.md idioma/gramatica.md idioma/lexico.md idioma/frases.md \
         idioma/processo.md idioma/hmf.md idioma/schema/README.md espelhos/README.md veracidade/dossie-quorum-v0.1.md; do
  printf '\n────────────────────────────────────────────────────────────────\nARQUIVO: %s\n\n' "$f"
  cat "$f"
done
printf '\n════════════════════════════════════════════════════════════════\nMANIFESTO SHA-256 (a prova no papel)\n\n'
cat MANIFESTO.sha256
printf '\n— Assinaturas dos guardiões (quórum §2 de permanencia.md) —\n'
printf '%s\n' "línguista-par: ______  data: ____  guardião Pilar 1: ______  data: ____  guardião Pilar 2: ______  data: ____  guardião CARE: ______  data: ____" \
"Revalidação viva: duas vezes ao ano, re-hash e re-ler; registrar quem conferiu."
} > "$OUT"
wc -l "$OUT"
echo "EDIÇÃO FRIA: $OUT"
