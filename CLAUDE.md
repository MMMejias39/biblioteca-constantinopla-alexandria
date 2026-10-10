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

## Estrutura

- `docs/index.html` — landing page multilíngue (8 idiomas), servida via GitHub Pages em https://mmmejias39.github.io/biblioteca-constantinopla-alexandria/. HTML/CSS/JS puro, sem build step.
- `catalogo/`, `idiomas/`, `divulgacao/`, `veracidade/` — conteúdo e materiais do projeto
- `babel-monitor/` — dashboard de monitoramento em Rust
