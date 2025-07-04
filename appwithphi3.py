import streamlit as st
from datetime import datetime
import requests
import json
import time

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

# OLLAMA INTEGRATION - MODIFY THIS SECTION AS NEEDED
def get_bot_response(user_message):
    """
    Function to get response from Ollama running locally with Phi-3 model.
    Make sure Ollama is running and Phi-3 model is available.
    """
    
    try:
        # Ollama API endpoint (default local)
        ollama_url = "http://localhost:11434/api/generate"
        
        # Prepare the request payload
        payload = {
            "model": "phi3",  # Make sure you have phi3 model pulled in Ollama
            "prompt": user_message,
            "stream": False  # Set to False to get complete response at once
        }
        
        # Make request to Ollama
        response = requests.post(
            ollama_url, 
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=120  # 120 second timeout
        )
        
        if response.status_code == 200:
            result = response.json()
            bot_response = result.get("response", "Sorry, I couldn't generate a response.")
            return bot_response.strip()
        else:
            return f"Error: Ollama API returned status code {response.status_code}"
            
    except requests.exceptions.ConnectionError:
        return "❌ Error:Cannot Connect to Ollama. Make sure Ollama is running on localhost:11434" 
    
    except requests.exceptions.Timeout:
        return "⏱️ Error: Request timed out. The model might be taking too long to respond."
    
    except Exception as e:
        return f"❌ Error: {str(e)}"
    

# App Title
st.title("🤖Phi-3 Chatbot(Ollama)")
st.markdown("*Powered by Phi-3 via Ollama*")

#main chat interface
st.subheader("💬Chat ")

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
        
#Other buttons outside the form
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
    
    # Reset typing indicator
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


