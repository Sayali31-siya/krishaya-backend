from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # To allow frontend requests from Vercel

@app.route('/')
def home():
    return render_template("chat.html")  # Show chatbot UI when visiting homepage

@app.route('/chat', methods=['POST'])  # ✅ This route now accepts POST
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"response": "Please enter a message."})

        # Dummy logic (replace with actual chatbot)
        bot_reply = f"You said: {user_message}"

        return jsonify({"response": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = f"You said: {user_message}"  # placeholder logic
    return jsonify({'reply': reply})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
