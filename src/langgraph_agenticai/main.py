import streamlit as st
from src.langgraph_agenticai.ui.streamlitui.loadui import LoadStreamlitUI
from langchain_groq import ChatGroq
from src.langgraph_agenticai.llms.groqllm import GroqLLM
from src.langgraph_agenticai.graph.graph_builder import GraphBuilder, setup_graph 
from src.langgraph_agenticai.ui.streamlitui.display_results import DisplayResultStreamlit



def load_langgraph_agenticai_app():
    """Load the LangGraph AgenticAI app.
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input from UI.")
    
    user_message = st.chat_input("enter your message here...")
    if user_message:
        try:
            ## configure the LLM model here
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
            if not model:
                st.error("Failed to load LLM model.")
                return
            usecase = user_input.get("select_usecase")
            if not usecase:
                st.error("Please select a use case.")
                return

            ## graph builder
            graph_builder = GraphBuilder(model=model)
            try:
                graph = graph_builder.setup_grapg(usecase=usecase)
                DisplayResultStreamlit(usecase=usecase, graph=graph, user_message=user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error in initializing LangGraph AgenticAI: {e}")
                return
            
        
        except Exception as e:
            st.error(f"Error in initializing LangGraph AgenticAI: {e}")
            return
