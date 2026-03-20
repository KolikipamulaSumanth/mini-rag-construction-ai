from typing import Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=2, max_length=2000)
    top_k: Optional[int] = Field(default=None, ge=1, le=10)
