from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    temperature=0,
    model='gpt-4-1106-preview',
    streaming=True
)
