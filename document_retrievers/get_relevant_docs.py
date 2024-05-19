from document_retrievers.grade_document import grade_document


def get_relevant_docs(state: dict) -> dict:
    """
    Only retrieves the documents that get a grade of A or B, (C, D, F grades are dropped)
    :param state: The current graph state
    :return: New keys added to state, documents, and retrieved docs
    """

    question = state["question"]
    docs = state["documents"]
    num_times_retrieved_docs = state["num_times_retrieved_docs"]
    graded_docs = []

    for doc in docs:
        grade = grade_document(question, doc)

        if grade.grade in ('A', 'B'):
            graded_docs.append(doc)

    print(f'Number of docs passing with grade A or B: {len(graded_docs)}\n')

    return {
        **state,
        "num_times_retrieved_docs": 1 if num_times_retrieved_docs is None else num_times_retrieved_docs + 1,
        "documents": graded_docs
    }
