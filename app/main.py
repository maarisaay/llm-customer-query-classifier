from fastapi import FastAPI
from pydantic import BaseModel
from app.llm_classifier import classify_text

"""
Usage
    uvicorn app.main:app --reload

Docs:
    http://127.0.0.1:8000/docs

Example request:
    POST /classify
        {
          "text": "I was charged twice for my last invoice."
        }
        
Expected response:
    {
      "category": "Billing",
      "confidence": 1.0
    }
"""

app = FastAPI(
    title="LLM Customer Query Classifier",
    description="API for classifying customer queries using the LLM model",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    text: str

@app.post("/classify")
def classify_query(request: QueryRequest):
    result = classify_text(request.text)
    return result

@app.get("/")
def home():
    return {"status": "ok", "message": "LLM classifier is running"}

