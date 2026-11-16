# from agno.agent import Agent
# from agno.models.openai import OpenAIResponses
# import greenlet
# import sqlalchemy

# print("Greenlet installed successfully!")
# print("SQLAlchemy version:", sqlalchemy.__version__)

# print("Agno imported successfully!")
# print("OpenAI integration imported successfully!")
from agno.agent import Agent
import inspect

print(inspect.signature(Agent.__init__))