# Visena–HMF — Perfil Humano–Máquina–Fauna v0.1

Camada de interface da linguagem Visena para comunicação mediada por máquina com o bioma.
Verificação: 2026-10-02 · camada de decodificação já existe em campo aberto.

## Arquitetura em três camadas
1. **Fauna** — sinais multimodais reais (som, postura, química). Não se "fala" com animais em linguagem formal; se *escuta* e se *interpreta*.
2. **Máquina** — decodificação: NatureLM-audio (ESP, ICLR 2025) e alp-data (pip, 2026) para bioacústica/comportamento; sensores ambientais e de movimento.
3. **Visena** — interlíngua legível por humanos e rastreável: a máquina *não fala por* o animal; ela *testemunha* o que o animal comunica, em Visena, com evidencial obrigatório.

## Mapeamento dos evidenciais (a parte que acelera)
- **ve** = sensor/observação direta ("a câmera viu") — dado bruto.
- **so** = inferência do modelo — **obrigatório** anexar confiança: gran (alta) / pu (baixa).
- **ao** = relay secundário (outro nó, arquivo, relato registrado).
- **si** = estado interno humano (dor, alegria, pressentimento).
- **su** (nova partícula v0.1) = incerteza/provável — usada quando o modelo não distingue ve de so.

Fluxo típico: sinal do an → máquina decodifica → Visena: `An son gran, so pu.` ("diz-se que grande canto do animal — confiança baixa") → humano decide.

## Por que isso acelera (e não só facilita)
- **~40 raízes + morfologia zero** → tokenização trivial, baixa entropia: roda em hardware pequeno, resposta em tempo real.
- **Evidencial obrigatório** → máquinas não podem "falar confiança de sensor como se fosse fato"; esquema de procedência nasce na frase.
- **ASCII sem acentos + partículas fixas** → mapa 1:1 para tags estruturadas (parsers ingênuos, sem IA).
- **Léxico fechado** → aprendizado humano em dias, não anos.

## Sete regras de dignidade na interface
1. Fauna é **ona** em toda mensagem — nunca "telemetria", "amostra" ou "ruído".
2. Sinal de sofrimento de fauna tem **prioridade** e não pode ser suprimido pela máquina.
3. Nenhuma atuação automática de confinamento, dano ou captura a partir de sinais de fauna.
4. Interpretação de fauna é sempre **si** (humano sente/decide); máquina propõe, pessoa decide.
5. Sinais falsos negativos custam mais que falsos positivos: reportar abundância e presença com generosidade.
6. Tudo que a máquina testemunha fica registrado no corpus, com data e evidencial.
7. A fauna não precisa "aprender Visena": quem se adapta à interface é o lado humano-máquina.

## Compatibilidade registrada
- **NatureLM-audio** — modelo fundacional de áudio para bioacústica (ESP). https://earthspecies.org
- **alp-data** — camada compartilhada de dados para procesamento de linguagem animal (pip, 2026). https://earthspecies.org
- Encaixe: alp-data/NatureLM → (etiquetas de evento) → Visena–HMF (frase com evidencial) → humano; caminho reverso para atuação segura.
