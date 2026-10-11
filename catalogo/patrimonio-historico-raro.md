# Catálogo — Patrimônio Histórico Raro e Documentação em Risco
**Prioridade:** memória documental que já foi, ou está em risco de ser, destruída, dispersa ou perdida — o problema que dá nome ao projeto (Alexandria, Constantinopla).
Referência de verificação: 2026-10-11.

## Arquivos em risco, resgatados
- **Endangered Archives Programme (EAP) — British Library / Arcadia Fund** — financia a digitalização de arquivos em risco de destruição, negligência ou deterioração física em todo o mundo. Desde 2004: 465+ projetos financiados em 90+ países, em mais de 100 idiomas e escritas, 11+ milhões de imagens e 35.000 trilhas sonoras digitalizadas. As cópias digitais ficam disponíveis gratuitamente online pelo site do EAP e pelo catálogo da British Library, além de uma cópia permanecer no país de origem. https://eap.bl.uk — *Nota: não verifiquei uma licença única e explícita (tipo CC0) para todo o acervo via fetch automatizado (site retorna shell JS); o acesso de leitura é gratuito e documentado pela própria British Library, mas reuso/redistribuição em massa deve ser confirmado item a item antes de integrar ao BABEL.*

- **Manuscritos de Timbuktu — "Mali Magic" (Google Arts & Culture + SAVAMA-DCI)** — dezenas de milhares de manuscritos (matemática, direito, astronomia, medicina, poesia) salvos por arquivistas malineses durante a ocupação de Timbuktu por grupo jihadista em 2012, que destruiu mausoléus e bibliotecas de 700 anos. Esforço de digitalização de 8 anos resultou em 40.000+ páginas em alta resolução, disponíveis gratuitamente em árabe, inglês, espanhol e francês. Acesso: coleção "Mali Magic" no Google Arts & Culture (artsandculture.google.com), parceria com a organização malinesa SAVAMA-DCI. *Eco direto do tema fundador do BABEL: conhecimento salvo da destruição deliberada, preservado via replicação.*

- **Papiros de Herculano — Vesuvius Challenge** — a única biblioteca da Antiguidade conhecida que sobreviveu intacta (carbonizada pela erupção do Vesúvio, 79 d.C.). Em junho de 2026, o primeiro rolo (PHerc. 1667) foi lido por completo pela primeira vez em ~2000 anos, via micro-CT + IA, sem desenrolar o papiro fisicamente — 16 rolos já desenrolados virtualmente em 2026. Dados (volumes de tomografia 3D, segmentos, predições de IA) disponíveis publicamente em bucket AWS S3, sem necessidade de conta. **Licença: CC BY-NC 4.0 (não-comercial)** — compatível com uso do BABEL (sem fins lucrativos), mas **incompatível com redistribuir como CC0** (teria que manter a atribuição + restrição não-comercial, não pode "soltar" a licença). https://registry.opendata.aws/vesuvius-challenge-herculaneum-scrolls/ · dados técnicos: https://scrollprize.org/data

## Bibliotecas nacionais e transnacionais digitais
- **BNDigital — Biblioteca Nacional Digital do Brasil** — mais de 3,09 milhões de documentos de acesso livre (hemeroteca, cartografia, iconografia, manuscritos, música, obras raras). Disponibiliza **apenas** obras em domínio público ou com autorização expressa do titular dos direitos (exceção: discos de 78 rotações, só acessíveis presencialmente). Sem necessidade de cadastro. https://bndigital.bn.gov.br — licença confirmada por fonte oficial da Fundação Biblioteca Nacional. **✅ Compatível com CC0.**

- **World Digital Library (Library of Congress)** — 19.000+ itens de quase 200 países, datando de 8000 a.C., mantida hoje pela Library of Congress dos EUA (originalmente projeto conjunto com a UNESCO). A LoC declara não ter conhecimento de restrições de copyright no acervo e considera os materiais "livres para usar e reusar", pedindo apenas crédito (não é exigência legal). https://www.loc.gov/collections/world-digital-library/ — **✅ Compatível com CC0** (maior confiança entre as fontes internacionais verificadas aqui).

- **Gallica (Bibliothèque nationale de France)** — 10 milhões de documentos digitalizados (livros, manuscritos, mapas, partituras, fotografias, objetos), majoritariamente domínio público, de 300+ instituições parceiras. **Licença: reuso não-comercial livre com atribuição da fonte** — mesma ressalva do caso Herculano: uso ok para o BABEL, mas não pode ser "rebaixado" para CC0 puro sem violar a condição de não-comercialidade da BnF. https://gallica.bnf.fr — **⚠️ Compatível com uso, não com redistribuição CC0 irrestrita.**

## Acesso de leitura apenas — NÃO integrar sem autorização expressa
- **Biblioteca do Vaticano (DigiVatLib)** — leitura gratuita, sem cadastro, de manuscritos, incunábulos e materiais de arquivo digitalizados via tecnologia IIIF. **Mas o conteúdo é expressamente protegido por copyright da Biblioteca Apostólica Vaticana: "neither the text nor the images may be reproduced, in any form, without the authorisation"** — ou seja, dá para consultar, mas não dá para copiar/integrar ao BABEL sem pedir permissão explícita primeiro. https://digi.vatlib.it — **❌ Não integrar sem autorização.** Registrado aqui só como fonte de consulta/descoberta, não para cópia.

## Registros de significância (descoberta, não repositório único)
- **UNESCO Memory of the World** — não é um repositório único de arquivos, é um **registro internacional** que reconhece e sinaliza documentação de significância histórica mundial (atualmente com registros regionais Ásia-Pacífico, África, Europa/América do Norte). Em 2026: US$ 6 milhões anunciados (abril/2026) para digitalização e preservação de coleções frágeis/em risco; primeiro depósito do próprio Registro Internacional no Arctic World Archive (fevereiro/2026). Útil como **mapa de descoberta** para encontrar itens raros específicos — cada item listado tem sua própria instituição custodiante e seus próprios termos de acesso, que precisam ser verificados individualmente. https://www.unesco.org/en/memory-world

## Metodologia desta entrada (transparência)
Esta lista foi montada com busca real (WebSearch) e tentativa de verificação direta das fontes (WebFetch/curl) em 2026-10-11, seguindo o mesmo padrão de citação dos demais arquivos deste catálogo e aplicando manualmente o "Filtro 1: Licença" descrito em `MINEIROS-CONHECIMENTO.md`.

**Resumo de compatibilidade de licença (para quem for integrar depois):**

| Fonte | Licença | Compatível com CC0? |
|---|---|---|
| BNDigital | Domínio público / autorização expressa | ✅ Sim |
| World Digital Library (LoC) | Sem restrições conhecidas, livre reuso | ✅ Sim |
| Timbuktu (Mali Magic) | Visualização gratuita; termos de reuso em massa não verificados | ⚠️ Verificar antes de copiar |
| EAP (British Library) | Leitura gratuita; termos de reuso em massa não verificados (site não renderizou via fetch) | ⚠️ Verificar antes de copiar |
| Gallica (BnF) | Reuso **não-comercial** com atribuição | ⚠️ Uso ok, redistribuição CC0 não |
| Herculaneum Papyri | CC BY-NC 4.0 | ⚠️ Uso ok, redistribuição CC0 não |
| Vatican DigiVatLib | Copyright reservado, reprodução proibida sem autorização | ❌ Não integrar |

**Próximo passo sugerido:** para uma integração piloto de baixo risco, priorizar BNDigital ou World Digital Library (✅ CC0 compatível, sem ressalvas) — escolher 1 item específico, baixar, verificar hash, catalogar em `catalogo/descobertas/`, testando manualmente o resto do pipeline descrito em `MINEIROS-CONHECIMENTO.md` (avaliação → ético → integrador) antes de automatizar.

**Arquivo adormecido — ativação só em caso de dano ao original:** para as fontes ✅ e ⚠️ desta lista, o papel do BABEL é guardar uma cópia verificada (hash + metadados) sem servi-la publicamente enquanto a fonte original estiver no ar e saudável — o BABEL aponta para o ORIGINAL, não compete com ele nem redistribui ativamente. A cópia só é tornada pública se o original for danificado, sair do ar ou tiver acesso restringido/censurado; nesse momento o objetivo de preservação para a humanidade e o futuro ativa a distribuição. Isso é compatível com as fontes ⚠️ (Gallica, Herculaneum Papyri): licença CC BY-NC permite a cópia para preservação, o que muda é só quando ela é servida publicamente. Não se aplica à fonte ❌ (Vatican DigiVatLib) — ali a cópia não deveria existir, dano ao original ou não.
