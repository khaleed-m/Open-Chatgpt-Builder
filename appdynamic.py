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

#Function to get available models
def get_available_models():
    """
    Fetches the list of available models from the local server.

    """
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            data = response.json()
            models =[]
            for model  in data.get("models",[]):
                model_name = model.get("name", "").split(":")[0] #remove taag if present
                if model_name and model_name not in models:
                    models.append(model_name)

            return sorted(models)
        else:
            return[]
    except:
        return []
    
#OLLAMA INTEGRATION -   DYNAMIC MODEL SELECTION
def get_bot_response(user_message, model_name):
    """Function to get response from ollama running locally with selected model.
    Make sure ollama is running and the selected model is available.""" 

    try:
        #ollama API endpoint
        ollama_url = "http://localhost:11434/api/generate"

        if model_name == 'qwen3':
            model_name = 'qwen3-0.6b'  # Use the specific chat model for Qwen3
        payload = {
            "model": model_name,
            "prompt": user_message,
            "stream": False, #set to False to get complete response at once
        }
        print(payload)
        #make request to ollama API
        response = requests.post(
            ollama_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=60 #60 second timeout for larger models
        )

        if response.status_code == 200:
            result = response.json()
            bot_response = result.get("response", "Sorry, something went wrong.")
            return bot_response.strip()
        else:
            return f"Error: ollama API returned status code {response.status_code}"
    
    except requests.exceptions.ConnectionError:
        return "✖️ Error: Cannot connect to ollama server. Please ensure it is running on localhost:11434"
    
    except requests.exceptions.Timeout:
        return "✖️ Error: Request to ollama server timed out. Please try again later."
    
    except Exception as e:
        return f"✖️ Error: {str(e)}. Please check the server logs for more details."
    
#App Title and Description
st.title(f"🤖 AI Chatbot ({st.session_state.selected_model.upper()})")
st.markdown("*Powered by Ollama*-Multi-Model Local LLMs")

#Main chat area
st.subheader("💬 Chat")

#Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.info(f"**You:** {message['content']}  \n*{message['timestamp']}*")
