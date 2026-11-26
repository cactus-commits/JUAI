from fastapi import FastAPI
# import ragagent
from backend.data_models import Prompt
import logfire

# Setup fastapi
app = FastAPI()


# Endpoint for JUAI - bot
@app.post("JUAI/ask")
async def rag_documentation(query: Prompt):
    result = await  # run ragagent here

    return result.output
