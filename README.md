# LLM-Powered Customer Query Classifier
A production-oriented prototype that uses LLMs to automatically classify customer support messages (email/chat) into categories such as Billing, Account Issues, Technical Problems, and more.
Designed as an end-to-end pipeline with ingestion, text preprocessing, embeddings, prompt engineering, and an LLM inference layer.

## Core Features
- **Automated message classification** using an LLM (HuggingFace Mistral-7B-Instruct or Azure OpenAI)
- **Text preprocessing pipeline**: cleaning, HTML/emoji removal, language detection, PII masking
- **Embeddings generation** using all-MiniLM-L6-v2 for semantic representation
- **Prompt engineering variants** tested in notebooks (baseline, few-shot, JSON schema)
- **FastAPI service** exposing the classifier as a REST API
- **Optional Azure integration** for enterprise deployments (Azure OpenAI, Key Vault, Blob Storage)
- **Well-structured modular architecture** following real-world ML/LLM production patterns

### Technologies Used
- **Python 3.11**
- **LangChain**, LangChain-HuggingFace, LangChain-OpenAI
- **Hugging Face Inference API**
- **Sentence Transformers** (`all-MiniLM-L6-v2`)
- **FastAPI** (service layer)
- **Pandas, regex, langdetect** (text preprocessing)
- **Azure SDK** (optional)

### Requirements
- Python 3.11+
- pip 25.x or newer

### How to Run
```bash
python -m venv venv source
venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# fill in your HF or Azure API keys

uvicorn app.api_server:app --reload
```


