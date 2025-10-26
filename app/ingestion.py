import re
import pandas as pd
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # ensures consistent results

def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print(f"Loaded {len(df)} rows from {path}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()


def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    text = re.sub(r"<[^>]+>", " ", text)               # remove HTML
    text = re.sub(r"\S+@\S+", "[EMAIL]", text)         # emails
    text = re.sub(r"http\S+|www\S+", "[URL]", text)    # links
    text = re.sub(r"\d+", "[NUM]", text)               # numbers

    # remove emoji and special characters, keep Polish letters
    text = re.sub(r"[^0-9a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s\[\]]+", " ", text)

    text = re.sub(r"\s+", " ", text).strip().lower()
    return text

def preprocess_text(df: pd.DataFrame) -> pd.DataFrame:
    if "message" not in df.columns:
        raise ValueError("DataFrame must contain a 'message' column")

    df["clean_message"] = df["message"].astype(str).apply(clean_text)

    def detect_lang_safe(text):
        try:
            return detect(text) if text.strip() else "unknown"
        except Exception:
            return "unknown"

    df["language"] = df["clean_message"].apply(detect_lang_safe)
    df["has_pii"] = df["clean_message"].str.contains(r"\[email\]|\[num\]|\[url\]", case=False)

    df = df.drop_duplicates(subset=["clean_message"])
    df = df[df["clean_message"].str.strip() != ""]
    print(f"Cleaned {len(df)} messages")

    return df

def run_ingestion_pipeline(path: str) -> pd.DataFrame:
    df_raw = load_data(path)
    df_clean = preprocess_text(df_raw)
    return df_clean


if __name__ == "__main__":
    df = run_ingestion_pipeline("data/messages_02.csv")
    print(df[["message", "clean_message", "language", "has_pii"]])