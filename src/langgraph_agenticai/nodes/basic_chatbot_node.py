
from src.langgraph_agenticai.state.state import State


class BasicChatbotNode():
    """
    Basic chatbot node.
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state: State)-> dict:
        """
        Process the state and generate a response.
        """
        return {"messages": self.llm.invoke(state['messages'])}