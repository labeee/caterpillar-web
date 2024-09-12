if __name__ == "__main__":
    import streamlit as st
    from pages.pages import switch_page

st.set_page_config(
    page_title="CATERPILLAR - RESULTADOS",
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

if st.button("Voltar", use_container_width=True):
    switch_page('app')

cols = st.columns(2)
cols[0].title("Resultados")
cols[1].subheader('')
cols[1].download_button("Baixar Resultados", data=st.session_state.get('resultados').replace('#', '').replace('---', '-'*40), file_name="resultados.txt", use_container_width=True)

with st.container(border=True):
    st.markdown(st.session_state.get('resultados'))