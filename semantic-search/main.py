from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

from src.pdf import load_pdf
from src.text import split_texts

# from src.search import SemanticSearch

if __name__ == '__main__':
  try:
    docs = load_pdf("./src/assets/nke-10k-2023.pdf")

    all_splits = split_texts(docs)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    for split in all_splits:
      vector = embeddings.embed_query(split.page_content)

    vector_store = InMemoryVectorStore(embeddings)

    results = vector_store.similarity_search("When was Nike incorporated?")

    for result in results:
      print(result)
      print("\n\n")

  except Exception as e:
    print(e)

  # sem_search = SemanticSearch(all_splits)
  # sem_search.search(all_splits, "How many distribution centers does Nike have in the US?")
  # ss.search_with_score("What was Nike's revenue in 2023?")
