from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.google import Gemini
load_dotenv()
def build_agent():
    return Agent(
        model=Groq(
        id="openai/gpt-oss-120b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are helpful and expert it department.",
        add_datetime_to_context=True
)

agent=build_agent()

agent.print_response("can you tell me what is the current news about Jensen Huang with China ?")