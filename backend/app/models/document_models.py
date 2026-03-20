from pydantic import BaseModel


class Document(BaseModel):
    document_id: str
    source: str
    text: str


class DocumentChunk(BaseModel):
    chunk_id: str
    document_id: str
    source: str
    text: str
    chunk_index: int
