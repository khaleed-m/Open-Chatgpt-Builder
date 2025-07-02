import streamlit as st
from datetime import datetime
import time
import requests
import json

#Set page configuration
st.set_page_config(
    page_title="Simple Chatbot",
    page_icon="🤖",
    layout="centered",
    # initial_sidebar_state="expanded"
)

#Initialize session state for messages and typing status
if "messages" not in st.session_state:
    st.session_state.messages = []
    #Add initial message from the assistant
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": "Hello! I'm Your AI  assistant. How can I assist you today?",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    )

if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "phi3" # Default model

if "available_models" not in st.session_state:
    st.session_state.available_models = [] 

