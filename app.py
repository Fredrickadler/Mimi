from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# داده‌های کاربر
user_data = {
    "username": "John Doe",
    "balance": 0,
    "energy": 50
}

# داده‌های نمونه بلوک
blocks = []

@app.route("/")
def index():
    return render_template("index.html", user=user_data, blocks=blocks)

@app.route("/mine", methods=["POST"])
def mine():
    global user_data, blocks

    if user_data["energy"] >= 10:
        # به‌روزرسانی داده‌ها
        user_data["balance"] += 1
        user_data["energy"] -= 10

        # ساخت بلوک جدید
        block = {
            "number": random.randint(100000, 999999),
            "reward": 1,
            "time": datetime.now().strftime("%H:%M:%S"),
            "miner": user_data["username"]
        }
        blocks.append(block)

        message = "Mining successful! +1 Balance"
    else:
        message = "Not enough energy to mine."

    return jsonify({
        "balance": user_data["balance"],
        "energy": user_data["energy"],
        "message": message,
        "block": block if 'block' in locals() else None
    })

if __name__ == "__main__":
    app.run(debug=True)