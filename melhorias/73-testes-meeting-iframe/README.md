# Testes de regressão do MeetingIframeEmbedder

Implementação da issue #73, ligada à Testabilidade (G2/Q2.3/M2.4). A fonte do teste está neste diretório. O patch aplicável ao produto, a saída RSpec e a análise estão em [dados da melhoria](../../documentation/content/dados/melhoria-73/index.md).

O teste deve ser instalado em `spec/services/decidim/meetings/meeting_iframe_embedder_spec.rb` no `decidim-govbr`, commit `176b04673d956af4b1ab645e922cedd796b6a22e`. O caminho relativo de carregamento pressupõe essa localização. Use o patch para preservar o destino.

Os 20 exemplos passaram no ambiente isolado descrito no registro. A suíte completa da aplicação não foi executada, e a integração com as dependências do produto não foi testada. A amostra da coleta G2 permanece sem alteração.
