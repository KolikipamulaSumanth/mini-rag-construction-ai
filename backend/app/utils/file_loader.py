from pathlib import Path
from typing import List

import fitz

from app.core.constants import SUPPORTED_EXTENSIONS
from app.models.document_models import Document


class FileLoader:
    def load_documents(self, raw_data_dir: Path) -> List[Document]:
        documents: List[Document] = []
        if not raw_data_dir.exists():
            return documents

        for file_path in sorted(raw_data_dir.iterdir()):
            if not file_path.is_file() or file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            text = self._extract_text(file_path)
            if not text.strip():
                continue

            documents.append(
                Document(
                    document_id=file_path.stem,
                    source=file_path.name,
                    text=text.strip(),
                )
            )
        return documents

    def _extract_text(self, file_path: Path) -> str:
        suffix = file_path.suffix.lower()
        if suffix == ".pdf":
            return self._extract_pdf_text(file_path)
        return file_path.read_text(encoding="utf-8", errors="ignore")

    @staticmethod
    def _extract_pdf_text(file_path: Path) -> str:
        pages = []
        with fitz.open(file_path) as pdf:
            for page in pdf:
                pages.append(page.get_text("text"))
        return "\n".join(pages)
