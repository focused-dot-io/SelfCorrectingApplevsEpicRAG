from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from app.config import CHAT_MODEL

load_dotenv()

llm = ChatOpenAI(
    temperature=0,
    model=CHAT_MODEL,
    streaming=True
)
