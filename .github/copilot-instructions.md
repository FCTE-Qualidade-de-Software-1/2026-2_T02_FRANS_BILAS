# GitHub Copilot Instructions

You are assisting the **Frans Bilas** team in the Software Quality 1 course (FGA0315 - 2026.2) at UnB (Campus UnB Gama: Faculdade de Ciências e Tecnologias em Engenharia - Brasília — FCTE), taught by Profa. Cristiane Soares Ramos.
The project evaluates the quality of the open-source platform **Brasil Participativo** (Decidim Gov.br / Lappis UnB).

---

## Core Rules & Context

1. **Master Context**:
   - Always adhere to the project rules and standards defined in [AGENTS.md](../AGENTS.md).

2. **Quality Model (ISO/IEC 25010:2023 SQuaRE)**:
   - Terminology update: Use **Capacidade de Interação** (*Interaction Capability*) instead of "Usabilidade".
   - The three evaluated characteristics are:
     1. Capacidade de Interação
     2. Manutenibilidade
     3. Segurança

3. **Anti-Meat-Proxy & Humanizer Protocol**:
   - Never generate boilerplate AI filler (e.g., "no cenário atual", "desempenha um papel fundamental", "é importante destacar que", "delve", "tapestry", "robusto", "vital").
   - Follow the guidelines in `.agents/skills/writing/SKILL.md` (no chatbot artifacts, no fake statistics, no invented data).
   - Write clear, concise, active sentences grounded in actual software architecture and course guidelines.

4. **File Structure**:
   - Scientific paper (LaTeX): `documentation/content/article/source/main.tex`
   - Slide presentation (Entrega 1): `documentation/content/entregas/1.md` (using `<p class="apresentador">...</p>`)
   - Documentation & GitPage: `documentation/content/`
   - Audit script: `python3 scripts/check_humanizer.py`

5. **Commit Messages**:
   - Follow Conventional Commits format (`docs:`, `feat:`, `fix:`, `refactor:`, `chore:`).

