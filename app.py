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
