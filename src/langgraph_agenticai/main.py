import streamlit as st
from src.langgraph_agenticai.ui.streamlitui.loadui import LoadStreamlitUI
from langchain_groq import ChatGroq

def load_langgraph_agenticai_app():
    """Load the LangGraph AgenticAI app.
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input from UI.")
    
    user_message = st.chat_input("enter your message here...")