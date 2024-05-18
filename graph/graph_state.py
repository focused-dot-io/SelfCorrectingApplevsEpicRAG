from typing import TypedDict, List

from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        num_times_retrieved_docs: Number of times we have tried to retrieve docs
        documents: list of documents
        are_docs_relevant: whether we have documents relevant to question
    """

    question: str
    num_times_retrieved_docs: int
    documents: List[Document]
    are_docs_relevant: bool
