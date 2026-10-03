# Visena-HMF — Esquema de Etiquetas v0.1 (JSON)

Versão de verificação: 2026-10-03 · alinha com **alp-data** (ESP, `pip install alp-data`; 35+ datasets bioacústicos; `v1.10.0`, MIT — verificada 2026-10-03 no PyPI e em github.com/earthspecies/alp-data — procedência viaja com os dados) e **NatureLM-audio** (ICLR 2025 — verificada 2026-10-03).

## Mapeamento partícula → campo
| Visena | JSON |
|---|---|
| ve (testemunho direto) | `evidencial:"ve"` + `fonte.tipo` mic/camara/sensor/humano |
| so (diz-se/modelo) | `evidencial:"so"` + `fonte.modelo` + `confianca` obrigatória |
| su (incerto) | `evidencial:"su"` + `confianca` obrigatória |
| gran/pu (gradação) | `confianca:"gran"|"pu"` |
| ona (ser vivo) | `ona:{tipo,id,especie_hint}` |
| distress | `evento.raiz:"distress"` ⇒ `prioridade:"alta"` + `acao_sugerida` obrigatórias |

## Alinhamento alp-data
- `fonte.{dataset,licenca}` e `alp_data.{dataset,sample_id,sample_rate}` — procedência e link da amostra, coerente com a filosofia do alp-data ("provenance viaja com os dados").
- Amostra: áudio + taxa fixos + anotações — mapeiam para `visena` (frase), `evento.raiz` e `valor`.
- Fluxo: alp-data (amostra) → NatureLM-audio (tags) → Visena-HMF (etiqueta) → humano. Caminho reverso sempre termina em `acao_sugerida` com `aprovada_por_humano`.

## Dignidade executável
- `dignidade` é **required** com três const `true` — etiqueta sem dignidade é inválida por schema e por validador.
- `acao_sugerida.tipo` **exclui** abrir/fechar/capturar por desenho (regra 3 de `hmf.md`): máquina propõe, pessoa decide.
- `distress` exige prioridade alta sem atuação automática; só alertar.

## Uso
```bash
python3 idioma/schema/validar.py
```
Testes: 4 exemplos positivos devem passar; 1 exemplo-negativo deve ser rejeitado.

## Implementado — config + hook (2026-10-03), o "próximo passo" de v0.1
- `alp-config.yaml` — contrato alp-data → Visena-HMF: evidencial pela origem do rótulo (ve=sensor · so=modelo · ao=relato de outrem · si nunca por máquina); `confianca` automática (score ≥ 0,80 = `gran`, abaixo/ausente = `pu`); distress generoso (prioridade alta sempre — falso negativo custa mais); ações proibidas (abrir, fechar, capturar, confinar, sedar, mover) **recusadas e registradas** — nunca executadas, nunca silenciadas.
- `pos_decodificar.py` — hook pós-decodificação: alp-data (amostra) → NatureLM-audio (tags) → Visena-HMF (etiqueta) → humano; toda etiqueta valida em `validar.py` antes de sair; duas passadas para a recusa valer em qualquer ordem de tags; registro append-only (`--out`).
- `exemplos-hook/` — 4 positivos (ve · so gran · su pu · distress) + 1 recusa de atuação automática.

```bash
python3 idioma/schema/pos_decodificar.py --check          # 5 verificações declaradas
python3 idioma/schema/pos_decodificar.py exemplos-hook/entrada-so.json
```

## Próximo passo
Rodar em amostra real do alp-data (dataset e `sample_id` reais) e registrar no corpus bilíngue; validação por línguista-par: **pendente**.
