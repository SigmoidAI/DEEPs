import streamlit as st
from tools import generate_response

BOOKMARKED_LINKS = []

# Creating the page configuration
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

            response, links = generate_response(prompt) 
            # write the output having the response string and afterwards the links in a mardown checkbox
            # additioanlly add a button to bookmark the link and a continuous check to see if the button is pressed
            # if it is pressed add the link to the bookmarked links list

            st.markdown(
                f"""
                {response} 
                """
            )
