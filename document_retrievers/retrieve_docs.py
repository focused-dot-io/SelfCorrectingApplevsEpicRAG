from modules.vector_store import vector_store


def retrieve(state: dict) -> dict:
    question = state["question"]

    docs = vector_store.similarity_search(query=question, k=5)

    print(f'Number of docs found: {len(docs)}\n')

    return {
        **state,
        "documents": docs,
        "question": question,
        "num_original_docs": len(docs)
    }
