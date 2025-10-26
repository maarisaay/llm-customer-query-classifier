from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import pandas as pd
from io import StringIO
from app.llm_classifier import classify_text
from app.pipeline import run_pipeline

app = FastAPI(
    title="LLM Customer Query API",
    description="API for classifying customer messages using Azure or Hugging Face models.",
    version="1.0.0",
)

class QueryRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "ok", "message": "LLM API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/classify")
def classify_query(request: QueryRequest):
    try:
        result = classify_text(request.text)
        return {"input": request.text, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/pipeline")
async def run_batch_pipeline(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode("utf-8")))

        if "message" not in df.columns:
            raise HTTPException(status_code=400, detail="CSV must contain a 'message' column")

        results = run_pipeline(df)
        return {"count": len(results), "results": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
