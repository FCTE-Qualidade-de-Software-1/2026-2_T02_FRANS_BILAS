# AGENTS.md — Diretrizes para Agentes de IA e Automações

Este repositório pertence à equipe **Frans Bilas (Turma 02)** na disciplina **Qualidade de Software 1 (FGA0315 - 2026.2)** da Universidade de Brasília (Campus UnB Gama: Faculdade de Ciências e Tecnologias em Engenharia - Brasília — FCTE), ministrada pela **Profa. Dra. Cristiane Soares Ramos**.

O usuário principal que lidera esta frente técnica é **João Victor da Silva Batista de Farias (João V. Farias — @beyondmagic)**, integrante da **Dupla 1 (Qualidade e GQM)** em conjunto com **Mateus Vinícius Vieira (@matix0)**.

### Divisão de Responsabilidades da Dupla 1 (Fase 1 / Entrega 1):
- **João V. Farias (Atividades Iniciais)**:
  - Visão geral e contextualização da avaliação (Critério AG-C1)
  - Propósito da avaliação e uso pretendido (Critério 1)
  - Requisitante e partes interessadas / stakeholders (Critério 2)
  - Tipo de produto e descrição estruturada do software / arquitetura (Critério 3)
- **Mateus Vinícius Vieira (Atividades Subsequentes da Dupla 1)**:
  - Modelo de qualidade SQuaRE e diagrama adaptado (Critério 4)
  - Seleção e priorização das características (Critério 5)
  - Escopo, profundidade e objetos de avaliação (Critério 6)
  - Alinhamento aos ODS, metas e indicadores (Critério 7)

---

## 1. Contexto Geral do Projeto

- **Software Avaliado**: [Brasil Participativo](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr) (instância governamental baseada na plataforma Decidim / Ruby on Rails).
- **Modelo de Qualidade**: **ISO/IEC 25010:2023 (SQuaRE)**.
  - *Atenção à Nomenclatura*: Na revisão 2023 da norma, "Usabilidade" passou formalmente a se chamar **Capacidade de Interação** (*Interaction Capability*). O termo atualizado deve ser mantido de forma consistente em todo o artigo, slides e documentação.
- **Três Características Selecionadas e Aprovadas**:
  1. **Capacidade de Interação** (*Interaction Capability*)
  2. **Manutenibilidade** (*Maintainability*)
  3. **Segurança** (*Security*)
- **Métodos Exigidos**:
  - **GQM (Goal-Question-Metric)**: Ligação estrita entre Objetivos de medição, Questões analíticas e Métricas quantificáveis.
  - **PSM/CID**: Gestão do projeto com métricas de processo, acompanhamento semanal e tomada de decisão.
- **Entregáveis Centrais**:
  - **GitPage**: Documentação estática gerada via [Zensical](https://github.com/krzysztofzuraw/zensical) localizada em `documentation/`.
  - **Artigo Científico em LaTeX**: Localizado em `documentation/content/article/source/main.tex` (limite de 15 páginas, modelo IEEE / IEEEtran).
  - **Apresentações / Slides**: Localizados em `documentation/content/entregas/` (a apresentação da Entrega 1 fica em `documentation/content/entregas/1.md`, renderizada pelo plugin `zensical-slides`).

---

## 2. Política Estrita Anti-Meat-Proxy

Muitos membros de equipes acadêmicas operam como *meat-proxies* — copiam e colam saídas de LLMs diretamente no repositório sem leitura crítica, gerando textos inflados, prolixos e vazios de conteúdo técnico real.

**Qualquer agente de IA atuando neste repositório DEVE OBRIGATORIAMENTE seguir estas restrições inegociáveis:**

1. **PROIBIDO INVENTAR DADOS**: Jamais alucine métricas, percentuais, linhas de código, números de vulnerabilidade ou estatísticas fictícias. Toda medida deve vir comprovadamente do código do Brasil Participativo, de ferramentas de análise estática ou de sessões documentadas de teste.
2. **ZERO TOLERÂNCIA A VÍCIOS DE IA**: Banimento absoluto de introduções clichês ("No cenário atual", "Na era digital contemporânea"), falsos contrastes ("não é apenas X, é Y"), encheções de linguiça ("vale ressaltar que", "desempenha um papel fundamental") e adjetivações vazias ("robusto", "inovador", "vital").
3. **GROUNDING TÉCNICO RIGOROSO**: Todas as afirmações sobre o software devem citar componentes reais do Decidim (módulos, gems, controllers, banco PostgreSQL, testes RSpec) ou trechos exatos das normas SQuaRE e critérios da professora (`references/discipline/`).
4. **SEM ARTEFATOS DE CHATBOT**: Nunca incluir saídas como "Certamente!", "Espero ter ajudado!", "Como uma inteligência artificial..." em arquivos de documentação, LaTeX ou slides.

---

## 3. Aplicação Obrigatória da Skill `humanizer`

Toda vez que um texto for gerado ou editado para o artigo em LaTeX (`documentation/content/article/source/main.tex`) ou para a documentação/GitPage (`documentation/content/`), **a skill `humanizer` (`.agents/skills/writing/SKILL.md`) deve ser aplicada antes de entregar o resultado**.

### Checklist Rápido de Humanização:
- [ ] **Sem travessões longos (em-dashes `—`) nem hifens duplos (`--`)** no meio de frases em prosa (exceto sintaxe nativa LaTeX para en-dash numérico). Use vírgula, dois-pontos ou ponto final.
- [ ] **Aspas retas (`"` e `'`)**: Sem aspas tipográficas curvas coladas.
- [ ] **Sem vocabulário inflado**: Eliminar *delve, tapestry, crucial, vital, pivotal, holistic, seamless, robusto, inovador*.
- [ ] **Ritmo de frases variado**: Alternar frases curtas e diretas com frases analíticas mais elaboradas. Evitar parágrafos simétricos de exatamente 3 frases.
- [ ] **Voz ativa e propositiva**: Dizer o que o dado é ou o que a equipe fez, sem rodeios.
- [ ] **Validação com script**: O arquivo alterado deve passar sem avisos por `python3 scripts/check_humanizer.py`.

---

## 4. Estrutura de Slides com `zensical-slides`

Os slides da Entrega 1 ficam em `documentation/content/entregas/1.md`.
- Cada slide começa com um header `## Título do Slide`.
- O apresentador é indicado pela tag HTML: `<p class="apresentador">Nome do Membro</p>`.
- Slides devem ser extremamente concisos: tópicos objetivos, dados diretos e diagramas, sem blocos densos de texto.

---

## 5. Convenções de Git e Contribuição

- **Branches**: `tipo/numero-descricao` (ex.: `docs/1-proposito-stakeholders`).
- **Commits**: Conventional Commits em português ou inglês (`docs:`, `feat:`, `fix:`, `refactor:`, `chore:`).
- **Pre-commit Hook**: Ativado via `git config core.hooksPath .githooks`. Executa automaticamente o script `scripts/check_humanizer.py` a cada commit de arquivos `.md` e `.tex`.

