import streamlit as st
import random
from LLM import send_to_front

chat_button_style = """
    width: 150px;
    height: 50px;
    font-size: 16px;
"""

# Creating the page configuration
st.set_page_config(
    page_title="DEEPs",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Your Biomedical Research AI Agent")

# Creating the sidebar
st.sidebar.header("DEEPs")

# if "research_mode" not in st.session_state.keys():
#     st.session_state.research_mode = st.sidebar.toggle("Research Mode", False)

if "number_of_conversations" not in st.session_state.keys():
    st.session_state.number_of_conversations = 1
    st.session_state.current_conversation_index = 1
    st.session_state.current_conversation = f"conversation_{st.session_state.current_conversation_index}"

# Creating the conversations
if "conversations" not in st.session_state.keys():
    st.session_state.conversations = dict()
    st.session_state.current_conversation = f"conversation_{st.session_state.current_conversation_index}"
    st.session_state.conversations[st.session_state.current_conversation] = [{"role": "assistant", "message": "How may I help you?"}]   

if "BOOKMARKED_LINKS" not in st.session_state.keys():
    st.session_state.BOOKMARKED_LINKS = set()

# Creating the buttons for a new chat
if st.sidebar.button("New Chat", use_container_width=True):
    st.session_state.number_of_conversations += 1
    st.session_state.current_conversation = f"conversation_{st.session_state.number_of_conversations}"
    st.session_state.conversations[st.session_state.current_conversation] = [{"role": "assistant", "message": "How may I help you?"}]

# Creatin the buttons for all the chats
for conversation_index in range(1, st.session_state.number_of_conversations + 1):
    if st.sidebar.button(f"Chat {conversation_index}", use_container_width=True):
        st.session_state.current_conversation = f"conversation_{conversation_index}"

# Display chat messages along with te lists of links
for prompt in st.session_state.conversations[st.session_state.current_conversation]:
    with st.chat_message(prompt["role"]):
        st.write(prompt["message"])
        if prompt["role"] == "assistant" and "links" in prompt.keys():
            for link in prompt["links"]:
                checkbox_id = f"checkbox_{link.replace(' ', '_')}_{prompt['message']}"
                is_checked = st.checkbox(link, key=checkbox_id)
                if is_checked:
                    st.session_state.BOOKMARKED_LINKS.add(link)

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.conversations[st.session_state.current_conversation].append({"role": "user", "message": prompt})
    with st.chat_message("user"):
        st.write(prompt)

if st.session_state.conversations[st.session_state.current_conversation][-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response, links = send_to_front(prompt)
            # Display the response
            st.markdown(response)

            # Display links
            for link in links:
                checkbox_id = f"checkbox_{link.replace(' ', '_')}"
                is_checked = st.checkbox(link, key=checkbox_id)
                if is_checked:
                    st.session_state.BOOKMARKED_LINKS.add(link)
            
            
            st.session_state.conversations[st.session_state.current_conversation].append(
                {
                    "role": "assistant",
                    "message": response,
                    "links": links,
                }
            )
            
# Display bookmarked links
st.sidebar.markdown("### Bookmarked Links")
new_bookmarked_links = st.session_state.BOOKMARKED_LINKS.copy()
for bookmarked_link in st.session_state.BOOKMARKED_LINKS:
    # create a sidebar checbkox for each bookmarked link
    checkbox_id = f"checkbox_{bookmarked_link.replace(' ', '_')}_{st.session_state.current_conversation}"
    is_checked = st.sidebar.checkbox(bookmarked_link, key=checkbox_id)
    if is_checked:
        # remove the bookmarked link if the checkbox is checked
        new_bookmarked_links.remove(bookmarked_link)
st.session_state.BOOKMARKED_LINKS = new_bookmarked_links


