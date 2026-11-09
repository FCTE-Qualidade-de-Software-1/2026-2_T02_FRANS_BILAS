---
icon: lucide/test-tube
---

# Melhoria 73: testes do serviço de embeds

A coleta de [Manutenibilidade](../manutenibilidade/index.md) identificou 69 de 175 sobrescritas com teste correspondente. `Decidim::Meetings::MeetingIframeEmbedder` está entre as classes sem correspondência. A melhoria da issue #73 acrescenta testes de regressão a esse serviço, ligada à Testabilidade, ao objetivo G2 e à questão Q2.3.

## Alteração entregue

O [patch](0001-add-meeting-iframe-spec.patch) adiciona `spec/services/decidim/meetings/meeting_iframe_embedder_spec.rb` ao `decidim-govbr` no commit `176b04673d956af4b1ab645e922cedd796b6a22e`. O código de produção permanece igual ao da coleta. Os testes exercitam o arquivo real `app/services/decidim/meetings/meeting_iframe_embedder.rb`, carregado diretamente.

São 20 exemplos: dez combinações de URL e resultado, URL vazia, parâmetro `parent` do Twitch, cinco casos de identificação dos serviços permitidos e três casos do HTML de embed. A Tabela 1 relaciona os comportamentos ao risco de regressão.

**Tabela 1. Comportamentos verificados pela melhoria.**

| Método | Casos | Regressão que o teste detecta |
| :--- | :--- | :--- |
| `embed_transformed_url` | YouTube com `v`, parâmetros adicionais ou repetidos, `v` vazio ou ausente; Twitch com e sem caminho de vídeo; host externo e URL vazia | Perda de parâmetros, transformação incorreta ou alteração do retorno de fallback |
| `embeddable?` | Hosts configurados, normalização de `www`, host externo e domínio que apenas contém `youtube.com` | Aceitação indevida de host ou rejeição de serviço configurado |
| `embed_code` | URL vazia, classe CSS e iframe comentado | Reativação involuntária do iframe no comportamento avaliado |

Fonte: exemplos RSpec do patch e código do serviço no commit avaliado. Estes testes caracterizam o comportamento atual; não demonstram segurança integral da incorporação de conteúdo externo.

## Validação

O patch foi aplicado a uma cópia isolada do commit da coleta. A execução independente de Rails e de banco de dados terminou com **20 exemplos, zero falhas e zero pendências**, conforme [rspec.json](rspec.json). As versões e hashes estão em [execution.json](execution.json).

Os testes substituem o retorno do método privado `embeddable_services` por uma lista controlada. Esse método já existe na classe, de modo que a configuração original do RSpec, com `verify_partial_doubles=true`, permanece ativa. As transformações de URL e a geração de HTML usam a implementação real do serviço.

O ambiente usado foi Ruby 3.4.7, RSpec Core 3.13.6 e ActiveSupport 8.1.3.1, em contêiner sem rede. Essas versões diferem das dependências do produto. A suíte completa do Rails não foi executada, e a integração com as versões travadas no produto não foi testada.

## Aplicação e reprodução

Use uma cópia de trabalho separada da amostra original. `PATCH` deve apontar para o arquivo baixado desta página; `COPIA` identifica o checkout do `decidim-govbr`.

```bash
git -C "$COPIA" rev-parse HEAD
git -C "$COPIA" apply --check "$PATCH"
git -C "$COPIA" apply "$PATCH"
cd "$COPIA"
rspec --format documentation spec/services/decidim/meetings/meeting_iframe_embedder_spec.rb
```

O comando carrega o `spec_helper` pela `.rspec` do produto. Esse arquivo configura o RSpec sem inicializar Rails; a inicialização da aplicação fica em `rails_helper`, que estes exemplos não usam. O registro de execução contém o comando completo do contêiner, incluindo as montagens.

O patch permanece local e não foi enviado ao GitLab. Não foi feita uma segunda medição de G2, conforme a decisão de coleta única da Fase 3.

Responsável da issue #73: Lucca Medeiros Silva. Implementação e execução em 08/11/2026.
