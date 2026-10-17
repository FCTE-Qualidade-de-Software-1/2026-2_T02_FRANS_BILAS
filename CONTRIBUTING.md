# Guia de Contribuição — Equipe Frans Bilas

Bem-vindo ao repositório de Qualidade de Software 1 (FGA0315 - 2026.2).
Para garantir que todo o código, artigo em LaTeX e documentação mantenham o mais alto padrão de qualidade e passem nos critérios da disciplina, siga este guia.

---

## 1. Configuração Inicial do Repositório

Ao clonar o repositório, ative imediatamente os hooks de validação do Git para que o linter do `humanizer` seja executado antes de cada commit:

```bash
git config core.hooksPath .githooks
```

Para rodar a verificação manualmente a qualquer momento:
```bash
python3 scripts/check_humanizer.py
```

Para visualizar a documentação local com live-reload:
```bash
cd documentation
zensical serve
```

---

## 2. Fluxo de Trabalho e Branches

1. **Issues**: Toda atividade deve ter uma issue correspondente com responsável e milestone do sprint.
2. **Branches**: Crie branches a partir da `main` seguindo o padrão:
   `tipo/numero-descricao`
   - Exemplos:
     - `docs/1-proposito-stakeholders`
     - `feat/10-coleta-metricas-manutenibilidade`
     - `fix/15-correcao-referencias-artigo`
3. **Commits**: Utilize [Conventional Commits](https://www.conventionalcommits.org/):
   - `docs:` Alterações em documentação, slides ou LaTeX.
   - `feat:` Nova funcionalidade, script de análise ou métrica.
   - `fix:` Correção de dados, links ou formatação.
   - `refactor:` Reorganização de arquivos ou reescrita sem alteração de escopo.
   - `chore:` Configurações de ambiente, dependências ou tarefas de build.
4. **Pull Requests**:
   - Abra um PR para a branch `main`.
   - Preencha o template do PR (`.github/pull_request_template.md`), incluindo a **Declaração de Uso de IA** e o **Checklist Anti-Meat-Proxy**.
   - Cada PR deve ser revisado por pelo menos um membro de outra dupla antes do merge (squash merge).

---

## 3. Política de Uso de Inteligência Artificial e Anti-Meat-Proxy

Não aceitamos entregas de *meat-proxy* (copiar e colar texto de IA sem curadoria crítica):

- **Aplicação da skill `humanizer`**: Todo texto destinado ao artigo (`documentation/content/article/source/main.tex`) ou documentação (`documentation/content/`) deve ser verificado contra vícios de IA.
- **Não invente dados**: Métricas, números de linhas, vulnerabilidades e tabelas devem vir comprovadamente de execuções ou inspeções reais no repositório do Brasil Participativo.
- **Terminologia SQuaRE (ISO/IEC 25010:2023)**: Usabilidade agora é formalmente chamada de **Capacidade de Interação**.
- **Registro Contínuo**: Declare de forma transparente a ferramenta, a tarefa e o método de revisão humana no PR.

---

## 4. Onde Fica Cada Arquivo

- `documentation/content/`: Páginas da GitPage (Markdown).
- `documentation/content/article/source/main.tex`: Artigo científico em LaTeX (SBC/IEEE/ACM).
- `documentation/content/entregas/1.md`: Slides da Entrega 1 (renderizados com `zensical-slides`).
- `scripts/`: Scripts utilitários e linters do projeto.
- `.agents/skills/`: Skills de apoio aos agentes e revisores.

