if __name__ == "__main__":
    import streamlit as st
    from pages.pages import switch_page

st.set_page_config(
    page_title="CATERPILLAR - SOBRE",
    page_icon="🐛",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
<style>
    [data-testid="stBaseButton-headerNoPadding"] {
        display: none
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True,)

if st.button("Voltar", use_container_width=True):
    switch_page('app')

st.title("CATERPILLAR WEB - SOBRE")
with st.container(border=True):
    st.markdown("""O repositório no GitHub onde está a ferramenta pode ser encontrado [aqui](https://github.com/labeee/caterpillar-web).""")
    
    st.markdown(
        """
Esta é a nova versão de uma antiga ferramenta desenvolvida no LabEEE, 
uma Calculadora de Assimetria de Temperatura Radiante Plana 
(de acordo com a ISO 7726 de 1998). 

Há uma nova versão já desenvolvida com python em forma de executável, 
com desenhos do ambiente feitos em tempo real que pode ser 
encontrada [aqui](https://github.com/labeee/Caterpillar-CATeRP) 

Seu uso é simples, basta inserir todas as medidas do
ambiente conforme indicado nas caixas de entrada, na unidade de medida indicada,
e clicar no botão "Calcular".""")

    st.markdown(
        """
Assim que os cálculos forem feitos, o usuário será
redirecionado para uma nova página contendo os resultados, que
podem ser baixados selecionando o botão "Baixar Resultados" ou simplesmente
copiados para o clipboard.
""")

    with st.expander("Desenho do ambiente para referência (print da versão desktop)"):
        st.image(r'static/desenho_ambiente.png', use_column_width=True)
    
    st.markdown(
        """
Feito por Zac Milioli, LabEEE 2024
- zacmilioli@gmail.com
- [Linkedin](https://www.linkedin.com/in/zac-milioli/)
- [GitHub](https://github.com/Zac-Milioli)""")

cols = st.columns(8)
cols[2].image(r"static/icon_default.ico", width=75)
cols[3].image(r"static/icon_Sakura.ico", width=75)
cols[4].image(r"static/icon_Steel.ico", width=75)
cols[5].image(r"static/icon_Console.ico", width=75)
