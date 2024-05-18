from operator import itemgetter
from typing import TypedDict
from langchain_core.runnables import RunnableParallel
from app.prompt import ANSWER_PROMPT
from modules.llm import llm
from modules.doc_retriever import vector_store


class RagInput(TypedDict):
    question: str


final_chain = (
        RunnableParallel(
            context=itemgetter("question") | vector_store.as_retriever(),
            question=itemgetter("question")
        ) | RunnableParallel(
            answer=(ANSWER_PROMPT | llm),
            docs=itemgetter("context")
        )
).with_types(input_type=RagInput)

print(final_chain.invoke({"question": "Where were the court proceedings?"}))
