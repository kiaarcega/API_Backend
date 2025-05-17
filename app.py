from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Flask server is running"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '').strip().lower()

    if message == "hi":
        reply = "hello, kia!"
    else:
        reply = "I don't understand that."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
