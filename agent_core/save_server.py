import json
from flask import Flask, request

app = Flask(__name__)
received = []


@app.route("/webhook", methods=["POST"])
def webhook():
    received.append(request.get_json())

    with open("received_alerts.json", "w", encoding="utf-8") as f:
        json.dump(received, f, ensure_ascii=False, indent=2)

    return {"status": "ok", "count": len(received)}, 200


app.run(port=5006)
