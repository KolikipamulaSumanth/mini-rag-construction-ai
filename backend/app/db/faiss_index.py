from pathlib import Path

import faiss
import numpy as np


class FaissIndexManager:
    def __init__(self, index_path: Path) -> None:
        self.index_path = index_path

    def build_and_save(self, embeddings: np.ndarray) -> None:
        if embeddings.size == 0:
            raise ValueError("Embeddings array is empty.")
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)
        index.add(embeddings)
        faiss.write_index(index, str(self.index_path))

    def load(self) -> faiss.Index:
        if not self.index_path.exists():
            raise FileNotFoundError(f"FAISS index not found at {self.index_path}")
        return faiss.read_index(str(self.index_path))
