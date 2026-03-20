from app.services.ingestion_service import IngestionService
from app.services.rag_pipeline import RAGPipeline


def get_ingestion_service() -> IngestionService:
    return IngestionService()


def get_rag_pipeline() -> RAGPipeline:
    return RAGPipeline()
