from typing import TypedDict


class AgentState(TypedDict):
    question: str
    location: str
    gathered_data: str
    ranked_results: str

