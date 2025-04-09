import streamlit as st

# Configuração da página
st.set_page_config(page_title="Projeto Saúde", layout="centered")

# Título principal
st.title("🌿 Projeto Saúde")

# Espaço
st.markdown("## Escolha um dos temas abaixo:")

# Botões de navegação
if st.button("💪 Como Ganhar Peso"):
    st.success("Você clicou em: Como Ganhar Peso")

if st.button("🔥 Como Perder Peso"):
    st.success("Você clicou em: Como Perder Peso")

if st.button("⏳ Vida com Jejum"):
    st.success("Você clicou em: Vida com Jejum")

if st.button("🍭 Doce Veneno"):
    st.success("Você clicou em: Doce Veneno")
