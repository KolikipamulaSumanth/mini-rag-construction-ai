from fastapi import APIRouter, Depends, HTTPException

from app.core.config import settings
from app.dependencies import get_rag_pipeline
from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse
from app.services.rag_pipeline import RAGPipeline

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, pipeline: RAGPipeline = Depends(get_rag_pipeline)) -> ChatResponse:
    try:
        top_k = request.top_k or settings.TOP_K
        return pipeline.ask(question=request.question, top_k=top_k)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=400, detail="Index not found. Please run /api/v1/ingest first.") from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
