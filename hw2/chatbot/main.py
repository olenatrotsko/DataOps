import os

import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["LLM_URL"],
    api_key="not-needed",
)

MODEL = os.environ["LLM_MODEL"]

st.title("AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
    })

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model=MODEL,
            messages=st.session_state.messages,
        )

        answer = response.choices[0].message.content
        st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
    })
