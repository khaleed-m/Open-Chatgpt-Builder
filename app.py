#pip install streamlit  commit msg

import streamlit as st #user interface
from datetime import datetime
import requests
import json

# Set page configuration
st.set_page_config(
    page_title="Chatbot",
    # page_icon=":robot:",
    # layout="wide",
    # initial_sidebar_state="expanded"
)

# Function to get the current time
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(
            {
                # "timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M
                "role" : "assistant",
                "content" : "Hello!,I am smart chartbot. How can I assist you today?"
            }
        )


if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

st.title("offline LLM")
st.markdown("This is a simple chatbot application using Streamlit and a local LLM model.")

st.subheader("Chat with the bot")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.info(message["content"])
    else:
        st.success(message["content"])

if st.session_state.is_typing:
    st.markdown("**Bot is typing...**")
    st.warning("Typing...")

st.markdown("---")
st.subheader("Your Message")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here:", key="user_input")
    submit_button = st.form_submit_button(label="Send Message" ,type="primary")

