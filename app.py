import streamlit as st
from tools import generate_response

# Creating the page configuration
st.set_page_config(
    page_title="DEEPs",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Your Biomedical Research AI Agent")
st.sidebar.header("DEEPs")

st.session_state.BOOKMARKED_LINKS = set()

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "message": "How may I help you?"}]

# Display chat messages along with te lists of links
for prompt in st.session_state.messages:
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
    st.session_state.messages.append({"role": "user", "message": prompt})
    with st.chat_message("user"):
        st.write(prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response, links = generate_response(prompt)

            # Display the response
            st.markdown(response)

            # Display links
            for link in links:
                checkbox_id = f"checkbox_{link.replace(' ', '_')}"
                is_checked = st.checkbox(link, key=checkbox_id)
                if is_checked:
                    st.session_state.BOOKMARKED_LINKS.add(link)
            
            
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "message": response,
                    "links": links,
                }
            )
            
# Display bookmarked links
st.sidebar.markdown("### Bookmarked Links")
for bookmarked_link in st.session_state.BOOKMARKED_LINKS:
    st.sidebar.markdown(f"- {bookmarked_link}")
