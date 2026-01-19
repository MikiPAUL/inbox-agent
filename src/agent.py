"""
LESSON 1: Provider-agnostic LLM setup

Notice how we use a factory pattern - the get_llm() function returns
the right LLM based on config. Your code doesn't care which provider it is!
"""

from langchain.agents import create_agent
from dotenv import load_dotenv

from tools import get_emails, create_draft

load_dotenv()

def call_llm(user_message: str) -> str:
    """A simple LLM call - still NOT an agent yet!"""
    agent = create_agent(
        "groq:llama-3.3-70b-versatile", 
        tools=[get_emails, create_draft],
        system_prompt="You are an email personal assistant"
    )

    result = agent.invoke({"messages": [{"role": "user", "content": user_message}]})
    return result["messages"][-1].content


if __name__ == "__main__":
    result = call_llm("Can you analysis whether the emails that I have received is important or not and create a draft asking why are the sending spam email?")
    print(result)
