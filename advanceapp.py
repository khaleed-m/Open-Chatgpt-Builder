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
    # Simple keyword-based responses
    user_message_lower = user_message.lower()
    
    if any(word in user_message_lower for word in ["hello", "hi", "hey"]):
        return "Hello there! Nice to meet you. I'm in demo mode!"
    
    elif any(word in user_message_lower for word in ["how are you", "how do you do"]):
        return "I'm doing great, thank you! I'm a demo chatbot."
    
    elif any(word in user_message_lower for word in ["bye", "goodbye"]):
        return "Goodbye! It was nice chatting with you!"
    
    elif any(word in user_message_lower for word in ["help", "what can you do"]):
        return "I'm a demo chatbot with placeholder responses. You can replace my logic with real AI!"
    
    elif any(word in user_message_lower for word in ["time", "date"]):
        current_time = datetime.now().strftime("%I:%M %p on %B %d, %Y")
        return f"The current time is {current_time}"
    
    elif any(word in user_message_lower for word in ["weather"]):
        return "I'd love to help with weather! Right now I'm just a demo, but you could add weather API here."
    
    else:
        return random.choice(dummy_responses)
   
# App Title
st.title("🤖 Simple Chatbot")
st.markdown("*A basic chatbot built with Streamlit*")

# Main chat area
st.subheader("💬 Chat")

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You** ({message['timestamp']})")
        st.info(message["content"])
    else:
        st.markdown(f"**Bot** ({message['timestamp']})")
        st.success(message["content"])

# Show typing indicator
if st.session_state.is_typing:
    st.markdown("**Bot** is typing...")
    st.warning("🤖 Thinking...")

# Input section
st.markdown("---")
st.subheader("📝 Your Message")
