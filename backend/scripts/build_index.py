from app.services.ingestion_service import IngestionService


if __name__ == "__main__":
    service = IngestionService()
    documents_processed, chunks_created = service.build_index()
    print(f"Documents processed: {documents_processed}")
    print(f"Chunks created: {chunks_created}")
