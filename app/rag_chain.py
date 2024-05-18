from operator import itemgetter
from typing import TypedDict
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from app.doc_retriever import vector_store
from app.prompt import ANSWER_PROMPT

load_dotenv()

llm = ChatOpenAI(
    temperature=0,
    model='gpt-4-1106-preview',
    streaming=True
)


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
