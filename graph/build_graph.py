from langgraph.graph import END, StateGraph
from ask_internet.ask_the_internet import ask_the_internet
from generate.generate_answer import generate_answer
from graph.decisions.decide_to_generate import decide_to_generate
from graph.graph_state import GraphState
from document_retrievers.get_relevant_docs import get_relevant_docs
from document_retrievers.retrieve_docs import retrieve
from query_transformers.question_for_internet.internet_query_transformer import internet_question_transformer
from query_transformers.question_rewriter.query_transformer import query_transformer

graph_nodes = ["retrieve", "get_relevant_docs", "transform_query", "generate_answer", "ask_the_internet"]
workflow = StateGraph(GraphState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("get_relevant_docs", get_relevant_docs)
workflow.add_node("question_rewriter", query_transformer)
workflow.add_node("internet_question_rewriter", internet_question_transformer)
workflow.add_node("generate_answer", generate_answer)
workflow.add_node("ask_the_internet", ask_the_internet)

workflow.add_edge("retrieve", "get_relevant_docs")
workflow.add_conditional_edges(
    "get_relevant_docs",
    decide_to_generate,
    {
        "generate_answer": "generate_answer",
        "question_rewriter": "question_rewriter",
        "internet_question_rewriter": "internet_question_rewriter",
    }
)
workflow.add_edge("internet_question_rewriter", "ask_the_internet")
workflow.add_edge("question_rewriter", "retrieve")
workflow.add_edge("ask_the_internet", "generate_answer")
workflow.add_edge("generate_answer", END)

workflow.set_entry_point("retrieve")
app_workflow = workflow.compile()
