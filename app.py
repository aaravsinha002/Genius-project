from flask import Flask, request, jsonify
import openai  
import os  

app = Flask(__name__)  

# Set your OpenAI API Key
openai.api_key = "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"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a course selection advisor. Give course selection advice based on the query."},
                  {"role": "user", "content": user_message}]
    )
    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
