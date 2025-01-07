from flask import Flask, jsonify, request
from datetime import datetime
import random

app = Flask(__name__)

# دیتای نمونه برای کاربر و بلاک‌چین
user_data = {"username": "John Doe", "balance": 0, "energy": 50}
blocks = []
blockchain_data = {"total_supply": 1000000000, "blocks_mined": 0}

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/mine", methods=["POST"])
def mine():
    global user_data, blocks, blockchain_data

    if user_data["energy"] >= 10:  # شرط برای استخراج
        user_data["balance"] += 1
        user_data["energy"] -= 10

        block = {
            "number": random.randint(100000, 999999),
            "reward": 1,
            "time": datetime.now().strftime("%H:%M:%S"),
            "miner": user_data["username"]
        }
        blocks.append(block)

        blockchain_data["blocks_mined"] += 1
        total_mined = (blockchain_data["blocks_mined"] / blockchain_data["total_supply"]) * 100

        message = "Mining successful! +1 Balance"
    else:
        message = "Not enough energy to mine."

    return jsonify({
        "balance": user_data["balance"],
        "energy": user_data["energy"],
        "message": message,
        "block": block if 'block' in locals() else None,
        "total_mined": round(total_mined, 2),
        "blocks_mined": blockchain_data["blocks_mined"]
    })

if __name__ == "__main__":
    app.run(debug=True)