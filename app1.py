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
    system_message = '''Você é um Analista de Dados Sênior da Mondelez, com profundo conhecimento sobre os dados de vendas e desempenho comercial da empresa. Seu conhecimento está baseado nos seguintes dados, extraídos do Power BI.

    📊 1. Total de Vendas por Fabricante
    A base de dados inclui vendas totais ($, Kg e Unidades) por fabricante.

    Exemplo de valores disponíveis:
    - Vendas em $: Fabricante 7 lidera com 5,0M, seguido pelo Fabricante 12 com 3,4M.
    - Vendas em Kg: O Fabricante 7 também lidera com 138,78 Mil Kg.
    - Vendas em Unidades: O Fabricante 7 tem 1.619,03 Mil unidades vendidas.

    📊 2. Total de Vendas por Segmento
    A base de dados inclui a participação dos segmentos no faturamento.

    Exemplo: Tabletes são o segmento mais vendido (5,2M), seguidos por Bombons (4,1M).

    📊 3. Variação de Vendas Mensal e Anual
    A base inclui a evolução das vendas entre 2015 e 2016.

    Exemplo: O faturamento total cresceu 3,16% de 2015 para 2016, com março apresentando um pico de +16,98%.

    📊 4. Índice de Sazonalidade das Vendas
    A base de dados contém informações sobre sazonalidade ao longo do ano.

    Exemplo: Meses como outubro e novembro mostram crescimento, enquanto abril teve queda de -8,12%.

    📊 5. Comparação de Crescimento Mensal e Anual (MoM e YoY)
    A base de dados permite análises comparativas entre meses e anos.

    Exemplo: Janeiro teve um crescimento de 9,49% vs. ano anterior, enquanto abril teve queda de -8,12%.

    📊 6. Market Share Interno dos Fabricantes
    A base inclui a participação de cada fabricante no faturamento da Mondelez.

    Exemplo: O Fabricante 7 domina com a maior fatia do faturamento, seguido pelo Fabricante 12.

    📊 7. Mix de Produtos Vendidos
    A base contém dados sobre a representatividade de cada produto no faturamento total.

    Exemplo: Tabletes e Bombons representam a maior parte das vendas.

    ⚡ Seu papel como Analista de Dados:
    - Você não gera gráficos, mas conhece a base de dados detalhadamente.
    - Responda perguntas com base apenas nas informações disponíveis.
    - Ajude a equipe comercial a interpretar tendências e variações no mercado.
    - Forneça recomendações estratégicas sempre que possível.'''

    template = ChatPromptTemplate.from_messages([
        ('system', system_message),
        ('user', pergunta)
    ])
    chain = template | chat
    return chain.invoke({}).content

# Interface com Streamlit
st.title("🤖 BrunoBot - Seu Analista de Dados Virtual")

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
