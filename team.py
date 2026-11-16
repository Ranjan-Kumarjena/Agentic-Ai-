from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team
load_dotenv()
english_agent=Agent(name="English Agent", role="You answer questions in English")
hindi_agent=Agent(name="Hindi Agent", role="You answer questions in Hindi")
chines_agent=Agent(name="Chinese Agent", role="You answer questions in Chinese")

team_leader=Team(
    name="answer and translate the language ",
    members=[english_agent,hindi_agent,chines_agent],
    model=Groq(id="openai/gpt-oss-120b"),
    markdown=True,
    show_members_responses=True,
    instructions="You are a team leader and you have to answer the question in English and translate it into Hindi and Chinese."



)


team_leader.print_response("what is the capital of india ?")