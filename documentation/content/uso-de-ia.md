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

- **Papel no Projeto**: A definir (Dupla 2 ou 3).
- **Ferramentas Utilizadas**: *[A preencher pelo integrante]*
- **Tarefas Realizadas com Apoio de IA**: *[A preencher pelo integrante]*
- **Procedimento de Revisão Humana**: *[A preencher pelo integrante]*

---

### Lucca Medeiros Silva

- **Papel no Projeto**: A definir (Dupla 2 ou 3).
- **Ferramentas Utilizadas**: *[A preencher pelo integrante]*
- **Tarefas Realizadas com Apoio de IA**: *[A preencher pelo integrante]*
- **Procedimento de Revisão Humana**: *[A preencher pelo integrante]*

---

### Miguel Arthur Oliveira de Lima

- **Papel no Projeto**: A definir (Dupla 2 ou 3).
- **Ferramentas Utilizadas**: *[A preencher pelo integrante]*
- **Tarefas Realizadas com Apoio de IA**: *[A preencher pelo integrante]*
- **Procedimento de Revisão Humana**: *[A preencher pelo integrante]*

---

## 3. Template Obrigatório para Novos Registros

Para manter a consistência, novas adições a esta página ou aos Pull Requests devem seguir o formato:

```markdown
### [Nome Completo do Integrante]

- **Papel no Projeto**: [Dupla X / Atividade Y]
- **Ferramentas Utilizadas**: [Nome da ferramenta e versão, ex.: Claude 3.5 Sonnet, GitHub Copilot]
- **Tarefas Realizadas**: [Descrição pontual das seções, scripts ou testes auxiliados]
- **Procedimento de Revisão Humana**: [Descrição objetiva de como os dados foram checados contra fontes primárias e como o texto foi retrabalhado manualmente]
```

