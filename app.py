from flask import Flask, render_template, jsonify

app = Flask(__name__)

# داده‌های کاربر به صورت نمونه
user_data = {
    "username": "John Doe",
    "balance": 0,
    "energy": 50
}

@app.route("/")
def index():
    return render_template("index.html", user=user_data)

@app.route("/mine", methods=["POST"])
def mine():
    global user_data

    # بررسی انرژی و افزایش موجودی
    if user_data["energy"] >= 10:
        user_data["balance"] += 1
        user_data["energy"] -= 10
        message = "Mining successful! +1 Balance"
    else:
        message = "Not enough energy to mine."

    return jsonify({
        "balance": user_data["balance"],
        "energy": user_data["energy"],
        "message": message
    })

if __name__ == "__main__":
    app.run(debug=True)