# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, DevOps Engineer! 🚀 This is your test web app."

@app.route("/health")
def health():
    return jsonify(status="UP")

if __name__ == "__main__":
    # Run on port 5000
    app.run(host="0.0.0.0", port=5000)
