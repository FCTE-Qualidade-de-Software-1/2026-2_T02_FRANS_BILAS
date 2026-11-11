---
icon: lucide/wrench
---

# Dados de Manutenibilidade

A coleta da issue #89 mede M2.1 a M2.4 no commit `176b04673d956af4b1ab645e922cedd796b6a22e` do Brasil Participativo. Os dados respondem às questões GQM da [Fase 2](../../fases/2.md); o [protocolo](../../procedimentos/coleta.md) explica como repetir os cálculos. A execução ocorreu em 08/11/2026, após a janela prevista de 05 a 06/11.

## Execução

A Tabela 1 identifica as fontes e o ambiente. O coletor analisou arquivos versionados de dois checkouts limpos, sem carregar Rails ou acessar a plataforma em produção.

**Tabela 1. Identificação da coleta G2.**

| Item | Registro |
| :--- | :--- |
| Horário registrado ao concluir | 08/11/2026, 13:44:56, UTC-03:00 |
| Produto | [decidim-govbr, 176b04673d956af4b1ab645e922cedd796b6a22e](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/tree/176b04673d956af4b1ab645e922cedd796b6a22e) |
| Referência | [Decidim v0.27.2, 67843526a7d60a5fc01ab0baa24db8ae4f4ca973](https://github.com/decidim/decidim/tree/67843526a7d60a5fc01ab0baa24db8ae4f4ca973) |
| Ferramentas | Ruby 3.4.7; RuboCop 1.86.2; Ripper do Ruby; coletor `scripts/collect_maintainability.rb` |
| Ambiente | Contêiner Linux x86_64, rede desativada; imagem e comandos em [reprodução](reproduction.txt) |
| Responsável da issue | Lucca Medeiros Silva |
| Execução | Coleta automatizada pelo script `scripts/collect_maintainability.rb` |

Fonte: [execution.json](execution.json), com versões, hashes dos arquivos de entrada e hash do coletor.

## Resultados

A Tabela 2 aplica os intervalos da Fase 2 aos valores obtidos. Os rótulos indicam essas faixas; o julgamento integrado de G2 permanece para a Fase 4.

**Tabela 2. Medidas de Manutenibilidade no commit avaliado.**

| Métrica | Numerador e denominador | Resultado | Faixa da Fase 2 |
| :--- | :--- | :--- | :--- |
| M2.1, TSN | 175 classes sobrescritas / 291 classes de produção | 60,14% | Insuficiente |
| M2.2, CCM | Soma 2.916 / 1.275 métodos | Média 2,29; máximo 47 | Excelente pela média |
| M2.3, DLC | 18.298 linhas efetivas / 273 arquivos de classe | Média 67,03; máximo 595 | Insuficiente pelo máximo maior que 400 |
| M2.4, ICT | 69 sobrescritas com teste identificado / 175 sobrescritas | 39,43% | Insuficiente |

Fonte: [summary.json](summary.json) e inventários da Tabela 3. Percentuais e médias arredondados somente para exibição.

Foram identificadas 106 sobrescritas sem correspondência pelo procedimento automático. Isso não prova ausência de testes indiretos. A métrica registra presença de exemplos RSpec identificáveis; a suíte da aplicação não foi executada durante a coleta.

A Tabela 3 permite conferir os denominadores e localizar cada ocorrência.

**Tabela 3. Arquivos de evidência.**

| Arquivo | Conteúdo |
| :--- | :--- |
| [M2.1-classes.csv](M2.1-classes.csv) | Constantes, caminhos locais, declarações no Decidim e testes associados |
| [M2.2-methods.csv](M2.2-methods.csv) | Método, arquivo, linha e complexidade |
| [M2.2-rubocop.json](M2.2-rubocop.json) | Saída original do RuboCop, com limiar zero para inventário |
| [M2.3-sloc.csv](M2.3-sloc.csv) | Linhas efetivas por arquivo que declara classe |
| [M2.4-specs.csv](M2.4-specs.csv) | Sobrescritas e caminhos de testes; campo vazio indica ausência de correspondência automática |
| [verification.json](verification.json) | Conferência dos totais e comparação com o relatório RuboCop |

Fonte: execução dos scripts de coleta e conferência do repositório da equipe.

## O que os dados permitem concluir

**Q2.1:** há 175 constantes de classes de `app/` também declaradas na referência Decidim. Isso sustenta H2.1, que previa a existência de sobrescritas. TSN mede a proporção; não mede sozinha o esforço de atualização nem a concentração por diretório.

**Q2.2:** a média 2,29 convive com métodos de maior complexidade. Em `app/permissions/decidim/admin/permissions.rb`, o método `permissions`, linha 6, tem complexidade 47. Em `app/permissions/decidim/proposals/admin/permissions.rb`, o método homônimo, linha 7, tem 25. São pontos para inspeção e testes antes de uma refatoração. O arquivo `app/lib/decidim/form_builder.rb` contém 595 linhas efetivas, o maior valor da amostra. Os inventários sustentam a parte descritiva de H2.2; não houve estudo do tempo gasto por desenvolvedores para entender o código.

**Q2.3:** os 69 casos com correspondência e os 106 sem correspondência sustentam H2.3 dentro do critério de busca adotado. A [melhoria #73](../melhoria-73/index.md) acrescenta testes de regressão a uma dessas classes, `Decidim::Meetings::MeetingIframeEmbedder`. Os testes ficam separados desta coleta, sem recalcular os indicadores da amostra original.

## Limites e verificações

O denominador de M2.1 inclui classes de produção nomeadas em `app/` e `lib/`; exclui testes e seus diretórios de suporte, migrações, configuração e dependências externas. Classes novas sob `Decidim::` não são consideradas sobrescritas sem declaração correspondente na referência. Módulos e alterações por metaprogramação ficam fora do inventário de classes.

M2.2 inclui métodos de classes e módulos nos quatro diretórios definidos na Fase 2. Os 1.272 métodos reportados pelo RuboCop concordaram, individualmente, com o coletor. Outros três métodos vazios receberam complexidade 1; a CLI não emite alerta para eles. Dois são auxiliares condicionados a `Rails.env.test?` no controller de membros de assembleias. O recorte estático os mantém e lista essa limitação em [verification.json](verification.json).

M2.3 usa tokens do Ripper em lugar de `scc` ou `cloc`. Strings que ocupam várias linhas contam como código; comentários e linhas vazias não. A unidade é arquivo que declara classe, não cada declaração interna.

M2.4 resolve a classe descrita dentro dos módulos Ruby do arquivo. O caminho espelhado só é usado para a classe que corresponde ao nome do arquivo, quando o teste não descreve explicitamente outra classe. Os dois casos exigem exemplo não pendente. A busca não verifica correspondências indiretas, exemplos compartilhados sem exemplo explícito no arquivo ou condições de execução. O índice não informa cobertura de linhas, aprovação da suíte ou qualidade das asserções.

Os 11 testes do coletor passaram. Eles verificam, entre outros casos, exclusão do suporte de testes, resolução de namespaces, correspondências por caminho, exemplos pendentes e rejeição de checkout modificado. O script `scripts/verify_maintainability.py` conferiu os totais e as complexidades contra o JSON original.

A conferência corrigiu dois valores da extração inicial: TSN passou de 59,12% para 60,14% após excluir cinco classes auxiliares de teste; ICT passou de 29,14% para 39,43% com a resolução dos namespaces RSpec e a restrição do vínculo por caminho. O [registro das correções](corrections.json) lista as classes afetadas. O commit do produto, a complexidade e a contagem de linhas permaneceram iguais.
