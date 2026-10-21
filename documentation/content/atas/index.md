---
icon: lucide/calendar-check
---

# Atas de Reunião da Equipe Frans Bilas

Esta página reúne o histórico formal das atas de reunião da equipe **Frans Bilas (Turma 01)** na disciplina **Qualidade de Software 1 (FGA0315 - 2026.2)**, ministrada pela Profa. Dra. Cristiane Soares Ramos na Universidade de Brasília (Campus UnB Gama: Faculdade de Ciências e Tecnologias em Engenharia - Brasília / FCTE).

O registro sistemático das reuniões documenta o processo de tomada de decisão técnica da equipe, a distribuição paritária do trabalho e a rastreabilidade das entregas, atendendo aos requisitos de gestão do projeto apoiados no framework **PSM (*Practical Software Measurement*)** e nas diretrizes metodológicas da disciplina.

---

## 1. Quadro Geral de Reuniões da Equipe

| Reunião | Data | Modalidade | Pauta Principal | Presença | Registro |
| :---: | :---: | :---: | :--- | :---: | :---: |
| **Ata 01** | 16/10/2026 | Síncrona (Whatsapp) | Planejamento da Entrega 1, análise de critérios, formação de duplas e governança técnica | 6/6 (100%) | [Ver Detalhes](#2-ata-da-reuniao-01-16102026) |

---

## 2. Ata da Reunião 01 (16/10/2026)

### 2.1 Identificação e Participantes

- **Data**: 16 de outubro de 2026 (sexta-feira)
- **Horário**: 16h00 às 22h40 (duração total: 6h40min)
- **Local**: Chat do Grupo do Whatsapp
- **Redator da Ata**: João Victor da Silva Batista de Farias
- **Participantes Presentes**:
  - Davi Mesquita Sousa
  - João Victor da Silva Batista de Farias
  - José Vinícius Alvares Soares de Queiroz
  - Lucca Medeiros Silva
  - Mateus Vinícius Vieira
  - Miguel Arthur Oliveira de Lima
- **Quórum**: 6 de 6 integrantes presentes (100% de participação).

---

### 2.2 Objetivos da Reunião

1. Discutir e nivelar o entendimento sobre os critérios de avaliação das Fases 1 e 2 divulgados pela Profa. Cristiane Soares Ramos, além dos critérios gerais da disciplina (AG-C1 a AG-C5).
2. Definir o plano de trabalho e as datas de congelamento para a Entrega 1, prevista para 26/10/2026.
3. Consolidar a divisão das duplas de trabalho e detalhar as atribuições individuais de cada integrante.
4. Estabelecer a governança técnica do repositório Git.

---

### 2.3 Pautas e Deliberações

#### Pauta 1: Alinhamento de Escopo e Critérios Normativos
- **Software Avaliado**: A equipe ratificou a escolha da plataforma federal [Brasil Participativo](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr), aplicação de deliberação pública desenvolvida sobre o framework Decidim (Ruby on Rails) com módulos customizados pelo LAPPIS UnB.
- **Características SQuaRE Selecionadas**: Confirmadas as três características baseadas na norma **ISO/IEC 25010:2023**:
  1. *Capacidade de Interação* (*Interaction Capability*, nomenclatura atualizada na revisão de 2023);
  2. *Manutenibilidade* (*Maintainability*);
  3. *Segurança* (*Security*).
- **Postura de Coleta em Segurança**: Ficou expressamente proibida qualquer tentativa de varredura ativa de vulnerabilidades ou testes de estresse direcionados aos servidores federais em produção. Todas as medições de segurança e manutenibilidade serão executadas por meio de análise estática do repositório público e testes em ambiente controlado local.
- **Aspectos Éticos em Usabilidade**: Ficou acordada a obrigatoriedade de aplicação do Termo de Consentimento Livre e Esclarecido (TCLE) devidamente assinado antes de quaisquer testes com usuários na Fase 3.

#### Pauta 2: Formação das Duplas de Trabalho e Divisão de Papéis
A equipe aprovou por unanimidade a estruturação paritária em três duplas especializadas, garantindo revisão cruzada entre os pares:

- **Dupla 1 (Qualidade e GQM)**: João Victor da Silva Batista de Farias e Mateus Vinícius Vieira. Foco no modelo de qualidade, critérios da Fase 1, formulação de objetivos e questões GQM da Fase 2, além do julgamento final na Fase 4.
- **Dupla 2 (GQM, Métricas e Implementação)**: José Vinícius Alvares Soares de Queiroz e Lucca Medeiros Silva. Foco na elaboração das fichas técnicas de métricas, equações matemáticas, testes empíricos de viabilidade e implementação dos dois aprimoramentos técnicos de software.
- **Dupla 3 (Gestão e Infraestrutura)**: Miguel Arthur Oliveira de Lima e Davi Mesquita Sousa. Foco nas métricas de processo PSM/CID, governança do repositório, suporte à automação da GitPage (Zensical), consolidação do artigo em LaTeX e elaboração visual dos slides.

#### Pauta 3: Subdivisão Interna das Tarefas da Fase 1
Para permitir a execução imediata e sem bloqueios, a Dupla 1 pactuou a divisão das atividades da Fase 1 entre seus dois membros:

- **João Victor da Silva Batista de Farias (Atividades Iniciais)**:
  - Contextualização geral da avaliação (Critério AG-C1);
  - Propósito da avaliação e uso pretendido (Critério 1);
  - Requisitante e mapeamento de partes interessadas / stakeholders (Critério 2);
  - Tipo de produto e descrição estruturada da arquitetura com diagrama Mermaid (Critério 3).
- **Mateus Vinícius Vieira (Atividades Subsequentes)**:
  - Modelo de qualidade SQuaRE e diagrama hierárquico adaptado (Critério 4);
  - Matriz de seleção e priorização formal das características (Critério 5);
  - Delimitação de escopo, profundidade e objetos de avaliação (Critério 6);
  - Alinhamento aos Objetivos de Desenvolvimento Sustentável (ODS 16, Meta 16.7) e indicadores (Critério 7).

#### Pauta 4: Padrões de Artefatos, LaTeX e Política Anti-Meat-Proxy

Responsável: João Victor da Silva Batista de Farias (Dupla 1)

- **Formato do Artigo Científico**: Aprovada a utilização do modelo **IEEEtran** em modo *journal* (duas colunas), respeitando o limite rigoroso de 15 páginas da disciplina. O texto possui caráter estritamente didático e avaliativo para a disciplina, sem exigência de submissão externa.
- **Documentação GitPage**: Manutenção do gerador estático Zensical em `documentation/`, estruturado com páginas dedicadas por fase, navegação clara e controle de versões no rodapé.
- **Apresentação do Ponto de Controle 1 (PC1)**: Estruturação dos slides de apresentação em `documentation/content/entregas/1.md` por meio do plugin `zensical-slides`, priorizando tópicos concisos de fala rápida e notas explicativas em comentários HTML.
- **Governança Anti-Meat-Proxy**: A equipe rejeitou veementemente o uso irresponsável de LLMs sem curadoria crítica. Foi decidida a criação imediata de:
  - Um script linter Python (`scripts/check_humanizer.py`) baseado na skill `humanizer`, que bloqueia vocabulário inflado, clichês e construções prolixas;
  - Um hook de pré-commit do Git (`.githooks/pre-commit`) para execução compulsória do linter antes de cada commit;
  - A página `documentation/content/uso-de-ia.md` contendo a declaração de uso e os procedimentos individuais de revisão humana.

---

## 3. Modelo Padronizado para Novas Atas

Para preservar a rastreabilidade e uniformidade da documentação da equipe, todas as atas subsequentes devem adotar a seguinte estrutura:

```markdown
### Ata da Reunião XX (DD/MM/AAAA)

#### Identificação e Participantes
- **Data e Horário**: DD de mês de AAAA, das HHhMM às HHhMM
- **Modalidade e Local**: [Presencial / Sala Virtual Whatsapp / Teams]
- **Redator**: [Nome do Integrante]
- **Participantes Presentes**: [Lista nominal com quórum verificado]

#### Objetivos
1. [Objetivo principal da reunião]
2. [Segundo objetivo da reunião]

#### Pautas e Discussões
- **Pauta 1**: [Detalhamento objetivo das discussões e decisões técnicas tomadas]
- **Pauta 2**: [Detalhamento objetivo das discussões e decisões técnicas tomadas]

#### Encaminhamentos
| Ação | Responsável | Prazo |
| :--- | :--- | :---: |
| [Descrição da tarefa] | [Nome do integrante] | [DD/MM/AAAA] |
```

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 21/10/2026 | Criação da página de atas, registro detalhado da Reunião 01 de planejamento (16/10/2026) e template padronizado | [João Victor da Silva Batista de Farias](https://github.com/beyondmagic) | [Mateus Vinícius Vieira](https://github.com/matix0) |

