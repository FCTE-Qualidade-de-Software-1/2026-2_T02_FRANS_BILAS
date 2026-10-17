#!/usr/bin/env python3
"""
check_humanizer.py - Script de verificação de qualidade de escrita contra vícios de IA.
Inspirado nas diretrizes da skill humanizer (.agents/skills/writing/SKILL.md) e na
política anti-meat-proxy da equipe Frans Bilas (FGA0315 - Qualidade de Software 1).

Verifica arquivos .md e .tex stageds ou passados por argumento, barrando termos
banidos, jargões inflados de IA, frases corporativas vazias e artefatos de chatbot.
"""

import sys
import re
import os
from pathlib import Path

# Lista de termos e padrões proibidos (case-insensitive)
BANNED_PATTERNS = [
    # Artefatos diretos de Chatbot
    (r"\b(espero ter ajudado|espero que ajude|como uma inteligência artificial|como uma ia)\b", "Artefato de chatbot"),
    (r"\b(certamente!|com certeza!|sinta-se à vontade para|qualquer dúvida estou à disposição)\b", "Artefato de chatbot"),
    (r"\b(i hope this helps|as an ai|feel free to ask|great question!)\b", "Artefato de chatbot (inglês)"),
    
    # Clichês de abertura e transição de IA
    (r"\b(no cenário atual|no mundo contemporâneo|na era digital|nos dias de hoje)\b", "Abertura clichê de IA"),
    (r"\b(in today's digital age|in today's fast-paced world)\b", "Abertura clichê de IA (inglês)"),
    (r"\b(vale ressaltar que|é importante destacar que|é fundamental notar que|cabe ressaltar que)\b", "Encheção de linguiça / vício de IA"),
    (r"\b(it is important to note that|it's crucial to|it is essential to note)\b", "Encheção de linguiça (inglês)"),
    
    # Vocabulário inflado / buzzwords de IA
    (r"\b(desempenha um papel fundamental|desempenha um papel crucial|desempenha papel vital)\b", "Importância inflada de IA"),
    (r"\b(serves as a testament|stands as a testament|plays a vital role|plays a pivotal role)\b", "Importância inflada de IA (inglês)"),
    (r"\b(delve|tapestry|intricate tapestry|holistic|seamless|seamlessly)\b", "Vocabulário clássico de IA"),
    (r"\b(revolucionário|inovador ecossistema|solução de ponta|divisor de águas)\b", "Tom promocional / buzzword"),
    (r"\b(game-changer|groundbreaking|cutting-edge|paradigm shift)\b", "Tom promocional (inglês)"),
    
    # Atribuições vagas (banned na regra da skill)
    (r"\b(especialistas afirmam que|observadores apontam que|estudos comprovam que)\b", "Atribuição vaga sem fonte explícita"),
    (r"\b(industry experts agree|observers have cited|several sources)\b", "Atribuição vaga sem fonte (inglês)"),
]

# Pastas e arquivos a ignorar (arquivos de regras que listam termos proibidos como exemplo)
IGNORED_DIRS = {
    ".git",
    ".cache",
    ".venv",
    "site",
    "references",
    ".agents/skills/writing",  # O próprio arquivo da skill contém os termos como exemplo
}

IGNORED_FILES = {
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    ".github/pull_request_template.md",
}

def is_ignored(path_str):
    for ignored in IGNORED_DIRS:
        if ignored in path_str:
            return True
    filename = os.path.basename(path_str)
    if filename in IGNORED_FILES:
        return True
    return False

def check_file(filepath):
    errors = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        return [f"Erro ao ler arquivo {filepath}: {e}"]

    for line_num, line in enumerate(lines, 1):
        # Ignora linhas comentadas em LaTeX ou Markdown se aplicável
        stripped = line.strip()
        if stripped.startswith("%") or stripped.startswith("<!--"):
            continue

        for pattern, desc in BANNED_PATTERNS:
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                errors.append(
                    f"{filepath}:{line_num}: [{desc}] Encontrado termo proibido: '{match.group(0)}'\n"
                    f"    Linha: {line.strip()}"
                )

    return errors

def main():
    files_to_check = []
    
    if len(sys.argv) > 1:
        # Arquivos passados por argumento (ex.: pelo pre-commit ou CI)
        for arg in sys.argv[1:]:
            p = Path(arg)
            if p.is_file() and p.suffix in [".md", ".tex"]:
                if not is_ignored(str(p)):
                    files_to_check.append(str(p))
    else:
        # Busca recursiva em documentation/
        for root, _, files in os.walk("documentation"):
            for file in files:
                if file.endswith((".md", ".tex")):
                    p = os.path.join(root, file)
                    if not is_ignored(p):
                        files_to_check.append(p)
        # Verifica também README.md e CONTRIBUTING.md se existirem
        for f in ["README.md", "CONTRIBUTING.md"]:
            if os.path.exists(f) and not is_ignored(f):
                files_to_check.append(f)

    all_errors = []
    for filepath in files_to_check:
        errors = check_file(filepath)
        if errors:
            all_errors.extend(errors)

    if all_errors:
        print("\n" + "="*80)
        print("❌ FALHA NO HUMANIZER CHECK (Regras Anti-Meat-Proxy e Escrita Humana)")
        print("="*80)
        print("Foram detectados vícios de escrita típicos de IA ou artefatos proibidos:")
        for err in all_errors:
            print(f"  • {err}")
        print("\n💡 Como corrigir:")
        print("  1. Consulte '.agents/skills/writing/SKILL.md' para entender as alternativas humanas.")
        print("  2. Reescreva as passagens com voz direta, dados concretos do Brasil Participativo e fontes reais.")
        print("  3. Não submeta textos gerados por IA sem curadoria e revisão criteriosa.")
        print("="*80 + "\n")
        sys.exit(1)

    print(f"✅ Humanizer Check passou com sucesso ({len(files_to_check)} arquivos verificados)!")
    sys.exit(0)

if __name__ == "__main__":
    main()
