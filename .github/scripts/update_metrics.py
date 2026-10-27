#!/usr/bin/env python3
"""
update_metrics.py

Extracts Git commit activity and GitHub issue workload metrics to generate
automated Mermaid chart snippets and Markdown tables under documentation/snippets/management/.
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


def get_issue_counts():
    """Retrieve issue counts per contributor via GitHub REST API or gh CLI."""
    counts = {
        author: {"total": 0, "closed": 0, "open": 0}
        for author in TRACKED_AUTHORS
    }

    # 1. Attempt fetching via GitHub REST API
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        try:
            mcp_file = Path.home() / ".gemini" / "config" / "mcp_config.json"
            if mcp_file.exists():
                cfg = json.loads(mcp_file.read_text())
                token = cfg.get("mcpServers", {}).get("github", {}).get("env", {}).get("GITHUB_PERSONAL_ACCESS_TOKEN")
        except Exception:
            pass

    headers = {"User-Agent": "MetricsScript", "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    all_issues = []
    try:
        page = 1
        while True:
            url = f"https://api.github.com/repos/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS/issues?state=all&per_page=100&page={page}"
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                batch = json.loads(resp.read().decode())
                if not batch:
                    break
                all_issues.extend(batch)
                if len(batch) < 100:
                    break
                page += 1
    except Exception:
        all_issues = []

    # 2. Fallback to gh CLI if REST API failed or returned empty
    if not all_issues:
        try:
            cmd = ["gh", "issue", "list", "--state", "all", "--json", "assignees,state,pullRequest", "--limit", "200"]
            res = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=10)
            if res.returncode == 0:
                all_issues = json.loads(res.stdout)
        except Exception:
            pass

    # Aggregate issue statistics per author
    for issue in all_issues:
        # Ignore pull requests listed as issues
        if "pull_request" in issue or issue.get("pullRequest") is not None:
            continue
        state = issue.get("state", "").lower()
        assignees = issue.get("assignees", [])
        for assignee in assignees:
            login = assignee.get("login", "")
            if login in counts:
                counts[login]["total"] += 1
                if state == "closed":
                    counts[login]["closed"] += 1
                else:
                    counts[login]["open"] += 1
            else:
                normalized = normalize_author(login, "")
                if normalized in counts:
                    counts[normalized]["total"] += 1
                    if state == "closed":
                        counts[normalized]["closed"] += 1
                    else:
                        counts[normalized]["open"] += 1

    return counts


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


def render_bar_chart(title: str, y_label: str, counts_by_author: dict) -> str:
    """Format Mermaid xychart-beta with dedicated series per contributor for distinct colors."""
    x_labels = [f'"{author}"' for author in TRACKED_AUTHORS]
    vals = [counts_by_author.get(author, {}).get("total", 0) for author in TRACKED_AUTHORS]
    max_bound = calculate_upper_bound(vals, min_bound=5)

    bar_lines = []
    for i, author in enumerate(TRACKED_AUTHORS):
        author_val = counts_by_author.get(author, {}).get("total", 0)
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
        "| Integrante | Usuário GitHub | Dupla | Commits | Linhas Adicionadas (+) | Linhas Removidas (-) | Saldo Líquido | Issues Atribuídas |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    tot_commits = 0
    tot_adds = 0
    tot_dels = 0
    tot_issues = 0

    for m in TEAM_MEMBERS:
        handle = m["handle"]
        name = m["name"]
        dupla = m["dupla"]

        c = git_totals["commits"].get(handle, 0)
        a = git_totals["additions"].get(handle, 0)
        d = git_totals["deletions"].get(handle, 0)
        net = a - d
        iss = issue_counts.get(handle, {}).get("total", 0)

        tot_commits += c
        tot_adds += a
        tot_dels += d
        tot_issues += iss

        sign_net = f"+{net}" if net > 0 else str(net)
        lines.append(
            f"| **{name}** | [{handle}](https://github.com/{handle}) | {dupla} | {c} | +{a} | -{d} | {sign_net} | {iss} |"
        )

    tot_net = tot_adds - tot_dels
    tot_sign_net = f"+{tot_net}" if tot_net > 0 else str(tot_net)
    lines.append(
        f"| **Total Consolidado** | - | - | **{tot_commits}** | **+{tot_adds}** | **-{tot_dels}** | **{tot_sign_net}** | **{tot_issues}** |"
    )

    return "\n".join(lines)


def generate_issues_table(issue_counts: dict) -> str:
    """Generate Markdown table detailing closed and open issues per member."""
    lines = [
        "| Integrante | Usuário GitHub | Dupla | Issues Fechadas | Issues Abertas | Total Atribuídas | Taxa de Conclusão |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: |",
    ]

    tot_closed = 0
    tot_open = 0
    tot_all = 0

    for m in TEAM_MEMBERS:
        handle = m["handle"]
        name = m["name"]
        dupla = m["dupla"]

        st = issue_counts.get(handle, {"total": 0, "closed": 0, "open": 0})
        closed = st.get("closed", 0)
        opened = st.get("open", 0)
        total = st.get("total", 0)
        rate = f"{(closed / total * 100):.1f}%".replace(".", ",") if total > 0 else "0,0%"

        tot_closed += closed
        tot_open += opened
        tot_all += total

        lines.append(
            f"| **{name}** | [{handle}](https://github.com/{handle}) | {dupla} | {closed} | {opened} | {total} | {rate} |"
        )

    overall_rate = f"{(tot_closed / tot_all * 100):.1f}%".replace(".", ",") if tot_all > 0 else "0,0%"
    lines.append(
        f"| **Total Consolidado** | - | - | **{tot_closed}** | **{tot_open}** | **{tot_all}** | **{overall_rate}** |"
    )

    return "\n".join(lines)


def main():
    SNIPPETS_DIR.mkdir(parents=True, exist_ok=True)

    weeks, commits, additions, deletions, git_totals = get_git_log_data()
    issue_counts = get_issue_counts()

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
    )

    # Generate markdown tables
    contributions_table = generate_contributions_table(git_totals, issue_counts)
    issues_table = generate_issues_table(issue_counts)

    # Write snippet files
    (SNIPPETS_DIR / "commit-velocity.mmd").write_text(velocity_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "code-additions.mmd").write_text(additions_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "code-deletions.mmd").write_text(deletions_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "assigned-issues.mmd").write_text(issues_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "contributions-summary.md").write_text(contributions_table + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "issues-summary.md").write_text(issues_table + "\n", encoding="utf-8")

    print(f"Updated metrics snippets in {SNIPPETS_DIR}")
    print(f"Timeline weeks: {weeks}")
    print(f"Tracked authors: {TRACKED_AUTHORS}")


if __name__ == "__main__":
    main()
