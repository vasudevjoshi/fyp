from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from langchain_huggingface import HuggingFaceEmbeddings
from create_index import create_index
# Initialize model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def get_embedding(text):
    return embeddings.embed_query(text)


is_index_created = False
client = MongoClient(MONGO_URI)

# -------------------------------
# Ping MongoDB
# -------------------------------
try:
    client.admin.command("ping")
    print("✅ Connected to MongoDB successfully")
except ConnectionFailure:
    print("❌ MongoDB connection failed")

db = client[DB_NAME]
collection = db[COLLECTION_NAME]

if not is_index_created:
    is_index_created = create_index()

def get_query_results(query):
  """Gets results from a vector search query."""

  query_embedding = get_embedding(query)
  # print(query_embedding)
  pipeline = [
      {
            "$vectorSearch": {
              "index": "vector_index",
              "queryVector": query_embedding,
              "path": "vector",
              "numCandidates":384,
              "limit": 5
            }
      }, {
            "$project": {
              "_id": 0,
              "text": 1
         }
      }
  ]

  results = collection.aggregate(pipeline)
  print(results)

  array_of_results = []
  for doc in results:
      print(doc)
      array_of_results.append(doc)
  return array_of_results

  # Test the function with a sample query
get_query_results("explain the details about the dry skin")
