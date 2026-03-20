from typing import List

from app.core.config import settings
from app.core.constants import DEFAULT_FALLBACK_ANSWER
from app.models.response_models import ChatResponse, RetrievedChunkResponse
from app.services.generation_service import GenerationService
from app.services.retrieval_service import RetrievalService


class RAGPipeline:
    def __init__(self) -> None:
        self.retrieval_service = RetrievalService()
        self.generation_service = GenerationService()

    def ask(self, question: str, top_k: int) -> ChatResponse:
        retrieved_chunks = self.retrieval_service.retrieve(question=question, top_k=top_k)
        context = self._build_context(retrieved_chunks)
        answer = (
            self.generation_service.generate(question=question, context=context)
            if retrieved_chunks
            else DEFAULT_FALLBACK_ANSWER
        )
        return ChatResponse(question=question, retrieved_context=retrieved_chunks, answer=answer)

    @staticmethod
    def _build_context(retrieved_chunks: List[RetrievedChunkResponse]) -> str:
        parts = []
        for chunk in retrieved_chunks:
            text = chunk.text[: settings.MAX_CONTEXT_CHARS_PER_CHUNK]
            parts.append(
                f"[Source: {chunk.source} | Chunk ID: {chunk.chunk_id} | Score: {chunk.score:.4f}]\n{text}"
            )
        return "\n\n---\n\n".join(parts)
