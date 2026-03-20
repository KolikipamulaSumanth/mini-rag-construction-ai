from typing import List

from app.models.document_models import Document, DocumentChunk
from app.utils.text_cleaner import normalize_text


class ChunkingService:
    def __init__(self, chunk_size: int, chunk_overlap: int) -> None:
        if chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be smaller than chunk_size")
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_documents(self, documents: List[Document]) -> List[DocumentChunk]:
        all_chunks: List[DocumentChunk] = []
        for document in documents:
            all_chunks.extend(self._chunk_single_document(document))
        return all_chunks

    def _chunk_single_document(self, document: Document) -> List[DocumentChunk]:
        text = normalize_text(document.text)
        if not text:
            return []

        start = 0
        chunk_index = 0
        chunks: List[DocumentChunk] = []

        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            if end < len(text):
                split_index = text.rfind(" ", start, end)
                if split_index > start + int(self.chunk_size * 0.6):
                    end = split_index

            chunk_text = text[start:end].strip()
            if chunk_text:
                chunks.append(
                    DocumentChunk(
                        chunk_id=f"{document.document_id}_chunk_{chunk_index}",
                        document_id=document.document_id,
                        source=document.source,
                        text=chunk_text,
                        chunk_index=chunk_index,
                    )
                )
                chunk_index += 1

            if end >= len(text):
                break
            start = max(end - self.chunk_overlap, 0)

        return chunks
