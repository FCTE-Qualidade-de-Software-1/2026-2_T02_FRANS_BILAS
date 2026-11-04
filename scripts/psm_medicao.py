#!/usr/bin/env python3
"""
psm_medicao.py - Medição de um sprint pelos indicadores N1 a N6 da Gestão (PSM/CID).

Lê o GitHub Projects 33, os PRs e o histórico da main e grava um retrato dos dados
brutos e dos indicadores em JSON. Os construtos de cada indicador estão na seção 4 de
documentation/content/gestao.md.

Uso (precisa do gh autenticado com acesso de leitura ao Projects da organização):

    python3 scripts/psm_medicao.py --sprint "Sprint 3" --inicio 2026-10-27 --fim 2026-11-04 \
        --comprometidas 59,60,69,70,67,68,44,43,62,66,65,90,45,63,89,64,46 \
        --saida documentation/content/dados/gestao/sprint-3.json
"""

import argparse
import importlib.util
import json
import subprocess
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OWNER = "FCTE-Qualidade-de-Software-1"
REPO = "2026-2_T02_FRANS_BILAS"
PROJECT_NUMBER = 33
BRT = timezone(timedelta(hours=-3))


def carregar_integrantes():
    """Reaproveita a lista de integrantes e duplas do painel automático."""
    caminho = REPO_ROOT / ".github" / "scripts" / "update_metrics.py"
    spec = importlib.util.spec_from_file_location("update_metrics", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return {m["handle"]: m for m in modulo.TEAM_MEMBERS}


def graphql(query, **variaveis):
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    for nome, valor in variaveis.items():
        cmd += ["-F", f"{nome}={valor}"]
    saida = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return json.loads(saida)["data"]


ITENS = """
query($cursor: String) {
  organization(login: "%s") {
    projectV2(number: %d) {
      items(first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          content {
            ... on Issue {
              number title state createdAt closedAt
              milestone { title }
              assignees(first: 10) { nodes { login } }
              timelineItems(itemTypes: [CLOSED_EVENT], last: 1) {
                nodes { ... on ClosedEvent { closer { ... on PullRequest { number } } } }
              }
            }
          }
          fieldValues(first: 30) {
            nodes {
              ... on ProjectV2ItemFieldNumberValue { number field { ... on ProjectV2FieldCommon { name } } }
              ... on ProjectV2ItemFieldDateValue { date field { ... on ProjectV2FieldCommon { name } } }
              ... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2FieldCommon { name } } }
              ... on ProjectV2ItemFieldIterationValue { title field { ... on ProjectV2FieldCommon { name } } }
            }
          }
        }
      }
    }
  }
}
""" % (OWNER, PROJECT_NUMBER)

PRS = """
query($cursor: String) {
  repository(owner: "%s", name: "%s") {
    pullRequests(first: 100, after: $cursor, states: MERGED) {
      pageInfo { hasNextPage endCursor }
      nodes {
        number mergedAt author { login }
        mergeCommit { oid }
        reviews(first: 20) { nodes { author { login } state } }
      }
    }
  }
}
""" % (OWNER, REPO)


def paginar(query, caminho):
    cursor, nos = None, []
    while True:
        dados = graphql(query, **({"cursor": cursor} if cursor else {}))
        bloco = dados
        for chave in caminho:
            bloco = bloco[chave]
        nos += bloco["nodes"]
        if not bloco["pageInfo"]["hasNextPage"]:
            return nos
        cursor = bloco["pageInfo"]["endCursor"]


def ler_issues():
    issues = {}
    for no in paginar(ITENS, ["organization", "projectV2", "items"]):
        c = no.get("content") or {}
        if "number" not in c:
            continue
        campos = {}
        for fv in no["fieldValues"]["nodes"]:
            if not fv:
                continue
            nome = fv["field"]["name"]
            campos[nome] = fv.get("number", fv.get("date", fv.get("name", fv.get("title"))))
        fechada_por = None
        eventos = c["timelineItems"]["nodes"]
        if eventos and eventos[0].get("closer"):
            fechada_por = eventos[0]["closer"].get("number")
        issues[c["number"]] = {
            "numero": c["number"],
            "titulo": c["title"],
            "estado": c["state"],
            "criada_em": c["createdAt"],
            "fechada_em": c["closedAt"],
            "milestone": (c.get("milestone") or {}).get("title"),
            "responsaveis": [a["login"] for a in c["assignees"]["nodes"]],
            "fechada_pelo_pr": fechada_por,
            "sprint": campos.get("Sprint"),
            "status": campos.get("Status"),
            "esforco_estimado_h": campos.get("Esforço estimado (h)"),
            "esforco_real_h": campos.get("Esforço real (h)"),
            "inicio": campos.get("Início"),
            "conclusao": campos.get("Conclusão"),
        }
    return issues


def ler_prs(integrantes):
    prs = {}
    for pr in paginar(PRS, ["repository", "pullRequests"]):
        autor = (pr.get("author") or {}).get("login")
        dupla_autor = integrantes.get(autor, {}).get("dupla")
        revisores = [
            {"login": r["author"]["login"], "estado": r["state"],
             "dupla": integrantes.get(r["author"]["login"], {}).get("dupla")}
            for r in pr["reviews"]["nodes"] if r.get("author")
        ]
        outra_dupla = any(r["dupla"] and r["dupla"] != dupla_autor for r in revisores)
        prs[pr["number"]] = {
            "numero": pr["number"],
            "autor": autor,
            "dupla_autor": dupla_autor,
            "mesclado_em": pr["mergedAt"],
            "commit": (pr.get("mergeCommit") or {}).get("oid"),
            "revisoes": revisores,
            "revisado_por_outra_dupla": outra_dupla,
        }
    return prs


def ler_integracoes(inicio, fim):
    """Commits que entraram na main (primeiro pai) no período, sem os do bot do painel."""
    formato = "%H%x1f%aI%x1f%an%x1f%s"
    saida = subprocess.run(
        ["git", "log", "origin/main", "--first-parent", f"--format={formato}"],
        capture_output=True, text=True, check=True, cwd=REPO_ROOT,
    ).stdout
    integracoes = []
    for linha in saida.splitlines():
        sha, quando, autor, assunto = linha.split("\x1f")
        dia = datetime.fromisoformat(quando).astimezone(BRT).date()
        if not (inicio <= dia <= fim) or autor == "github-actions[bot]":
            continue
        integracoes.append({"commit": sha, "data": dia.isoformat(), "autor": autor, "assunto": assunto})
    return integracoes


def pct(parte, total):
    return round(100 * parte / total, 1) if total else None


def medir(args):
    integrantes = carregar_integrantes()
    inicio = date.fromisoformat(args.inicio)
    fim = date.fromisoformat(args.fim)
    issues = ler_issues()
    prs = ler_prs(integrantes)
    pr_por_commit = {p["commit"]: p for p in prs.values() if p["commit"]}

    # N1: comprometido x concluído. Pronto = fechada por PR revisado por outra dupla (Gestão, 4.4).
    comprometidas = [issues[n] for n in args.comprometidas if n in issues]
    fechadas = [i for i in comprometidas if i["estado"] == "CLOSED"]
    prontas = [i for i in fechadas
               if i["fechada_pelo_pr"] and prs.get(i["fechada_pelo_pr"], {}).get("revisado_por_outra_dupla")]
    n1 = {
        "comprometidas": len(comprometidas),
        "fechadas": len(fechadas),
        "prontas": len(prontas),
        "pct_concluido": pct(len(prontas), len(comprometidas)),
        "pct_fechado": pct(len(fechadas), len(comprometidas)),
        "itens_prontos": [i["numero"] for i in prontas],
        "itens_fechados": [i["numero"] for i in fechadas],
    }
    n1["desvio"] = round(100 - n1["pct_concluido"], 1) if n1["pct_concluido"] is not None else None

    # N2: burndown do milestone E2 (itens abertos ao fim de cada dia do sprint).
    e2 = [i for i in issues.values() if i["milestone"] == "E2"]
    burndown = []
    dia = inicio
    while dia <= fim:
        def ate(ts):
            return ts and datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(BRT).date() <= dia
        planejados = [i for i in e2 if ate(i["criada_em"])]
        concluidos = [i for i in planejados if ate(i["fechada_em"])]
        burndown.append({"dia": dia.isoformat(), "planejados": len(planejados),
                         "concluidos": len(concluidos), "abertos": len(planejados) - len(concluidos)})
        dia += timedelta(days=1)

    # N3 e N4: dependem do campo "Esforço real (h)".
    com_real = [i for i in comprometidas if i["esforco_real_h"] is not None]
    n3 = {"issues_com_esforco_real": len(com_real), "issues_comprometidas": len(comprometidas),
          "horas_reais_por_pessoa": {}}
    for i in com_real:
        for r in i["responsaveis"]:
            n3["horas_reais_por_pessoa"][r] = n3["horas_reais_por_pessoa"].get(r, 0) + i["esforco_real_h"]
    est = sum(i["esforco_estimado_h"] or 0 for i in com_real)
    real = sum(i["esforco_real_h"] for i in com_real)
    n4 = {"issues_com_esforco_real": len(com_real), "estimado_h": est, "real_h": real,
          "precisao_pct": pct(real, est)}

    # N5: depende dos campos "Início" e "Conclusão".
    com_datas = [i for i in fechadas if i["inicio"] and i["conclusao"]]
    tempos = [(date.fromisoformat(i["conclusao"]) - date.fromisoformat(i["inicio"])).days + 1 for i in com_datas]
    n5 = {"fechadas": len(fechadas), "com_inicio_e_conclusao": len(com_datas),
          "tempo_medio_dias": round(sum(tempos) / len(tempos), 1) if tempos else None}

    # N6: revisão por pares nas integrações da main.
    integracoes = ler_integracoes(inicio, fim)
    revisadas = []
    for it in integracoes:
        pr = pr_por_commit.get(it["commit"])
        it["pr"] = pr["numero"] if pr else None
        it["revisado_por_outra_dupla"] = bool(pr and pr["revisado_por_outra_dupla"])
        if it["revisado_por_outra_dupla"]:
            revisadas.append(it)
    n6 = {"integracoes": len(integracoes), "por_pr": sum(1 for i in integracoes if i["pr"]),
          "revisadas_por_outra_dupla": len(revisadas), "pct_revisado": pct(len(revisadas), len(integracoes))}

    return {
        "sprint": args.sprint,
        "periodo": {"inicio": args.inicio, "fim": args.fim},
        "medido_em": datetime.now(BRT).isoformat(timespec="minutes"),
        "indicadores": {"N1": n1, "N2": burndown, "N3": n3, "N4": n4, "N5": n5, "N6": n6},
        "dados_brutos": {
            "issues_comprometidas": comprometidas,
            "integracoes_main": integracoes,
            "prs": [p for p in prs.values() if p["commit"] in {i["commit"] for i in integracoes}],
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--sprint", required=True)
    parser.add_argument("--inicio", required=True, help="AAAA-MM-DD")
    parser.add_argument("--fim", required=True, help="AAAA-MM-DD")
    parser.add_argument("--comprometidas", required=True,
                        type=lambda s: [int(x) for x in s.split(",")],
                        help="issues comprometidas na planning, separadas por vírgula")
    parser.add_argument("--saida", required=True)
    args = parser.parse_args()

    resultado = medir(args)
    destino = REPO_ROOT / args.saida
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(resultado, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(resultado["indicadores"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
