from operator import itemgetter
from typing import List
from langchain.docstore.document import Document
from langchain_core.runnables import RunnableParallel
from generate.prompt import ANSWER_PROMPT
from modules.llm import llm


async def ask_chat(docs: List[Document], question: str) -> str:

    rag_chain = (RunnableParallel(
        context=itemgetter("context"),
        question=itemgetter("question")
    ) | RunnableParallel(
        answer=(ANSWER_PROMPT | llm),
        docs=itemgetter("context")
    ))

    response = await rag_chain.ainvoke({"context": docs, "question": question})
    return response
