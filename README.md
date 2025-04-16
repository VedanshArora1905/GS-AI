# Internal Research Assistant (Local, Free Version)

This version uses local, open-source models to answer questions from documents — no OpenAI API key or usage charges.

## Features
- Ingest PDFs, markdown, and text files
- Embed with SentenceTransformers locally
- Store embeddings using FAISS
- Answer using HuggingFace's QA pipeline
- Web UI with FastAPI + HTML

## How to Use
1. Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```

2. Add documents in `data/docs` (PDFs or `.txt`)

3. Run the full pipeline (ingest + serve):
```bash
python runall.py
```

4. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to start querying.

## Example Questions to Try

🗂️ From `company_policy.pdf`
- How many days of maternity leave are allowed?
- Can earned leave be carried forward?
- What is the policy on medical certificates for sick leave?

📘 From `product_guide.pdf`
- How do I reset the SmartControl device?
- What happens after resetting the device?
- What is the current firmware version?

---

✅ Built using local HuggingFace models + FAISS, with zero API cost
# Internal Research Assistant (Local, Free Version)

This version uses local, open-source models to answer questions from documents — no OpenAI API key or usage charges.
