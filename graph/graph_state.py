from typing import TypedDict, List

from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        num_times_retrieved_docs: Number of times we have tried to retrieve docs
        documents: list of documents
        num_original_docs: how many docs we originally retrieved
    """

    question: str
    num_times_retrieved_docs: int
    documents: List[Document]
    num_original_docs: int
