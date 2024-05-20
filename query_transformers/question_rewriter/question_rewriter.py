from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.utils import Output
from modules.llm import llm
from query_transformers.question_rewriter.rewriting_prompt import REWRITING_PROMPT


def question_rewriter(question: str) -> Output:
    question_rewriter_chain = REWRITING_PROMPT | llm | StrOutputParser()
    return question_rewriter_chain.invoke({"question": question})
