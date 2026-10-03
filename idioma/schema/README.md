# Visena-HMF — Esquema de Etiquetas v0.1 (JSON)

Versão de verificação: 2026-10-02 · alinha com **alp-data** (ESP, `pip install alp-data`, 35+ datasets bioacústicos, procedência viaja com os dados) e **NatureLM-audio**.

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

## Próximo passo
Config YAML do alp-data + hook pós-decodificação que emite Visena-HMF com `confianca` automática do modelo.
