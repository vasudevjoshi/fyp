from flask import Flask
from controllers.search_controller import search_bp
from config.db import client

app = Flask(__name__)
app.register_blueprint(search_bp)


@app.route("/health", methods=["GET"])
def health():
    client.admin.command("ping")
    return {"status": "MongoDB connected"}

# if __name__ == "__main__":
#     app.run(debug=True)
