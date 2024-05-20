from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.utils import Output
from modules.llm import llm
from query_transformers.question_for_internet.internet_prompt import INTERNET_PROMPT


def internet_question_rewriter(question: str) -> Output:
    question_rewriter_chain = INTERNET_PROMPT | llm | StrOutputParser()
    return question_rewriter_chain.invoke({"question": question})
