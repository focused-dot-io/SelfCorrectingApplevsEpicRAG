from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

template = """
Answer given the following context:
{context}

Question: {question}
"""

ANSWER_PROMPT = ChatPromptTemplate.from_template(template)

relevancy_template = """
Given the query: {question}
And the document: {evaluated_doc}

Is this document relevant to the query? Grade the document. Here's the rubric:
F: The document is completely unrelated to the question.
D: The document has minor relevance but does not align with the question.
C: The document has moderate relevance but contains inaccuracies.
B: The document aligns with the question but has minor errors or omissions.
A: The document is completely accurate and aligns perfectly with the question.

Answer only with the letter grade.
"""

RELEVANCY_PROMPT = PromptTemplate(template=relevancy_template, input_variables=["query", "evaluated_doc"])
