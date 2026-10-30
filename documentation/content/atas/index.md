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
| **Ata 02** | 29/10/2026 | Síncrona (Google Meet) | Planning do Sprint 3: Fase 3, Ponto de Controle 2 e manutenção das duplas | 5/6 (83%) | [Ver Detalhes](#3-ata-da-reuniao-02-29102026) |

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

## 3. Ata da Reunião 02 (29/10/2026)

### 3.1 Identificação e Participantes

- **Data**: 29 de outubro de 2026 (quinta-feira)
- **Horário**: 20h04 às 20h23 (duração aproximada: 19 min)
- **Local**: Google Meet, com transcrição automática
- **Redator da Ata**: Mateus Vinícius Vieira
- **Facilitador**: Mateus Vinícius Vieira, com o roteiro da planning enviado ao grupo antes da reunião
- **Participantes Presentes**:
  - Davi Mesquita Sousa
  - João Victor da Silva Batista de Farias
  - José Vinícius Alvares Soares de Queiroz
  - Mateus Vinícius Vieira
  - Miguel Arthur Oliveira de Lima
- **Ausente**: Lucca Medeiros Silva tentou entrar na chamada depois do encerramento.
- **Quórum**: 5 de 6 integrantes presentes (83%).

---

### 3.2 Objetivos da Reunião

1. Apresentar o planejamento do Sprint 3, voltado à Fase 3 e ao Ponto de Controle 2 (PC2).
2. Definir o formato de trabalho das atividades do Sprint 3.
3. Fixar o prazo de encerramento do sprint.

---

### 3.3 Pautas e Deliberações

#### Pauta 1: Critérios das Fases 3 e 4

- José Vinícius enviou no grupo os prints dos critérios gerais das Fases 3 e 4.
- Três integrantes ainda não tinham respondido o formulário avaliativo da disciplina, que fecha em 30/10: Davi, Mateus e Miguel.

#### Pauta 2: Foco e prazo do Sprint 3

- O Sprint 3 começou no papel em 27/10, mas a planning só aconteceu em 29/10.
- O foco é deixar a Fase 3 estruturada para o PC2. A equipe vai mostrar à professora o início da Fase 3, as Fases 1 e 2 revisadas e a gestão PSM atualizada.
- O calendário sorteia 5 equipes para 04/11 e 5 para 09/11. A equipe se prepara para 04/11, para ganhar tempo para a Fase 4 antes da Entrega 2 (18/11).
- O escopo segue os blocos 2 e 3 do roteiro e do GitHub Projects: critérios F3-C1, F3-C2 e F3-C8, adequação da gestão ao PSM e correções do PC1. Entram o plano de avaliação, as instruções de coleta, o ambiente de avaliação, o cronograma de coleta alinhado à Fase 4 e o TCLE, cuja base já está no repositório.
- As atividades do Sprint 4 ainda não foram definidas. Dependem do que sobrar do Sprint 3.

#### Pauta 3: Trabalho em duplas e carga

- José Vinícius contou 14 atividades no bloco 3 do roteiro.
- O grupo decidiu manter o trabalho em duplas, para que um revise o outro e assuma a tarefa se o colega travar.
- As duplas continuam as da Ata 01: Dupla 1 (João e Mateus), Dupla 2 (José Vinícius e Lucca) e Dupla 3 (Davi e Miguel). Na Dupla 1, João fica com mais revisão neste sprint, já que fez a maior parte na Entrega 1.
- José Vinícius apontou o desequilíbrio da distribuição atual no Projects: seis atividades com a Dupla 2, quatro com a Dupla 3 e uma com a Dupla 1.
- Mateus vai revisar as horas estimadas de cada issue e redistribuir as tarefas para que as três duplas fiquem com carga parecida. A estimativa falada na reunião foi de 15 a 20 horas para o sprint inteiro. O quadro soma hoje 39 horas estimadas nas issues abertas do Sprint 3, então a revisão deve conciliar os dois números.

#### Pauta 4: Artigo

- O artigo tem as Fases 1 e 2. As Fases 3 e 4 entram depois de concluídas.

#### Pautas do roteiro que ficaram para depois

Os pontos em validação da [Gestão](../gestao.md#10-pontos-em-validacao) não foram votados: critério de esforço por integrante (N3), faixa de precisão de estimativa (N4) e responsáveis pela coleta. Também ficaram em aberto quem apresenta cada parte do PC2 e a diferença entre a release E2 em 17/11 (Gestão) e a Entrega 2 em 18/11 (calendário).

---

### 3.4 Decisões

| Decisão | Registro para a medição |
| :--- | :--- |
| As atividades do Sprint 3 são feitas em duplas, com revisão mútua | Divisão em uma issue por pessoa ainda pendente (regra 1 da coleta) |
| O Sprint 3 termina em 04/11 | Fim do período de N1 a N6 no Sprint 3 |
| A equipe se prepara para apresentar o PC2 em 04/11 | Vale mesmo se o sorteio cair em 09/11 |

---

### 3.5 Encaminhamentos

| Ação | Responsável | Prazo |
| :--- | :--- | :---: |
| Revisar as horas estimadas e redistribuir as issues do Sprint 3 entre as duplas | Mateus Vinícius Vieira | Antes do início das tarefas |
| Responder o formulário avaliativo da disciplina | Davi, Mateus e Miguel | 30/10/2026 |
| Executar as atividades da Fase 3 do Sprint 3 | Todas as duplas | 04/11/2026 |
| Votar os pontos em validação da Gestão e definir quem apresenta cada parte do PC2 | Equipe | Próxima reunião |
| Atualizar o artigo com as Fases 3 e 4 | Equipe | 18/11/2026 |

---

### 3.6 Redistribuição de 30/10

O primeiro encaminhamento foi concluído em 30/10. Mateus redistribuiu o Sprint 3 no GitHub Projects por pessoa, com as horas revistas para considerar o uso de IA nas tarefas de escrita. O sprint passou de 13 issues e 39 h para 18 issues e 31 h, cada uma com um responsável só.

| Integrante | Issues | Horas estimadas |
| :--- | :--- | :---: |
| Mateus Vinícius Vieira | #59 e #60 (revisão das Fases 1 e 2), #69 (correções do PC1), #70 (slides do PC2) | 8 |
| Miguel Arthur Oliveira de Lima | #67 (recrutamento), #68 (revisão do plano), #44 (pontos em validação), #43 (PR obrigatório) | 5,5 |
| José Vinícius Alvares Soares de Queiroz | #62 (Plano de Avaliação), #66 (análise estática de segurança), #65 (cronograma da coleta) | 5 |
| João Victor da Silva Batista de Farias | #90 (coleta piloto de usabilidade), #45 (campos do TCLE) | 4,5 |
| Lucca Medeiros Silva | #63 (passo a passo das medidas), #89 (análise estática de manutenibilidade) | 4 |
| Davi Mesquita Sousa | #64 (ambiente de avaliação), #46 (medição do Sprint 3) | 4 |

Outras mudanças:

- A #66 e a #67 foram divididas: a parte de manutenibilidade virou a #89 e a coleta piloto virou a #90.
- A #59 e a #60 saíram do Sprint 2 e passaram a cobrir as Fases 1 e 2.
- Revisão de fases, correções do PC1 e slides ficam com Mateus. Nas apresentações (#70 e #84), Mateus monta os slides e a equipe apresenta.
- Os 8 h de Mateus passam do teto de 25% por pessoa proposto para N3. A decisão foi dele, como líder do grupo.

---

## 4. Modelo Padronizado para Novas Atas

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
| `1.1` | 30/10/2026 | Registro da Reunião 02, planning do Sprint 3 (29/10/2026), e da redistribuição de tarefas de 30/10 | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |

