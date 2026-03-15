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

            if not groq_api_key:
                st.error("Please provide the Groq API Key")
                return None

            if not selected_model:
                st.error("Please select a model")
                return None

            llm = ChatGroq(
                groq_api_key=groq_api_key,
                model_name=str(selected_model)  # ensure string
            )

            return llm

        except Exception as e:
            st.error(f"Error in initializing Groq LLM: {e}")
            return None