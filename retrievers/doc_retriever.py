import math

from modules.vector_store import vector_store

from retrievers.grade_document import grade_document

k = 5


def retrieve_relevant_docs(question):
    print(math.ceil(k/2))
    docs = vector_store.similarity_search(query=question, k=k)
    graded_docs = []
    for doc in docs:
        grade = grade_document(question, doc)

        if grade.grade in ('A', 'B'):
            graded_docs.append(doc)

    # if(math.ceil(k/2) )


retrieve_relevant_docs("Where is apple located?")
