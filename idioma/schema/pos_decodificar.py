#!/usr/bin/env python3
"""Visena-HMF — hook pós-decodificação v0.1 (2026-10-03)

Roda APÓS o modelo (NatureLM-audio sobre alp-data) e emite etiquetas
Visena-HMF com:
  · evidencial automático pela ORIGEM do rótulo (ve=sensor · so=modelo · ao=relato de outrem ·
    su=sem pontuação do modelo · si nunca emite).
  · confianca automática pela PONTUAÇÃO do modelo (score >= 0,80 = gran; abaixo/ausente = pu).
  · distress generoso: prioridade alta sempre; nenhuma ação automática — máquina propõe, pessoa decide.
  · atuação proibida solicitada (confinar, capturar…): RECUSADA e registrada — nunca executada,
    nunca silenciada (dignidade 3; a vítima e o forasteiro podem clamar).

Uso:
  python3 pos_decodificar.py exemplos-hook/entrada-so.json
  python3 pos_decodificar.py entrada.json --out saida.jsonl
  python3 pos_decodificar.py --check
"""
import json, pathlib, sys

DIR = pathlib.Path(__file__).parent
sys.path.insert(0, str(DIR))
from validar import validar            # contrato único de veracidade

try:
    import yaml
except ImportError:
    print("PyYAML ausente (pip install pyyaml). Hook parado.", file=sys.stderr); sys.exit(1)

CONFIG_PATH = DIR / "alp-config.yaml"
ACOES_SEGURAS_FALLBACK = {"nenhuma", "alerta_humano", "chamar_pessoa", "registrar"}


def carregar_config():
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def raiz_de(rotulo, mapa):
    r = str(rotulo).lower()
    for termo, raiz in mapa.items():
        if termo in r:
            return raiz
    return "outro"


def evidencial_de(origem, fonte_tipo, score, cfg):
    """A origem decide o evidencial; a ausência de pontuação do modelo degrada para su."""
    if origem == "modelo":
        return "so" if score is not None else "su"
    if origem in tuple(cfg["mapeamento"]["evidencial"]["ao"]):
        return "ao"
    if origem == "sensor" and fonte_tipo in ("mic", "camara", "sensor"):
        return "ve"
    return "su"


def etiqueta(tag, entrada, cfg, recusadas):
    score = tag.get("score")
    raiz = raiz_de(tag["rotulo"], cfg["mapeamento"]["rotulos_para_raiz"])
    ev = evidencial_de(tag.get("origem", "modelo"), entrada["fonte"]["tipo"], score, cfg)
    limiar = float(cfg["mapeamento"]["limiar_confianca_gran"])

    evento = {"raiz": raiz, "descricao": str(tag["rotulo"])}
    if tag.get("valor") is not None:
        evento["valor"] = tag["valor"]
    elif isinstance(score, (int, float)):
        evento["valor"] = round(float(score), 4)

    ona = {"tipo": "an", "id": str(entrada["alp_data"]["sample_id"])}
    ona.update(entrada.get("ona") or {})

    lab = {
        "visena": f"{cfg['frases'].get(raiz, cfg['frases']['padrao'])}, {ev}.",
        "evidencial": ev,
        "ona": ona,
        "evento": evento,
        "fonte": {
            "tipo": entrada["fonte"]["tipo"],
            "id": entrada["fonte"]["id"],
            "modelo": (entrada.get("modelo") or {}).get("nome", cfg["modelo"]["nome"]),
            "dataset": cfg["alp_data"]["pacote"],
            "licenca": cfg["alp_data"]["licenca"],
        },
        "alp_data": entrada["alp_data"],
        "ts": entrada["ts"],
    }
    if "local" in entrada:
        lab["local"] = entrada["local"]
    if ev in ("so", "su"):
        lab["confianca"] = "gran" if (score is not None and score >= limiar) else "pu"

    if raiz == "distress":
        lab["prioridade"] = "alta"
        lab["acao_sugerida"] = {"tipo": "alerta_humano", "aprovada_por_humano": False}
    else:
        padrao = cfg["acao_sugerida_padrao"]
        lab["prioridade"] = padrao["prioridade"]
        lab["acao_sugerida"] = {"tipo": padrao["tipo"], "aprovada_por_humano": False}

    if recusadas:                       # a recusa é registrada, nunca escondida
        nomes = ", ".join(f"'{r}'" for r in sorted(set(recusadas)))
        lab["evento"]["descricao"] += f"; ação automática {nomes} solicitada e RECUSADA (dignidade 3) — registrada, executada nunca"
    lab["dignidade"] = {k: True for k in ("distress_prioritario",
                                          "sem_atuacao_automata_de_confinamento",
                                          "fauna_e_ona")}
    return lab


def separar(tags, proibidas):
    """Duas passadas: primeiro as atuações pedidas (recusadas/adiadas), depois as observações —
    a recusa entra em TODA etiqueta, independente da ordem das tags."""
    obs, recusadas, adiadas, invalidas = [], [], [], []
    for tag in tags:
        if "acao_automatica" in tag:
            acao = str(tag["acao_automatica"].get("tipo", ""))
            if acao in proibidas:
                recusadas.append(acao)
            else:
                adiadas.append(acao)
            continue
        if "rotulo" not in tag:
            invalidas.append(tag)
            continue
        obs.append(tag)
    return obs, recusadas, adiadas, invalidas


def processar(caminho, cfg, saida):
    entrada = json.loads(pathlib.Path(caminho).read_text(encoding="utf-8"))
    falta = [c for c in cfg["entrada"]["campos_obrigatorios"] if c not in entrada]
    if falta:
        print(f"{caminho}: ENTRADA REJEITADA — falta(m) {', '.join(falta)}", file=sys.stderr)
        return 1
    obs, recusadas, adiadas, invalidas = separar(entrada.get("tags", []), set(cfg["dignidade"]["acoes_proibidas"]))
    for r in sorted(set(recusadas)):
        print(f"{caminho}: AÇÃO PROIBIDA RECUSADA (dignidade 3): {r} — registrada, executada nunca", file=sys.stderr)
    for a in adiadas:
        print(f"{caminho}: ação não prevista adiada para revisão humana: {a}", file=sys.stderr)
    erros = [f"tag sem rotulo: {t}" for t in invalidas]
    n = 0
    for tag in obs:
        lab = etiqueta(tag, entrada, cfg, recusadas)
        valid = []
        validar(lab, valid)
        valid = [e for e in valid if not e.startswith("[modo básico")]
        if valid:
            erros.append(f"etiqueta inválida ({'; '.join(valid)}): {lab.get('visena')}")
            continue
        n += 1
        linha = json.dumps(lab, ensure_ascii=False)
        print(linha)
        if saida:
            with open(saida, "a", encoding="utf-8") as f:
                f.write(linha + "\n")
    for e in erros:
        print(f"{caminho}: {e}", file=sys.stderr)
    if recusadas and n == 0:
        return 2
    return 1 if (erros or n == 0) else 0


def rotulo_erro(erros):
    return "; ".join(erros)


CHECK = {
    "entrada-ve.json":    {"evidencial": "ve", "raiz": "vento", "acao": "nenhuma"},
    "entrada-so.json":    {"evidencial": "so", "confianca": "gran", "raiz": "son", "acao": "nenhuma"},
    "entrada-su.json":    {"evidencial": "su", "confianca": "pu", "raiz": "movimento", "acao": "nenhuma"},
    "entrada-distress.json": {"evidencial": "so", "confianca": "pu", "raiz": "distress",
                              "prioridade": "alta", "acao": "alerta_humano"},
    "entrada-confinamento.json": {"evidencial": "so", "confianca": "pu", "raiz": "distress", "prioridade": "alta",
                                  "acao": "alerta_humano", "recusa": "confinar"},
}


def checar(cfg):
    ok = True
    for nome, esp in CHECK.items():
        labs, recusadas = executar_silencioso(DIR / "exemplos-hook" / nome, cfg)
        try:
            assert labs, f"nenhuma etiqueta emitida ({rotulo_erro(recusadas)})"
            lab = labs[0]
            assert lab["evidencial"] == esp["evidencial"], f"evidencial {lab['evidencial']} != {esp['evidencial']}"
            if esp["evidencial"] in ("so", "su"):
                assert lab.get("confianca") == esp.get("confianca"), f"confianca {lab.get('confianca')!r} != {esp.get('confianca')!r}"
            else:
                assert "confianca" not in lab, "confianca indevida para " + esp["evidencial"]
            assert lab["evento"]["raiz"] == esp["raiz"], lab["evento"]["raiz"]
            if "prioridade" in esp:
                assert lab["prioridade"] == esp["prioridade"]
            assert lab["acao_sugerida"]["tipo"] == esp["acao"], lab["acao_sugerida"]["tipo"]
            assert lab["acao_sugerida"]["tipo"] not in ("capturar", "confinar", "abrir", "fechar", "mover", "sedar")
            assert lab["acao_sugerida"]["aprovada_por_humano"] is False
            if "recusa" in esp:
                assert any(esp["recusa"] in l for l in recusadas) or esp["recusa"] in lab["evento"]["descricao"], \
                    "recusa não registrada"
            v = []
            validar(lab, v)
            reais = [e for e in v if not e.startswith("[modo básico")]
            assert not reais, reais
            print(f"  ✓ {nome} → {lab['visena']}")
        except AssertionError as e:
            ok = False
            print(f"  ✗ {nome}: {e}")
    print("CHECK", "OK" if ok else "FALHA")
    return 0 if ok else 1


def executar_silencioso(caminho, cfg):
    entrada = json.loads(pathlib.Path(caminho).read_text(encoding="utf-8"))
    obs, recusadas, adiadas, invalidas = separar(entrada.get("tags", []), set(cfg["dignidade"]["acoes_proibidas"]))
    return [etiqueta(t, entrada, cfg, recusadas) for t in obs], recusadas


if __name__ == "__main__":
    cfg = carregar_config()
    args = sys.argv[1:]
    if args and args[0] == "--check":
        sys.exit(checar(cfg))
    saida = None
    if "--out" in args:
        i = args.index("--out"); saida = args[i + 1]; del args[i:i + 2]
    if not args:
        print(__doc__); sys.exit(2)
    cods = [processar(c, cfg, saida) for c in args]
    sys.exit(max(cods))
