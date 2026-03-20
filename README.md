# Mini RAG Construction AI

A complete Mini RAG assignment project with:

- FastAPI backend
- FAISS vector search
- Sentence Transformers embeddings
- Grounded answer generation
- React custom frontend showing retrieved context and final answer

## Project structure

- `backend/` - RAG pipeline and APIs
- `frontend/` - custom chatbot interface
- `docs/` - architecture and API docs

## Quick start

### Backend   
### I Used Windows for develping this project

```bash
cd backend
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Ingest documents

Place your PDFs/TXT/MD files inside:

```text
backend/data/raw/
```

Then call:

```bash
POST http://127.0.0.1:8000/api/v1/ingest
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Notes

- Default LLM provider is `mock` so the project runs without API keys.
- To use OpenRouter, update `backend/.env` and set `LLM_PROVIDER=openrouter`.
- The frontend shows both retrieved chunks and final answer to satisfy assignment transparency requirements.
