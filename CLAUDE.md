# CLAUDE.md — Instruções para Claude Code

Este arquivo orienta o Claude Code ao operar no repositório da equipe **Frans Bilas (Turma 02)** na disciplina **Qualidade de Software 1 (FGA0315 - 2026.2)** da UnB FGA.

O usuário que está interagindo é **João Victor da Silva Batista de Farias (João V. Farias — @beyondmagic)**, integrante da **Dupla 1 (Qualidade e GQM)** junto com **Mateus Vinícius Vieira (@matix0)**. João lidera as atividades iniciais da Fase 1 (Visão Geral, Propósito C1, Stakeholders C2 e Tipo de Produto/Arquitetura C3), enquanto Mateus assume as subsequentes da Dupla 1 (Modelo de Qualidade SQuaRE C4, Priorização C5, Escopo C6 e ODS C7).

---

## 1. Referência Mestra Obrigatória

O arquivo [AGENTS.md](AGENTS.md) contém as diretrizes completas de contexto do projeto, premissas da Profa. Cristiane Ramos, critérios da norma ISO/IEC 25010:2023 (SQuaRE) e regras de contribuição.
**Toda sessão de assistência deve respeitar integralmente o que está definido no AGENTS.md.**

---

## 2. Comandos Frequentes de Desenvolvimento

- **Servir a documentação localmente (Live Reload)**:
  ```bash
  cd documentation && zensical serve
  ```
- **Compilar a documentação estática (Clean Build)**:
  ```bash
  cd documentation && zensical build --clean
  ```
- **Executar a validação do Humanizer (Anti-Meat-Proxy)**:
  ```bash
  python3 scripts/check_humanizer.py
  ```
- **Configurar os hooks locais do Git**:
  ```bash
  git config core.hooksPath .githooks
  ```

---

## 3. Diretrizes de Escrita e Anti-Meat-Proxy

Ao gerar ou editar qualquer arquivo em `documentation/content/` (artigo, markdown, slides):

1. **Aplique rigorosamente a skill `humanizer`** (`.agents/skills/writing/SKILL.md`):
   - Nunca use construções como "no cenário atual", "desempenha um papel fundamental", "é importante destacar que", "vale ressaltar que".
   - Não use termos inflados como *delve, tapestry, crucial, vital, robusto, inovador*.
   - Mantenha frases diretas, variando o tamanho e a estrutura das sentenças.
2. **Grounding Factual**:
   - Não invente métricas, dados ou referências. Se um dado do Brasil Participativo ainda não foi coletado, sinalize explicitamente que depende da execução da coleta na Fase 3.
3. **Nomenclatura SQuaRE 2023**:
   - Use sempre **Capacidade de Interação** (*Interaction Capability*) para se referir à característica anteriormente denominada Usabilidade.
4. **Apresentação de Slides**:
   - Os slides da Entrega 1 ficam em `documentation/content/entregas/1.md`.
   - Mantenha a sintaxe de slides do Zensical (`## Título` e `<p class="apresentador">Nome</p>`).

---

## 4. Estilo de Código e Commits

- Conventional Commits em português ou inglês: `docs:`, `feat:`, `fix:`, `chore:`.
- Sempre execute `python3 scripts/check_humanizer.py` antes de concluir edições em arquivos `.md` e `.tex`.

