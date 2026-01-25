import requests
from python-dotenv import load_dotenv
import os
load_dotenv()
PHI_API_KEY = os.getenv("PHI_API_KEY")
PHI_API_URL = os.getenv("PHI_API_URL")

def build_prompt(docs, question):
    context = "\n".join([f"- {d['text']}" for d in docs])

    return f"""
You are a helpful AI assistant.
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""


headers = {
    "Authorization": f"Bearer {PHI_API_KEY}",
    "Content-Type": "application/json"
}

def ask_phi2(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.2,
            "return_full_text": False
        }
    }

    response = requests.post(PHI_API_URL, headers=headers, json=payload)
    response.raise_for_status()

    result = response.json()

    # HF returns a list
    return result[0]["generated_text"]



def generate_response(retrieved_docs, user_query):
    prompt = build_prompt(retrieved_docs, user_query)
    return ask_phi2(prompt)
