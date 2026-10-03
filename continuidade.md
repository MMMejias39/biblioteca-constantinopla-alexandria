# Continuidade — sessão 2026-10-03 → retomada no dia seguinte

**Estado salvado:** v0.9 (`a5fa4e4`) sincronizada com `origin/main`; manifesto **38/38 OK**; carimbo mais recente `v0.9/126153764f835c5f7610bf297aa134204b3250c39b90741103975ba02e947999`.

## O que foi entregue hoje (para não re-fazer)
- **v0.5** — verificação de URLs (38/38 vivas) + ordem §5/§6 + §7 (registro do contrato)
- **v0.6/v0.7** — Visena-HMF executável: `idioma/schema/alp-config.yaml` + `pos_decodificar.py` + `exemplos-hook/` (5/5 no `--check`; `validar.py` 4 OK + 1 rejeitada); manifesto completo corrigido
- **v0.8** — verificação factual de `catalogo/poder-global.md` (vetos 161/95/32/21/18 de 271; ACT 121+2; UFP Res. 377 A (V); OTAN 32) com fontes anexadas
- **v0.9** — pendências viraram ferramentas: `espelhos/README.md` (7 espelhos, comandos), `espelhos/zenodo-metadata.json` + `ia-metadata.txt` (prontos para upload), `fria.sh` (edição de papel gerada em `biblioteca-fria/`), `veracidade/dossie-quorum-v0.1.md` (aguarda 4 assinaturas)

## Pendência imediata — Codeberg (jurisdição 2)
- Conta **MMMejias39** ✓ · remote local `codeberg` ✓ (HTTPS)
- SSH porta 22 → codeberg: *timeout* nesta rede (IPv4 e IPv6); GitHub SSH funciona → plano: **HTTPS + token**
- **Seus passos (amanhã):**
  1. `https://codeberg.org/repo/create` → nome `biblioteca-constantinopla-alexandria` → criar **vazio** (sem README/licença — nosso histórico já é o cânon)
  2. `https://codeberg.org/user/settings/applications` → token novo, escopo **repository: read+write** (mostrado uma única vez)
  3. Configurar como o Git guarda a senha (a documentação oficial: `git help` — guia de transporte HTTP; opção disco = texto puro no home, opção memória = ~15 min por sessão)
  4. `git push codeberg main` → usuário `MMMejias39` · senha = o token
- **Meus passos (quando o push rodar):** `git ls-remote codeberg main` ✓ → espelho marcado ✓ em `espelhos/README.md` → Codeberg entra no §3 de `permanencia.md` → versão nova (o hook espelha os dois a cada commit).
- *Plano B:* copiar sua chave SSH pública (pasta `~/.ssh/`, arquivo `.pub` — imprimi no seu terminal; eu não leio chaves) no Codeberg e fazer push SSH em outra rede; remote SSH então: `git@codeberg.org:MMMejias39/biblioteca-constantinopla-alexandria.git`.

## Fila depois do Codeberg (ordem sugerida)
1. Forgejo próprio (opcional) · 2. Uploads IA + Zenodo (comandos em `espelhos/README.md`; atualizar carimbo nos metadados a cada versão) · 3. IPFS (`ipfs add -r --cid-version 1 .` + pinning) · 4. Kiwix `.zim` (zimwriterfs sobre HTML do acervo) · 5. **Imprimir e assinar** `biblioteca-fria/biblioteca-fria-2026-*.txt` · 6. Línguista-par assina `veracidade/dossie-quorum-v0.1.md` · 7. Demonstração HMF real (instalar `alp-data`; Python ≥ 3.11 — pedido sob sua autorização).

## Regra que não muda
Correção antes de ruptura; append-only; cite `documento.md «versão/hash»`. Retomar por aqui: `sha256sum -c MANIFESTO.sha256` antes de confiar em qualquer cópia.
