import re
import html

def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r'<[^>]+>', '', text)       # HTML
    text = re.sub(r'http\S+', '', text)       # links
    text = re.sub(r'\s+', ' ', text).strip()  # whitespace
    return text

def redact_pii(text: str) -> str:
    text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '[EMAIL]', text)
    text = re.sub(r'\b\d{9,}\b', '[NUMBER]', text)
    return text
