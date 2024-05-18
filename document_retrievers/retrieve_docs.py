from modules.vector_store import vector_store


def retrieve(state):
    """
    Retrieves the documents from the doc store
    :param state: The current graph state
    :return: New keys added to state, documents, and retrieved docs
    """

    question = state["question"]

    docs = vector_store.similarity_search(query=question, k=5)

    print(f'Number of docs found: {len(docs)}')

    return {
        **state,
        "documents": docs,
        "question": question,
        "num_original_docs": len(docs)
    }
