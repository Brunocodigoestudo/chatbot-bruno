import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Aplicar estilo customizado
st.markdown(
    """
    <style>
        .stApp {
            background-color: #001f3f; /* Azul escuro */
            color: white;
        }
        h1, h2, h3, h4, h5, h6, p, span, div {
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Definir a chave da API
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

# Inicializar o modelo de IA
chat = ChatGroq(model='llama-3.3-70b-versatile')

# Função para obter resposta do bot
def resposta_do_bot(pergunta):
    system_message = 'Você é um engenheiro de dados especialista chamado BrunoBot'
    template = ChatPromptTemplate.from_messages([
        ('system', system_message),
        ('user', pergunta)
    ])
    chain = template | chat
    return chain.invoke({}).content

# Interface com Streamlit
st.title("🤖 BrunoBot - Seu Engenheiro de Dados Virtual")

# Inicializar o estado da sessão para a pergunta atual e resposta
if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = None
    
if "resposta_atual" not in st.session_state:
    st.session_state.resposta_atual = None

# Campo de entrada para o usuário
pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:
    # Atualizar a pergunta atual
    st.session_state.pergunta_atual = pergunta
    
    # Obter resposta do bot
    resposta = resposta_do_bot(pergunta)
    st.session_state.resposta_atual = resposta
    
    # Limpar a interface (não necessário, o Streamlit recarrega a página)
    
# Exibir apenas a conversa atual, se existir
if st.session_state.pergunta_atual:
    st.chat_message("user").write(st.session_state.pergunta_atual)
    
if st.session_state.resposta_atual:
    st.chat_message("assistant").write(st.session_state.resposta_atual)
