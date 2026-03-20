from pathlib import Path

import requests

from app.core.config import settings
from app.core.constants import DEFAULT_FALLBACK_ANSWER


class GenerationService:
    def __init__(self) -> None:
        self.provider = settings.LLM_PROVIDER
        self.prompt_path = settings.PROMPTS_DIR / "rag_prompt.txt"

    def generate(self, question: str, context: str) -> str:
        if not context.strip():
            return DEFAULT_FALLBACK_ANSWER

        prompt = self._load_prompt().format(context=context, question=question)

        if self.provider == "mock":
            return self._mock_answer(context)
        if self.provider == "openrouter":
            return self._call_openrouter(prompt)
        raise ValueError(f"Unsupported LLM provider: {self.provider}")

    def _load_prompt(self) -> str:
        return Path(self.prompt_path).read_text(encoding="utf-8")

    @staticmethod
    def _mock_answer(context: str) -> str:
        snippet = context.split("\n", 1)[0][:180]
        return f"Mock grounded answer based on retrieved context: {snippet}"

    def _call_openrouter(self, prompt: str) -> str:
        if not settings.OPENROUTER_API_KEY:
            raise ValueError("OPENROUTER_API_KEY is missing in environment variables.")

        response = requests.post(
            f"{settings.OPENROUTER_BASE_URL}/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": settings.OPENROUTER_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.0,
            },
            timeout=settings.REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        payload = response.json()
        return payload["choices"][0]["message"]["content"].strip()
