from flask import Flask, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)


model = GPT4All("gpt4all-falcon")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    response = model.generate(user_message, ma_tokens=200)

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)