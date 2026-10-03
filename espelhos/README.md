# Espelhos — lista operacional (núcleo Constantinopla)

Estado na verificação: **2026-10-03** (`permanencia.md «v0.8/bd883ea6…»`).
Regra: ≥3 mídias, ≥2 jurisdições. Hoje: disco local ✓ · GitHub ✓ (jurisdição US — risco) · bundle `~/Documentos` ✓ (mesmo disco — insuficiente) · tar.gz na nuvem pessoal (se configurada).

| # | Espelho | O que falta | Comando (quando pronto) | Jurisdição |
|---|---|---|---|---|
| 1 | **Codeberg** (Forgejo público) | conta em codeberg.org; criar repo | `git remote add codeberg git@codeberg.org:<usuário>/biblioteca-constantinopla-alexandria.git && git push codeberg main` | Alemanha — jurisdição 2 ✓ |
| 2 | **Forgejo próprio** | servidor/VM ou home-server | instância Forgejo + mesmo remote acima apontando pra ela | a definir pelo guardião |
| 3 | **Internet Archive** (acervo histórico público) | conta + chaves S3 do IA (`ia configure`; `pip install internetarchive`) | `ia upload biblioteca-constantinopla-alexandria --metadata-from-file espelhos/ia-metadata.txt espelhos/zenodo-metadata.json MANIFESTO.sha256 veracidade/carimbo.txt` | US — espelho público, não único |
| 4 | **Zenodo** (DOI citável, espelho acadêmico) | conta + token em zenodo.org → Configurações → Aplicações | `curl -X POST https://zenodo.org/api/deposit/depositions -H "Authorization: Bearer <TOKEN>"` + upload do bundle + `espelhos/zenodo-metadata.json` (1 DOI por versão do carimbo) | UE (CERN, Suíça) — jurisdição 2 ✓ |
| 5 | **IPFS** (rede sem dono) | nó próprio ou serviço de pinning (ex.: pinata) | `ipfs add -r --cid-version 1 .` e fixar o CID; registrar o CID no carimbo | nenhuma — sem dono ✓ |
| 6 | **Kiwix `.zim`** (offline comunitário) | zimwriterfs com o acervo em HTML | converter `biblioteca-fria/` para HTML → `zimwriterfs --welcome=index.html acervo-html biblioteca.zim` | offline — sem jurisdição ✓ |
| 7 | **Papel** (séc. de resistência) | impressão anual assinada | `./fria.sh` → imprimir `biblioteca-fria/…txt` + assinatura dos guardiões | física — sem jurisdição ✓ |

## Ordens permanentes
- Nenhum espelho é dono; GitHub hoje é espelho entre vários — migrar o **push automático** (`espelhar.sh`) assim que codeberg/forgejo existirem.
- Cada espelho novo entra no §3 de `permanencia.md` como versão nova citando a antiga.
- `sha256sum -c MANIFESTO.sha256` valida qualquer cópia antes de confiar (veracidade/README.md §2).
