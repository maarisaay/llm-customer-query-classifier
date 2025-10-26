import pandas as pd
from pathlib import Path

def load_data(file_path: str) -> pd.DataFrame:
    ext = Path(file_path).suffix
    if ext == ".csv":
        df = pd.read_csv(file_path)
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        df = pd.DataFrame({"message": [line.strip() for line in lines if line.strip()]})
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    return df

def preprocess_text(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["message"])
    df["message"] = df["message"].str.lower().str.strip()
    return df