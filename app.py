import streamlit as st
from src.pages import switch_page
# import src.assimetry

st.set_page_config(
    page_title="CATERPILLAR",
    page_icon="🐛",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
    [data-testid="stToolbarActions"] {
        display: none
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True,)

cols = st.columns(8)
cols[2].image(r"static/icon_default.ico", width=75)
cols[3].image(r"static/icon_Sakura.ico", width=75)
cols[4].image(r"static/icon_Steel.ico", width=75)
cols[5].image(r"static/icon_Console.ico", width=75)

cols = st.columns([0.4,1,0.3])
cols[1].title("CATERPILLAR WEB")
if st.button("Sobre", use_container_width=True):
    switch_page("sobre")

with st.container(border=True):
    st.subheader("Medidas do Ambiente")
    largura = st.number_input("Largura (m)", value=None, min_value=0, placeholder="Largura")
    comprimento = st.number_input("Comprimento (m)", value=None, min_value=0, placeholder="Comprimento")
    altura = st.number_input("Altura (m)", value=None, min_value=0, placeholder="Altura")
    st.subheader("Posição do Plano")
    x = st.number_input("X (m)", value=None, min_value=0, placeholder="X")
    y = st.number_input("Y (m)", value=None, min_value=0, placeholder="Y")
    z = st.number_input("Z (m)", value=None, min_value=0, placeholder="Z")
    st.subheader("Temperaturas")
    cols = st.columns(2)
    frontal = cols[0].number_input("Frontal (°C)", value=None, placeholder="Frontal")
    posterior = cols[1].number_input("Posterior (°C)", value=None, placeholder="Posterior")
    lat_esq = cols[0].number_input("Lateral Esquerda (°C)", value=None, placeholder="Lateral Esquerda")
    lat_dir = cols[1].number_input("Lateral Direita (°C)", value=None, placeholder="Lateral Direita")
    teto = cols[0].number_input("Teto (°C)", value=None, placeholder="Teto")
    piso = cols[1].number_input("Piso (°C)", value=None, placeholder="Piso")
    if st.button("Calcular"):
        switch_page("resultados")
