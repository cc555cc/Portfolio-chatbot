import os
import nltk
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import generate_response

nltk.download('wordnet', quiet=True)

app = Flask(__name__)
CORS(app)


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get('message', '')
    try:
        reply = generate_response(message)
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': f'Server error: {e}'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
