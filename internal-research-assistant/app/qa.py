from transformers import pipeline
from app.utils import load_vectorstore

# Load FAISS retriever and QA model
retriever = load_vectorstore()
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def get_answer(query: str) -> str:
    """Retrieve relevant context and answer the question using a local model."""
    docs = retriever.similarity_search(query, k=2)
    context = "\n".join([doc.page_content for doc in docs])
    result = qa_pipeline(question=query, context=context)
    return result['answer']
