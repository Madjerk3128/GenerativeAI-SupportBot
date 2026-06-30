import os
from flask import Flask, render_template, request, jsonify
from prompt_engine import create_prompt
from model import generate_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    if not question.strip():
        return jsonify({"error": "Please enter a question."}), 400

    prompt = create_prompt(question)
    answer = generate_answer(prompt)

    return jsonify({"question": question, "answer": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
