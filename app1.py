import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Definir configurações da página para remover GitHub e editar código
st.set_page_config(
    page_title="🤖 BrunoBot",
    page_icon="🤖",
    layout="wide",  # ou 'centered', dependendo da sua preferência
    initial_sidebar_state="collapsed"  # Isso esconde a sidebar, removendo a opção de editar código
)

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
    system_message = '''Você é o Brunobot, Agente Analytics Engineer do Bruno Corrêa, especialista em pipelines de dados, produtos de dados e AI Agents. Você é um assistente virtual que ajuda a responder perguntas sobre dados, análises e engenharia de dados. Você pode ajudar com SQL, Python, ETL, Data Warehousing e outras tecnologias relacionadas a dados.'''

    template = ChatPromptTemplate.from_messages([
        ('system', system_message),
        ('user', pergunta)
    ])
    chain = template | chat
    return chain.invoke({}).content

# Interface com Streamlit
st.title("🤖 BrunoBot - Seu Analytics Engineer Virtual")

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
    
# Exibir apenas a conversa atual, se existir
if st.session_state.pergunta_atual:
    st.chat_message("user").write(st.session_state.pergunta_atual)
    
if st.session_state.resposta_atual:
    st.chat_message("assistant").write(st.session_state.resposta_atual)
