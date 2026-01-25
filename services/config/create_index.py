from pymongo.operations import SearchIndexModel
import time
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "rag_db"
COLLECTION_NAME = "vectors"


client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def create_index():
    index_name="vector_index"

    # Attempt to drop the index if it already exists to ensure the latest definition
    try:
        collection.drop_search_index(index_name)
        print(f"Dropped existing index: {index_name}")
        # Wait for the index to be truly dropped before proceeding
        print(f"Waiting for index '{index_name}' to be completely removed...")
        while True:
            current_indices = list(collection.list_search_indexes(index_name))
            if not current_indices: # If the list is empty, the index is gone
                print(f"Index '{index_name}' confirmed as removed.")
                break
            print(f"Index '{index_name}' still detected, waiting...")
            time.sleep(5) # Wait before checking again
    except Exception as e:
        if "IndexNotFound" in str(e):
            print(f"Index {index_name} did not exist, proceeding with creation.")
        else:
            print(f"Error during index drop or check for removal: {e}")

    # Create your index model, then create the search index
    search_index_model = SearchIndexModel(
    definition = {
        "fields": [
        {
            "type": "vector",
            "numDimensions": 384,
            "path": "vector", # Ensures correct path to vector embeddings
            "similarity": "cosine"
        }
        ]
    },
    name = index_name,
    type = "vectorSearch"
    )
    collection.create_search_index(model=search_index_model)

    # Wait for initial sync to complete
    print("Polling to check if the index is ready. This may take up to a minute.")
    predicate=None
    if predicate is None:
        predicate = lambda index: index.get("queryable") is True

    while True:
        indices = list(collection.list_search_indexes(index_name))
        if len(indices) and predicate(indices[0]):
            break
        time.sleep(5)
    print(index_name + " is ready for querying.")

    return True