from agno.agent import Agent
from tools.markdown_validator import validate_markdown

def markdown_validation_tool(text):
    return validate_markdown(text)

def create_markdown_agent():
    agent = Agent(
        name="Markdown Validator Agent",
        instructions="Validate markdown files using the provided tool.",
        tools=[markdown_validation_tool]
    )
    return agent
