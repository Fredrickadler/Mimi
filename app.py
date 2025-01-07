from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

# Configurations
BOT_TOKEN = "7992131826:AAESzqUPUYmXQMPi81rDZlekIRBiQRUuLJA"
BASE_URL = "https://mimi-ijdu.onrender.com"

# Mock database
users = [
    {"id": 1, "name": "John Doe", "balance": 0, "energy": 50},
    {"id": 2, "name": "Jane Doe", "balance": 0, "energy": 75},
]
blockchain_stats = {
    "total_mined": 0,
    "total_supply": 1000000000,
    "blocks_mined": 0
}

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/user/<int:user_id>")
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/api/blockchain")
def get_blockchain_stats():
    return jsonify(blockchain_stats)

@app.route("/api/update", methods=["POST"])
def update_user():
    data = request.json
    user = next((u for u in users if u["id"] == data["id"]), None)
    if user:
        user["balance"] += data.get("balance", 0)
        user["energy"] = max(0, min(100, data.get("energy", user["energy"])))
        return jsonify({"message": "User updated successfully"})
    return jsonify({"error": "User not found"}), 404

@app.route("/api/send_message", methods=["POST"])
def send_message():
    data = request.json
    chat_id = data.get("chat_id")
    message = data.get("message")
    if chat_id and message:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        response = requests.post(url, json={"chat_id": chat_id, "text": message})
        return response.json()
    return jsonify({"error": "Invalid request"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")