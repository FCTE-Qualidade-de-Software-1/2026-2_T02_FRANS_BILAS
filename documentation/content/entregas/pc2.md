# Ponto de Controle 2: Plano de Avaliação do Brasil Participativo

**Equipe Frans Bilas (Turma 01)**  
Disciplina: Qualidade de Software 1 (FGA0315, semestre 2026.2)  
Professora: Dra. Cristiane Soares Ramos  
Faculdade de Ciências e Tecnologias em Engenharia (FCTE, Campus UnB Gama)

---

## 1. Desde o PC1: Gestão Corrigida

<p class="apresentador">Mateus Vinícius Vieira</p>

<!--
NOTA PARA APRESENTAÇÃO (Mateus):
- Abrir em 30 segundos: gestão corrigida, Fases 1 e 2 revisadas, Fase 3 iniciada com os primeiros dados.
- A correção pedida no PC1 foi a gestão. A versão 1.0 tinha as três categorias do PSM, mas não o modelo de informação nem o processo de medição. A Tabela 2 da página de Gestão liga cada falha à correção.
- Sprint 3: planning em 29/10 (Ata 02) e redistribuição por pessoa em 30/10. O slide 2 traz a medição.
- Premissa 3 da especificação: medições, interpretação e decisões de gestão registradas.
-->

- **Necessidades de informação**: N1 a N6, cada uma nascida de um problema, risco ou falta de informação
- **Indicadores**: cinco da tabela ICM do guia CID e uma adaptação declarada (revisão por pares)
- **Construto completo** e **coleta no GitHub Projects 33**, com esforço estimado e real por issue
- **Série medida**: começa no Sprint 3 e segue até a release da Entrega 2

---

## 2. Gestão: Medição do Sprint 3

<p class="apresentador">Davi Mesquita Sousa</p>

<!--
NOTA PARA APRESENTAÇÃO (Davi):
- Primeira medição da série, feita em 04/11 com o script scripts/psm_medicao.py; dados brutos em dados/gestao/sprint-3.json. Detalhes na Seção 12 da Gestão.
- N1: o critério de Pronto exige PR revisado por outra dupla. Só a #62 passou; 6 de 17 issues fecharam.
- N2: 8 de 40 itens concluídos com 32% do prazo até a release de 21/11 já passado; o escopo cresceu de 33 para 40.
- N3, N4 e N5 não puderam ser calculados: ninguém preencheu horas reais nem datas. Isso é o resultado da avaliação da medição, e a decisão vai para a Ata 03.
- A medição também achou uma falha no painel automático, que mostrava valores fixos (issue #106).
-->

| Indicador | Sprint 3 | Decisão |
| :--- | :--- | :--- |
| N1 Comprometido × concluído | 1 de 17 no critério de Pronto (5,9%) | Redistribuição dos Sprints 4 a 6, uma issue por pessoa |
| N2 Burndown da E2 | 32 de 40 abertos; variância de 12 p.p. | Cortar a #80 se passar de 10% em 11/11 |
| N3, N4 e N5 | Sem dado: horas reais e datas em branco | Campos obrigatórios ao fechar a issue |
| N6 Revisão por pares | 11,1% das integrações | PR obrigatório na `main` (#43) |

Fonte: [Gestão, Seção 12](../gestao.md#12-medicao-do-sprint-3).

---

## 3. Fases 1 e 2 Revisadas

<p class="apresentador">Mateus Vinícius Vieira</p>

<!--
NOTA PARA APRESENTAÇÃO (Mateus):
- Antes da revisão, nenhuma das 12 tabelas de conteúdo e 3 figuras tinha legenda numerada nem fonte, e as páginas não tinham referências.
- Algumas métricas tinham até três nomes diferentes dentro da Fase 2. Agora cada uma tem um nome só, o mesmo usado na Fase 3.
- Termos sem métrica correspondente (Content Security Policy, acoplamento, planejamento de infraestrutura) saíram da Fase 1.
- Fórmulas, níveis e critérios não mudaram: os pontos de dúvida estão no slide 8.
-->

- **Legendas e fontes (F2-C8, AG-C2)**: 12 tabelas e 3 figuras numeradas, com fonte e citadas no texto
- **Referências**: seção nova nas duas páginas (normas ISO/IEC, GQM, SUS, McCabe, WCAG e eMAG)
- **Terminologia (F2-C12)**: um nome por métrica, siglas definidas no primeiro uso, termos sem métrica retirados

---

## 4. Fase 3: Método, Plano e Ambiente

<p class="apresentador">José Vinícius Alvares Soares de Queiroz</p>

<!--
NOTA PARA APRESENTAÇÃO (José):
- Critérios F3-C1 (método e instruções repetíveis) e F3-C2 (recursos e ambiente).
- Mostrar a tabela da Seção 2 da Fase 3 no site: cada métrica tem questão, método, recursos e saída registrada.
- Atualizar no dia a situação do passo a passo (#63, Lucca) e do ambiente (#64, Davi). Em 04/11 as duas seções ainda estavam em elaboração. Não citar versões, hardware ou passos que não estejam escritos.
- F3-C7: a Fase 3 está no menu da GitPage, com links para a Fase 2, o TCLE e os dados.
-->

- **Quatro métodos**: teste com usuários (M1.1 a M1.3), questionário SUS (M1.5), inspeção automatizada de acessibilidade (M1.4) e análise estática (M2.x e M3.x)
- **Decisões**: nenhum teste contra a produção, versão fixa no commit `176b046` e coleta única no Sprint 4
- **Passo a passo de cada medida** (#63) e **ambiente com massa de dados e perfil dos participantes** (#64): em elaboração
- Detalhes na [Fase 3](../fases/3.md)

---

## 5. Fase 3: Cronograma e Consistência com a Fase 2

<p class="apresentador">José Vinícius Alvares Soares de Queiroz</p>

<!--
NOTA PARA APRESENTAÇÃO (José):
- Critérios F3-C3 (cronograma alinhado à Fase 4) e F3-C8 (consistência entre as Fases 2 e 3).
- A análise estática não depende de participantes e começa primeiro.
- As sessões dependem de três itens do Sprint 3: TCLE completo (#45), cópia local (#64) e participantes (#67). Com menos de cinco sessões até 10/11, a limitação entra no julgamento da Fase 4.
- A tabela que confere o plano contra os níveis e critérios da Fase 2 (#68) ainda está em elaboração: dizer isso, sem prometer o que não está pronto.
-->

| Data | Atividade | Métricas |
| :---: | :--- | :--- |
| 03/11 | Análise estática de Segurança | M3.1 a M3.3 (concluída) |
| 05/11 a 06/11 | Análise estática de Manutenibilidade | M2.1 a M2.4 |
| 06/11 a 10/11 | Inspeção de acessibilidade e sessões com usuários | M1.1 a M1.5 |
| 10/11 a 11/11 | Cálculo e dados brutos no repositório | Todas |

Fonte: cronograma da coleta (issue #65), que entra na Seção 5 da Fase 3.

- **Consistência**: as 12 métricas da Fase 2 têm método e recurso no plano; a conferência contra os níveis e critérios (#68) está em elaboração

---

## 6. Primeiros Dados: Segurança

<p class="apresentador">José Vinícius Alvares Soares de Queiroz</p>

<!--
NOTA PARA APRESENTAÇÃO (José):
- Coleta em 03/11 no commit 176b046, com Brakeman 8.1.0, bundler-audit 0.9.3 e o script m33_endpoints.py. Os arquivos brutos estão no repositório (premissa 5).
- M3.1: 2 alertas de confiança alta (versões de Ruby e Rails sem suporte) e 8 de média. Sem os dois de alta, a DVC seria 16, ainda Insuficiente.
- M3.2: 198 avisos em 51 gems; um crítico na graphql 1.12.24, corrigido na 1.12.25.
- M3.3: das 13 ações sem verificação, 8 vêm do código do governo. Os achados vêm da leitura do código, sem teste em execução.
- O julgamento do G3 fica para a Fase 4.
-->

| Métrica | Valor medido | Nível (Fase 2) |
| :--- | :--- | :---: |
| **M3.1** Densidade de Vulnerabilidades de Código (DVC) | 22 (2 alertas de confiança alta, 8 de média) | Insuficiente |
| **M3.2** Dependências Vulneráveis (CDV) | 156 CVEs em 51 gems | Insuficiente |
| **M3.3** Proteção de Endpoints Sensíveis (TPE) | 136 de 149 ações: 91,3% | Regular |

Fonte: [Dados da Coleta: Segurança](../dados/seguranca/index.md).

---

## 7. Melhoria Técnica: Candidatos

<p class="apresentador">Lucca Medeiros Silva</p>

<!--
NOTA PARA APRESENTAÇÃO (Lucca):
- A especificação exige executar pelo menos uma ação de melhoria, justificada pelas evidências da avaliação.
- Os candidatos vêm da coleta de Segurança. A escolha final cabe à equipe, junto com os resultados de Manutenibilidade (#89).
- O PC2 é em 16/11 ou 18/11, depois do Sprint 4: trocar este slide pela melhoria escolhida e pelo que já foi feito (#73).
-->

- **Selos de propostas**: quatro ações sem verificação de permissão, com rotas fora do escopo de administração (M3.3); esforço baixo
- **Relatórios**: a checagem de administrador não interrompe a ação (M3.3); esforço baixo
- **Dependências**: atualizar gems na mesma série, começando pela `graphql` 1.12.24 → 1.12.25 (M3.2); exige rodar a suíte de testes
- **Primeira melhoria (#73)**: implementada no Sprint 4 e justificada pelos dados

---

## 8. Riscos e Perguntas para a Professora

<p class="apresentador">Mateus Vinícius Vieira</p>

<!--
NOTA PARA APRESENTAÇÃO (Mateus):
- Os riscos vêm das dependências do cronograma da Fase 3.
- As perguntas saíram da revisão da Fase 2 e afetam o julgamento da Fase 4. Pedir orientação antes de mudar a especificação.
- Registrar as respostas na próxima ata.
-->

- **Riscos**: cópia local e recrutamento atrasarem as sessões; quadro do Projects sem horas reais
- **Perguntas**:
  - M3.1 soma alertas com peso pela confiança do Brakeman. Chamá-la de "densidade" é aceitável, ou ela deve ser dividida pelo tamanho do código?
  - M3.3 mede autorização. Ela fica melhor em Autenticidade ou em Confidencialidade e Integridade?
  - Coleta única, sem piloto e sem nova medição depois das melhorias: atende ao que se espera da Fase 4?

---

## A1. Apêndice: Sessões com Usuários

<p class="apresentador">João Victor da Silva Batista de Farias</p>

<!--
NOTA PARA APRESENTAÇÃO (João):
- Usar só se a professora perguntar pelas sessões.
- Atualizar com a situação do dia: campos do TCLE (#45), participantes recrutados (#67) e datas marcadas.
- Premissas 5 e 6: sessão só com TCLE assinado, gravação com consentimento, termo guardado separado dos dados.
-->

- **TCLE** ([página](../tcle.md)): campos preenchidos e validados (duração de 20 a 30 min, formato híbrido, áudio opcional e guarda institucional privada) (#45)
- **Recrutamento** (#67): meta de pelo menos cinco participantes
- **Coleta** (#90): sessões entre 06/11 e 10/11, com TCLE assinado, na cópia local

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 04/11/2026 | Slides do Ponto de Controle 2 com notas de apresentação | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `1.1` | 04/11/2026 | Sete slides principais e dois de apêndice, slide de melhoria técnica e critérios da Fase 3 nas notas | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `1.2` | 04/11/2026 | Slide da medição do Sprint 3 (N1 a N6) no lugar do apêndice do quadro | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `1.3` | 04/11/2026 | Datas do cronograma versão 2 (PC2 em 16/11 ou 18/11) e N2 recalculado para a release de 21/11 | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
| `1.4` | 10/11/2026 | Atualização do status dos campos do TCLE na nota de apresentação (#45) | [João Victor da Silva Batista de Farias](https://github.com/beyondmagic) | [Mateus Vinícius Vieira](https://github.com/matix0) |
