import os
from dotenv import load_dotenv

load_dotenv()

USE_AZURE = False # False - local test on Hugging Face, True - Azure OpenAI

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_MODEL = os.getenv("AZURE_MODEL", "gpt-4-turbo")

HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
HF_MODEL = os.getenv("HF_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")

def get_llm():
    if USE_AZURE:
        from langchain_openai import AzureChatOpenAI

        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=OPENAI_API_KEY,
            deployment_name=AZURE_MODEL,
            temperature=0,
            max_tokens=300
        )
    else:
        from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

        endpoint_llm = HuggingFaceEndpoint(
            repo_id=HF_MODEL,
            huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
            temperature=0.3,
            max_new_tokens=300
        )

        llm = ChatHuggingFace(llm=endpoint_llm)

    return llm

if __name__ == "__main__":
    llm = get_llm()
    print("LLM loaded successfully:", type(llm))