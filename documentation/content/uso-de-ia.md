---
icon: lucide/bot
---

# Declaração e Registro de Uso de Inteligência Artificial

Esta página registra como a equipe **Frans Bilas (Turma 01)** usa ferramentas de IA na disciplina **Qualidade de Software 1 (FGA0315 - 2026.2)**.

---

## 1. Política da Equipe Contra Práticas de Meat-Proxy

A equipe proíbe a cópia de saídas de IA sem leitura crítica, prática conhecida como *meat-proxy*. Os integrantes respondem pelo conteúdo que submetem.

Toda informação quantitativa sobre o software avaliado deve vir do código-fonte do Brasil Participativo, de ferramentas de análise estática ou de sessões documentadas de teste. O script `scripts/check_humanizer.py`, executado no pré-commit e no GitHub Actions, verifica termos proibidos, artefatos de chatbot e construções prolixas.

---

## 2. Relatos Individuais de Contribuição com IA

Os relatos identificam a ferramenta, as tarefas apoiadas por IA e as conferências registradas por cada integrante.

---

### João Victor da Silva Batista de Farias

- **Papel no Projeto**: Dupla 1 (Qualidade e GQM) - Responsável pelas atividades iniciais da Fase 1 (Visão Geral, Propósito, Stakeholders e Arquitetura do Software).
- **Ferramentas Utilizadas**: Antigravity (Gemini 3.8 Flash).

#### Habilidades (Skills) Empregadas
- **`grill-me`**: Utilizada para conduzir uma entrevista técnica estruturada antes de qualquer escrita. A dinâmica permitiu esclarecer requisitos da disciplina, alinhar a distribuição de tarefas da Entrega 1 com o Mateus e deliberar sobre decisões de arquitetura e governança sem assumir premissas implícitas.
- **`humanizer`**: Aplicada para limpar vícios sintáticos de IA, garantir ritmo de leitura natural, remover construções artificiais e adequar a nomenclatura estritamente à norma ISO/IEC 25010:2023 (garantindo o uso de *Capacidade de Interação* em vez de *Usabilidade*).

#### Tarefas Realizadas com Apoio de IA
- Concepção do script de auditoria `scripts/check_humanizer.py`, do pre-commit hook versionado (`.githooks/pre-commit`) e do workflow de CI (`.github/workflows/humanizer-check.yml`).
- Rascunho inicial e diagramação em Mermaid da arquitetura do Brasil Participativo para a GitPage (`fases/1.md`) e para os slides (`entregas/1.md`).
- Estruturação do esqueleto em LaTeX do artigo científico sob a classe `IEEEtran` em modo *journal*.

#### Procedimento de Revisão Humana
- Inspeção manual do repositório clonado do Brasil Participativo (`brasil-participativo/`), confirmando diretamente nos arquivos `Gemfile.lock`, `config/initializers/` e rotas a presença do Ruby 3.0.4, Rails 6.1.7, Decidim 0.27.2, PostgreSQL, Sidekiq e da gem `decidim-ej` desenvolvida pelo LAPPIS.
- Reescrever os tópicos dos slides para torná-los concisos e adequados ao tempo de fala de uma apresentação rápida, adicionando notas de contexto em comentários HTML (`<!-- ... -->`) para guiar a oratória.
- Validação local da compilação do artigo via `pdflatex` e verificação da integridade do site gerado via `zensical build --clean`.

---

### Mateus Vinícius Vieira

- **Papel no Projeto**: Líder do grupo, na Dupla 1. Coordena o backlog, os sprints e a gestão PSM/CID no GitHub Projects 33; revisa as Fases 1 e 2, cuida das correções do PC1 e monta os slides.
- **Ferramentas Utilizadas**: Claude (Anthropic), pelo Claude Code.
- **Tarefas Realizadas com Apoio de IA**:
  - Proposta preliminar do plano de sprints (`references/artificial-intelligence/claude/plano.md`), a partir dos critérios da disciplina.
  - Gestão v2.0 e TCLE da Fase 3 (PR #86): diagnóstico da versão 1.0, rascunho das necessidades N1 a N6 e dos construtos, e adaptação do modelo de TCLE da disciplina.
  - Ata 02 e redistribuição do Sprint 3 (PR #91), além da identificação do usuário em `AGENTS.md` e `CLAUDE.md`.
  - Sprint 3: registro das correções do PC1 na Gestão, revisão das Fases 1 e 2 (legendas, fontes, referências e terminologia) e slides do PC2.
- **Procedimento de Revisão Humana**:
  - As contribuições feitas com apoio da IA entraram no repositório por PR (#86, #91 e #100 a #103), e cada PR declara a ferramenta, a tarefa e quem revisou.
  - Os commits feitos com apoio da IA levam a linha `Co-Authored-By` do Claude, o que deixa visível no histórico o que teve participação da ferramenta.
  - A linha de base de N6 na Gestão foi calculada pelo histórico da `main` e pelos PRs no GitHub, e não por estimativa.
  - Na revisão das Fases 1 e 2, as mudanças de forma entraram; as que alterariam fórmulas, níveis ou critérios das métricas ficaram de fora e foram listadas no PR #101 para a Dupla 2 e a professora.
  - Nos slides do PC2, cada tabela de números cita a página de origem como fonte.

---

### Davi Mesquita Sousa

- **Papel no Projeto**: Ainda não definido no registro atual da equipe.
- **Ferramentas Utilizadas**: Gemini.
- **Tarefas Realizadas com Apoio de IA**: Correção textual dos conteúdos da documentação.
- **Procedimento de Revisão Humana**: O texto corrigido foi revisado manualmente antes do registro.

---

### José Vinícius Alvares Soares de Queiroz

- **Papel no Projeto**: Referencial teórico, objetivos GQM, questões e hipóteses da Fase 2.
- **Ferramentas Utilizadas**: Claude (Anthropic).
- **Tarefas Realizadas com Apoio de IA**: Rascunho do referencial teórico (SQuaRE, GQM, PSM), dos objetivos no template GQM, das questões e das hipóteses em `fases/2.md`, da seção correspondente em `main.tex` e do slide 9 de `entregas/1.md`.
- **Procedimento de Revisão Humana**: Clonei o repositório `decidim-govbr` (commit `176b046`, ramo `develop`) e conferi no código as afirmações das hipóteses: as extensões vêm de repositórios separados, o projeto sobrescreve classes do Decidim em `app/permissions/` e `app/commands/`, e há 156 testes RSpec em `spec/`. Confirmei no `Gemfile.lock` as versões Decidim 0.27.2, Rails 6.1.7.2 e Ruby 3.0.4 e corrigi as hipóteses H2.1, H2.3 e H3.2 com base nisso. Conferi as referências nas páginas da ISO e do editor, completando a do GQM com editor, volume e páginas. 

---

### Lucca Medeiros Silva

- **Papel no Projeto**: Dupla 2. Seleção de Métricas (F2-C4), Níveis de Julgamento (F2-C5) e Consistência entre Fases 1 e 2 (F2-C11); no Sprint 3, passo a passo das medidas e análise estática de Manutenibilidade.
- **Ferramentas Utilizadas**: Antigravity (Gemini 3.8 Flash) e Codex.
- **Tarefas Realizadas com Apoio de IA**: Estruturação preliminar das fichas técnicas das 12 métricas de avaliação, formulação matemática das métricas, definição das faixas de pontuação da tabela de julgamento e diagrama Mermaid do GQM em três níveis.
- **Procedimento de Revisão Humana**: Calibração dos limiares de pontuação com base nas boas práticas do ecossistema Ruby on Rails e Decidim, validação da viabilidade operacional das coletas para impedir testes intrusivos contra servidores de produção e verificação da rastreabilidade com as decisões e stakeholders da Fase 1.

Em 08/11/2026, o Codex preparou os procedimentos das 12 métricas (#63), implementou e executou a coleta estática de Manutenibilidade no commit `176b046` (#89) e acrescentou testes de regressão do `MeetingIframeEmbedder` em patch separado (#73). Também apoiou a redação dessas páginas e a conferência posterior dos algoritmos, das fórmulas e da configuração dos testes. Os CSVs, hashes, relatórios de ferramentas e testes automatizados estão ligados às páginas de [G2](dados/manutenibilidade/index.md) e da [melhoria](dados/melhoria-73/index.md), junto com os limites das verificações executadas.

---

### Miguel Arthur Oliveira de Lima

- **Papel no Projeto**: Dupla 3 (Gestão e Infraestrutura): planejamento de sprints, governança, métricas de processo (PSM/CID), consolidação da documentação da Fase 1 e apoio à Entrega 1.
- **Ferramentas Utilizadas**: Antigravity (Gemini 3.8 Flash).
- **Tarefas Realizadas com Apoio de IA**: Modelagem do diagrama conceitual da norma ISO/IEC 25010:2023 em Mermaid, estruturação da matriz de priorização formal com ponderação de impacto e risco para as características de qualidade, e auditoria dos critérios de entrega da Fase 1 e 2.
- **Procedimento de Revisão Humana**: Calibração dos pesos e notas da matriz de priorização com base no contexto de software público deliberativo, validação da integridade sintática do diagrama de subcaracterísticas e adequação rigorosa à terminologia da ISO/IEC 25010:2023 e às regras da disciplina.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 17/10/2026 | Criação da política de uso ético de IA, registro individual e estrutura para a equipe | [João Victor da Silva Batista de Farias](https://github.com/beyondmagic) | [Mateus Vinícius Vieira](https://github.com/matix0) |
| `1.1` | 18/10/2026 | Registro de uso de IA referente à especificação das métricas, níveis de julgamento e rastreabilidade da Fase 2 | [Lucca Medeiros Silva](https://github.com/luccameds) | - |
| `1.2` | 19/10/2026 | Registro individual de uso de IA de Miguel Arthur (modelagem SQuaRE, priorização e governança) | [Miguel Arthur Oliveira de Lima](https://github.com/zlimaz) | - |
| `1.3` | 04/11/2026 | Registro individual de uso de IA de Mateus (gestão, atas, revisão das Fases 1 e 2 e slides do PC2) | [Mateus Vinícius Vieira](https://github.com/matix0) | - |
| `1.4` | 08/11/2026 | Registro de apoio do Codex às issues #63, #89 e #73 | Lucca Medeiros Silva | - |


