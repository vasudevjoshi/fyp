from flask import Blueprint, request, jsonify
from config.db import get_db
from models.vector_model import vector_search
from config.get_embeddings import get_embedding
from config.generate_response import generate_response
search_bp = Blueprint("search", __name__)

db = get_db()
collection = db["vectors"]


@search_bp.route("/ask", methods=["POST"])
def search():
    data = request.json

    if not data or "query" not in data:
        return jsonify({"error": "query is required"}), 400

    query_embedding = get_embedding(data["query"])

    try:

        results = vector_search(collection, query_embedding)
        response = generate_response(results, data["query"])    
        return jsonify({
            "response": response
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
