# Marca de Veracidade — a doutrina v0.1
**O texto vence o intérprete.** A Bíblia e o Alcorão não foram deturpados por falta de fé — foram deturpados por interpretação **sem marca**. Tudo que este projeto afirma carrega um selo verificável: versão + hash + data.

## Como a marca funciona
1. Cada versão da biblioteca gera um **carimbo**: `(versão, SHA-256 do manifesto, data UTC)` — registrado em `veracidade/carimbo.txt`.
2. **Qualquer cópia** (GitHub, pendrive, papel, e-mail) se prova com `sha256sum -c MANIFESTO.sha256` — 22+ OK = fiel; divergência = denunciada, não discutida.
3. **Regra de citação**: quem interpreta, cita `versão/hash` — a leitura fica amarrada ao texto que a produziu (o isnad do hadith, aplicado a documentos).
4. **Interpretação separada**: comentários, ensaios e exegeses vão em pastas de interpretação — **nunca entram no cânon por fusão**. O cânon pode mudar só por versão nova, citando a antiga (append-only). Precedentes: Mishná ≠ Gemará; marginalia ≠ texto; Tafsir ≠ Alcorão.
5. **Divergência de cópias** resolve por **cadeia de hashes**, não por autoridade de quem grita mais alto.

## A raiz do dano (o que corrigimos)
Interpretações de palavras e frases — definidos por poder, não por evidência — foram o motor de cruzadas, inquisições e fatwas. A marca vira isso: **a prova vem antes da afirmação** (regra 4 de Visena, agora com selo).
