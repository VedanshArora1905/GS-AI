import os
import shutil
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings

# Use a local sentence transformer model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def load_documents(directory: str):
    documents = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if filename.endswith(".pdf"):
            loader = PyMuPDFLoader(path)
        elif filename.endswith(".md") or filename.endswith(".txt"):
            loader = TextLoader(path)
        else:
            continue
        documents.extend(loader.load())
    return documents

def ingest_and_store_documents(documents, db_path="vector_db"):
    # Clear existing index to avoid FileExistsError
    if os.path.exists(db_path):
        shutil.rmtree(db_path)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local(db_path)
    return db

def load_vectorstore(db_path="vector_db"):
    return FAISS.load_local(db_path, embedding_model, allow_dangerous_deserialization=True)