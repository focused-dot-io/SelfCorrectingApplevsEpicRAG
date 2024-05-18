from langgraph.graph import END, StateGraph
from graph.graph_state import GraphState
from document_retrievers.get_relevant_docs import get_relevant_docs
from document_retrievers.retrieve_docs import retrieve

workflow = StateGraph(GraphState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("get_relevant_docs", get_relevant_docs)

workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "get_relevant_docs")
workflow.add_edge("get_relevant_docs", END)

app_workflow = workflow.compile()
