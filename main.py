from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["GET"])
def home():
    return "Bot Sinyal BTC Aktif!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("message", "Sinyal baru BTC belum ditentukan.")
    send_message(message)
    return {"status": "ok"}

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        r = requests.post(url, json=payload)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
