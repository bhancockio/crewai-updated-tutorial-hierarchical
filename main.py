from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from file_io import save_markdown
import os
#from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = "NA"
# Initialize the agents and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

# Initialize the OpenAI GPT-4 language model
OpenAIGPT4 = ChatOpenAI(
    model = "crewai-llama3.1:latest", #llama3-groq-tool-use:latest #arcee-ai/arcee-agent:latest phi3:medium crewai-llama3.1:latest
    base_url = "http://localhost:11434/v1"
    )



# Instantiate the agents
editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler_agent()

# Instantiate the tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
compile_newsletter_task = tasks.compile_newsletter_task(newsletter_compiler, [analyze_news_task], save_markdown)

# Form the crew
crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.hierarchical,
    #planning=True,
    #planning_llm=OpenAIGPT4,
    manager_llm=OpenAIGPT4,
    verbose=True
)

while True:
    # Kick off the crew's work
 result = crew.kickoff()

    # Print the results
 print("Crew Work Results:")
 print(str(result))
 save_markdown # type: ignore 
