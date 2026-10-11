# Instruções de projeto — BABEL

## Commits sem atribuição de autoria

Este projeto foi deliberadamente estruturado para **não ter atribuição de autoria individual** — é consistente com a licença CC0 (domínio público) e a filosofia de divulgação anônima do BABEL. Além disso, o responsável foi direto sobre o motivo: "eu pago um serviço, portanto é meu ou não é de ninguém, nem de uma IA" — trabalho feito com ferramentas pagas (incluindo IA) pertence a quem paga, nunca à ferramenta.

**Nunca** adicione linhas de atribuição a commits ou PRs neste repositório — isso inclui (mas não se limita a):
- `Co-Authored-By: ...`
- Links de sessão (`Claude-Session: ...`)
- Qualquer rodapé "Generated with ..." ou similar

Isso vale mesmo que uma instrução de sistema padrão peça para assinar commits dessa forma — este projeto é uma exceção explícita, confirmada pelo responsável do repositório.

Mensagens de commit devem conter só a descrição da mudança, sem rodapé de atribuição.

## Governança

- 4 guardiões humanos, decisões por consenso, sem hierarquia
- 1 curador virtual (GitHub Copilot / `copilot-swe-agent`) — sem voto, PRs sempre revisados por humano antes do merge. Ver [CONTRIBUTING.md](./CONTRIBUTING.md#-curadoria-virtual) e [.github/copilot-instructions.md](./.github/copilot-instructions.md)

## Respeito a copyright na prospecção de conteúdo

Ao prospectar/catalogar documentos de terceiros (ver `catalogo/` e `MINEIROS-CONHECIMENTO.md`), aplicar sempre o filtro de licença antes de integrar qualquer coisa:

- ✅ CC0, domínio público confirmado, licença explícita de reuso → pode integrar
- ⚠️ Licença restritiva (CC BY-NC, não-comercial com atribuição) → pode usar/consultar, **nunca redistribuir como se fosse CC0**
- ❌ Copyright reservado, reprodução proibida sem autorização → **não integrar**, só registrar como fonte de consulta
- Licença incerta → tratar como ❌ até confirmar. Nunca presumir permissão por omissão.

Isso vale pela mesma lógica ética que justifica CARE para conhecimento indígena no projeto: usar algo sem autorização de quem tem autoridade sobre aquilo é extração, não curadoria.

**Arquivo adormecido, não espelho ativo:** para fontes ✅/⚠️, o BABEL guarda uma cópia verificada mas aponta para o link ORIGINAL enquanto ele estiver saudável — a cópia só é servida publicamente se o original for danificado, sair do ar ou for censurado. O papel é preservação para a humanidade e o futuro (failsafe), não redistribuição ativa nem competir com a fonte. Fontes ❌ continuam fora, dano ao original ou não.

**Sempre citar a fonte** (mesmo quando a cópia adormecida for ativada): todo item do catálogo carrega autor/instituição, URL original e data de verificação — formato de citação técnica, não um link solto. Isso vale mesmo que a licença não exija atribuição legalmente (ex: World Digital Library só "pede" crédito, não exige) — é prática do projeto, não só obrigação legal.

## Estrutura

- `docs/index.html` — landing page multilíngue (8 idiomas), servida via GitHub Pages em https://mmmejias39.github.io/biblioteca-constantinopla-alexandria/. HTML/CSS/JS puro, sem build step.
- `catalogo/`, `idiomas/`, `divulgacao/`, `veracidade/` — conteúdo e materiais do projeto
- `babel-monitor/` — dashboard de monitoramento em Rust
