import streamlit as st
from datetime import datetime
import time
import random

# Set page configuration
st.set_page_config(
    page_title="Simple Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! I'm your AI assistant. How can I help you today?",
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })

if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

 # DUMMY RESPONSE FUNCTION - MODIFY THIS LATER
def get_bot_response(user_message):
    """
    Dummy response function that returns static responses.
    Replace this function with your actual AI/chatbot logic later.
    """
    
    # Simulate processing time
    time.sleep(1)
    
    # List of dummy responses
    dummy_responses = [
        "That's an interesting question! I'm currently in demo mode.",
        "I understand what you're saying. This is a placeholder response.",
        "Thanks for your message! I'm using dummy responses for now.",
        "I'm processing your request... Actually, I'm just a demo bot!",
        "Your message has been received! This is a test response.",
        "Interesting! I'm designed to give helpful responses.",
        "I appreciate your input! I'm in demo mode currently.",
        "That's a great point! I'm cycling through pre-written responses.",
        "I'm here to help! Though I'm just a placeholder for now.",
        "Got it! This will be replaced with real AI logic later."
    ]
       