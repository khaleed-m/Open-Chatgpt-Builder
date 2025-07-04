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

# Create a form for input to handle submission properly
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "Type your message:",
        placeholder="Ask me anything..."
    )
    
    # Form submit button
    send_button = st.form_submit_button("📤 Send Message", type="primary")

# Other buttons outside the form
col1, col2 = st.columns([1, 1])

with col1:
    clear_button = st.button("🗑️ Clear Chat")

with col2:
    export_button = st.button("💾 Export Chat")

# Handle send message
if send_button and user_input.strip():
    # Add user message to chat
    current_time = datetime.now().strftime("%H:%M:%S")
    st.session_state.messages.append({
        "role": "user",
        "content": user_input.strip(),
        "timestamp": current_time
    })
    
    # Set typing indicator
    st.session_state.is_typing = True
    st.rerun()
# Handle bot response
if st.session_state.is_typing:
    # Get bot response
    user_message = st.session_state.messages[-1]["content"]
    bot_response = get_bot_response(user_message)
    
    # Add bot response to chat
    current_time = datetime.now().strftime("%H:%M:%S")
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response,
        "timestamp": current_time
    })
    
    # Remove typing indicator
    st.session_state.is_typing = False
    st.rerun()

# Handle clear chat
if clear_button:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! I'm your AI assistant. How can I help you today?",
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })
    st.session_state.is_typing = False
    st.success("Chat cleared!")
    st.rerun()

# Handle export chat
if export_button:
    if len(st.session_state.messages) > 1:  # More than just welcome message
        chat_content = "CHATBOT CONVERSATION\n" + "="*50 + "\n\n"
        for msg in st.session_state.messages:
            role = "You" if msg["role"] == "user" else "Bot"
            chat_content += f"[{msg['timestamp']}] {role}: {msg['content']}\n\n"
        
        st.download_button(
            label="📄 Download Chat History",
            data=chat_content,
            file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )
    else:
        st.warning("No messages to export yet!")

# Sidebar with info
with st.sidebar:
    st.header("ℹ️ About")
    st.write("This is a simple chatbot demo built with Streamlit.")
    
    st.header("📊 Stats")
    total_messages = len(st.session_state.messages)
    user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
    bot_messages = len([m for m in st.session_state.messages if m["role"] == "assistant"])
    
    st.metric("Total Messages", total_messages)
    st.metric("Your Messages", user_messages)
    st.metric("Bot Messages", bot_messages)
    
    st.header("🔧 For Developers")
    st.write("To add real AI functionality:")
    st.code("""
def get_bot_response(user_message):
    # Replace this function with:
    # - OpenAI API
    # - Hugging Face models
    # - Your custom AI logic
    # - Database queries
    # - etc.
    return your_ai_response
    """)
    
    st.header("✨ Features")
    st.write("✅ Simple chat interface")
    st.write("✅ Message history")
    st.write("✅ Typing indicator")
    st.write("✅ Export functionality")
    st.write("✅ Clear chat option")
    st.write("✅ Easy to modify")

# Footer
st.markdown("---")
st.markdown("**Instructions:** Type a message and click 'Send Message' to chat with the bot!")
st.markdown("*Note: This bot currently uses dummy responses. Modify the `get_bot_response()` function to add real AI.*")