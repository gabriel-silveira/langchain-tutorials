from src.loader import load_and_split
from src.graph import graph, vector_store

all_splits = load_and_split(
  "https://lilianweng.github.io/posts/2023-06-23-agent/",
  ("post-content", "post-title", "post-header"),
)

_ = vector_store.add_documents(documents=all_splits)

response = graph.invoke({"question": "What is Task Decomposition? How it can helps us?"})

print(response["answer"])
