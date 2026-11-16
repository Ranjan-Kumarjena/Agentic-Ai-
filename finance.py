from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
load_dotenv()
def build_agent():
    return Agent(
        model=Groq(
        id="openai/gpt-oss-120b"),
        tools=[YFinanceTools(all=True),DuckDuckGoTools()],
        markdown=True,
       

        add_datetime_to_context=True,
        
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["use given tools when ever possible.Format your response using markdown and use tables to display data where possible."]
    )


agent=build_agent()

agent.print_response("share the MSFT stock price in INR and analyst recommendation ?")