from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

template = """
Answer given the following context:
{context}

Question: {question}
"""

ANSWER_PROMPT = ChatPromptTemplate.from_template(template)

relevancy_template = """
Given the query: {question}
And the document: {doc_text}

Is this document relevant to the query? Reply with 1 for Relevant or 0 for Not Relevant.
"""

RELEVANCY_PROMPT = PromptTemplate(template=relevancy_template, input_variables=["query", "doc_text"])
