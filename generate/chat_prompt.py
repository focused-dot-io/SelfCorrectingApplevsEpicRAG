from langchain_core.prompts import ChatPromptTemplate

template = """
You are an expert on the Epic vs Apple lawsuit. Epic Games sued Apple after it introduced a direct billing 
mechanism to its video game, Fortnite, on iPhone.

Answer given the following context:
{context}

Question: {question}
"""

ANSWER_PROMPT = ChatPromptTemplate.from_template(template)
