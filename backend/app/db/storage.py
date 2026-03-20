import json
from pathlib import Path
from typing import List

from app.models.document_models import DocumentChunk


class MetadataStorage:
    def __init__(self, chunks_path: Path, metadata_path: Path) -> None:
        self.chunks_path = chunks_path
        self.metadata_path = metadata_path

    def save_chunks(self, chunks: List[DocumentChunk]) -> None:
        payload = [chunk.model_dump() for chunk in chunks]
        self.chunks_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        self.metadata_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def load_chunks(self) -> List[DocumentChunk]:
        if not self.metadata_path.exists():
            raise FileNotFoundError(f"Metadata file not found at {self.metadata_path}")
        raw = json.loads(self.metadata_path.read_text(encoding="utf-8"))
        return [DocumentChunk(**item) for item in raw]
