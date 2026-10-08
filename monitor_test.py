from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "CSRF Monitor is running"


@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "monitor": "CSRF Scanner Monitor"
    })


if __name__ == "__main__":

    print("=" * 50)
    print("CSRF MONITOR TEST")
    print("=" * 50)
    print("http://127.0.0.1:5050")
    print("http://127.0.0.1:5050/health")
    print("=" * 50)

    app.run(
        host="127.0.0.1",
        port=5050,
        debug=True
    )