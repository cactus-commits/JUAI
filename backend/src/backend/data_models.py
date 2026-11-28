from dotenv import load_dotenv
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
from pydantic import BaseModel, Field

load_dotenv()


# embedding model here:
embedding_model = get_registry().get(
    "cohere").create(name="embed-multilingual-v3.0")


# Class Paragraf is used to create the vector embeddings
class Paragraph(LanceModel):
    chunk_id: str
    paragraph_nr: str
    # content and embed_text contains same
    content: str = embedding_model.SourceField()
    embedding: Vector(embedding_model.ndims()
                      ) = embedding_model.VectorField()  # type: ignore


# BaseModel class for prompt
class Prompt(BaseModel):
    prompt: str = Field(
        description="prompt from user. If the prompt is empty consider it as missing."
    )


# Response from RAG
# - title is read from the first line of the retrieved content ("12 kap. <rubrik>")
class RagResponse(BaseModel):
    paragraph_nr: str = Field(
        description="Number of the paragraph the answer is based on, e.g. '26' or '6 a'. Must be one of the retrieved paragraphs."
    )
    # law_nr: str = Field(description="law number in this format 'Lag()") - only one law
    title: str = Field(
        description="Heading of that paragraph: the text after '12 kap.' on the first line of its retrieved content, e.g. 'Arbetsresor'."
    )
                       
    answer: str = Field(
        description="Answer in Swedish, based only on the retrieved paragraphs."
    )

# Detta dunkar inte att ha med för modellen verkar det som - ta bort??
#     abstained: bool = Field(
#     description="True if the answer cannot be found in the retrieved paragraphs."
# )
