import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def app():
    st.header("Chat with AI", divider=True)
    st.write("### Converse com a IA:")

    mensagem = st.chat_input("Digite sua mensagem:")
    if mensagem:
        if "mensagens" in st.session_state:
            mensagens = st.session_state["mensagens"]
        else:
            mensagens = []
            st.session_state["mensagens"] = mensagens
        
        # mensagem do usuário
        mensagens.append({"usuario": "user", "content": mensagem})

        # resposta da IA
        resposta_ia = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=mensagem
        )
        mensagens.append({"usuario": "assistant", "content": resposta_ia.text})

        for msg in mensagens:
            with st.chat_message(msg["usuario"]):
                st.write(msg["content"])


app()
