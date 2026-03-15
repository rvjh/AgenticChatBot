import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY")
            selected_model = self.user_controls_input.get("selected_model")

            if groq_api_key:
                llm = ChatGroq(
                    groq_api_key=groq_api_key,
                    model_name=selected_model
                )
            else:
                st.error("Please provide the Groq API Key")
                llm = None
        except Exception as e:
            st.error(f"Error in initializing Groq LLM: {e}")
            llm = None
        return llm