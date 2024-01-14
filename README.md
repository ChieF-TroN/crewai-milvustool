# crewai-milvustool
Milvus Vector Database implementation for CrewAI using Ollama

[CrewAI](https://github.com/joaomdmoura/crewAI)
[Milvus](https://milvus.io/)
[Ollama](https://ollama.ai)

Currently you will need to update the following for it to work correctly for your environment:

1. Make sure you have the correct Ollama Model defined.
2. Make sure that the Milvus DB connection info is correct.

Usage Example:

```
from MilvusCrewAITool import MilvusTool

db_store = Tool(
    name="Store data",
    func=MilvusTool().store_documents,
    description="Store documents and other data to the vector database",
)

db_retrieve = Tool(
    name="Retrieve data",
    func=MilvusTool().retrieve_documents,
    description="Retrieve documents and other data from the vector database",
)

data_scraper = Agent(
    role='Data Scraper',
    goal='Scrape financial websites for market trends and store data into the vector database',
    backstory=f"""As the Data Scraper, your role is to collect data from financial websites,
    focusing on market trends. Utilize web scraping techniques to gather relevant information.
    Store the collected data into the vector database for further analysis.""",
    verbose=True,
    allow_delegation=True,
    tools=[db_store, db_retrieve],
)
```