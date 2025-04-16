from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.qa import get_answer

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

@app.get("/")
def serve_ui():
    return FileResponse("frontend/index.html")

@app.post("/ask")
def ask_question(question: str = Form(...)):
    answer = get_answer(question)
    return {"answer": answer}
