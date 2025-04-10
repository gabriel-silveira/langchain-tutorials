from src.loader import load_docs
from src.splitter import split_docs
from src.graph import graph, vector_store

docs = load_docs(
  "https://lilianweng.github.io/posts/2023-06-23-agent/",
  ("post-content", "post-title", "post-header"),
)

all_splits = split_docs(docs)

_ = vector_store.add_documents(documents=all_splits)

# response = graph.invoke({"question": "What is Task Decomposition? How this can help us?"})
response = graph.invoke({"question": "What are the types of memory in autonomous agents?"})

print(response["answer"])
