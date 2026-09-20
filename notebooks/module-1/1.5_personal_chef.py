from dotenv import load_dotenv

load_dotenv()

from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient

tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:

    """Search the web for information. Takes simple string input and return a dictionary of results. DO NOT INPUT A DICTIONARY OF OBJECT."""

    return tavily_client.search(query=query)    

system_prompt = """

You are a personal chef. The user will give you a list of ingredients they have left over in their house.

Using the web search tool, search the web for recipes that can be made with the ingredients they have.

Return recipe suggestions and eventually the recipe instructions to the user, if requested.

"""
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

llm = ChatOllama(model="llama3.2", temperature=0.3)

agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt=system_prompt
)