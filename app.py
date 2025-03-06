from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set the Google Gemini API Key directly in the code
GEMINI_API_KEY = "AIzaSyAOPQv1Y321hOcSEhOSVW5a7pZPjR22Qrs"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"  # Adjust if necessary

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    # Make a request to the Google Gemini API
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "contents": [{
            "parts": [{"text": user_message}]
        }]
    }

    # Send the request to Gemini API
    response = requests.post(GEMINI_API_URL, json=data, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        return jsonify({"response": response_data.get("content")})  # Extract content from response
    else:
        return jsonify({"error": "Failed to get a response from Gemini API", "details": response.text}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
