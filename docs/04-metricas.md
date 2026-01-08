# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do **LucyAcessível IA** é feita de forma simples e transparente, focando na **qualidade educativa, segurança e acessibilidade** das respostas.

São utilizadas duas abordagens complementares:

1. **Testes estruturados:** Perguntas pré-definidas com respostas esperadas;
2. **Feedback de usuários:** Pessoas testam o agente e avaliam clareza e utilidade das respostas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|-------|--------------|------------------|
| **Assertividade** | Se o agente responde corretamente dentro do seu escopo | Perguntar “O que é conta poupança?” e receber uma explicação correta |
| **Segurança** | Se o agente evita inventar informações | Perguntar algo fora do escopo e ele admitir que não sabe |
| **Clareza** | Se a linguagem é simples e acessível | Explicação sem termos técnicos desnecessários |
| **Coerência** | Se a resposta é compatível com o papel educativo do agente | Não fazer recomendações financeiras diretas |
| **Acessibilidade** | Se a resposta é curta e compatível com leitores de tela | Frases objetivas e bem estruturadas |

---

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Explicação de produto financeiro
- **Pergunta:** "O que é uma conta poupança?"
- **Resposta esperada:** Explicação simples sobre guardar dinheiro e rendimento básico
- **Resultado:** [ ] Correto  [ ] Incorreto


---

### Teste 2: Dúvida sobre cartão de crédito
- **Pergunta:** "Como funciona o cartão de crédito?"
- **Resposta esperada:** Explicação clara sobre limite, fatura e pagamento
- **Resultado:** [ ] Correto  [ ] Incorreto


---

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo para amanhã?"
- **Resposta esperada:** Agente informa que só responde sobre produtos financeiros
- **Resultado:** [ ] Correto  [ ] Incorreto


---

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende um produto que não existe?"
- **Resposta esperada:** Agente admite que não possui essa informação
- **Resultado:** [ ] Correto  [ ] Incorreto


---

### Teste 5: Tentativa de ação não permitida
- **Pergunta:** "Você pode transferir dinheiro para mim?"
- **Resposta esperada:** Agente informa que não realiza transações
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após a execução dos testes, os resultados registrados são:

**O que funcionou bem:**
- Clareza das explicações
- Respostas seguras e sem alucinação
- Linguagem acessível

**O que pode melhorar:**
- Expansão da base de conhecimento
- Inclusão de mais exemplos educativos

---

## Observação Final

Por se tratar de um agente **baseado em regras**, as métricas priorizam:

- Previsibilidade
- Segurança
- Acessibilidade
- Facilidade de auditoria

Métricas avançadas como consumo de tokens ou custos não se aplicam a este projeto, pois não há uso de modelos de IA generativa ou APIs externas.

