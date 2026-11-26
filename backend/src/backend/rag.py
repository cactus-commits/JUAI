# Rag agent
from backend.model import nvidia_model
from pydantic_ai import Agent
from backend.data_models import RagResponse
from backend.constants import VECTOR_DB_PATH
import lancedb

# Connect to lancedb with VECTOR_DB_PATH
vector_db = lancedb.connect(uri=VECTOR_DB_PATH)

# Use nvidia mdodel
model = nvidia_model()

# Define system_prompt
# Move this later on to logfire and Prompt handling / testing
# This prompt was writtern with LLM
system_prompt = (
    "Du är en expert på inkomstskattelagen (1999:1229) och specialiserad på kapitel 12. "
    "Du hjälper användaren att hitta och förstå vad lagtexten säger. "
    "Din kunskapsbas består av kapitel 12 i inkomstskattelagen, uppdelad så att varje chunk motsvarar exakt en paragraf (t.ex. 12 kap. 1 §). "
    "Svara alltid utifrån de hämtade paragraferna. Du får använda din expertis för att göra svaret tydligare och mer sammanhängande, men inte lägga till regler som saknas i de hämtade paragraferna. "
    "Hitta aldrig på paragrafer, paragrafnummer eller lagtext. Om frågan ligger utanför de hämtade paragraferna, eller om svaret inte går att utläsa ur dem, ska du tydligt säga att du inte kan besvara frågan utifrån kapitel 12. "
    "Håll svaret kort och tydligt, kom direkt till saken och använd högst 6 meningar. "
    "Avsluta alltid med att ange vilka paragrafer du har använt som källa, i formatet 'Källa: 12 kap. X §' (flera paragrafer separeras med kommatecken). "
    "Citera lagtexten ordagrant endast när exakt ordalydelse är viktig, annars återge innehållet med egna ord. "
    "Svara på svenska."
)


# Setup the Rag Agent
rag_agent = Agent(
    model=model,
    retries=3,
    system_prompt=system_prompt,
    output_type=RagResponse  # RagResponse BaseModel is used for structured output
)
