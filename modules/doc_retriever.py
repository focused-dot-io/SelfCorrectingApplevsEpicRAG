from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from app.prompt import RELEVANCY_PROMPT
from modules.llm import llm
from modules.vector_store import vector_store


def retrieve_relevant_docs(question):
    docs = vector_store.similarity_search(query=question, k=5)
    graded_docs = []
    for doc in docs:
        chain = (RunnableParallel(
            evaluated_doc=lambda x: RunnablePassthrough(),
            question=RunnablePassthrough()
        ) | RELEVANCY_PROMPT
          | llm
          | StrOutputParser()
        )
        graded_docs.append({
            "grade": chain.invoke({"question": question, "evaluated_doc": doc}),
            "evaluated_doc": doc
        })
    print(graded_docs)
