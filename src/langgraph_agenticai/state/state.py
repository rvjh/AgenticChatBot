from pydantic import BaseModel, Field
from typing_extensions import TypedDict, Annotated, list
from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    Represents the state of the conversation.
    """
    messages: Annotated[list, add_messages]