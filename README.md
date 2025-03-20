# Self Correcting Apple vs Epic RAG

This application demonstrates a chatbot using a self corrective methodology with LangGraph.
Reference documents from the Apple v Epic lawsuit were loaded into a vector store. 
A user can ask questions about the lawsuit. 

We look for relevant sources, if half aren't relevant, we rephrase the question and try to retrieve sources again.
If the sources still aren't relevant, we ask the internet. Then respond to the user's query.
