from fastapi import APIRouter

from app.core.config import settings
from app.models.response_models import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", app_name=settings.APP_NAME, version=settings.APP_VERSION)
