from app.core.config import settings
from app.db.faiss_index import FaissIndexManager
from app.db.storage import MetadataStorage


def get_index_manager() -> FaissIndexManager:
    return FaissIndexManager(settings.FAISS_INDEX_PATH)


def get_metadata_storage() -> MetadataStorage:
    return MetadataStorage(settings.CHUNKS_FILE_PATH, settings.METADATA_PATH)
