
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
import os
from dotenv import load_dotenv

load_dotenv()


# NVIDIA model function
# Don't forget to put your NVIDIA_API_KEY in your .env
def nvidia_model() -> OpenAIChatModel:
    return OpenAIChatModel(
        model_name="nvidia/nemotron-3.5-super-vl-120b-a12b",
        provider=OpenAIProvider(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.environ["NVIDIA_API_KEY"]),
    )
