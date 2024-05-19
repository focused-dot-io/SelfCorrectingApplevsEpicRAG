from document_retrievers.grade_document import grade_document


def get_relevant_docs(state: dict) -> dict:
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
