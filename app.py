import streamlit as st
from pages.pages import switch_page
from src.assimetry import assimetry 
st.markdown('#')

st.set_page_config(
    page_title="CATERPILLAR",
    page_icon="🐛",
    layout="centered",
    initial_sidebar_state="collapsed"
)

cols = st.columns([0.4,1,0.3])
cols[1].title("CATERPILLAR WEB")
cols[2].image(r"static/icon_default.ico", width=100)

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
""", unsafe_allow_html=True)

if st.button("Sobre", use_container_width=True):
    switch_page("sobre")


with st.container(border=True):
    st.subheader("Medidas do Ambiente")
    largura = st.number_input("Largura (m)", value=None, min_value=0.0, placeholder="Largura")
    comprimento = st.number_input("Comprimento (m)", value=None, min_value=0.0, placeholder="Comprimento")
    altura = st.number_input("Altura (m)", value=None, min_value=0.0, placeholder="Altura")
    st.subheader("Posição do Plano")
    x = st.number_input("X (m)", value=None, min_value=0.0, placeholder="X")
    y = st.number_input("Y (m)", value=None, min_value=0.0, placeholder="Y")
    z = st.number_input("Z (m)", value=None, min_value=0.0, placeholder="Z")
    st.subheader("Temperaturas")
    cols = st.columns(2)
    frontal = cols[0].number_input("Frontal (°C)", value=None, placeholder="Frontal")
    posterior = cols[1].number_input("Posterior (°C)", value=None, placeholder="Posterior")
    lat_esq = cols[0].number_input("Lateral Esquerda (°C)", value=None, placeholder="Lateral Esquerda")
    lat_dir = cols[1].number_input("Lateral Direita (°C)", value=None, placeholder="Lateral Direita")
    teto = cols[0].number_input("Teto (°C)", value=None, placeholder="Teto")
    piso = cols[1].number_input("Piso (°C)", value=None, placeholder="Piso")

    st.title('')
    if st.button("Calcular", use_container_width=True):
        inputs_list = [largura, comprimento, altura, x, y, z, frontal, posterior, lat_esq, lat_dir, teto, piso]
        check_inputs = True if None in inputs_list else False
        check_position = all([
            x not in [0.0, largura],
            y not in [0.0, comprimento],
            z not in [0.0, altura]
        ])
        if check_inputs:
            st.warning("Insira todos os dados para prosseguir", icon="ℹ️")
        elif not check_position:
            st.warning("O plano não pode estar encostado em nenhuma superfície", icon="ℹ️")
        else:
            try:
                with st.spinner('Calculando...'):
                    st.session_state['resultados'] = assimetry(largura=largura, comprimento=comprimento, altura=altura, x=x, y=y, z=z, frontal=frontal, posterior=posterior, lat_esq=lat_esq, lat_dir=lat_dir, teto=teto, piso=piso)
                    switch_page("resultados")
            except Exception as e:
                st.error(f"Ocorreu um erro ao realizar o cálculo: {e}", icon="⚠️")