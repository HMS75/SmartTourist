from flask import Flask, jsonify, request
from flask_cors import CORS
from blockchain import blockchain

app = Flask(__name__)
CORS(app)  # allow requests from frontend

@app.route("/")
def home():
    return jsonify({"message": "Backend running ✅"})

# Generate a tourist ID
@app.route("/generateID", methods=["POST"])
def generate_id():
    data = request.get_json()
    name = data.get("name", "")
    if not name:
        return jsonify({"error": "Name required"}), 400
    
    hash_value = blockchain.generate_id(name)
    return jsonify({"tourist_id": hash_value})

# Verify a tourist ID
@app.route("/verifyTourist/<hash_value>")
def verify_tourist(hash_value):
    valid = blockchain.verify(hash_value)
    return jsonify({"valid": valid})

if __name__ == "__main__":
    app.run(debug=True)
