# from langchain_huggingface import HuggingFaceEmbeddings
# # Initialize model
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )
# def get_embedding(text):
#     return embeddings.embed_query(text)

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import numpy as np

load_dotenv()

import time

HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="sentence-transformers/all-MiniLM-L6-v2",
    token=HF_API_KEY,
    timeout=60
)

def get_embedding(text, retries=3):
    for attempt in range(retries):
        try:
            emb = client.feature_extraction(text)
            if isinstance(emb, np.ndarray):
                emb = emb.tolist()
            return emb
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(2 ** attempt)
