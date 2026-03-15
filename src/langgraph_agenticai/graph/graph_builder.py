from src.langgraph_agenticai.state.state import State
from langgraph.graph import StateGraph
from langgraph.graph import StateGraph, START, END
from src.langgraph_agenticai.nodes.basic_chatbot_node import BasicChatbotNode



class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Basic chatbot graph builder. 
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self):
        """
        Setup the graph.
        """
        if usecase == "basic_chatbot":
            self.basic_chatbot_build_graph()
        
        
        

