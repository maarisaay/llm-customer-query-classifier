from langchain_core.prompts import PromptTemplate
from .config import (get_llm)
import json

def classify_text(text: str) -> dict:

    llm = get_llm()

    prompt = PromptTemplate(
        input_variables=["text"],
        template=(
            "You are a customer service assistant. "
            "Classify the following customer message into one of the categories: "
            "[Billing, Technical, Account, Complaint, Other].\n\n"
            "Message:\n{text}\n\n"
            "Respond strictly as JSON with fields 'category' and 'confidence' (0-1).\n"
        )
    )

    final_prompt = prompt.format(text=text)

    try:
        response = llm.invoke(final_prompt)
        content = getattr(response, "content", str(response))
        parsed = json.loads(content)
        return parsed
    except Exception as e:
        return {"error": f"Model error: {e}"}


if __name__ == "__main__":
    example = "I was charged twice for my last invoice."
    print("Input:", example)
    print("Output:", classify_text(example))

