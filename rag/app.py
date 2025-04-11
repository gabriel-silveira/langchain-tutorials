from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langchain.chains import RetrievalQA
from src.loader import load_docs
from src.splitter import split_docs
from src.graph import graph, vector_store

app = Flask(__name__)
cors = CORS(app)

docs = load_docs(
  "https://lilianweng.github.io/posts/2023-06-23-agent/",
  ("post-content", "post-title", "post-header"),
)

all_splits = split_docs(docs)

_ = vector_store.add_documents(documents=all_splits)


@app.route("/", methods=["GET"])
def home():
  return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
  data = request.get_json()

  question = data.get("question")

  if not question:
    return jsonify({"error": "Pergunta não enviada."}), 400

  response = graph.invoke({"question": question})

  return jsonify({"answer": response["answer"]})


if __name__ == "__main__":
  app.run(debug=True)
