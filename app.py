from flask import Flask, request, jsonify, render_template
from chatbot import chatbot_reply
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Krishaya Chatbot is running!'

@app.route('/chat')
def chat_page():
    return render_template("chat.html")

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['message']
    reply = chatbot_reply(user_message)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
