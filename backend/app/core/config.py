from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Mini RAG Construction Assistant"
    APP_VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    BASE_DIR: Path = Path(__file__).resolve().parents[2]
    DATA_DIR: Path = BASE_DIR / "data"
    RAW_DATA_DIR: Path = DATA_DIR / "raw"
    PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"
    INDEX_DIR: Path = BASE_DIR / "index"
    PROMPTS_DIR: Path = BASE_DIR / "app" / "prompts"

    CHUNKS_FILE_PATH: Path = PROCESSED_DATA_DIR / "chunks.json"
    FAISS_INDEX_PATH: Path = INDEX_DIR / "faiss.index"
    METADATA_PATH: Path = INDEX_DIR / "metadata.json"

    EMBEDDING_MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 120
    TOP_K: int = 4
    MIN_SIMILARITY_SCORE: float = 0.2
    MAX_CONTEXT_CHARS_PER_CHUNK: int = 3000

    LLM_PROVIDER: str = "mock"  # mock | openrouter
    OPENROUTER_API_KEY: str = ""
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"
    OPENROUTER_MODEL: str = "mistralai/mistral-7b-instruct"
    REQUEST_TIMEOUT_SECONDS: int = 60

    CORS_ALLOW_ORIGINS: str = "*"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()

for path in [settings.RAW_DATA_DIR, settings.PROCESSED_DATA_DIR, settings.INDEX_DIR, settings.PROMPTS_DIR]:
    path.mkdir(parents=True, exist_ok=True)
