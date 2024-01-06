import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Sobre mim", page_icon="🧑‍💻", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Carregar assets
lottie_pc_url = "https://lottie.host/941a0b95-a67b-4b6f-bc1e-c36b6a4ab8ec/gbl3Qpyi3x.json"
lottie_hello_url = "https://lottie.host/cccc3d60-af7b-4cfe-8974-e910ae3e20e2/IpzviRqcnK.json"
lottie_hello = load_lottieurl(lottie_hello_url)
lottie_pc = load_lottieurl(lottie_pc_url)

# Header
hleft_column, hright_column = st.columns(2)
with hleft_column:
    st.subheader("Oi, meu nome é André Luis :wave:")
    st.title("Estudante de programação UNIFIO, Ourinhos SP")
    st.write(
        "Eu sou apaixonado por Python e criação de jogos, estou estudando Godot Engine na linguagem C# e GDscript, sempre buscando uma forma de deter mais conhecimento e ser mais eficiente.")
with hright_column:
    st_lottie(lottie_hello, height=300, key="hello")

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
        st_lottie(lottie_pc, height=300, key="pc")

    contact_form = """
    <form action="https://formsubmit.co/andre.piratello@hotmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Seu nome" required>
         <input type="email" name="email" placeholder="Seu email" required>
         <textarea name="message" placeholder="Sua mensagem aqui" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    fleft_column, fright_column = st.columns(2)
    with fleft_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with fright_column:
        st.empty()

st.write("---")
st.write("[GitHub >](https://github.com/PiratelloLuis)")
st.write("[Linkedin >](https://www.linkedin.com/in/andré-luis-piratello-zanini-879265217/)")
st.write("[Instagram >](https://www.instagram.com/piratelloz/)")
