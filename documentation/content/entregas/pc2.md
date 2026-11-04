---
icon: lucide/flag
---

# Ponto de Controle 2: Plano de Avaliação do Brasil Participativo

**Equipe Frans Bilas (Turma 01)**  
Disciplina: Qualidade de Software 1 (FGA0315, semestre 2026.2)  
Professora: Dra. Cristiane Soares Ramos  
Faculdade de Ciências e Tecnologias em Engenharia (FCTE, Campus UnB Gama)

---

## 1. O que mudou desde o PC1

<p class="apresentador">Mateus Vinícius Vieira</p>

<!--
NOTA PARA APRESENTAÇÃO (Mateus):
- Abrir em 30 segundos com a agenda.
- O Sprint 3 foi de 27/10 a 04/11; a planning aconteceu em 29/10 (Ata 02).
- Três blocos: gestão corrigida, Fases 1 e 2 revisadas, Fase 3 iniciada com os primeiros dados.
-->

- **Gestão**: correção pedida no PC1, com a medição adequada ao PSM/CID
- **Fases 1 e 2**: revisão de português, terminologia, legendas, fontes e referências
- **Fase 3**: plano de avaliação, cronograma da coleta e primeira coleta (Segurança)
- **Próximos passos**: coleta do Sprint 4 e perguntas para a professora

---

## 2. Correções do PC1: Gestão v1.0 → v2.0

<p class="apresentador">Mateus Vinícius Vieira</p>

<!--
NOTA PARA APRESENTAÇÃO (Mateus):
- A versão 1.0 tinha as três categorias do PSM, mas não o modelo de informação nem o processo de medição.
- A tabela de diagnóstico da página de Gestão mostra cada elemento que estava em Falta ou Parcial e onde a 2.0 corrigiu.
- Detalhe na seção 1.1 da página de Gestão.
-->

- **Necessidades de informação**: N1 a N6, cada uma nascida de um problema, risco ou falta de informação
- **Indicadores**: cinco da tabela ICM do guia CID e uma adaptação declarada (revisão por pares)
- **Construto completo**: entidade, medidas, função, modelo de análise e critério de decisão
- **Coleta no GitHub Projects 33**: status, sprint, esforço estimado e real, início e conclusão
- **Série medida**: começa no Sprint 3 e segue até a release da Entrega 2

---

## 3. Gestão em execução: Sprint 3

<p class="apresentador">Miguel Arthur Oliveira de Lima</p>

<!--
NOTA PARA APRESENTAÇÃO (Miguel):
- Redistribuição de 30/10: uma issue por pessoa, horas revistas considerando o uso de IA na escrita.
- Linha de base de N6 (26/10): 0 de 42 integrações revisadas.
- Ser honesto sobre o quadro: em 04/11 ele ainda mostrava quase tudo em Backlog, embora já houvesse trabalho em branches. A primeira medição (issue #46) depende de atualizar status, datas e horas reais.
- Exigir PR na main (#43) ainda está pendente.
-->

- **Planning em 29/10** ([Ata 02](../atas/index.md)) e redistribuição por pessoa em 30/10
- **Quadro em 04/11**: 19 itens no Sprint 3, 35 h estimadas, 2 concluídos (#41 e #42)
- **Revisão por pares (N6)**: linha de base de 0% em 26/10; trabalho do Sprint 3 entra por PR
- **Pendências de processo**: status e horas reais no quadro, PR obrigatório na `main` (#43) e primeira medição de N1 a N6 (#46)

---

## 4. Fases 1 e 2 revisadas

<p class="apresentador">Mateus Vinícius Vieira</p>

<!--
NOTA PARA APRESENTAÇÃO (Mateus):
- Antes da revisão, nenhuma das 12 tabelas de conteúdo e 3 figuras tinha legenda numerada nem fonte.
- As páginas não tinham seção de referências.
- Algumas métricas tinham até três nomes diferentes dentro da Fase 2. Agora cada uma tem um nome só, o mesmo usado na Fase 3.
- Fórmulas, níveis e critérios não foram alterados: os pontos de dúvida estão no último slide.
-->

- **Legendas e fontes (AG-C2)**: 12 tabelas e 3 figuras numeradas, cada uma com fonte
- **Referências**: seção nova nas duas páginas, com normas ISO/IEC, GQM, SUS, McCabe, WCAG e eMAG
- **Terminologia (F2-C12)**: um nome por métrica, "Proteção contra Erros do Usuário", siglas definidas no primeiro uso
- **Português (F2-C8)**: erros de digitação, registro informal e termos em inglês sem itálico

---

## 5. Fase 3: Método de Avaliação

<p class="apresentador">José Vinícius Alvares Soares de Queiroz</p>

<!--
NOTA PARA APRESENTAÇÃO (José):
- Quatro métodos, escolhidos pela origem dos dados de cada métrica.
- Três decisões valem para todos: nada contra a produção, commit fixo e coleta única.
- A decisão de coleta única precisa estar registrada em ata antes da apresentação.
-->

- **Teste com usuários**: M1.1, M1.2 e M1.3, numa cópia local da plataforma
- **Questionário SUS**: M1.5, na mesma sessão
- **Inspeção automatizada de acessibilidade**: M1.4, com axe-core e Lighthouse
- **Análise estática**: M2.1 a M2.4 e M3.1 a M3.3, no clone do `decidim-govbr`
- **Decisões**: nenhum teste contra a produção, versão fixa no commit `176b046` e coleta única no Sprint 4

---

## 6. Fase 3: Plano por Métrica

<p class="apresentador">José Vinícius Alvares Soares de Queiroz</p>

<!--
NOTA PARA APRESENTAÇÃO (José):
- Mostrar a tabela da Seção 2 da Fase 3 no site.
- Cada métrica tem questão, método, recursos e a saída registrada no repositório.
- Os responsáveis pela coleta serão confirmados na distribuição do Sprint 4.
-->

- **12 métricas da Fase 2**, cada uma com questão, método, recursos e saída registrada
- **Sessões com usuários**: TCLE assinado antes, login de teste e quatro tarefas (entrar, encontrar um processo, enviar e apoiar uma proposta)
- **Análise estática**: cada execução guarda data, commit e versão da ferramenta junto da saída bruta
- Detalhes na [Fase 3](../fases/3.md)

---

## 7. Fase 3: Passo a Passo e Ambiente

<p class="apresentador">Lucca Medeiros Silva e Davi Mesquita Sousa</p>

<!--
NOTA PARA APRESENTAÇÃO (Lucca e Davi):
- Atualizar este slide com o que estiver pronto no dia. Em 04/11, as duas seções ainda estavam "Em elaboração" no site.
- Não citar versões, hardware ou passos que ainda não estejam escritos na Fase 3.
-->

- **Instruções para obter cada medida** (#63): passo a passo para outra pessoa repetir a coleta
- **Ambiente de avaliação** (#64): cópia local, versões, massa de dados e perfil dos participantes
- **Situação em 04/11**: as duas seções ainda em elaboração; a cópia local é pré-requisito das sessões e da inspeção de acessibilidade

---

## 8. Fase 3: Cronograma da Coleta

<p class="apresentador">José Vinícius Alvares Soares de Queiroz</p>

<!--
NOTA PARA APRESENTAÇÃO (José):
- A análise estática não depende de participantes e começa primeiro.
- As sessões dependem de três itens do Sprint 3: TCLE completo (#45), cópia local (#64) e participantes (#67).
- Com menos de cinco sessões até 10/11, a limitação entra no julgamento da Fase 4.
-->

| Data | Atividade | Métricas |
| :---: | :--- | :--- |
| 03/11 | Análise estática de Segurança | M3.1 a M3.3 (concluída) |
| 05/11 a 06/11 | Análise estática de Manutenibilidade | M2.1 a M2.4 |
| 06/11 | Inspeção de acessibilidade | M1.4 |
| 06/11 a 10/11 | Sessões com usuários (meta de cinco) | M1.1, M1.2, M1.3, M1.5 |
| 10/11 a 11/11 | Cálculo e dados brutos no repositório | Todas |

Fonte: Fase 3, Seção 5.

---

## 9. Primeiros Dados: Segurança

<p class="apresentador">José Vinícius Alvares Soares de Queiroz</p>

<!--
NOTA PARA APRESENTAÇÃO (José):
- Coleta em 03/11 no commit 176b046, com Brakeman 8.1.0, bundler-audit 0.9.3 e o script m33_endpoints.py.
- M3.1: 2 alertas de confiança alta (versões de Ruby e Rails sem suporte) e 8 de média. Sem os dois de alta, a DVC seria 16, ainda Insuficiente.
- M3.2: 198 avisos em 51 gems; um crítico na graphql 1.12.24, corrigido na 1.12.25.
- M3.3: das 13 ações sem verificação, 8 vêm do código do governo. Achados vêm da leitura do código, sem teste em execução.
- O julgamento do G3 fica para a Fase 4.
-->

| Métrica | Valor medido | Nível (Fase 2) |
| :--- | :--- | :---: |
| **M3.1** Densidade de Vulnerabilidades de Código (DVC) | 22 (2 alertas de confiança alta, 8 de média) | Insuficiente |
| **M3.2** Dependências Vulneráveis (CDV) | 156 CVEs em 51 gems | Insuficiente |
| **M3.3** Proteção de Endpoints Sensíveis (TPE) | 136 de 149 ações: 91,3% | Regular |

Fonte: [Dados da Coleta: Segurança](../dados/seguranca/index.md).

---

## 10. Sessões com Usuários

<p class="apresentador">João Victor da Silva Batista de Farias e Miguel Arthur Oliveira de Lima</p>

<!--
NOTA PARA APRESENTAÇÃO (João e Miguel):
- Atualizar com a situação do dia: campos do TCLE (#45), participantes recrutados (#67) e datas marcadas.
- A sessão só acontece com o TCLE assinado; o termo fica separado dos dados.
- Não citar número de participantes que ainda não foi confirmado.
-->

- **TCLE** ([página](../tcle.md)): base pronta; faltam seis campos, como local, tempo, gravação de áudio, contato e guarda dos dados (#45)
- **Recrutamento** (#67): meta de pelo menos cinco participantes
- **Coleta** (#90): sessões entre 06/11 e 10/11, com TCLE assinado, na cópia local

---

## 11. Riscos, Próximos Passos e Perguntas

<p class="apresentador">Mateus Vinícius Vieira</p>

<!--
NOTA PARA APRESENTAÇÃO (Mateus):
- Os riscos vêm das dependências do cronograma da Fase 3.
- As perguntas saíram da revisão da Fase 2 e afetam o julgamento da Fase 4. Pedir orientação antes de mudar a especificação.
-->

- **Riscos**: cópia local e recrutamento atrasarem as sessões; quadro do Projects sem horas reais
- **Sprint 4 (05/11 a 11/11)**: coleta de Manutenibilidade e Capacidade de Interação e primeira melhoria técnica
- **Perguntas para a professora**:
  - M3.1 soma alertas com peso pela confiança do Brakeman. Chamá-la de "densidade" é aceitável, ou ela deve ser dividida pelo tamanho do código?
  - M3.3 mede autorização. Ela fica melhor em Autenticidade ou em Confidencialidade e Integridade?
  - Coleta única, sem piloto e sem nova medição depois das melhorias técnicas: atende ao que se espera da Fase 4?

---

## 12. Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 04/11/2026 | Slides do Ponto de Controle 2 com notas de apresentação | [Mateus Vinícius Vieira](https://github.com/matix0) | A definir |
