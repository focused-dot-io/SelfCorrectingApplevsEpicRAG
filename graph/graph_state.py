from typing import TypedDict, List

from langchain_core.documents import Document


class GraphState(TypedDict):
    question: str
    num_times_retrieved_docs: int
    documents: List[Document]
    num_original_docs: int
    answer: str
    sources: List[Document]
