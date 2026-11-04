---
icon: lucide/shield
---

# Dados da Coleta: Segurança (G3)

Esta página reúne a coleta das métricas de Segurança (M3.1, M3.2 e M3.3) definidas na [Fase 2](../../fases/2.md) e planejadas na [Fase 3](../../fases/3.md). A análise foi feita só no código clonado do `decidim-govbr`, sem nenhuma requisição à plataforma em produção. O julgamento final do objetivo G3 fica para a Fase 4.

---

## 1. Execução

| Item | Valor |
| :--- | :--- |
| Data | 03/11/2026, 23:17 (horário de Brasília) |
| Repositório e commit | `decidim-govbr`, commit `176b04673d956af4b1ab645e922cedd796b6a22e` (ramo `develop`) |
| Ferramentas | Brakeman 8.1.0; bundler-audit 0.9.3 com a base RubySec atualizada no dia; script `scripts/m33_endpoints.py` do repositório da equipe |
| Responsável | José Vinícius Alvares Soares de Queiroz |

| Arquivo | Conteúdo | Métrica |
| :--- | :--- | :---: |
| [`execucao.txt`](execucao.txt) | Data, commit e versão das ferramentas | Todas |
| [`M3.1-brakeman.json`](M3.1-brakeman.json) e [`M3.1-brakeman.txt`](M3.1-brakeman.txt) | Relatório completo do Brakeman | M3.1 |
| [`M3.2-bundler-audit.txt`](M3.2-bundler-audit.txt) | Lista das dependências com aviso de segurança | M3.2 |
| [`M3.3-endpoints.csv`](M3.3-endpoints.csv) | Ações sensíveis dos controllers, com a conferência manual de cada uma | M3.3 |

Fonte: elaborado pela equipe.

Para repetir a coleta, siga a Seção 3 da Fase 3 com o mesmo commit. Os resultados de M3.1 e M3.3 se repetem; o de M3.2 pode crescer, porque a base RubySec recebe avisos novos.

---

## 2. Resultados

| Métrica | Valor medido | Nível (Fase 2) | Hipótese |
| :--- | :--- | :---: | :--- |
| **M3.1** Densidade de Vulnerabilidades de Código (DVC) | 2 alertas de confiança alta, 8 de média, 0 de fraca; DVC = 3×2 + 2×8 + 0 = **22** | **Insuficiente** | H3.1 refutada |
| **M3.2** Dependências Vulneráveis (CDV) | **156 CVEs** em 198 avisos, distribuídos em 51 gems | **Insuficiente** | H3.2 confirmada |
| **M3.3** Proteção de Endpoints Sensíveis (TPE) | 136 de 149 ações sensíveis com verificação explícita: TPE = **91,3%** | **Regular** | H3.3 refutada |

Fonte: elaborado pela equipe a partir dos arquivos da Seção 1.

### 2.1 M3.1: alertas do Brakeman

| Confiança | Qtd. | Alertas |
| :--- | :---: | :--- |
| Alta | 2 | Ruby 3.0.4 sem suporte desde 31/03/2024; Rails 6.1.7.2 sem suporte desde 01/10/2024 |
| Média | 4 | Atribuição em massa com `permit!` em `components_controller.rb`, `participatory_texts_controller.rb` (2) e `proposals_controller.rb` |
| Média | 4 | Possível SQL injection em `app/models/decidim/govbr/user_proposals_statistic_setting.rb` |

Fonte: relatório do Brakeman (`M3.1-brakeman.txt`).

Os dois alertas de confiança alta tratam de versões sem suporte, e não de padrões no código. Sem eles, a DVC seria 16 e o nível continuaria Insuficiente, porque passa de 15. Os quatro alertas de SQL injection estão num model criado pela equipe do governo, e não no Decidim; o Brakeman marca a confiança como média, então eles precisam de confirmação manual antes de virarem correção.

### 2.2 M3.2: dependências com avisos

O `bundler-audit` encontrou 198 avisos em 51 gems; 156 deles têm CVE. Por gravidade declarada no aviso: 3 críticos, 49 altos, 81 médios, 7 baixos e 58 sem classificação. As gems com mais avisos são `rack` (2.2.6.2), `nokogiri` (1.13.10), `net-imap` (0.3.4), `loofah` (2.3.1) e `rails-html-sanitizer` (1.4.3). Um dos avisos críticos é da `graphql` (1.12.24), com execução remota de código; o próprio aviso indica correção na versão 1.12.25, da mesma série.

### 2.3 M3.3: ações sem verificação explícita

O script `m33_endpoints.py` listou 188 ações públicas nos controllers. A conferência manual excluiu 40 que não são endpoints sensíveis (métodos auxiliares, telas de login e cadastro, uma ação sem rota e uma que só redireciona) e acrescentou uma ação de exportação que o script não classificou como sensível. A coluna `conferencia_manual` do CSV registra a decisão de cada linha.

Das 13 ações sem verificação explícita, 8 foram introduzidas no `decidim-govbr` e 5 são iguais ao Decidim 0.27.2:

| Origem | Controller | Ações |
| :--- | :--- | :--- |
| `decidim-govbr` | `admin/proposal_badges_controller.rb` | `update`, `update_proposal_badge`, `destroy_all_badges`, `destroy_one_badge` |
| `decidim-govbr` | `forms/admin/concerns/has_questionnaire.rb` | `import` |
| `decidim-govbr` | `proposals/admin/proposal_answers_controller.rb` | `remove_label_from_proposal` |
| `decidim-govbr` | `proposals/admin/proposals_controller.rb` | `index` |
| `decidim-govbr` | `reports/reports_controller.rb` | `create` |
| Decidim 0.27.2 | `admin/components_controller.rb` | `share` |
| Decidim 0.27.2 | `admin/organization_controller.rb` | `users`, `user_entities` |
| Decidim 0.27.2 | `forms/admin/concerns/has_questionnaire.rb` | `answer_options` |
| Decidim 0.27.2 | `proposals/admin/proposals_controller.rb` | `show` |

Fonte: conferência manual da equipe sobre `M3.3-endpoints.csv` e comparação com o código do Decidim 0.27.2.

Dois casos do código do governo pesam mais que os demais. As quatro ações de selos de propostas têm rotas declaradas no `config/routes.rb` principal, fora das rotas de administração do Decidim, que exigem acesso ao painel; no código analisado, nem a rota nem a ação verificam o usuário. Na ação de relatórios, existe uma checagem de administrador, mas ela só agenda um redirecionamento e não interrompe a execução. Os dois achados vêm da leitura do código e não foram testados em execução.

---

## 3. Candidatos a Melhoria

| Candidato | Evidência | Esforço estimado |
| :--- | :--- | :--- |
| Adicionar `enforce_permission_to` às quatro ações de selos e mover as rotas para o escopo de administração | M3.3 | Baixo: um controller e quatro rotas |
| Interromper a ação de relatórios para não administradores e substituir a checagem por `enforce_permission_to`, como pede o próprio comentário `TODO` no código | M3.3 | Baixo: um controller |
| Atualizar gems dentro da mesma série, começando por `graphql` (1.12.24 para 1.12.25), `rack` (série 2.2) e `puma` (série 5.6) | M3.2 | Médio: exige rodar a suíte de testes para conferir compatibilidade |
| Confirmar e corrigir os quatro alertas de SQL injection no model de estatísticas | M3.1 | Médio: depende da confirmação manual |

Fonte: elaborado pela equipe.

A escolha das melhorias dos Sprints 4 e 5 cabe à equipe, junto com os resultados de Manutenibilidade.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 03/11/2026 | Coleta das métricas M3.1, M3.2 e M3.3 no commit `176b046` | [José Vinícius Alvares Soares de Queiroz](https://github.com/JoseViniciusQueiroz) | A definir |
