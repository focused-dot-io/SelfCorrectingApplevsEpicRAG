from operator import itemgetter

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from app.prompt import RELEVANCY_PROMPT
from modules.llm import llm
from langchain.docstore.document import Document


class DocumentGrade(BaseModel):
    """Letter grade to determine relevancy of a document"""

    grade: str = Field(
        description="Document grade for relevancy, 'A', 'B', 'C', 'D', or 'F'",
    )


structured_llm = llm.with_structured_output(DocumentGrade)


def grade_document(question: str, doc: Document):
    page_content = doc
    chain = (RunnableParallel(
        evaluated_doc=itemgetter("evaluated_doc"),
        question=itemgetter("question")
    ) | RELEVANCY_PROMPT
      | structured_llm
    )

    return chain.invoke({"question": question, "evaluated_doc": page_content})
