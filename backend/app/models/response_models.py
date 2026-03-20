from typing import List
from pydantic import BaseModel


class RetrievedChunkResponse(BaseModel):
    chunk_id: str
    document_id: str
    source: str
    text: str
    chunk_index: int
    score: float


class ChatResponse(BaseModel):
    question: str
    retrieved_context: List[RetrievedChunkResponse]
    answer: str


class IngestResponse(BaseModel):
    message: str
    documents_processed: int
    chunks_created: int
    index_saved_to: str


class HealthResponse(BaseModel):
    status: str
    app_name: str
    version: str
