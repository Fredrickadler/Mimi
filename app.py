from flask import Flask, render_template, jsonify

app = Flask(__name__)

# متغیرهای شبیه‌سازی‌شده برای داده‌های بلاکچین
blockchain_stats = {
    "balance": 0,
    "energy": 50,
    "total_mined": 0,
    "total_supply": 1000000000,
    "blocks_mined": 0
}

@app.route("/")
def home():
    return render_template(
        "index.html",
        balance=blockchain_stats["balance"],
        energy=blockchain_stats["energy"],
        total_mined=blockchain_stats["total_mined"],
        total_supply=blockchain_stats["total_supply"],
        blocks_mined=blockchain_stats["blocks_mined"]
    )

@app.route("/mine", methods=["POST"])
def mine():
    # شبیه‌سازی استخراج
    if blockchain_stats["energy"] > 0:
        blockchain_stats["balance"] += 10  # پاداش استخراج
        blockchain_stats["blocks_mined"] += 1
        blockchain_stats["total_mined"] += 0.01  # درصد استخراج‌شده از کل عرضه
        blockchain_stats["energy"] -= 5  # مصرف انرژی
        return jsonify({"status": "Mining successful!"})
    else:
        return jsonify({"status": "Not enough energy!"})

if __name__ == "__main__":
    app.run(debug=True)