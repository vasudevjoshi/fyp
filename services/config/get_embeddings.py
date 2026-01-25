from langchain_huggingface import HuggingFaceEmbeddings
# Initialize model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
def get_embedding(text):
    return embeddings.embed_query(text)