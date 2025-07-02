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
    st.session_state.messages = [
        st.session_state.messages.append(
            {
                # "timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M
                "role" : "assistant",
                "content" : "Hello!,I am smart chartbot. How can I assist you today?"
            }
        )
    ]

if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

