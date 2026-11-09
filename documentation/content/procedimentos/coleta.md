---
icon: lucide/list-checks
---

# Procedimentos de coleta

Este protocolo detalha a Seção 3 da [Fase 3](../fases/3.md) para as 12 métricas da [Fase 2](../fases/2.md). Os resultados de G2 coletados em 08/11/2026 estão em [dados de Manutenibilidade](../dados/manutenibilidade/index.md). As sessões e a inspeção de G1 seguem o cronograma da Fase 3.

## Preparação e identificação da execução

1. Use uma cópia local da plataforma. Desative integrações que enviem dados para serviços reais e use somente contas e conteúdo de teste.
2. Confirme o commit `176b04673d956af4b1ab645e922cedd796b6a22e` do [decidim-govbr](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/tree/176b04673d956af4b1ab645e922cedd796b6a22e). Uma versão diferente exige registro do motivo e dos arquivos alterados. Não misture resultados de versões diferentes numa única amostra.
3. Crie uma pasta por execução em `documentation/content/dados/`. Registre data com fuso, commit completo, sistema, versões das ferramentas, comandos e códigos de saída. Preserve as saídas brutas junto aos cálculos.
4. Antes das sessões, complete o [TCLE](../tcle.md), confirme o ambiente da issue #64 e registre o processo participativo, a proposta de teste e as quatro URLs usadas. As rotas variam conforme a massa de dados local.
5. Mantenha termos assinados e qualquer chave entre identidade e código do participante fora do repositório público. Os dados publicados usam códigos como `P01`. Não publique cookies, credenciais ou gravações identificáveis.

## M1.1, M1.2 e M1.3: sessão observada

As três métricas usam a mesma ficha. A Tabela 1 define a situação inicial e o resultado esperado para cada tarefa. Prepare esses estados antes de iniciar o cronômetro; não conte o tempo de preparação.

**Tabela 1. Roteiro das quatro tarefas.**

| Código | Instrução ao participante | Situação inicial | Conclusão observável |
| :--- | :--- | :--- | :--- |
| T1 | Entre na plataforma com a conta de teste fornecida | Página inicial, sessão encerrada e autenticação local de teste disponível | Interface indica a conta autenticada |
| T2 | Encontre o processo participativo indicado no roteiro | Página inicial com sessão ativa | Página do processo solicitado aberta |
| T3 | Envie uma proposta nesse processo usando o conteúdo de teste fornecido | Página do processo, propostas abertas e conta apta a publicar | Proposta persistida e confirmação visível |
| T4 | Apoie a proposta indicada no roteiro | Página do processo, proposta que a conta ainda não apoiou | Apoio registrado e estado visual atualizado |

Fonte: elaboração a partir da Fase 2, Seção 6.1. Os nomes e URLs da massa de dados devem ser anexados à execução.

1. Após o TCLE, explique que o objeto da avaliação é a plataforma. Leia as instruções sem ensinar o caminho na interface.
2. Identifique participante, tarefa, data, commit e estado inicial na ficha. Use uma linha por participante e tarefa; tarefa não iniciada recebe `nao_iniciada` e fica fora do denominador.
3. Inicie o cronômetro quando o participante começar a ler a instrução. Pare ao atingir a conclusão da Tabela 1 ou ao desistir. O protocolo não impõe limite arbitrário de tempo.
4. Com gravação autorizada, anote os instantes inicial e final. Sem autorização, use cronômetro monotônico do observador, registre segundos com uma casa decimal e marque a fonte como `cronometro`. Não estime o tempo de memória. Em interrupção externa, registre a ocorrência e marque a duração como inválida.
5. Registre cada erro com instante, ação e resposta observada. Uma submissão inválida conta como um evento, mesmo que apareçam várias mensagens. Uma nova tentativa inválida conta novamente. Não conte exploração voluntária como desvio involuntário.
6. Se houver ajuda do observador, marque `ajuda=sim`. Registre o desfecho, mas não classifique a tarefa como conclusão autônoma. Preserve desistências e falhas na amostra de TCR e FET.
7. Para cada tarefa, calcule `TCR = 100 × conclusoes_sem_ajuda / tentativas_iniciadas` e `FET = eventos_de_erro / tentativas_iniciadas`. Para TME, selecione apenas as linhas com `status=concluida`, `ajuda=nao` e `tempo_valido=sim`. Some as durações dessas mesmas linhas e divida pela quantidade delas. Informe os três denominadores. Sem observações válidas, o resultado é indisponível, nunca zero.

Use os campos da Tabela 2 para preparar a ficha, sem dados pessoais. Registre eventos detalhados em arquivo separado, ligado por participante e tarefa.

**Tabela 2. Campos mínimos da ficha de observação.**

| Campo | Valores ou unidade |
| :--- | :--- |
| `participante`, `tarefa` | Código pseudônimo; T1 a T4 |
| `status`, `ajuda` | concluida, falhou, desistiu ou nao_iniciada; sim ou nao |
| `inicio`, `fim`, `duracao_s`, `tempo_valido` | Instantes, segundos e sim ou nao |
| `fonte_tempo`, `erros` | video ou cronometro; contagem inteira não negativa |
| `interrupcao`, `observacao` | Motivo de exclusão de tempo e descrição factual |

Fonte: elaboração para operacionalizar M1.1 a M1.3. O TME usa somente conclusões autônomas para evitar mistura com o tempo de instrução do observador.

## M1.5: questionário SUS

1. Após as quatro tarefas, entregue a mesma versão em português dos dez itens SUS a todos. Anexe à execução a referência e a versão do instrumento utilizado. Não reescreva os itens durante a aplicação.
2. Registre `participante` e `R1` a `R10`, com respostas inteiras de 1 a 5. O observador não sugere respostas.
3. Para itens ímpares, use `Rk - 1`; para pares, `5 - Rk`. Some as dez parcelas e multiplique por 2,5. O resultado vai de 0 a 100 pontos.
4. Se faltar resposta, registre o questionário como incompleto e exclua-o da média, informando a quantidade excluída. Não substitua respostas ausentes por zero ou pela média.
5. Publique os escores individuais pseudônimos e a média dos questionários completos. SUS é percepção declarada; o escore não comprova acessibilidade.

## M1.4: inspeção das quatro páginas

Registre as URLs locais da página inicial, da lista de processos, do formulário de proposta e da visualização de proposta. O formulário deve estar aberto com a conta de teste autenticada. Um relatório da tela de login não substitui o relatório do formulário.

1. Instale `@axe-core/cli` e `lighthouse` num diretório de ferramentas separado. Preserve o `package-lock.json`, as versões de Node, Chromium, axe-core e Lighthouse e a resolução da janela. Para reproduzir, use `npm ci` com esse lockfile.
2. Crie um perfil de navegador exclusivo para a coleta. Faça login local com a conta de teste, confira as quatro páginas e feche o navegador antes da execução dos comandos. Mantenha esse perfil fora do Git.
3. Execute os comandos abaixo para cada URL. `URL_LOCAL`, `PERFIL_COLETA` e `SAIDA` são valores da execução; `SAIDA` deve distinguir as quatro páginas. O navegador e o ChromeDriver da CLI precisam ter versões compatíveis.

```bash
axe "$URL_LOCAL" --tags wcag2a,wcag2aa,wcag21a,wcag21aa --chrome-options="user-data-dir=$PERFIL_COLETA" --save "$SAIDA-axe.json"
lighthouse "$URL_LOCAL" --only-categories=accessibility --disable-storage-reset --chrome-flags="--headless --user-data-dir=$PERFIL_COLETA" --output=json --output-path="$SAIDA-lighthouse.json"
```

4. Confira `url` no axe e `finalDisplayedUrl` ou `finalUrl` no Lighthouse. Rejeite redirecionamento para autenticação, erro de navegação ou página diferente da planejada. Registre a ocorrência antes de repetir a tentativa inválida.
5. No axe, conte os IDs distintos em `passes` e `violations`, por página. Um ID presente nos dois conjuntos conta como reprovado. Separe `incomplete` para revisão manual; não o trate como aprovado. Exclua `inapplicable`.
6. No Lighthouse, use somente os IDs referenciados pela categoria `accessibility`, com `scoreDisplayMode=binary` e `score` igual a 0 ou 1. Separe auditorias manuais, erros e itens não aplicáveis. A nota ponderada da categoria não é uma porcentagem de regras aprovadas.
7. Registre aprovadas `A` e reprovadas `R` por ferramenta e página. Calcule `ICA_operacional = 100 × soma(A) / soma(A + R)`. Essa escolha pondera cada resultado pela quantidade de verificações decididas. Preserve os resultados de cada ferramenta separadamente, pois há verificações sobrepostas.
8. Informe a quantidade de itens sem decisão. Sem verificações decididas, registre indisponível. Relacione cada falha à regra, à página e ao seletor, removendo conteúdo pessoal dos relatórios antes de publicar.

Os pesos são os totais de verificações com decisão de cada ferramenta e página, como detalhado na Fase 2. O índice descreve esses resultados automáticos. A conformidade integral com WCAG ou eMAG depende também das verificações manuais, registradas separadamente.

Os comandos seguem as referências da [CLI do axe](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/cli/README.md) e do [Lighthouse](https://github.com/GoogleChrome/lighthouse). A autenticação e as URLs dependem do ambiente da issue #64; esta etapa ainda não foi executada neste trabalho.

## M2.1 a M2.4: código e testes de Manutenibilidade

O coletor fica em `scripts/collect_maintainability.rb`. Ele lê a árvore sintática Ruby e não carrega a aplicação. A análise requer Ruby 3.4.7 e RuboCop 1.86.2; as versões efetivamente carregadas constam em `execution.json`.

```bash
git clone https://gitlab.com/lappis-unb/decidimbr/decidim-govbr.git brasil-participativo
git -C brasil-participativo checkout --detach 176b04673d956af4b1ab645e922cedd796b6a22e
git clone --depth 1 --branch v0.27.2 https://github.com/decidim/decidim.git /tmp/decidim-0.27.2
gem install rubocop -v 1.86.2 --no-document
ruby scripts/collect_maintainability.rb brasil-participativo /tmp/decidim-0.27.2 /tmp/coleta-g2
rubocop --ignore-disable-comments --cache false --config scripts/maintainability.rubocop.yml --only Metrics/CyclomaticComplexity --format json --out /tmp/coleta-g2/M2.2-rubocop.json brasil-participativo/app/commands brasil-participativo/app/controllers brasil-participativo/app/permissions brasil-participativo/app/services
```

O comando RuboCop retorna 1 quando emite os alertas esperados. O limiar zero serve para listar todos os métodos não vazios; não é o limiar de julgamento. Erro de sintaxe, falha de ferramenta ou arquivo ausente invalida a execução. O coletor recusa checkouts modificados e registra os hashes SHA-256 dos arquivos lidos.

Como alternativa ao Ruby instalado no sistema, use `bash scripts/run_maintainability.sh brasil-participativo /tmp/decidim-0.27.2 /tmp/nova-coleta-g2`. O wrapper exige a imagem Docker identificada em [reproduction.txt](../dados/manutenibilidade/reproduction.txt) já disponível localmente. Ele monta as duas fontes somente para leitura, desativa a rede e recusa sobrescrever uma pasta com resultados. Ao final, confere os CSVs contra o JSON do RuboCop.

1. **M2.1:** conte classes nomeadas distintas em arquivos Ruby versionados de `app/` e `lib/`. Exclua testes, inclusive diretórios internos `test/`, `spec/`, `rspec_support/` e `fixtures/`, além de migrações, configuração e dependências. Para cada classe de `app/`, procure a mesma constante nas árvores `app/` e `lib/` das engines do Decidim 0.27.2. Conte cada constante uma vez e divida as sobrescritas pelo total. Inspecione `M2.1-classes.csv`, que inclui caminhos da referência.
2. **M2.2:** use os métodos `def` e `def self` de `app/commands/`, `app/controllers/`, `app/permissions/` e `app/services/`, incluindo privados e métodos de módulos nesses diretórios. O coletor usa o cálculo do cop `Metrics/CyclomaticComplexity` e atribui 1 a métodos vazios. Confira `M2.2-methods.csv` contra o JSON do RuboCop, somando as complexidades e dividindo pelo total de métodos. Registre máximo e localização dos maiores valores, pois a média pode esconder concentração.
3. **M2.3:** conte linhas com tokens Ruby em cada arquivo de `app/` que declara classe. Exclua linhas em branco, comentários e documentação embutida. O coletor usa `Ripper.lex`, do Ruby, em lugar de `scc` ou `cloc`. Conte um arquivo uma vez mesmo que declare duas classes. Some a coluna `sloc` de `M2.3-sloc.csv`, divida pela quantidade de arquivos e informe o máximo. O resultado é por arquivo de classe, conforme a definição da Fase 2.
4. **M2.4:** cruze as sobrescritas com `spec/`. Resolva a classe descrita em `describe` dentro dos módulos Ruby do arquivo. Se não houver classe explicitamente descrita, aceite o caminho espelhado de `app/` para `spec/`, com sufixo `_spec.rb`, somente para a classe cujo nome corresponde ao arquivo. A correspondência exige exemplo não pendente. `M2.4-specs.csv` registra essas associações; testes indiretos ficam fora da contagem automática. Divida classes com evidência por sobrescritas. Não chame esse índice de cobertura de linhas ou de testes aprovados.
5. Preserve CSVs, `summary.json`, `execution.json` e o relatório RuboCop. Verifique somas e denominadores antes de publicar. O julgamento final continua na Fase 4.

O recorte de classes de produção evita contar classes de testes e migrações no denominador de M2.1. A igualdade com a referência evita tratar toda classe nova dentro de `Decidim::` como sobrescrita. Módulos, decorators dinâmicos e mudanças em métodos por metaprogramação não são medidos por esse inventário. Registre esses limites ao interpretar TSN.

O uso da API interna do RuboCop exige a versão fixada; mudanças de versão podem mudar a contagem. Consulte também a [documentação de CyclomaticComplexity](https://docs.rubocop.org/rubocop/cops_metrics.html#metricscyclomaticcomplexity).

## M3.1: Brakeman

1. Use o mesmo checkout limpo e registre `brakeman --version`. A coleta existente usou 8.1.0.
2. Execute `brakeman -q -p "$FONTE" -o "$SAIDA/M3.1-brakeman.json"`, com `FONTE` apontando para o clone e `SAIDA` para uma nova pasta. Preserve também a saída de diagnóstico e o código de retorno.
3. Leia os avisos em `warnings`, sem contar o mesmo aviso novamente a partir do relatório textual. Agrupe os valores textuais de `confidence`: `High` (alta), `Medium` (média) e `Weak` (fraca), como no JSON da coleta de 03/11. Rejeite valores desconhecidos em vez de contá-los como zero.
4. Calcule `DVC = 3 × alta + 2 × media + fraca`. Registre também erros de análise, avisos ignorados e a quantidade de arquivos analisados. Relatório incompleto exige investigação antes de julgamento.
5. Confiança do analisador não equivale a gravidade ou exploração confirmada. Confronte cada candidato a correção com arquivo e linha do commit avaliado.

## M3.2: bundler-audit

1. Registre `bundler-audit --version` e o SHA-256 de `Gemfile.lock`. A coleta existente usou 0.9.3.
2. Na pasta do clone, execute `bundler-audit check --update --format json` e guarde stdout, stderr e código de retorno. Essa operação consulta a base de avisos, sem enviar requisições à plataforma avaliada.
3. Registre data e commit da cópia local `ruby-advisory-db`. Preserve essa referência para repetir a consulta sem `--update`.
4. Conte pares distintos `(gem, CVE)` reportados no lockfile. Avisos sem CVE ficam em contagem separada; não invente um identificador. Se a mesma CVE afetar duas gems, registre os dois pares, conforme a soma por gem da Fase 2.
5. Liste nome, versão instalada, CVE e versões corrigidas. Saída com vulnerabilidades não é erro operacional; erro ao ler o lockfile ou atualizar a base precisa ser registrado separadamente.

Os passos de segurança seguem os projetos [Brakeman](https://github.com/presidentbeef/brakeman) e [bundler-audit](https://github.com/rubysec/bundler-audit). A data da base de avisos altera M3.2; a coleta de 03/11 permanece preservada em [Segurança](../dados/seguranca/index.md).

## M3.3: endpoints sensíveis

```bash
python3 scripts/m33_endpoints.py "$FONTE" "$SAIDA/M3.3-candidatos.csv"
```

1. Inspecione cada ação candidata no código e confirme sua rota em `config/routes.rb` e nas engines. Exclua auxiliares sem rota e ações fora da definição de endpoint sensível da Fase 2, anotando o motivo.
2. Verifique a ação, os filtros `before_action`, os controllers ancestrais e a classe de permissões. A mera presença de `allowed_to?` não prova bloqueio: confira se a resposta impede a operação. Diferencie autenticação de autorização.
3. Acrescente ações sensíveis que a busca textual omitiu. Para cada linha, registre sensibilidade, proteção, arquivo, linha e justificativa da conferência. Preserve o CSV original ao lado da versão revisada.
4. Calcule `TPE = 100 × acoes_com_protecao_confirmada / acoes_sensiveis`. Casos não resolvidos devem ser informados; não os classifique automaticamente como protegidos.
5. Revise especialmente rotas declaradas fora do escopo administrativo. Esta inspeção estática não demonstra ausência de vulnerabilidades e não executa requisições contra produção.

## Registros

Compare os arquivos com as fórmulas da Fase 2 e registre qualquer desvio de procedimento. Uma tentativa inválida por falha de ferramenta pode ser refeita com justificativa; não substitua silenciosamente dados válidos. Testes da melhoria #73 ficam separados dos dados de G2, preservando a decisão de coleta única.

Responsável da issue #63: Lucca Medeiros Silva.
