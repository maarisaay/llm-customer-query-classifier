from app.llm_classifier import classify_text

def run_pipeline(df):
    messages = df["message"].tolist()
    results = []
    for msg in messages:
        try:
            result = classify_text(msg)
            results.append({"message": msg, "result": result})
        except Exception as e:
            results.append({"message": msg, "error": str(e)})
    return results