from ask_internet.search_internet import search_internet
from langchain_core.documents import Document


def ask_the_internet(state: dict) -> dict:
    question = state["question"]
    documents = state["documents"]

    print(f"Asking the internet: {question}\n")

    web_docs = search_internet(question)
    web_results = [Document(page_content=d["content"], metadata={"source": d["url"]}) for d in web_docs]

    all_docs = documents + web_results

    return {
        **state,
        "documents": all_docs,
    }
