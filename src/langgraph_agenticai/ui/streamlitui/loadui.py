import streamlit as st
from src.langgraph_agenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):

        st.set_page_config(
            page_title=self.config.get_page_title(),
            page_icon=":robot_face:",
            layout="wide"
        )

        st.header(self.config.get_page_title())

        with st.sidebar:

            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            groq_model_options = self.config.get_groq_model_options()

            # LLM Selection
            selected_llm = st.selectbox(
                "Select LLM",
                llm_options,
                key="select_llm"
            )

            self.user_controls["select_llm"] = selected_llm

            # API Key
            groq_key = st.text_input(
                "GROQ API KEY",
                type="password",
                value=st.session_state.get("GROQ_API_KEY", ""),
                key="GROQ_API_KEY"
            )

            self.user_controls["GROQ_API_KEY"] = groq_key

            if not groq_key:
                st.warning("Please enter your API key.")

            # Show model selector only when GROQ selected
            if selected_llm.lower() == "groq":

                selected_model = st.selectbox(
                    "Select GROQ Model",
                    groq_model_options,
                    key="selected_model"
                )

                self.user_controls["selected_model"] = selected_model

            else:
                self.user_controls["selected_model"] = None

            # Use case
            selected_usecase = st.selectbox(
                "Select Use Case Name",
                usecase_options,
                key="selected_usecase"
            )

            self.user_controls["selected_usecase"] = selected_usecase

        return self.user_controls