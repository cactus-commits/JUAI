from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
from pydantic import BaseModel, Field
from dotenv import load_dotenv


load_dotenv()


# embedding model here:
embedding_model = ""


# Class Paragraf is used to create the vector embeddings
class Paragraph(LanceModel):
    doc_id: str
    title: str
    paragraf_nr: str
    law: str
    content: str = embedding_model.SourceField()
    embedding: Vector(embedding_model.ndims()
                      ) = embedding_model.VectorField()  # type: ignore

# BaseModel class for prompt


class Prompt(BaseModel):
    prompt: str = Field(
        description="prompt from user. If the prompt is empty consider it as missing.")


# response from the RAG
# - maybe include title and paragraf nr in the answer instead but test it?
class RagResponse(BaseModel):
    filename: str = Field("filename of the retrieved file.")
    filepath: str = Field("filepath to the retrieved file")
    paragraf_nr: str = Field(
        description="Number of the paragraf from the retrieved file")
    law_nr: str = Field(description="law number in this format 'Lag()")
    title: str = Field(
        description="Title of the paragraf based on the retrieved file")
    answer: str = Field(
        description="answer based on the retrieved file, if the law is exchanged within the future mention both laws and when they start or ceases to apply (by date)")
