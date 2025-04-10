from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore


def get_vector_store(model: str):
  embeddings = OpenAIEmbeddings(model=model)

  vector_store = InMemoryVectorStore(embeddings)

  return vector_store
