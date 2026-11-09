# BibleWaze is a Python script to localize oneself in the JW Bible app
# By Claude Païssé (Nov 2026)

#STEP 1 Importar as bibliotecas necessárias
#STEP 2 Definir a tabela de dados
#STEP 3 Definir tela de interface do usuário

#STEP 1 Importar as bibliotecas necessárias
#requerimentos do sistema
# carregar comandos do MAC
import os
# carregar comandos do Streamlit para deploy
import streamlit as st
# carregar comandos do Pandas para manipulação de dados
import pandas as pd
# carregar comandos do Plotly para gráficos
import plotly.express as px
# carregar a localidade brasileira para ordenação correta de strings
import locale
# configurar o jogo de caracteres para português do Brasil
try:
    locale.setlocale(locale.LC_COLLATE, "pt_BR.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_COLLATE, "C")
#STEP 2 Definir a tabela de dados
tabela = pd.read_csv("biblewaze.csv", sep=";", encoding="utf-8-sig")
#STEP 3 Definir tela de interface do usuário
st.write("## Sistema de localização dos livros da Bíblia no aplicativo JW Bible ")
st.markdown(
    '<h4 style="margin-left: 40px;">by Claude Païssé  © 2026',
    unsafe_allow_html=True
)
#abrir a lista para seleção do livro
livros = tabela["livro"].dropna().astype(str).str.strip()
livros = sorted(livros[livros.ne("")].unique(), key=str.casefold)
livro = st.selectbox("Livro *", ["Selecione o livro"] + livros, key="livro")

if livro == "Selecione o livro":
    st.info("Selecione um livro para continuar.")
    st.stop()

registro = tabela.loc[tabela["livro"] == livro].iloc[0]
escritura = registro["escritura"]
linha = registro["linha"]
coluna = registro["coluna"]

st.markdown(f"### Livro: {livro}")
st.markdown(f"### Escritura: {escritura}")
st.markdown(f"### Linha: {linha}")
st.markdown(f"### Coluna: {coluna}")





    