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