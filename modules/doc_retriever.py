import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_community.vectorstores import PGVector
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings

from app.config import PG_COLLECTION_NAME, EMBEDDING_MODEL
from app.prompt import RELEVANCY_PROMPT
from modules.llm import llm

load_dotenv()

vector_store = PGVector(
    collection_name=PG_COLLECTION_NAME,
    connection_string=os.getenv("POSTGRES_URL"),
    embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL),
)


class RelevantDocsInput(TypedDict):
    question: str
    doc_text: str


def retrieve_relevant_docs(question):
    docs = vector_store.similarity_search_with_relevance_scores(query=question, k=5)

    for doc in docs:
        chain = (RunnableParallel(
            doc_text=lambda x: doc[0].page_content,
            question=RunnablePassthrough()
        ) | RELEVANCY_PROMPT
          | llm
          | StrOutputParser()).with_types(input_type=RelevantDocsInput)
        print(chain.invoke({"question": question}))
        print(doc)


retrieve_relevant_docs("Where were the court proceedings?")
