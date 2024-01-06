import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="André Zanini", page_icon="🧑‍💻", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Carregar assets
lottie_coding_pc = "https://lottie.host/941a0b95-a67b-4b6f-bc1e-c36b6a4ab8ec/gbl3Qpyi3x.json"
lottie_coding_hello = "https://lottie.host/cccc3d60-af7b-4cfe-8974-e910ae3e20e2/IpzviRqcnK.json"


# Header
hleft_column, hright_column = st.columns(2)
with hleft_column:
    st.subheader("Oi, meu nome é André Luis Piratello Zanini :wave:")
    st.title("Estudante de programação UNIFIO, Ourinhos SP")
    st.write("Eu sou apaixonado por Python e criação de jogos, estou estudando Godot Engine na linguagem C# e GDscript, sempre buscando uma forma de deter mais conhecimento e ser mais eficiente.")
    st.write("Email: andre.piratello@hotmail.com")
with hright_column:
    st_lottie(lottie_coding_hello, height=300, key="hello_coding")


# Oque eu faço
with st.container():
    st.write("---")
    aleft_column, aright_column = st.columns(2)
    with aleft_column:
        st.header("O que eu faço")
        st.write("##")
        st.write(
            """
            Desenvolvo soluções de problemas em Python e aplicativos úteis.
            - Aplicativo de previsão do tempo usando API 'openweathermap'.
            - Aplicativo que transcreve oque foi dito e passa para o jogo 'Minecraft'.
            - Machine Learning para detecção de lesões (em desenvolvimento)
            - Vários projetos de bots para o Discord
            Se soa interessante para você, meu Linkedin e Github estão no final da página
                 """)
    with aright_column:
        st_lottie(lottie_coding_pc, height=300, key="pc_coding")


st.write("[GitHub >](https://github.com/PiratelloLuis)")
st.write("[Linkedin >](https://www.linkedin.com/in/andré-luis-piratello-zanini-879265217/)")
st.write("[Instagram >](https://www.instagram.com/piratelloz/)")
