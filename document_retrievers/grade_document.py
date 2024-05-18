from operator import itemgetter
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables.utils import Output
from document_retrievers.document_grade import DocumentGrade
from document_retrievers.relevancy_prompt import RELEVANCY_PROMPT
from modules.llm import llm
from langchain.docstore.document import Document


def grade_document(question: str, doc: Document) -> Output:
    structured_llm = llm.with_structured_output(DocumentGrade)
    page_content = doc
    chain = (RunnableParallel(
        evaluated_doc=itemgetter("evaluated_doc"),
        question=itemgetter("question")
    ) | RELEVANCY_PROMPT
      | structured_llm
    )

    return chain.invoke({"question": question, "evaluated_doc": page_content})
