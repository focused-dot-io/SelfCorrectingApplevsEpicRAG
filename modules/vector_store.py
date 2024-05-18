import os

from langchain_community.vectorstores import PGVector
from langchain_openai import OpenAIEmbeddings
from app.config import PG_COLLECTION_NAME, EMBEDDING_MODEL

vector_store = PGVector(
    collection_name=PG_COLLECTION_NAME,
    connection_string=os.getenv("POSTGRES_URL"),
    embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL),
)