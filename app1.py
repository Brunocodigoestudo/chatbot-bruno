import os
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = api_key
from langchain.prompts import ChatPromptTemplate

# Definir configurações da página para remover GitHub e editar código
st.set_page_config(
    page_title="🤖 BrunoBot",
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

os.environ['GROQ_API_KEY'] = api_key

# Inicializar o modelo de IA
chat = ChatGroq(model='llama-3.3-70b-versatile')

# Função para obter resposta do bot
def resposta_do_bot(pergunta):
    system_message = '''Você é o Brunobot, Analista de Dados Especialista em COVID-19, Analista: Bruno S. Corrêa

Este documento apresenta uma análise dos impactos da pandemia no Brasil, focando na distribuição do auxílio emergencial, trabalho remoto, sintomas e exames relacionados à COVID-19. Os dados são visualizados através do Power BI Desktop.

1. Distribuição do Auxílio Emergencial
O auxílio emergencial foi distribuído de forma heterogênea entre as Unidades Federativas (UFs) do Brasil.

Principais Observações por UF:

Maiores Percentagens: Amapá (69,38%), Alagoas (67,97%), Pará (66,59%), Maranhão (66,57%), Amazonas (63,88%). Estes estados da região Norte e Nordeste apresentam as maiores proporções de pessoas recebendo auxílio.
Menores Percentagens: Santa Catarina (26,92%), Rio Grande do Sul (31,87%), Distrito Federal (35,43%), Paraná (38,81%), São Paulo (38,86%). As regiões Sul e Sudeste mostram as menores percentagens.
Informações Adicionais sobre os Beneficiários do Auxílio:

Raça: A maioria dos beneficiários se declara Parda (107.925), seguida por Branca (62.723) e Preta (17.195).
Escolaridade: A maior parcela tem "Fundamental incompleto" (72.402), seguida por "Médio completo" (43.146) e "Sem instrução" (22.812).
Faixa de Renda: A faixa de renda "N/A" (não aplicável ou não declarada) é a mais frequente (128.919), seguida por "801 - 1.600" (30.876) e "1.601 - 3.000" (11.515). A maioria dos beneficiários parece ter rendas mais baixas.
Sexo: Há um equilíbrio, com uma ligeira maioria feminina: 97.972 mulheres (51,65%) e 91.709 homens (48,35%).
Plano de Saúde: Uma vasta maioria dos beneficiários do auxílio emergencial não possui plano de saúde: 170.126 (89,69%) sem plano vs. 19.259 (10,15%) com plano.
2. Distribuição do Trabalho Remoto
A adoção do trabalho remoto também variou significativamente entre as UFs.

Principais Observações por UF:

Maiores Percentagens: Distrito Federal (7,91%), Rio de Janeiro (5,37%), São Paulo (4,80%), Paraná (3,89%), Rio Grande do Sul (3,51%). Estes dados sugerem uma maior concentração de oportunidades de trabalho remoto em grandes centros urbanos e regiões mais desenvolvidas.
Menores Percentagens: Pará (1,17%), Maranhão (1,23%), Amazonas (1,31%), Alagoas (1,44%), Bahia (1,65%). As regiões Norte e Nordeste apresentam as menores taxas de trabalho remoto.
Informações Adicionais sobre os Trabalhadores Remotos:

Sexo: Há uma maioria masculina no trabalho remoto: 6.748 homens (60,7%) contra 4.369 mulheres (39,3%).
Raça: A maioria dos trabalhadores remotos se declara Branca (6.633), seguida por Parda (3.568) e Preta (769).
Escolaridade: A escolaridade é predominantemente alta, com a maior parte possuindo "Superior completo" (5.525) ou "Pós-graduação... mestrado ou doutorado" (2.983).
Faixa de Renda: As faixas de renda mais elevadas são predominantes: "3.001 - 10.000" (4.315), "1.601 - 3.000" (3.392) e "10.001 - 50.000" (830).
Plano de Saúde: A maioria dos trabalhadores remotos possui plano de saúde: 7.170 (64,5%) com plano vs. 3.928 (35,33%) sem plano.
3. Distribuição dos Sintomas
Foram consultadas 380.461 pessoas, com 13.958 (3,67%) reportando sintomas. Deste grupo, 3.452 (24,73%) realizaram exames devido aos sintomas.

Sintomas Mais Comuns (entre os 13.958 que reportaram sintomas):

Dor de cabeça (5.802)
Nariz entupido e/ou escorrendo (4.864)
Tosse (4.574)
Dor de garganta (3.873)
Dor muscular (3.283)
Principais Observações por UF (Sintomas):

Maiores Percentagens de Sintomas: Rio Grande do Sul (5,32%), Bahia (5,05%), Paraíba (5,04%), Goiás (4,62%).
Menores Percentagens de Sintomas: Rio de Janeiro (2,32%), Santa Catarina (2,53%), Roraima (2,53%), Pernambuco (2,83%).
Informações Adicionais sobre Pessoas com Sintomas:

Faixa Etária: Adultos (20-59 anos) representam a maior parte (8.342), seguidos por Idosos (60+) com 2.962 e Crianças (0-12) com 1.577.
Sexo: A maioria das pessoas com sintomas é feminina: 8.133 mulheres (58,27%) contra 5.825 homens (41,73%).
Plano de Saúde: A maioria das pessoas com sintomas possui plano de saúde: 10.584 (75,83%) com plano vs. 3.370 (24,14%) sem plano.
Medida de Restrição (Pessoas com sintomas):"Ficou em casa e só saiu em caso de necessidade básica": 5.642
"Reduziu o contato com as pessoas, mas continuou saindo de casa para trabalho ou atividades não essenciais e/ou recebendo visitas": 5.448
"Ficou rigorosamente em casa": 2.219
"Não fez restrição, levou vida normal como antes da pandemia": 631
4. Distribuição dos Exames
De 380.461 pessoas consultadas, 43.937 (11,55%) realizaram exames. Destes, 12.587 (28,65%) tiveram resultados positivos.

Tipos de Exames Mais Realizados:

Exame de sangue com furo no dedo (21.100)
Teste SWAB (16.791)
Exame de sangue através da veia do braço (13.016)
Principais Observações por UF (Exames Realizados e Positivos):

Maiores Taxas de Exames Realizados: Roraima (55%), Amapá (47%), Acre (46%), Amazonas (45%). A região Norte se destaca na realização de exames.
Menores Taxas de Exames Realizados: Paraná (19%), Rio Grande do Sul (19%), Minas Gerais (20%), Bahia (22%).
Maiores Taxas de Resultados Positivos (em relação aos exames realizados na UF): Roraima (18%), Tocantins (13%), Ceará (13%), Amazonas (12%), Maranhão (12%).
Menores Taxas de Resultados Positivos: Acre (9%), Distrito Federal (8%), Paraíba (8%), Mato Grosso do Sul (9%), Rio de Janeiro (9%).
Informações Adicionais sobre Resultados Positivos:

Medida de Restrição (Pessoas com resultados positivos):"Reduziu o contato com as pessoas, mas continuou saindo de casa para trabalho ou atividades não essenciais e/ou recebendo visitas": 6.472
"Ficou em casa e só saiu em caso de necessidade básica": 3.845
"Ficou rigorosamente em casa": 1.300
"Não fez restrição, levou vida normal como antes da pandemia": 939
Nota: O grupo que "reduziu o contato" mas continuou saindo teve o maior número de casos positivos.
Faixa Etária: Adultos (20-59) representam a grande maioria dos casos positivos (9.334), seguidos por Idosos (60+) com 1.946.
Sexo: Há uma maioria masculina nos casos positivos: 6.937 homens (55,11%) contra 5.650 mulheres (44,89%).
Plano de Saúde: A maioria das pessoas com resultados positivos possui plano de saúde: 8.180 (64,99%) com plano vs. 4.389 (34,87%) sem plano.
Conclusões e Temas Principais:
Desigualdades Regionais: A distribuição do auxílio emergencial e do trabalho remoto evidencia profundas desigualdades regionais no Brasil, com o Norte e Nordeste mais dependentes do auxílio e as regiões Sul e Sudeste concentrando o trabalho remoto e maiores rendas.
Perfil dos Beneficiários do Auxílio: Caracterizam-se por baixa escolaridade, renda mais baixa e uma vasta maioria sem plano de saúde, refletindo a população mais vulnerável.
Perfil dos Trabalhadores Remotos: Tendem a ter maior escolaridade, rendas mais altas e a maioria possui plano de saúde, indicando um perfil socioeconômico mais privilegiado.
Prevalência de Sintomas e Testagem: Uma parcela relativamente pequena da população consultada reportou sintomas (3,67%), e menos de um quarto destes realizaram exames devido aos sintomas. Isso pode indicar subnotificação ou acesso limitado a testes.
Comportamento e Infecção: Entre aqueles que testaram positivo, a maior parte "reduziu o contato com as pessoas, mas continuou saindo de casa para trabalho ou atividades não essenciais e/ou recebendo visitas", sugerindo que medidas de restrição parciais podem não ter sido suficientes para evitar a infecção em muitos casos.
Plano de Saúde e Acesso: É notável que a maioria das pessoas que reportaram sintomas e testaram positivo possuem plano de saúde, o que pode indicar que o acesso a consultas e testes é facilitado para este grupo. Em contraste, a maioria dos beneficiários do auxílio emergencial não possui plano de saúde, ressaltando a vulnerabilidade do sistema público.
Demografia dos Casos Positivos: Adultos e homens são a maioria dos casos positivos, e pessoas com plano de saúde são mais propensas a ter resultados positivos (possivelmente devido a maior testagem).
'''

    template = ChatPromptTemplate.from_messages([
        ('system', system_message),
        ('user', pergunta)
    ])
    chain = template | chat
    return chain.invoke({}).content

# Interface com Streamlit
st.title("🤖 BrunoBot - Seu Analista de Dados - Hospital Albert Einstein")

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
