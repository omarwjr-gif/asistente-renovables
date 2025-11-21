import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Asistente IA Renovables", page_icon="⚡")

st.title("⚡ Asistente Virtual – Energías Renovables (Gemini)")

# Cargar API Key de Gemini desde Secrets
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Historial de chat
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hola, soy tu asistente de Energías Renovables. ¿En qué te ayudo?"}
    ]

# Mostrar historial
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Entrada del usuario
prompt = st.chat_input("Escribe tu pregunta…")

if prompt:
    # Guardar mensaje usuario
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Llamada a Gemini
    modelo = genai.GenerativeModel("gemini-1.5-flash")
    response = modelo.generate_content(prompt)
    answer = response.text

    # Guardar respuesta IA
    st.session_state["messages"].append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
