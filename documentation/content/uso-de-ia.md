---
icon: lucide/bot
---

# Declaração e Registro de Uso de Inteligência Artificial

Esta página documenta a política, os mecanismos de controle e os relatos individuais de uso de ferramentas de Inteligência Artificial pela equipe **Frans Bilas (Turma 01)** na disciplina **Qualidade de Software 1 (FGA0315 - 2026.2)**.

---

## 1. Política da Equipe Contra Práticas de Meat-Proxy

Em projetos acadêmicos e técnicos, o uso irrefletido de modelos de linguagem frequentemente degrada a qualidade dos entregáveis. Copiar e colar saídas de LLMs sem leitura crítica (postura conhecida como *meat-proxy*) produz textos inflados, introduções clichês, dados fictícios e adjetivações vazias.

Nossa equipe estabeleceu três diretrizes inegociáveis:

1. **Vedação à Invenção de Dados**: Toda informação quantitativa sobre o software avaliado provém do código-fonte real do Brasil Participativo, de ferramentas de análise estática ou de sessões documentadas de teste.
2. **Revisão Humana Ativa**: A IA atua apenas como copiloto de ideação, estruturação ou correção gramatical. O conteúdo técnico é auditado, validado e reescrito pelos membros antes de qualquer submissão.
3. **Fiscalização Automatizada**: Criamos o script `scripts/check_humanizer.py` acoplado a um hook de pré-commit do Git e a uma ação de integração contínua (GitHub Actions), barrando termos proibidos, artefatos de chatbot e construções prolixas.

---

## 2. Relatos Individuais de Contribuição com IA

Cada integrante do grupo é responsável por declarar explicitamente como utilizou ferramentas de IA em suas atribuições, indicando a ferramenta, a tarefa realizada e o procedimento exato de revisão humana aplicada.

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

- **Papel no Projeto**: Dupla 1 (Qualidade e GQM) - Responsável pelas atividades subsequentes da Fase 1 (Modelo SQuaRE, Priorização, Escopo e ODS) e coordenação geral do plano de sprints.
- **Ferramentas Utilizadas**: Claude (Anthropic).
- **Tarefas Realizadas com Apoio de IA**: Elaboração preliminar da proposta de sprints (`references/artificial-intelligence/claude/plano.md`) a partir da leitura dos critérios da disciplina.
- **Procedimento de Revisão Humana**: *[Placeholder: O integrante atualizará esta seção com o detalhamento de suas revisões humanas e uso das ferramentas ao longo da execução da Fase 1 e Fase 2].*

---

### Davi Mesquita Sousa

- **Papel no Projeto**: A definir (Dupla 2 ou 3).
- **Ferramentas Utilizadas**: *[A preencher pelo integrante]*
- **Tarefas Realizadas com Apoio de IA**: *[A preencher pelo integrante]*
- **Procedimento de Revisão Humana**: *[A preencher pelo integrante]*

---

### José Vinícius Alvares Soares de Queiroz

- **Papel no Projeto**: Referencial teórico, objetivos GQM, questões e hipóteses da Fase 2.
- **Ferramentas Utilizadas**: Claude (Anthropic).
- **Tarefas Realizadas com Apoio de IA**: Rascunho do referencial teórico (SQuaRE, GQM, PSM), dos objetivos no template GQM, das questões e das hipóteses em `fases/2.md`, da seção correspondente em `main.tex` e do slide 9 de `entregas/1.md`.
- **Procedimento de Revisão Humana**: *[A preencher pelo integrante: como conferiu os objetivos contra a Fase 1, as referências e as hipóteses.]*

---

### Lucca Medeiros Silva

- **Papel no Projeto**: Dupla 1 (Qualidade e GQM) - Seleção de Métricas (F2-C4), Níveis de Julgamento (F2-C5) e Consistência entre Fases 1 e 2 (F2-C11).
- **Ferramentas Utilizadas**: Antigravity (Gemini 3.8 Flash).
- **Tarefas Realizadas com Apoio de IA**: Estruturação preliminar das fichas técnicas das 10 métricas de avaliação, formulação matemática das métricas, definição das faixas de pontuação da tabela de julgamento e diagrama Mermaid do GQM em três níveis.
- **Procedimento de Revisão Humana**: Calibração dos limiares de pontuação com base nas boas práticas do ecossistema Ruby on Rails e Decidim, validação da viabilidade operacional das coletas para impedir testes intrusivos contra servidores de produção e verificação da rastreabilidade com as decisões e stakeholders da Fase 1.

---

### Miguel Arthur Oliveira de Lima

- **Papel no Projeto**: A definir (Dupla 2 ou 3).
- **Ferramentas Utilizadas**: *[A preencher pelo integrante]*
- **Tarefas Realizadas com Apoio de IA**: *[A preencher pelo integrante]*
- **Procedimento de Revisão Humana**: *[A preencher pelo integrante]*

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 17/10/2026 | Criação da política de uso ético de IA, registro individual e estrutura para a equipe | [João Victor da Silva Batista de Farias](https://github.com/beyondmagic) | [Mateus Vinícius Vieira](https://github.com/matix0) |
| `1.1` | 18/10/2026 | Registro de uso de IA referente à especificação das métricas, níveis de julgamento e rastreabilidade da Fase 2 | [Lucca Medeiros Silva](https://github.com/luccameds) | [José Vinícius Alvares Soares de Queiroz](https://github.com/JoseViniciusQueiroz) |




