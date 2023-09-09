import os
import streamlit as st
from tools import generate_response


import uuid

st.set_page_config(
    page_title="DEEPs",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Your Biomedical Research AI Agent")
st.sidebar.header("DEEPs")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}    
    st.session_state.messages.append(message)