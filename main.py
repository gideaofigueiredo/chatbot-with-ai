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
    if not "mensagens" in st.session_state:
        st.session_state["mensagens"] = []

    for msg in st.session_state["mensagens"]:
        st.chat_message(msg["role"]).write(msg["parts"][0]["text"])
    
    if mensagem:
        
        # mensagem do usuário
        st.chat_message("user").write(mensagem)
        st.session_state["mensagens"].append({"role": "user", "parts": [{"text": mensagem}]})
        print(st.session_state["mensagens"])

        # resposta da IA com base no histórico de mensagens
        resposta_ia = client.models.generate_content(model="gemini-3-flash-preview", contents=st.session_state["mensagens"])
        st.chat_message("assistant").write(resposta_ia.text)
        st.session_state["mensagens"].append({"role": "assistant", "parts": [{"text": resposta_ia.text}]})

app()
