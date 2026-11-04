#!/usr/bin/env python3
"""
m33_endpoints.py - Coleta da métrica M3.3 (Taxa de Proteção de Endpoints Sensíveis, TPE).

Percorre os controllers de um clone do decidim-govbr e lista, para cada ação pública,
se ela é sensível e se há verificação de permissão explícita.

Uso:
    python3 scripts/m33_endpoints.py CAMINHO_DO_DECIDIM_GOVBR SAIDA.csv

Regras (as mesmas descritas na Fase 3):
- Ação = método público (def) de uma classe em app/controllers/, antes de private/protected.
- Ação sensível = qualquer ação de controller no namespace admin/, ou ação de escrita
  (create, update, destroy, new, edit e nomes que alteram estado, listados em ESCRITA)
  em qualquer controller.
- Ação protegida = o corpo da ação chama enforce_permission_to ou allowed_to?, ou a
  classe declara before_action que chama um desses métodos ou um método de permissão.
- Proteção herdada da classe pai não é detectada pelo script: essas linhas saem como
  "verificar" e são conferidas à mão, com o resultado anotado no CSV.
"""
import csv
import re
import sys
from pathlib import Path

ESCRITA = {
    "create", "update", "destroy", "new", "edit",
    "publish", "unpublish", "withdraw", "approve", "reject", "hide", "unhide",
    "block", "unblock", "import", "export", "duplicate", "accept", "answer",
}
CHECAGEM = re.compile(r"enforce_permission_to|allowed_to\?")
BEFORE = re.compile(r"^\s*before_action\s+(.+)$")
DEF = re.compile(r"^\s*def\s+([a-z_][a-zA-Z0-9_!?]*)")
PRIVADO = re.compile(r"^\s*(private|protected)\s*$")
CLASSE = re.compile(r"^\s*class\s+([\w:]+)(\s*<\s*([\w:]+))?")


def analisar(arquivo: Path, raiz: Path):
    linhas = arquivo.read_text(encoding="utf-8", errors="replace").splitlines()
    rel = arquivo.relative_to(raiz).as_posix()
    admin = "/admin/" in rel
    classe, pai = "", ""
    before_protege = False
    acoes = []  # (nome, linha, corpo)
    atual = None
    privado = False
    for i, l in enumerate(linhas, 1):
        m = CLASSE.match(l)
        if m and not classe:
            classe, pai = m.group(1), (m.group(3) or "")
        b = BEFORE.match(l)
        if b and (CHECAGEM.search(b.group(1)) or "permission" in b.group(1)):
            before_protege = True
        if PRIVADO.match(l):
            privado = True
            atual = None
            continue
        d = DEF.match(l)
        if d:
            if privado:
                atual = None
                continue
            atual = [d.group(1), i, []]
            acoes.append(atual)
            continue
        if atual is not None:
            atual[2].append(l)
    saida = []
    for nome, linha, corpo in acoes:
        sensivel = admin or nome in ESCRITA
        if not sensivel:
            continue
        if CHECAGEM.search("\n".join(corpo)):
            status = "protegida (no corpo da ação)"
        elif before_protege:
            status = "protegida (before_action da classe)"
        else:
            status = "verificar"
        saida.append({
            "arquivo": rel, "linha": linha, "classe": classe, "classe_pai": pai,
            "acao": nome, "namespace_admin": "sim" if admin else "não",
            "status": status, "conferencia_manual": "",
        })
    return saida


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    raiz = Path(sys.argv[1]).resolve()
    destino = Path(sys.argv[2])
    linhas = []
    for arq in sorted((raiz / "app" / "controllers").rglob("*.rb")):
        linhas.extend(analisar(arq, raiz))
    destino.parent.mkdir(parents=True, exist_ok=True)
    campos = ["arquivo", "linha", "classe", "classe_pai", "acao", "namespace_admin",
              "status", "conferencia_manual"]
    with destino.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(linhas)
    total = len(linhas)
    prot = sum(1 for l in linhas if l["status"].startswith("protegida"))
    verif = total - prot
    print(f"Ações sensíveis encontradas: {total}")
    print(f"Protegidas pelo script: {prot}")
    print(f"A verificar à mão: {verif}")


if __name__ == "__main__":
    main()
