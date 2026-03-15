from src.langgraph_agenticai.state.state import State
from langgraph.graph import StateGraph
from langgraph.graph import StateGraph, START, END


class GraphBuilder:
    def __init__(self, model):
        self.model = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Basic chatbot graph builder. 
        """
        self.graph_builder.add_node("chatbot","")
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        
        

