import streamlit as st

st.set_page_config(page_title="Projeto Saúde", layout="centered")

st.title("🌿 Projeto Saúde")
st.markdown("## Bem-vindo! Escolha um tema para explorar:")

st.page_link("Ganhar_Peso.py", label="💪 Como Ganhar Peso")
st.page_link("Perder_Peso.py", label="🔥 Como Perder Peso")
st.page_link("Vida_Jejum.py", label="⏳ Vida com Jejum")
st.page_link("Doce_Veneno.py", label="🍭 Doce Veneno")
