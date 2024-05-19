from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv


def search_internet(question: str) -> TavilySearchResults:
    load_dotenv()
    return TavilySearchResults(k=3).invoke({"query": question})
