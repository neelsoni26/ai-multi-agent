from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os
import arxiv
from typing import List, Dict, AsyncGenerator
from autogen_agentchat.teams import RoundRobinGroupChat
import asyncio

load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]

openai_brain = OpenAIChatCompletionClient(
    api_key=api_key,
    model="gpt-4o-mini"
)

def arxiv_search(query: str, max_results: int = 5) -> List[Dict]:
    """Return a companct list of arXiv papers matching the query.
    Each element contains: ``title``, ``authors``, ``summary``, and ``published`` and ``pdf_url``. The helper is wrapped as an Autogen **FunctionTool** below so it can be invoked by agents through the normal tool-use mechanism.
    """
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    client = arxiv.Client()
    papers: List[Dict] = []
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "authors": [author.name for author in result.authors],
            "published": result.published.strftime("%Y-%m-%d"),
            "summary": result.summary,
            "pdf_url": result.pdf_url
        })
    return papers

arxiv_research_agent = AssistantAgent(
    name="arxiv_research_agent",
    description="An agent that searches for papers on arXiv",
    model_client=openai_brain,
    tools= [arxiv_search],
    system_message="Given a user topic, think of the best arXiv query. When the tool returns, choose exactly the number of papers requested and pass them to the concise JSON format to the sumamarizer."
)

summarize_agent = AssistantAgent(
    name="summarize_agent",
    description="An agent that summarizes the results",
    model_client=openai_brain,
    system_message="You are an expert researcher. When you receive the JSON list of "
    "papers, write a literature-review style report in Markdown: \n " \
    "1. Start with a 2-3 sentence introduction of the topic. \n" \
    "2. Then include one bullet per paper with: title (as Markdown "
    "link), authors, the specific problem tackled, and its key "
    "contribution. \n" \
    "3. Close with a single-sentence takeaway.",
)

team = RoundRobinGroupChat(
    participants=[arxiv_research_agent, summarize_agent],
    max_turns=2
)

async def run_team():
    task = "Conduct a literature review on the topic - Autogen and return exactly 5 papers."
    async for msg in team.run_stream(task=task):
        print(msg)

if __name__ == "__main__":
    asyncio.run(run_team())