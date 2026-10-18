---
icon: lucide/microscope
---

# Artigo Científico

Esta página apresenta as diretrizes, a estrutura e o andamento do artigo científico elaborado pela equipe **Frans Bilas (Turma 01)** na disciplina **Qualidade de Software 1 (FGA0315 - 2026.2)**, ministrada pela Profa. Dra. Cristiane Soares Ramos na Universidade de Brasília (Campus UnB Gama: Faculdade de Ciências e Tecnologias em Engenharia - Brasília / FCTE).

---

## 1. Contexto e Natureza da Publicação

O artigo científico constitui o relatório técnico final consolidado da disciplina. A produção foi concebida como instrumento didático e avaliativo de comunicação científica para exercitar o rigor metodológico na avaliação de software:

- **Finalidade Acadêmica**: O trabalho é produzido estritamente para a avaliação contínua da disciplina no semestre 2026.2. O formato de artigo foi determinado pela professora para exercitar síntese, precisão técnica e escrita formal.
- **Destinação**: Não há compromisso de submissão externa compulsória para periódicos ou conferências da IEEE.
- **Transparência**: O texto é acompanhado da disponibilização integral de dados brutos, scripts de cálculo, modelos GQM e registros de gestão em nosso repositório público.

---

## 2. Padrão Adotado (IEEE / IEEEtran)

A especificação do projeto permitia a escolha entre três modelos clássicos de computação: SBC, ACM ou IEEE. A equipe optou pelo padrão **IEEE (classe `IEEEtran` em modo `journal`)**:

- **Justificativa da Escolha**: O formato IEEE organiza o conteúdo em duas colunas densas, permitindo acomodar equações matemáticas, tabelas comparativas de métricas e gráficos analíticos de forma compacta e padronizada na engenharia de software.
- **Localização dos Fontes**: O código-fonte em LaTeX está versionado no repositório em [`documentation/content/article/source/main.tex`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANS_BILAS/tree/main/documentation/content/article/source/main.tex), acompanhado do modelo original de referência `ieee_bare_jrnl.tex`.
- **Ambiente Colaborativo**: A redação em equipe é sincronizada via [projeto compartilhado no Overleaf](https://www.overleaf.com/project/6ac3b29fe9cf3708a6a46735) e versionada via Git.

---

## 3. Restrições e Requisitos da Disciplina

Conforme a especificação do trabalho final, o artigo deve respeitar as seguintes regras formais:

1. **Limite de Extensão**: Máximo de **15 páginas** (incluindo texto principal e referências bibliográficas). A Tabela de Contribuição dos integrantes entra como apêndice ao final, fora dessa contagem.
2. **Autonomia do Texto (Autocontido)**: O artigo deve fornecer todas as informações necessárias para que o leitor compreenda o problema, os objetivos, a metodologia e os resultados sem depender da leitura prévia de anexos externos.
3. **Fundamentação Teórica Rigorosa**:
   - Normas da família SQuaRE: **ISO/IEC 25010:2023** (com atenção ao termo atualizado *Capacidade de Interação*) e **ISO/IEC 25000:2005**.
   - Métodos de Medição: **Goal-Question-Metric (GQM)** e **Practical Software Measurement (PSM / ISO/IEC 15939)**.
   - Literatura clássica de qualidade: Galin (2018) e Naik & Tripathy (2008).
4. **Padronização Visual e Rastreabilidade (Critério AG-C2)**:
   - Toda figura e tabela deve conter numeração sequencial, legenda descritiva e indicação explícita da fonte.
   - Citações bibliográficas gerenciadas via BibTeX.
   - Menção explícita ao repositório público e à tag da release correspondente (E1 para o artigo v1; E2 para o artigo final).

---

## 4. Estrutura das Seções do Artigo

O manuscrito segue a progressão lógica das quatro fases de avaliação de produto:

| Seção do Artigo | Conteúdo Principal | Fase Correspondente |
| :--- | :--- | :--- |
| **Resumo e Abstract** | Síntese do objeto, método GQM, características SQuaRE e conclusões | Transversal |
| **1. Introdução** | Relevância democrática do Brasil Participativo, histórico LAPPIS e motivação | AG-C1 |
| **2. Planejamento da Avaliação** | Propósito (C1), stakeholders (C2), arquitetura (C3), modelo SQuaRE (C4), priorização (C5), escopo (C6) e ODS (C7) | Fase 1 |
| **3. Definição de Métricas (GQM)** | Grafo GQM, fichas técnicas de métricas, critérios de interpretação e hipóteses analíticas | Fase 2 |
| **4. Plano de Avaliação e Coleta** | Métodos de medição, ferramentas de análise estática, ambiente de teste e protocolo de coleta | Fase 3 |
| **5. Análise dos Resultados** | Apresentação dos dados, correlação entre características e as duas melhorias técnicas implementadas | Fase 4 |
| **6. Julgamento e Recomendações** | Avaliação conclusiva contra os critérios de sucesso e recomendações para o governo | Fase 4 |
| **Referências Bibliográficas** | Fontes normativas e teóricas gerenciadas em BibTeX | AG-C2 |
| **Apêndices** | Tabela de Contribuição (esforço somando 100%) e Declaração de Uso de IA | AG-C3 e AG-C5 |

---

## 5. Como Compilar Localmente

Para compilar o artigo localmente e gerar o PDF com o compilador TeX instalado:

```bash
cd documentation/content/article/source
pdflatex -interaction=nonstopmode main.tex
```

Os arquivos temporários (`*.aux`, `*.log`, `*.out`) são ignorados pelo Git e podem ser removidos após a compilação.

O artigo científico constitui o relatório técnico final consolidado da disciplina. A produção foi concebida como instrumento didático e avaliativo de comunicação científica para exercitar o rigor metodológico na avaliação de software:

- **Finalidade Acadêmica**: O trabalho é produzido estritamente para a avaliação contínua da disciplina no semestre 2026.2. O formato de artigo foi determinado pela professora para exercitar síntese, precisão técnica e escrita formal.
- **Destinação**: Não há compromisso de submissão externa compulsória para periódicos ou conferências da IEEE. Qualquer eventual submissão futura a eventos científicos dependerá de decisão posterior conjunta da equipe e dos professores orientadores.
- **Transparência**: O texto é acompanhado da disponibilização integral de dados brutos, scripts de cálculo, modelos GQM e registros de gestão em nosso repositório público.


