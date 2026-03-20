from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_ingestion_service
from app.models.response_models import IngestResponse
from app.services.ingestion_service import IngestionService

router = APIRouter()


@router.post("/ingest", response_model=IngestResponse)
def ingest_documents(service: IngestionService = Depends(get_ingestion_service)) -> IngestResponse:
    try:
        documents_processed, chunks_created = service.build_index()
        return IngestResponse(
            message="Index built successfully.",
            documents_processed=documents_processed,
            chunks_created=chunks_created,
            index_saved_to="backend/index/faiss.index",
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
