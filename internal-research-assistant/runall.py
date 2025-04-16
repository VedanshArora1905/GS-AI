import subprocess
from app.utils import load_documents, ingest_and_store_documents

if __name__ == "__main__":
    print("🔄 Ingesting documents...")
    docs = load_documents("data/docs")
    ingest_and_store_documents(docs)
    print("✅ Ingestion complete. Launching FastAPI server...")
    subprocess.run(["uvicorn", "app.main:app", "--reload"])