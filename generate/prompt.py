from langchain import hub
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer given the following context:
{context}

Question: {question}
"""

CUSTOM_PROMPT = ChatPromptTemplate.from_template(template)


ANSWER_PROMPT = hub.pull("rlm/rag-prompt")