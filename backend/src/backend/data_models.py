from dotenv import load_dotenv
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
from pydantic import BaseModel, Field

load_dotenv()


# embedding model here:
embedding_model = get_registry().get("cohere").create(name="embed-multilingual-v3.0")


# Class Paragraf is used to create the vector embeddings
class Paragraph(LanceModel):
    doc_id: str
    title: str
    paragraph_nr: str
    law: str
    content: str 
    embed_text: str = embedding_model.SourceField()
    embedding: Vector(embedding_model.ndims()) = embedding_model.VectorField()  # type: ignore


# BaseModel class for prompt


class Prompt(BaseModel):
    prompt: str = Field(
        description="prompt from user. If the prompt is empty consider it as missing."
    )


# response from the RAG
# - maybe include title and paragraf nr in the answer instead but test it?
class RagResponse(BaseModel):
    #filename: str = Field("filename of the retrieved file.")
    #filepath: str = Field("filepath to the retrieved file")
    paragraph_nr: str = Field(
        description="Number of the paragraph the answer is based on, e.g. '26' or '6 a'. Must be one of the retrieved paragraphs."
    )

    # law_nr: str = Field(description="law number in this format 'Lag()") - only one law
    title: str = Field(description="Heading of that paragraph, copied from the retrieved paragraphs."
    )
    answer: str = Field(
        description="Answer in Swedish, based only on the retrieved paragraphs."
    )
    abstained: bool = Field(
    description="True if the answer cannot be found in the retrieved paragraphs."
)
