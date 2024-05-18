import os

from dotenv import load_dotenv
from langchain_community.vectorstores import PGVector
from langchain_openai import OpenAIEmbeddings

from app.config import PG_COLLECTION_NAME, EMBEDDING_MODEL

load_dotenv()

vector_store = PGVector(
    collection_name=PG_COLLECTION_NAME,
    connection_string=os.getenv("POSTGRES_URL"),
    embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL),
)


def retrieve_docs(question: str):
    return vector_store.similarity_search_with_relevance_scores(query=question, k=5)


print(retrieve_docs("Where were the court proceedings?"))
