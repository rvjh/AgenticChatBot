import streamlit as st
from src.langgraph_agenticai.ui.streamlitui.loadui import LoadStreamlitUI
from langchain_groq import ChatGroq
from src.langgraph_agenticai.llms.groqllm import GroqLLM
from src.langgraph_agenticai.graph.graph_builder import GraphBuilder
from src.langgraph_agenticai.ui.streamlitui.display_results import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """Load the LangGraph AgenticAI app."""
    # Load the Streamlit UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input from UI.")
        return

    # Streamlit chat input
    user_message = st.chat_input("Enter your message here...")
    if not user_message:
        return

    try:
        # Configure the LLM model
        obj_llm_config = GroqLLM(user_controls_input=user_input)
        model = obj_llm_config.get_llm_model()

        if not model:
            st.error("Failed to load LLM model. Please check your API key and model selection.")
            return

        # Get use case
        usecase = user_input.get("selected_usecase")
        if not usecase:
            st.error("Please select a use case.")
            return

        # Initialize the graph with usecase
        graph_builder = GraphBuilder(model=model, usecase=usecase)
        try:
            graph = graph_builder.setup_graph()

            # Display the results
            DisplayResultStreamlit(
                usecase=usecase,
                graph=graph,
                user_message=user_message
            ).display_result_on_ui()
        except Exception as e:
            st.error(f"Error in initializing LangGraph graph: {e}")
            return

    except Exception as e:
        st.error(f"Error in initializing LangGraph AgenticAI: {e}")
        return