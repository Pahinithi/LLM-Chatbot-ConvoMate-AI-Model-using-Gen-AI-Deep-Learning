# ConvoMate AI Model
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="ConvoMate AI Model",
    page_icon=":brain:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for enhanced UI/UX
st.markdown("""
    <style>
        /* Background styling */
        .stApp {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Title styling */
        h1 {
            color: #005f73;
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        /* Chat message bubbles */
        .st-chat-message-user {
            background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);
            border-radius: 20px;
            padding: 15px;
            margin: 10px 0;
            font-size: 1.1em;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .st-chat-message-user:hover {
            transform: scale(1.02);
        }

        .st-chat-message-assistant {
            background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
            border-radius: 20px;
            padding: 15px;
            margin: 10px 0;
            font-size: 1.1em;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .st-chat-message-assistant:hover {
            transform: scale(1.02);
        }

        /* Input box styling */
        .st-chat-input {
            border: 2px solid #005f73;
            border-radius: 25px;
            padding: 12px;
            font-size: 1.2em;
            width: 100%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Button styling */
        .stButton>button {
            background-color: #005f73;
            color: white;
            border: none;
            border-radius: 25px;
            padding: 10px 20px;
            font-size: 1.1em;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #0a9396;
            transform: scale(1.05);
        }

        /* Footer styling */
        footer {
            text-align: center;
            font-size: 1.2em;
            color: #555555;
            margin-top: 40px;
            font-weight: bold;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("🤖 ConvoMate - ChatBot")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask ConvoMate...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

# Footer with developer credit
st.markdown("""
    <footer>
        Developed by Nithilan
    </footer>
""", unsafe_allow_html=True)
