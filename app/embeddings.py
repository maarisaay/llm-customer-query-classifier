from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings(texts):
    emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return emb.embed_documents(texts)

