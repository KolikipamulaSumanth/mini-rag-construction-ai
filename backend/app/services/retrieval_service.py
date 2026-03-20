from typing import List

from app.core.config import settings
from app.db.loader import get_index_manager, get_metadata_storage
from app.models.response_models import RetrievedChunkResponse
from app.services.embedding_service import EmbeddingService
from app.utils.similarity import passes_similarity_threshold


class RetrievalService:
    def __init__(self) -> None:
        self.embedding_service = EmbeddingService(settings.EMBEDDING_MODEL_NAME)
        self.index_manager = get_index_manager()
        self.metadata_storage = get_metadata_storage()

    def retrieve(self, question: str, top_k: int) -> List[RetrievedChunkResponse]:
        query_embedding = self.embedding_service.embed_query(question)
        index = self.index_manager.load()
        metadata = self.metadata_storage.load_chunks()

        scores, indices = index.search(query_embedding, top_k)
        results: List[RetrievedChunkResponse] = []

        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue
            chunk = metadata[idx]
            if not passes_similarity_threshold(float(score), settings.MIN_SIMILARITY_SCORE):
                continue
            results.append(
                RetrievedChunkResponse(
                    chunk_id=chunk.chunk_id,
                    document_id=chunk.document_id,
                    source=chunk.source,
                    text=chunk.text,
                    chunk_index=chunk.chunk_index,
                    score=float(score),
                )
            )
        return results
