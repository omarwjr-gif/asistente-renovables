import streamlit as st
import openai
import os

st.set_page_config(page_title="Asistente IA Renovables", page_icon="⚡")

st.title("⚡ Asistente Virtual – Energías Renovables")
st.write("Pregunta lo que necesites sobre el módulo.")

# Coge la API key desde Secrets (NO la pedirá al usuario)
openai.api_key = os.getenv("OPENAI_API_KEY")

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
    # Guardamos mensaje usuario
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Llamada a OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=st.session_state["messages"]
    )

    answer = response["choices"][0]["message"]["content"]

    # Guardamos respuesta IA
    st.session_state["messages"].append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
