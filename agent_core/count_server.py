from flask import Flask, request

app = Flask(__name__)

received = []


@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.get_json()

    received.append(event)

    return {"status": "ok", "count": len(received)}, 200


app.run(port=5004)
