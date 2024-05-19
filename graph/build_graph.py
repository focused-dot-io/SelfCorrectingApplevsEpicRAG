from langgraph.graph import END, StateGraph
from ask_internet.ask_the_internet import ask_the_internet
from generate.generate_answer import generate_answer
from graph.decisions.decide_to_generate import decide_to_generate
from graph.graph_state import GraphState
from document_retrievers.get_relevant_docs import get_relevant_docs
from document_retrievers.retrieve_docs import retrieve
from query_transformer.query_transformer import query_transformer

graph_nodes = ["retrieve", "get_relevant_docs", "transform_query", "generate_answer", "ask_the_internet"]
workflow = StateGraph(GraphState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("get_relevant_docs", get_relevant_docs)
workflow.add_node("transform_query", query_transformer)
workflow.add_node("generate_answer", generate_answer)
workflow.add_node("ask_the_internet", ask_the_internet)

workflow.add_edge("retrieve", "get_relevant_docs")
workflow.add_conditional_edges(
    "get_relevant_docs",
    decide_to_generate,
    {
        "generate_answer": "generate_answer",
        "transform_query": "transform_query",
        "ask_the_internet": "ask_the_internet",
    }
)
workflow.add_edge("transform_query", "retrieve")
workflow.add_edge("ask_the_internet", END)
workflow.add_edge("generate_answer", END)

workflow.set_entry_point("retrieve")
app_workflow = workflow.compile()
