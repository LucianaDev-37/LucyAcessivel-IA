import streamlit as st

st.set_page_config(page_title="LucyAcessível IA")

st.title('🤖 LucyAcessível IA')
st.subheader('Assistente financeiro educativo e acessível')

pergunta = st.text_input('Digite sua dúvida sobre produtos bancários:')

respostas = {
    'conta': 'Uma conta bancária permite guardar dinheiro, fazer pagamentos e transferências.',
    'poupança': 'A poupança é um investimento de baixo risco, indicado para quem busca segurança.',
    'cartão': 'O cartão de crédito permite compras agora e pagamento posterior.'
}

if pergunta:
    pergunta_lower = pergunta.lower()

    resposta_encontrada = None
    for chave in respostas:
        if chave in pergunta_lower:
            resposta_encontrada = respostas[chave]
            break

    if resposta_encontrada:
        st.success(resposta_encontrada)
    else:
        st.warning(
            'Ainda não tenho informações sobre isso. '
            'Posso ajudar com conta corrente, poupança ou cartão de crédito.'
        )
