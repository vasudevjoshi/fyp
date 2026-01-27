# from langchain_huggingface import HuggingFaceEmbeddings
# # Initialize model
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )
# def get_embedding(text):
#     return embeddings.embed_query(text)

import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

MODEL_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def get_embedding(text: str) -> list:
    payload = {
        "inputs": text,
        "options": {"wait_for_model": True}
    }

    response = requests.post(MODEL_URL, headers=headers, json=payload)
    response.raise_for_status()

    embedding = response.json()

    # HF returns shape: [1, 384]
    return embedding[0]
