from flask import request, jsonify
from app import app
from app.utils import generate_response

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("text", "")

    if not user_input:
        return jsonify({"error": "Text input is required"}), 400

    response = generate_response(user_input)
    return jsonify({"response": response})
