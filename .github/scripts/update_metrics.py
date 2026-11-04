#!/usr/bin/env python3
"""
update_metrics.py

Extracts Git commit activity, GitHub issue workload, and effort metrics (estimated and real hours)
from GitHub Projects 33 to generate automated Mermaid charts and Markdown tables under documentation/snippets/management/.
Follows project anti-meat-proxy and humanizer guidelines.
"""

import json
import os
import re
import subprocess
import sys
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SNIPPETS_DIR = REPO_ROOT / "documentation" / "snippets" / "management"

PROJECT_ID = "PVT_kwDODIobq84BoE3c"
REPO_OWNER = "FCTE-Qualidade-de-Software-1"
REPO_NAME = "2026-2_T02_FRANS_BILAS"

TEAM_MEMBERS = [
    {
        "name": "João Victor da Silva Batista de Farias",
        "handle": "BeyondMagic",
        "dupla": "Dupla 1",
    },
    {
        "name": "Mateus Vinícius Vieira",
        "handle": "matix0",
        "dupla": "Dupla 1",
    },
    {
        "name": "José Vinícius Alvares Soares de Queiroz",
        "handle": "JoseViniciusQueiroz",
        "dupla": "Dupla 2",
    },
    {
        "name": "Lucca Medeiros Silva",
        "handle": "luccameds",
        "dupla": "Dupla 2",
    },
    {
        "name": "Miguel Arthur Oliveira de Lima",
        "handle": "zlimaz",
        "dupla": "Dupla 3",
    },
    {
        "name": "Davi Mesquita Sousa",
        "handle": "davimesquit",
        "dupla": "Dupla 3",
    },
]

TRACKED_AUTHORS = [m["handle"] for m in TEAM_MEMBERS]
MEMBER_BY_HANDLE = {m["handle"]: m for m in TEAM_MEMBERS}

COLOR_PALETTE = "#2563eb, #7c3aed, #db2777, #ea580c, #16a34a, #0891b2"
MERMAID_INIT = f'%%{{init: {{"themeVariables": {{"xyChart": {{"plotColorPalette": "{COLOR_PALETTE}"}}}}}}}}%%\n'


def normalize_author(name: str, email: str) -> str:
    """Normalize git author signature to recognized team GitHub handles."""
    combined = f"{name} {email}".lower()
    if "github-actions" in combined or "actions@github.com" in combined:
        return "github-actions[bot]"
    if "beyondmagic" in combined or "koetemagie" in combined or "joão" in combined or "joao" in combined:
        return "BeyondMagic"
    if "mateus" in combined or "matix0" in combined or "mateusviniciuspw" in combined:
        return "matix0"
    if "josevinicius" in combined or "viniciusa.s.queiroz" in combined or "jose_viniciusq" in combined or ("vinicius" in combined and "queiroz" in combined):
        return "JoseViniciusQueiroz"
    if "lucca" in combined or "luccameds" in combined:
        return "luccameds"
    if "miguel" in combined or "zlimaz" in combined or "miguell1040z" in combined:
        return "zlimaz"
    if "davimesquit" in combined or "davimesquita" in combined or "davi" in combined:
        return "davimesquit"
    return name.strip() or "Unknown"


def get_git_log_data():
    """Extract commit timestamps, normalized authors, additions, and deletions."""
    cmd = [
        "git",
        "log",
        "--numstat",
        "--date=iso-strict",
        "--format=COMMIT|%ad|%an|%ae",
    ]
    result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
    lines = result.stdout.splitlines()

    commits_by_week = defaultdict(lambda: defaultdict(int))
    additions_by_week = defaultdict(lambda: defaultdict(int))
    deletions_by_week = defaultdict(lambda: defaultdict(int))
    total_commits = defaultdict(int)
    total_additions = defaultdict(int)
    total_deletions = defaultdict(int)
    all_weeks = set()

    current_week = None
    current_author = None

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("COMMIT|"):
            parts = line.split("|")
            date_str = parts[1]
            author_name = parts[2]
            author_email = parts[3] if len(parts) > 3 else ""

            dt = datetime.fromisoformat(date_str)
            iso_year, iso_week, _ = dt.isocalendar()
            week_key = f"{iso_year}-W{iso_week:02d}"

            current_week = week_key
            current_author = normalize_author(author_name, author_email)
            all_weeks.add(week_key)

            commits_by_week[week_key][current_author] += 1
            total_commits[current_author] += 1
        else:
            # numstat line: <added> <deleted> <filename>
            parts = line.split("\t")
            if len(parts) >= 3 and current_week and current_author:
                added = int(parts[0]) if parts[0].isdigit() else 0
                deleted = int(parts[1]) if parts[1].isdigit() else 0
                additions_by_week[current_week][current_author] += added
                deletions_by_week[current_week][current_author] += deleted
                total_additions[current_author] += added
                total_deletions[current_author] += deleted

    if not all_weeks:
        now_year, now_week, _ = datetime.now().isocalendar()
        all_weeks.add(f"{now_year}-W{now_week:02d}")

    # Generate sequential weekly buckets from earliest to latest
    sorted_weeks = sorted(all_weeks)
    earliest_yr, earliest_wk = [int(x) for x in sorted_weeks[0].split("-W")]
    latest_yr, latest_wk = [int(x) for x in sorted_weeks[-1].split("-W")]

    from datetime import date
    earliest_date = date.fromisocalendar(earliest_yr, earliest_wk, 1)
    latest_date = date.fromisocalendar(latest_yr, latest_wk, 1)

    full_weeks = []
    curr = earliest_date
    while curr <= latest_date or len(full_weeks) < 3:
        yr, wk, _ = curr.isocalendar()
        wk_str = f"{yr}-W{wk:02d}"
        if wk_str not in full_weeks:
            full_weeks.append(wk_str)
        curr += timedelta(days=7)

    totals = {
        "commits": total_commits,
        "additions": total_additions,
        "deletions": total_deletions,
    }

    return full_weeks, commits_by_week, additions_by_week, deletions_by_week, totals


def resolve_token(*env_names):
    """Token do GitHub: variáveis de ambiente, depois o gh CLI local, depois a config local do MCP."""
    for name in env_names:
        if os.environ.get(name):
            return os.environ[name]
    try:
        token = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
        if token:
            return token
    except Exception:
        pass
    try:
        mcp_file = Path.home() / ".gemini" / "config" / "mcp_config.json"
        if mcp_file.exists():
            cfg = json.loads(mcp_file.read_text())
            return cfg.get("mcpServers", {}).get("github", {}).get("env", {}).get("GITHUB_PERSONAL_ACCESS_TOKEN")
    except Exception:
        pass
    return None


def graphql_paginate(query: str, path: list, token: str) -> list:
    """Executa uma consulta GraphQL paginada e devolve todos os nós. Falha com exceção."""
    headers = {"Content-Type": "application/json", "User-Agent": "MetricsScript"}
    if token:
        headers["Authorization"] = f"bearer {token}"
    nodes, cursor = [], None
    while True:
        req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=json.dumps({"query": query, "variables": {"cursor": cursor}}).encode("utf-8"),
            headers=headers,
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        if data.get("errors"):
            raise RuntimeError(data["errors"][0].get("message"))
        block = data.get("data")
        for key in path:
            block = (block or {}).get(key)
        if block is None:
            raise RuntimeError(f"resposta sem {'.'.join(path)} (token sem acesso?)")
        nodes += block["nodes"]
        if not block["pageInfo"]["hasNextPage"]:
            return nodes
        cursor = block["pageInfo"]["endCursor"]


ISSUES_QUERY = """
query($cursor: String) {
  repository(owner: "%s", name: "%s") {
    issues(first: 100, after: $cursor) {
      pageInfo { hasNextPage endCursor }
      nodes { number state assignees(first: 10) { nodes { login } } }
    }
  }
}
""" % (REPO_OWNER, REPO_NAME)

PROJECT_QUERY = """
query($cursor: String) {
  node(id: "%s") {
    ... on ProjectV2 {
      items(first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          content { ... on Issue { number } }
          fieldValues(first: 30) {
            nodes {
              ... on ProjectV2ItemFieldNumberValue {
                number
                field { ... on ProjectV2FieldCommon { name } }
              }
            }
          }
        }
      }
    }
  }
}
""" % PROJECT_ID


def get_project_and_issue_metrics():
    """Conta issues por integrante pelo repositório e soma as horas do GitHub Projects 33.

    As contagens vêm das issues do repositório, que o token do GitHub Actions consegue ler.
    As horas vêm do Projects, que exige um token com acesso à organização (PROJECTS_TOKEN).
    Sem esse acesso, as horas ficam como None e as tabelas mostram "sem acesso". Não há
    valores de reserva: se as issues não puderem ser lidas, o script falha e nada é gravado.
    """
    issues = graphql_paginate(ISSUES_QUERY, ["repository", "issues"], resolve_token("GITHUB_TOKEN", "GH_TOKEN"))

    hours = {}
    try:
        items = graphql_paginate(PROJECT_QUERY, ["node", "items"], resolve_token("PROJECTS_TOKEN", "GITHUB_TOKEN", "GH_TOKEN"))
        for it in items:
            number = (it.get("content") or {}).get("number")
            if number is None:
                continue
            fields = {}
            for fv in it["fieldValues"]["nodes"]:
                if fv and fv.get("field"):
                    fields[fv["field"]["name"]] = fv.get("number")
            hours[number] = (fields.get("Esforço estimado (h)"), fields.get("Esforço real (h)"))
    except Exception as e:
        print(f"Projects 33 sem acesso; horas não serão exibidas: {e}", file=sys.stderr)
        hours = None

    counts = {
        author: {
            "total": 0, "closed": 0, "open": 0,
            "est_closed": 0.0, "real_closed": 0.0, "est_all": 0.0, "real_all": 0.0,
        }
        for author in TRACKED_AUTHORS
    }
    for issue in issues:
        assignees = [a["login"] for a in issue["assignees"]["nodes"]]
        closed = issue["state"] == "CLOSED"
        est, real = (hours or {}).get(issue["number"], (None, None))
        weight = 1.0 / len(assignees) if assignees else 1.0
        for a in assignees:
            handle = normalize_author(a, "")
            if handle not in counts:
                continue
            c = counts[handle]
            c["total"] += 1
            c["closed" if closed else "open"] += 1
            if est is not None:
                c["est_all"] += est * weight
                if closed:
                    c["est_closed"] += est * weight
            if real is not None:
                c["real_all"] += real * weight
                if closed:
                    c["real_closed"] += real * weight

    if hours is None:
        for c in counts.values():
            for key in ("est_closed", "real_closed", "est_all", "real_all"):
                c[key] = None
    return counts


def format_hours(value) -> str:
    return "sem acesso" if value is None else f"{value:.1f}h".replace(".", ",")

def calculate_upper_bound(values, min_bound=10):
    """Compute clean y-axis ceiling rounded to a readable multiple."""
    max_val = max(values) if values else 0
    if max_val <= 0:
        return min_bound
    if max_val <= 10:
        return 10
    if max_val <= 50:
        return ((max_val // 10) + 1) * 10
    if max_val <= 500:
        return ((max_val // 50) + 1) * 50
    return ((max_val // 200) + 1) * 200


def render_timeline_chart(title: str, y_label: str, weeks: list, series_by_author: dict) -> str:
    """Format Mermaid xychart-beta for timeline metrics."""
    x_labels = [f'"{w}"' for w in weeks]
    x_axis_str = f'[{", ".join(x_labels)}]'

    all_vals = []
    lines = []
    for author in TRACKED_AUTHORS:
        vals = [series_by_author.get(w, {}).get(author, 0) for w in weeks]
        all_vals.extend(vals)
        lines.append(f"    line [{', '.join(str(v) for v in vals)}]")

    max_bound = calculate_upper_bound(all_vals)

    chart = (
        MERMAID_INIT +
        f'xychart-beta\n'
        f'    title "{title}"\n'
        f'    x-axis {x_axis_str}\n'
        f'    y-axis "{y_label}" 0 --> {max_bound}\n'
        + "\n".join(lines)
    )
    return chart


def render_bar_chart(title: str, y_label: str, counts_by_author: dict, key: str = "total") -> str:
    """Format Mermaid xychart-beta with dedicated series per contributor for distinct colors."""
    x_labels = [f'"{author}"' for author in TRACKED_AUTHORS]
    vals = [counts_by_author.get(author, {}).get(key, 0) for author in TRACKED_AUTHORS]
    max_bound = calculate_upper_bound(vals, min_bound=5)

    bar_lines = []
    for i, author in enumerate(TRACKED_AUTHORS):
        author_val = counts_by_author.get(author, {}).get(key, 0)
        slot_vals = [author_val if j == i else 0 for j in range(len(TRACKED_AUTHORS))]
        bar_lines.append(f'    bar [{", ".join(str(v) for v in slot_vals)}]')

    chart = (
        MERMAID_INIT +
        f'xychart-beta\n'
        f'    title "{title}"\n'
        f'    x-axis [{", ".join(x_labels)}]\n'
        f'    y-axis "{y_label}" 0 --> {max_bound}\n'
        + "\n".join(bar_lines)
    )
    return chart


def generate_contributions_table(git_totals: dict, issue_counts: dict) -> str:
    """Generate Markdown table consolidating git commits, lines altered and assigned issues."""
    lines = [
        "| Integrante | Usuário GitHub | Dupla | Commits | Linhas (+/-) | Issues Fechadas | Horas Est. (h) | Horas Reais (h) |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    tot_commits = 0
    tot_adds = 0
    tot_dels = 0
    tot_closed = 0
    tot_est = 0.0
    tot_real = 0.0

    for m in TEAM_MEMBERS:
        handle = m["handle"]
        name = m["name"]
        dupla = m["dupla"]

        c = git_totals["commits"].get(handle, 0)
        a = git_totals["additions"].get(handle, 0)
        d = git_totals["deletions"].get(handle, 0)
        net = a - d

        st = issue_counts.get(handle, {})
        closed_iss = st.get("closed", 0)
        est = st.get("est_closed")
        real = st.get("real_closed")

        tot_commits += c
        tot_adds += a
        tot_dels += d
        tot_closed += closed_iss
        tot_est = None if est is None or tot_est is None else tot_est + est
        tot_real = None if real is None or tot_real is None else tot_real + real

        est_str = format_hours(est)
        real_str = format_hours(real)
        sign_net = f"+{net}" if net > 0 else str(net)
        lines.append(
            f"| **{name}** | [{handle}](https://github.com/{handle}) | {dupla} | {c} | +{a} / -{d} ({sign_net}) | {closed_iss} | {est_str} | {real_str} |"
        )

    tot_net = tot_adds - tot_dels
    tot_sign_net = f"+{tot_net}" if tot_net > 0 else str(tot_net)
    tot_est_str = format_hours(tot_est)
    tot_real_str = format_hours(tot_real)
    lines.append(
        f"| **Total Consolidado** | - | - | **{tot_commits}** | **+{tot_adds} / -{tot_dels} ({tot_sign_net})** | **{tot_closed}** | **{tot_est_str}** | **{tot_real_str}** |"
    )

    return "\n".join(lines)


def generate_issues_table(issue_counts: dict) -> str:
    """Generate Markdown table detailing closed and open issues per member with real effort."""
    lines = [
        "| Integrante | Usuário GitHub | Dupla | Issues Fechadas | Issues Abertas | Total Issues | Horas Est. (h) | Horas Reais (h) | Taxa Conclusão |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    tot_closed = 0
    tot_open = 0
    tot_all = 0
    tot_est = 0.0
    tot_real = 0.0

    for m in TEAM_MEMBERS:
        handle = m["handle"]
        name = m["name"]
        dupla = m["dupla"]

        st = issue_counts.get(handle, {})
        closed = st.get("closed", 0)
        opened = st.get("open", 0)
        total = st.get("total", 0)
        est = st.get("est_closed")
        real = st.get("real_closed")
        rate = f"{(closed / total * 100):.1f}%".replace(".", ",") if total > 0 else "0,0%"

        tot_closed += closed
        tot_open += opened
        tot_all += total
        tot_est = None if est is None or tot_est is None else tot_est + est
        tot_real = None if real is None or tot_real is None else tot_real + real

        est_str = format_hours(est)
        real_str = format_hours(real)
        lines.append(
            f"| **{name}** | [{handle}](https://github.com/{handle}) | {dupla} | {closed} | {opened} | {total} | {est_str} | {real_str} | {rate} |"
        )

    overall_rate = f"{(tot_closed / tot_all * 100):.1f}%".replace(".", ",") if tot_all > 0 else "0,0%"
    tot_est_str = format_hours(tot_est)
    tot_real_str = format_hours(tot_real)
    lines.append(
        f"| **Total Consolidado** | - | - | **{tot_closed}** | **{tot_open}** | **{tot_all}** | **{tot_est_str}** | **{tot_real_str}** | **{overall_rate}** |"
    )

    return "\n".join(lines)


def main():
    SNIPPETS_DIR.mkdir(parents=True, exist_ok=True)

    weeks, commits, additions, deletions, git_totals = get_git_log_data()
    issue_counts = get_project_and_issue_metrics()

    # Generate charts
    velocity_chart = render_timeline_chart(
        "Commits por Integrante ao Longo do Tempo",
        "Commits",
        weeks,
        commits,
    )
    additions_chart = render_timeline_chart(
        "Linhas Adicionadas por Integrante ao Longo do Tempo",
        "Linhas Adicionadas",
        weeks,
        additions,
    )
    deletions_chart = render_timeline_chart(
        "Linhas Removidas por Integrante ao Longo do Tempo",
        "Linhas Removidas",
        weeks,
        deletions,
    )
    issues_chart = render_bar_chart(
        "Issues Atribuídas por Integrante",
        "Issues",
        issue_counts,
        key="total",
    )
    resolved_chart = render_bar_chart(
        "Tarefas Resolvidas por Integrante",
        "Tarefas Resolvidas",
        issue_counts,
        key="closed",
    )

    # Generate markdown tables
    contributions_table = generate_contributions_table(git_totals, issue_counts)
    issues_table = generate_issues_table(issue_counts)

    # Write snippet files
    (SNIPPETS_DIR / "commit-velocity.mmd").write_text(velocity_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "code-additions.mmd").write_text(additions_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "code-deletions.mmd").write_text(deletions_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "assigned-issues.mmd").write_text(issues_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "resolved-issues.mmd").write_text(resolved_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "contributions-summary.md").write_text(contributions_table + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "issues-summary.md").write_text(issues_table + "\n", encoding="utf-8")

    print(f"Updated metrics snippets in {SNIPPETS_DIR}")
    print(f"Timeline weeks: {weeks}")
    print(f"Tracked authors: {TRACKED_AUTHORS}")


if __name__ == "__main__":
    main()
