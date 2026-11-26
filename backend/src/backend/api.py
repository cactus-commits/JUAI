from fastapi import FastAPI
# import ragagent
from backend.data_models import Prompt
import logfire
from backend.rag import rag_agent

# Setup fastapi
app = FastAPI()


# Initialize Logfire (reads from .env)
logfire.configure()

# Trace Pydantic AI agent runs
logfire.instrument_pydantic_ai()

# Trace incoming FastAPI requests
logfire.instrument_fastapi(app)


# Endpoint for JUAI - bot
@app.post("JUAI/ask")
async def rag_documentation(query: Prompt):
    # The user query is the prompt that the agent runs
    result = await rag_agent.run(query.prompt)

    return result.output
