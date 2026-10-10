# Catalogação Descentralizada — Organização, Busca, Descoberta

**Problema:** BABEL replica informação, mas como alguém ENCONTRA algo?

**Solução:** Sistema de catalogação agnóstico, descentralizado, colaborativo que funciona sem bibliotecário central.

---

## I. O Que Falta em BABEL

### Comparação: Biblioteca Física vs. BABEL

```
BIBLIOTECA FÍSICA:
  ✓ Catalogação (Dewey, LC, etc.)
  ✓ Índice de assuntos
  ✓ Fichas bibliográficas
  ✓ Localização física (prateleira 3B)
  ✓ Busca por tema, autor, data
  ✓ Recomendações (livros relacionados)
  ✓ Controle de qualidade (revisão)
  ✓ Política de aquisição

BABEL ATUAL:
  ✓ Replicação universal
  ✓ Integridade (hash)
  ✓ Histórico (append-only)
  ✓ Consenso (quórum aprova)
  
  ✗ Catalogação estruturada
  ✗ Metadados padronizados
  ✗ Busca organizada
  ✗ Indexação por tema
  ✗ Rotulagem
  ✗ Localização (onde está?)
  ✗ Relacionamentos (links entre documentos)
  ✗ Descoberta (como achei isto?)

RESULTADO: BABEL replica mas não organiza. Informação fica "perdida no ar".
```

---

## II. Catálogo Descentralizado — Princípios

### Como organizar sem bibliotecário central?

```
PRINCÍPIO 1: METADADOS UNIVERSAIS
  Cada documento tem:
    - Identificador único (UUID ou hash)
    - Título
    - Autor/Origem
    - Data de criação/modificação
    - Descrição breve
    - Licença
    - Idioma
    - Tema principal (1-3 palavras-chave)
    - Tema secundário (tags opcionais)
    - Relacionamentos (links para documentos afins)
    - Fonte original (de onde veio)
    - Versão/Edição
    - Qualidade (revisado? verificado?)

PRINCÍPIO 2: CATALOGAÇÃO DISTRIBUÍDA
  Não há catalogador central.
  Qualquer pessoa pode:
    - Catalogar seu próprio documento (cria metadados)
    - Sugerir catalogação para outro documento
    - Refinar tags/descrições (consenso melhora)
    - Apontar relacionamentos

PRINCÍPIO 3: PADRÕES ABERTOS
  Usa padrões existentes (Dublin Core, schema.org):
    - Compatível com Google Scholar
    - Compatível com bibliotecas digitais
    - Compatível com Zenodo, Archive.org
    - Não reinventa roda

PRINCÍPIO 4: VERSIONAMENTO DE METADADOS
  Metadados também são versionados (append-only):
    - Documento v1 → descrição A
    - Documento v1 → descrição B (melhorada)
    - Documento v2 → descrição C (nova versão do doc)
    - Histórico sempre preservado

PRINCÍPIO 5: TAGS = CONSENSO DESCENTRALIZADO
  Ninguém é dono das tags.
  Tags emergem do uso coletivo:
    - Pessoa A adiciona: "biodiversidade"
    - Pessoa B adiciona: "amazonia"
    - Pessoa C adiciona: "mata-atlantica"
    → Índice converge naturalmente
    → Consenso sem votação

PRINCÍPIO 6: BUSCA AGNÓSTICA
  Busca funciona em QUALQUER meio:
    - Texto puro: grep biodiversidade /babel/*.txt
    - Índice local: busca em catálogo local
    - IPFS: busca em nós com índice
    - Papel: índice impresso
    - Oral: "me recomenda algo sobre..."
```

---

## III. Estrutura de Metadados (Texto Puro)

### Como representar catalogação em arquivo texto?

```
FORMATO: Cada documento tem bloco de metadados

---
ID: uuid-v4-ou-hash-curto
TITULO: Nome Completo do Documento
AUTOR: Autor(es) ou "Coletivo BABEL"
DATA_CRIACAO: 2026-10-09
DATA_MODIFICACAO: 2026-10-15
DATA_VERIFICACAO: 2026-10-15 (última revisão)
VERSAO: 1.2
LICENCA: CC0 | CC-BY | CC-BY-SA | GPL | Outro
IDIOMA: pt | en | es | fr | zh | ar | ja | [outras]
TAMANHO: 1.2 MB
HASH_SHA256: a7f2e3c9...
FONTE_ORIGINAL: https://arxiv.org/... | null
TIPO: documento | artigo | livro | dados | código | outro
STATUS: publicado | rascunho | revisar | obsoleto
QUALIDADE: verificado | revisado | pendente | contestado
TEMA_PRINCIPAL: biodiversidade | educação | saúde | tecnologia | [tags]
TEMA_SECUNDARIO: tag1, tag2, tag3
DESCRICAO: Uma linha com resumo (max 200 caracteres)
RESUMO: Parágrafo explicativo (max 500 caracteres)
RELACIONADOS: id1, id2, id3 (documentos afins)
PRECURSOR: id-anterior (versão anterior deste documento)
SUCESSOR: id-proximo (versão mais nova)
TAGS_USUARIO: forest, indigenous, climate (tags que comunidade adiciona)
CONTRIBUIDORES: pessoa1, pessoa2, coletivo3
REVISORES: revisor1 (confirmou qualidade)
NIVEL_ACESSO: publico | restrito | privado
CONTATO_CURADOR: email@exemplo.com (quem posso perguntar?)
---

[CONTEÚDO AQUI]

---
```

**Isto é agnóstico:** Qualquer editor de texto consegue ler.

---

## IV. Índice Centralizado (Mas Replicado)

### Como organizar múltiplos documentos?

```
ARQUIVO: /babel/INDICE.csv
(CSV texto puro, compatível com qualquer planilha)

ID,TITULO,AUTOR,DATA,TEMA,SUBTEMAS,HASH,TIPO,QUALIDADE,IDIOMA
uuid-1,"Biodiversidade da Amazônia","Silva et al.",2025-03-15,"biodiversidade","floresta,amazonia,brasil","a7f2e3c9...",artigo,verificado,pt
uuid-2,"Guia CARE para Povos Indígenas","Coletivo BABEL",2026-10-09,"indigena","CARE,direitos,gestao","b8f3e4d0...",documento,revisado,pt
uuid-3,"Sistema de Governança Distribuída","Marcelo",2026-10-09,"tecnologia","consenso,governance,descentralizado","c9g4e5e1...",artigo,pendente,pt
...

VANTAGENS:
  ✓ Simples (CSV é universal)
  ✓ Buscável (qualquer ferramenta abre)
  ✓ Compatível (importa em Excel, Google Sheets, etc.)
  ✓ Agnóstico (não requer software específico)
  ✓ Replicável (cabe em USB, email, papel)

COMO MANTER?
  - Qualquer pessoa pode sugerir adição
  - Quórum valida (é qualidade suficiente?)
  - Automaticamente gerado de metadados dos documentos
  - Versionado (INDICE_v1.0.csv, INDICE_v1.1.csv, etc.)

RESULTADO: Catálogo central mas descentralizado (em 1000+ lugares)
```

---

## V. Busca Agnóstica (5 Formas)

### Como encontrar conhecimento em BABEL?

```
BUSCA 1: GREP (linha de comando)
  grep -r "biodiversidade" /babel/
  → Lista todos documentos mencionando termo
  
  Funciona em: terminal, offline, qualquer SO
  Custo: R$ 0

BUSCA 2: ÍNDICE LOCAL (spreadsheet)
  Baixa INDICE.csv
  Abre em planilha (Excel, Google Sheets, LibreOffice)
  Procura por tema, autor, data
  Filtra por critério
  
  Funciona em: qualquer computador
  Custo: R$ 0

BUSCA 3: BUSCA FULL-TEXT (índice invertido)
  Sistema local indexa: "biodiversidade" → documentos 1, 3, 5
  Pessoa digita: "mata atlantica"
  → Retorna documentos contendo termo
  
  Funciona em: IPFS com índice, servidor local, etc.
  Custo: R$ 0 (software aberto)

BUSCA 4: NAVEGAÇÃO POR TEMA (Taxonomia)
  Estrutura hierárquica:
    ├─ Biodiversidade
    │  ├─ Floresta
    │  │  ├─ Amazônia
    │  │  └─ Mata Atlântica
    │  ├─ Oceano
    │  └─ Urbano
    ├─ Educação
    └─ Tecnologia
  
  Pessoa clica: Biodiversidade → Floresta → Amazônia
  → Vê todos documentos naquela categoria
  
  Funciona em: website BABEL, app mobile, papel impresso
  Custo: R$ 0

BUSCA 5: RECOMENDAÇÃO SOCIAL (Boca-a-Boca)
  "Procuro algo sobre povos indígenas"
  Amigo: "Leia documento uuid-2, é bom"
  Você: Acha uuid-2 no índice, acessa
  
  Funciona em: conversas, grupos WhatsApp, reuniões
  Custo: R$ 0 (é como sempre funcionou)

RESULTADO: 5 formas de busca funcionam SEM infraestrutura central
```

---

## VI. Taxonomia Descentralizada (Ontologia Simples)

### Como organizar temas sem autoridade central?

```
ABORDAGEM 1: TAXONOMIA FACETADA
  Dimensões de busca:

  TEMA (Disciplina):
    ├─ Biodiversidade
    ├─ Educação
    ├─ Saúde
    ├─ Tecnologia
    ├─ Governance
    └─ Outro

  TIPO (Formato):
    ├─ Artigo científico
    ├─ Livro/Capítulo
    ├─ Dados (dataset)
    ├─ Código/Software
    ├─ Guia prático
    ├─ Manifesto
    └─ Outro

  IDIOMA:
    ├─ Português
    ├─ Inglês
    ├─ Espanhol
    └─ Outros

  QUALIDADE:
    ├─ Verificado (revisão pares)
    ├─ Revisado (por quórum)
    ├─ Publicado (em meio reconhecido)
    └─ Pendente

  REGIÃO/CONTEXTO:
    ├─ Brasil
    ├─ América Latina
    ├─ Global
    └─ Específico

Busca facetada:
  Filtro 1: Tema = Biodiversidade
  Filtro 2: Tipo = Artigo científico
  Filtro 3: Idioma = Português
  Filtro 4: Qualidade = Verificado
  → Retorna documentos matching

ABORDAGEM 2: TAGS EMERGENTES (Folksonomia)
  Sem estrutura predefinida.
  Comunidade cria tags organicamente:
    - Pessoa 1 adiciona: "biodiversidade"
    - Pessoa 2 adiciona: "floresta"
    - Pessoa 3 adiciona: "amazonia"
    - Pessoa 4 adiciona: "indigenous"
    → Cloud de tags converge naturalmente
    → Mais menções = mais relevante

  Ferramenta de análise mostra:
    biodiversidade (453 usos)
    ├─ floresta (298 usos)
    │  ├─ amazonia (187 usos)
    │  └─ atlantica (94 usos)
    ├─ oceano (112 usos)
    └─ urbano (43 usos)

ABORDAGEM 3: HIBRIDIZAÇÃO (Taxonomia + Tags)
  Categoria obrigatória (estruturada):
    Documento → Tema = "Biodiversidade"
  
  Tags opcionais (descentralizadas):
    Documento → Tags = "floresta, amazon, nativa, sustentavel"
  
  Resultado: Estrutura + flexibilidade

RECOMENDAÇÃO: Híbrido
  - Taxonomia facetada simples (6-7 dimensões)
  - Tags emergentes da comunidade
  - Índice automático mostra relação entre tags
  - Sem autoridade (comunidade decide, não centro)
```

---

## VII. Rotulagem Colaborativa (Consenso Semântico)

### Como comunidade monta a catalogação?

```
PROCESSO:

1. DOCUMENTO CHEGA
   Quórum o aprova (consenso básico)
   Adquire metadados mínimos:
     - ID único
     - Título
     - Autor
     - Hash
     - Descrição

2. CATALOGAÇÃO INICIAL
   Submissor (ou primeiro revisor) adiciona:
     - Tema principal (1 escolha)
     - Tipo (artigo/livro/dados/etc.)
     - Idioma
     - Resumo breve

3. SUGESTÕES COLABORATIVAS
   Qualquer pessoa pode sugerir:
     - Tags adicionais ("biodiversidade", "amazonia")
     - Tema secundário ("educação", "governança")
     - Relacionamentos ("conecta com documento X")
     - Melhor descrição (reescreve resumo)

4. CONSENSO SEMÂNTICO
   Tags ganham "peso" (quantos usaram?):
     biodiversidade (5 sugestões)
     forest (2 sugestões)
     amazon (8 sugestões)
     indigenous-rights (1 sugestão)
   
   Mostra: "8 pessoas adicionaram 'amazon'"
   Comunidade vê consenso emergindo

5. INTEGRAÇÃO
   Tags com consenso (5+ sugestões) viram oficiais
   Outras ficam como "sugestões comunitárias"
   Todas ficam registradas no histórico append-only

6. EVOLUÇÃO
   Nova pessoa vê documento catalogado
   Adiciona tag nova: "climate-change"
   Depois 3 pessoas concordam
   Sobe para "tag sugerida"
   Depois 5 pessoas adicionam
   Vira "tag oficial"

RESULTADO: Catalogação cresce com comunidade
           Sem autoridade central
           Transparente (tudo é histórico)
```

---

## VIII. Integração com Padrões Existentes

### Como BABEL fala com bibliotecas já existentes?

```
DUBLIN CORE (Padrão internacional de metadados)

Mapeamento BABEL → Dublin Core:

BABEL                    →  Dublin Core
---                          ---
TITULO                   →  dc:title
AUTOR                    →  dc:creator
DATA_CRIACAO             →  dc:issued
DATA_MODIFICACAO         →  dc:modified
DESCRICAO                →  dc:description
RESUMO                   →  dc:abstract
IDIOMA                   →  dc:language
FONTE_ORIGINAL           →  dc:isVersionOf
LICENCA                  →  dc:license
RELACIONADOS             →  dc:relation
TIPO                     →  dc:type
TEMA_PRINCIPAL           →  dc:subject

Resultado: Arquivo BABEL consegue exportar para Dublin Core
           Compatível com Google Scholar
           Compatível com OAI-PMH (protocolo de repositórios)
           Compatível com Zenodo
           Compatível com Archive.org

---

CITABILIDADE

Documento BABEL deve ser citável:

Formato APA:
  Coletivo BABEL. (2026). Guia CARE para Povos Indígenas. 
  Recuperado de https://babel-library.org/uuid-2
  DOI: 10.5281/zenodo.12345678

Formato BibTeX:
  @misc{babel2026guide,
    title={Guia CARE para Povos Indígenas},
    author={Coletivo BABEL},
    year={2026},
    url={https://babel-library.org/uuid-2},
    doi={10.5281/zenodo.12345678}
  }

Como conseguir DOI?
  - Registra em Zenodo (gratuito)
  - Zenodo gera DOI automático
  - DOI fica permanente mesmo se BABEL sai do ar

Resultado: Pesquisadores conseguem citar BABEL
           Rastreabilidade acadêmica
           Integração com ferramentas de referência (Zotero, Mendeley)
```

---

## IX. Busca por Contexto (Recomendação Inteligente)

### Como descobrir documentos relacionados?

```
CONTEXTO 1: LEITURA
  Você está lendo: "Biodiversidade da Amazônia"
  Sistema mostra:
    - Documentos citados neste (autor mencionou)
    - Documentos que citam este (outros concordam)
    - Documentos com tags iguais (mesma categoria)
    - Documentos com tags relacionadas (próximas)

CONTEXTO 2: BUSCA
  Você buscou: "povos indígenas"
  Sistema mostra:
    - Documentos com tag "indigenous"
    - Documentos com tag "CARE"
    - Documentos com tag relacionada "rights"
    - Documentos que citam "povos indígenas"

CONTEXTO 3: HISTÓRICO
  Você leu 5 documentos sobre "biodiversidade"
  Sistema aprende seu interesse
  Recomenda: "Baseado no que você leu, temos X novo sobre..."

CONTEXTO 4: COMUNIDADE
  Outras pessoas com histórico similar a você leram Y
  Sistema recomenda: "Pessoas que leram isto também leram..."

MECANISMO AGNÓSTICO (sem IA):
  Recomendação = "tag overlap"
  Se documento A tem tags: [biodiversidade, floresta, amazonia]
  E documento B tem tags: [biodiversidade, floresta]
  → Similaridade = 2/3 tags em comum
  → Recomendar B a quem lê A

Cálculo simples:
  similaridade(A, B) = tags_em_comum / max(len(tags_A), len(tags_B))
  Se > 0.5 → recomenda

Resultado: Busca "inteligente" sem algoritmo complexo
           Funciona em texto puro
           Agnóstico
```

---

## X. Implementação Mínima (Comece Agora)

### Estrutura inicial de catalogação

```
ARQUIVO 1: /babel/INDICE.md

---
# ÍNDICE BABEL v1.0
## Catalogação Descentralizada

[Tabela de documentos]

| ID | Título | Tema | Data | Qualidade |
|----|--------|------|------|-----------|
| uuid-1 | Guia CARE | Governance | 2026-10-09 | Revisado |
| uuid-2 | Biodiversidade Amazônia | Biodiversidade | 2025-03-15 | Verificado |
| uuid-3 | Replicação Universal | Tecnologia | 2026-10-09 | Pendente |

---

ARQUIVO 2: /babel/METADADOS.yaml (ou .txt)

documento:
  id: uuid-1
  titulo: "Guia CARE para Povos Indígenas"
  tema: [governance, indigenous, rights]
  tipo: documento
  status: publicado
  hash: a7f2e3c9...
  relacionados: [uuid-2, uuid-3]

---

ARQUIVO 3: /babel/TAGS.csv (tag → documentos)

tag,frequencia,documentos
biodiversidade,12,"uuid-2, uuid-5, uuid-8"
floresta,8,"uuid-2, uuid-4, uuid-6"
amazonia,6,"uuid-2, uuid-3, uuid-7"
indigenous,10,"uuid-1, uuid-4, uuid-9"

---

COMEÇAR:
  1. Criar INDICE.md (lista de todos docs)
  2. Criar pasta /metadados/ (um .txt por documento)
  3. Criar TAGS.csv (relação tags-documentos)
  4. Comunidade colabora adicionando/refinando

Pronto. Catalogação começou.
```

---

## XI. Resultado: Biblioteca Completa

### O que você consegue com catalogação

```
ANTES (BABEL sem catalogação):
  ✗ "Tenho 50.000 documentos"
  ✗ "Como acho biodiversidade?"
  ✗ "Está perdido em lugar nenhum"
  ✗ "Ninguém consegue usar"

DEPOIS (BABEL com catalogação):
  ✓ "50.000 documentos em 4 categorias"
  ✓ "Busca: 'biodiversidade' → 2.340 resultados"
  ✓ "Filtro: Portugal + português + artigos verificados"
  ✓ "Resultado: 47 artigos científicos sobre biodiversidade em PT"
  ✓ "Relacionados: X, Y, Z (por tag overlap)"
  ✓ "Citável: documento tem DOI, aparece em Google Scholar"
  ✓ "Rastreável: todas edições + histórico de catalogação"

CARACTERÍSTICAS:
  ✓ Agnóstico (texto puro + CSV + padrões abertos)
  ✓ Descentralizado (qualquer pessoa contribui)
  ✓ Compatível (Dublin Core, schema.org, Google Scholar, Zenodo)
  ✓ Simples (não requer tecnologia complexa)
  ✓ Extensível (comunidade adiciona dimensões)
  ✓ Colaborativo (consenso semântico)
  ✓ Transparente (histórico append-only)
  ✓ Citável (DOI, BibTeX, APA)
  ✓ Buscável (5+ métodos de busca)
  ✓ Recomendável (relacionamentos inteligentes)

CUSTO: R$ 0 (tudo é padrão aberto)
```

---

**Versão:** v1.0  
**Status:** Desenho de catalogação descentralizada  
**Princípio:** Bibliotecário = comunidade, não centro  
**Durabilidade:** Indefinida (agnóstica, texto puro)
