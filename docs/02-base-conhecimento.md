# Base de Conhecimento

## Dados Utilizados

O agente LucyAcessível IA utiliza uma base de conhecimento educacional e acessível, composta por arquivos JSON e CSV armazenados na pasta `data`.
Esses dados contêm explicações simples sobre produtos financeiros, perguntas frequentes e termos básicos, sem o uso de dados pessoais ou informações sensíveis.


|      Arquivo   | Formato | Utilização no Agente |
|----------------|---------|----------------------|
| `glossario_financeiro.csv` | CSV     | Explicar termos financeiros em linguagem clara e acessível|
| `perfis_usuario.json`      | JSON    | Ajustar linguagem e nível de explicação conforme o tipo de usuário |
| `produtos_financeiros.json`| JSON    | Explicar produtos financeiros básicos de forma simples |
| `perguntas_frequentes.csv` | CSV     | Base principal do motor de regras para responder dúvidas comuns|


> [!TIP]
Os dados utilizados são mockados e educativos, inspirados em conteúdos públicos de educação financeira, garantindo ética, segurança e acessibilidade.


---

## Adaptações nos Dados

Os dados foram criados e adaptados manualmente com foco em acessibilidade e inclusão, seguindo os princípios:

- Linguagem simples e não técnica
- Frases curtas e objetivas
- Conteúdo educativo e não persuasivo
- Ausência de dados sensíveis ou pessoais
- Estrutura pensada para fácil expansão


---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV são carregados no início da execução da aplicação, utilizando bibliotecas padrão do Python.
Após o carregamento, os dados permanecem disponíveis em memória para consulta durante a interação com o usuário.

Essa abordagem garante:

- Baixa complexidade
- Facilidade de manutenção
- Transparência no funcionamento do agente

### Como os dados são usados no prompt?

Os dados não são inseridos integralmente no system prompt.
O agente consulta a base de conhecimento por meio de um motor de regras, que identifica a intenção da pergunta do usuário e direciona a resposta correta, sem gerar respostas livres.

- A intenção é detectada por palavras-chave
- O agente busca a informação correspondente na base de conhecimento
- A resposta é construída em linguagem acessível e educativa

Essa estratégia reduz riscos de alucinação e mantém o controle total das respostas.


---

## Exemplo de Contexto Montado

```

Tipo de usuário: Iniciante
Nível de linguagem: Simples

Pergunta do usuário:
"O que é conta poupança?"

Contexto consultado:
- Produto: Conta Poupança
- Descrição simples disponível na base de conhecimento

Resposta da Lucy:
"Conta poupança é uma forma simples de guardar dinheiro.
Ela rende um pouco, seguindo regras definidas pelo Banco Central, e é considerada uma opção básica e segura."

...
```
