from langchain_huggingface import HuggingFaceEmbeddings
from functools import lru_cache

@lru_cache(maxsize=1)
def _get_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_embeddings(texts):
    emb = _get_model()
    return emb.embed_documents(list(texts))
