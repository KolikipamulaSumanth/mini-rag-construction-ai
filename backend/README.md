# Backend

Run:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Place source documents in `backend/data/raw/`, then call `POST /api/v1/ingest`.
