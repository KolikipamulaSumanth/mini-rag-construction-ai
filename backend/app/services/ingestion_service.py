from app.core.config import settings
from app.db.loader import get_index_manager, get_metadata_storage
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.utils.file_loader import FileLoader


class IngestionService:
    def __init__(self) -> None:
        self.file_loader = FileLoader()
        self.chunker = ChunkingService(settings.CHUNK_SIZE, settings.CHUNK_OVERLAP)
        self.embedding_service = EmbeddingService(settings.EMBEDDING_MODEL_NAME)
        self.index_manager = get_index_manager()
        self.metadata_storage = get_metadata_storage()

    def build_index(self) -> tuple[int, int]:
        documents = self.file_loader.load_documents(settings.RAW_DATA_DIR)
        if not documents:
            raise ValueError("No supported documents found in backend/data/raw")

        chunks = self.chunker.chunk_documents(documents)
        if not chunks:
            raise ValueError("No chunks were created from the provided documents")

        embeddings = self.embedding_service.embed_texts([chunk.text for chunk in chunks])
        self.index_manager.build_and_save(embeddings)
        self.metadata_storage.save_chunks(chunks)

        return len(documents), len(chunks)
