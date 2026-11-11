---
icon: lucide/rocket
---

# Avaliação da Qualidade de Software: Brasil Participativo

Este portal reúne o planejamento, as medições e as evidências da avaliação de qualidade de software da plataforma **Brasil Participativo**. A equipe **Frans Bilas (Turma 01)** desenvolve o projeto na disciplina **Qualidade de Software 1 (FGA0315 - 2026.2)**, ministrada pela Profa. Dra. Cristiane Soares Ramos na Universidade de Brasília (Campus UnB Gama: Faculdade de Ciências e Tecnologias em Engenharia - Brasília / FCTE).

---

## 1. Sobre o Projeto e o Objeto de Avaliação

O **Brasil Participativo** é a plataforma digital oficial do Governo Federal brasileiro para consultas públicas, deliberação popular e coleta de propostas da sociedade civil. O sistema atuou em escala nacional durante o Plano Plurianual (PPA 2024-2027), registrando mais de 1,4 milhão de votos de cidadãos em todo o país.

A solução deriva de pesquisas do Laboratório Avançado de Pesquisa e Desenvolvimento de Software (LAPPIS) da UnB Gama. Na prática, a plataforma é uma customização governamental (*fork*) do software livre [Decidim](https://decidim.org/), criado pela comunidade de Barcelona. O repositório central (`decidim-govbr`) emprega Ruby 3.0 com o framework Ruby on Rails 6.1 e integra autenticação unificada via Gov.br (OpenID Connect com JWKS), módulos de deliberação e banco relacional PostgreSQL.

A avaliação audita o sistema para identificar barreiras na interação com o cidadão, acúmulo de débitos técnicos nas classes customizadas e vulnerabilidades de segurança, gerando dados objetivos para apoiar manutenções no software público.

---

## 2. Metodologia e Normas de Referência

A avaliação segue normas técnicas de engenharia de software e modelos consolidados de medição:

1. **ISO/IEC 25010:2023 (SQuaRE)**: Modelo de qualidade de produto de software. A equipe adaptou a norma ao contexto da plataforma federal e priorizou três características:
   - **Capacidade de Interação** (*Interaction Capability*, denominação que substituiu Usabilidade na revisão 2023 da norma), com foco no cidadão que participa das consultas;
   - **Manutenibilidade** (*Maintainability*), com foco na equipe de engenharia do LAPPIS responsável pela sustentação do repositório;
   - **Segurança** (*Security*), com foco no órgão gestor governamental (Secretaria de Participação Digital / MGI) e na integridade das deliberações.
2. **ISO/IEC 25040:2024**: Modelo de processo para avaliação sistemática de produtos de software, estruturado em cinco atividades normativas: estabelecer requisitos (Fase 1), especificar a avaliação (Fase 2), projetar a avaliação (Fase 3), executar a avaliação (Fase 3/4) e concluir a avaliação (Fase 4).
3. **Goal-Question-Metric (GQM)**: Método analítico proposto por Basili, Caldiera e Rombach. Desdobra as características em 3 objetivos, 9 questões operacionais, 9 hipóteses teóricas e 12 métricas quantitativas com critérios de julgamento em quatro faixas (Insuficiente, Regular, Bom e Excelente).
4. **Practical Software Measurement (PSM / ISO/IEC/IEEE 15939:2017)**: Gestão interna do projeto por meio de categorias de informação (Calendário e Progresso, Recursos e Custos, Desempenho dos Processos), com registro de esforço semanal e cálculo automatizado de indicadores via GitHub Actions.

---

## 3. Mapa de Navegação da Documentação

A documentação está organizada em seções interligadas para facilitar a leitura por avaliadores e visitantes externos:

### Fases da Avaliação de Produto
- [Fase 1: Planejamento da Avaliação e Modelo de Qualidade](fases/1.md): Propósito da avaliação, mapeamento de stakeholders, caracterização arquitetural do software, modelo SQuaRE adaptado, matriz de priorização ponderada, escopo de auditoria e alinhamento ao ODS 16 (Meta 16.7).
- [Fase 2: Especificação da Avaliação (GQM)](fases/2.md): Objetivos de medição G1 a G3, questões operacionais, hipóteses, fichas técnicas das doze métricas quantitativas, níveis de pontuação e matriz de rastreabilidade vertical.
- [Fase 3: Plano de Avaliação](fases/3.md): Métodos de avaliação (testes de usabilidade, questionário SUS, inspeção de acessibilidade e análise estática), ambiente de teste e cronograma de coleta.
- [TCLE das Sessões com Usuários](tcle.md): Termo de Consentimento Livre e Esclarecido para as sessões de teste com participantes humanos, garantindo salvaguardas éticas e anonimização de dados.
- [Dados Brutos de Segurança](dados/seguranca/index.md): Relatórios primários de execução das ferramentas Brakeman, bundler-audit e matriz de endpoints sensíveis.

### Gestão e Governança do Projeto
- [Gestão do Projeto com Métricas PSM/CID](gestao.md): Diagnóstico do processo, necessidades N1 a N6, construtos de medição, tabela oficial de contribuição paritária (Critério AG-C5) e painel automatizado de commits, linhas de código e issues.
- [Atas de Reunião](atas/index.md): Registro histórico das reuniões semanais da equipe, pautas discutidas e decisões técnicas deliberadas.
- [Declaração de Uso de IA](uso-de-ia.md): Política de governança anti-meat-proxy, script automatizado de fiscalização de texto e registro individual de ferramentas utilizadas.

### Publicações e Apresentações
- [Artigo Científico (IEEE / LaTeX)](article/index.md): Detalhamento do manuscrito acadêmico preparado no formato IEEEtran de duas colunas, diretrizes pedagógicas e instruções de compilação.
- [Entregas e Apresentações](entregas/1.md): Slides e registros das apresentações dos pontos de controle da disciplina.

---

## 4. Repositório, Código e Releases

Todo o trabalho desenvolvido pela equipe é público e auditável:

- **Repositório Oficial no GitHub**: [FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS)
- **Quadro de Gestão (GitHub Projects 33)**: [FRANS BILAS - Brasil Participativo](https://github.com/orgs/FCTE-Qualidade-de-Software-1/projects/33/views/1)
- **Releases do Projeto**: [Histórico de Releases no GitHub](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS/releases)

---

## 5. Integrantes da Equipe Frans Bilas

A equipe é composta por seis estudantes de Engenharia de Software da Universidade de Brasília:

| Foto | Nome Completo | Matrícula | Dupla | GitHub | Contribuições no Git |
| :---: | :--- | :---: | :---: | :---: | :---: |
| <img src="https://github.com/davimesquit.png" width="40" style="border-radius: 50%;" alt="Foto de Davi Mesquita Sousa"> | Davi Mesquita Sousa | 222006650 | Dupla 3 | [@davimesquit](https://github.com/davimesquit) | [Commits](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS/commits?author=davimesquit) |
| <img src="https://github.com/beyondmagic.png" width="40" style="border-radius: 50%;" alt="Foto de João Victor da Silva Batista de Farias"> | João Victor da Silva Batista de Farias | 221022604 | Dupla 1 | [@beyondmagic](https://github.com/beyondmagic) | [Commits](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS/commits?author=beyondmagic) |
| <img src="https://github.com/JoseViniciusQueiroz.png" width="40" style="border-radius: 50%;" alt="Foto de José Vinícius Alvares Soares de Queiroz"> | José Vinícius Alvares Soares de Queiroz | 222006884 | Dupla 2 | [@JoseViniciusQueiroz](https://github.com/JoseViniciusQueiroz) | [Commits](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS/commits?author=JoseViniciusQueiroz) |
| <img src="https://github.com/luccameds.png" width="40" style="border-radius: 50%;" alt="Foto de Lucca Medeiros Silva"> | Lucca Medeiros Silva | 222031528 | Dupla 2 | [@luccameds](https://github.com/luccameds) | [Commits](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS/commits?author=luccameds) |
| <img src="https://github.com/matix0.png" width="40" style="border-radius: 50%;" alt="Foto de Mateus Vinícius Vieira"> | Mateus Vinícius Vieira | 202016963 | Dupla 1 | [@matix0](https://github.com/matix0) | [Commits](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS/commits?author=matix0) |
| <img src="https://github.com/zlimaz.png" width="40" style="border-radius: 50%;" alt="Foto de Miguel Arthur Oliveira de Lima"> | Miguel Arthur Oliveira de Lima | 211062320 | Dupla 3 | [@zlimaz](https://github.com/zlimaz) | [Commits](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS/commits?author=zlimaz) |

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 17/10/2026 | Estruturação da página inicial, tabela de integrantes e características avaliadas | [João Victor da Silva Batista de Farias](https://github.com/beyondmagic) | [Mateus Vinícius Vieira](https://github.com/matix0) |
| `1.1` | 10/11/2026 | Expansão da narrativa para leitor externo, inclusão do mapa de navegação das fases e texto alternativo (alt-text) nas imagens | [João Victor da Silva Batista de Farias](https://github.com/beyondmagic) | [Mateus Vinícius Vieira](https://github.com/matix0) |
