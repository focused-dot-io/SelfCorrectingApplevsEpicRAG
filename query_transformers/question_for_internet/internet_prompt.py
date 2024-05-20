from langchain_core.prompts import PromptTemplate

rewrite_prompt = """
Given the query: {question}
You a question re-writer that converts an input question to a better version that is optimized 
for web search. Look at the input and try to reason about the underlying semantic intent / meaning.
The question may be about the epic vs apple lawsuit. If it seems to be about the lawsuit, mention the lawsuit
in the question context. If it doesn't pertain to the lawsuit then rewrite it for an internet search.

Answer only with a newly rephrased question. Do not give tips for optimization.
 """

INTERNET_PROMPT = PromptTemplate(template=rewrite_prompt, input_variables=["question"])
