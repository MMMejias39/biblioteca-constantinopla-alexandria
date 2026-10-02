#!/usr/bin/env python3
"""Validador Visena-HMF v0.1. jsonschema quando disponível; regras de dignidade e gatilhos SEMPRE."""
import json, sys, pathlib
DIR = pathlib.Path(__file__).parent
schema = json.loads((DIR / "visena-hmf.schema.json").read_text(encoding="utf-8"))
EVIDENCIAIS = {"ve", "ao", "so", "si", "su"}
ACOES_SEGURAS = {None, "nenhuma", "alerta_humano", "chamar_pessoa", "registrar"}

def validar(doc, erros):
    try:
        import jsonschema
        try:
            jsonschema.validate(doc, schema)
        except jsonschema.ValidationError as e:
            erros.append("[jsonschema] " + e.message)
    except ImportError:
        yield_note(erros)
    ev = doc.get("evidencial")
    if ev not in EVIDENCIAIS:
        erros.append(f"evidencial inválido: {ev!r}")
    if ev in ("so", "su") and "confianca" not in doc:
        erros.append("confianca (gran/pu) obrigatória quando evidencial é so/su")
    if doc.get("evento", {}).get("raiz") == "distress":
        if doc.get("prioridade") != "alta":
            erros.append("distress exige prioridade alta")
        a = doc.get("acao_sugerida", {}).get("tipo")
        if a not in {"nenhuma", "alerta_humano", "chamar_pessoa"}:
            erros.append(f"distress não admite ação automática: {a!r}")
    d = doc.get("dignidade", {})
    for k in ("distress_prioritario", "sem_atuacao_automata_de_confinamento", "fauna_e_ona"):
        if d.get(k) is not True:
            erros.append(f"dignidade.{k} deve ser true")

def yield_note(erros):
    erros.append("[modo básico: jsonschema indisponível]")

if __name__ == "__main__":
    ok = True
    for i, line in enumerate((l for l in (DIR / "exemplos.jsonl").read_text(encoding="utf-8").strip().splitlines() if l), 1):
        erros = []
        validar(json.loads(line), erros)
        status = "OK" if not erros else "FALHA: " + "; ".join(erros)
        print(f"exemplo {i} (positivo): {status}")
        ok &= not erros
    erros = []
    validar(json.loads((DIR / "exemplo-negativo.json").read_text(encoding="utf-8")), erros)
    print(f"exemplo-negativo: {'REJEITADO (correto)' if erros else 'ACEITO (ERRO GRAVE)'}")
    ok &= bool(erros)
    sys.exit(0 if ok else 1)
