from langchain_core.vectorstores import InMemoryVectorStore

from src.embeddings import embeddings


class SemanticSearch:
  __all_splits = None
  __vector_store = None

  def __init__(self, all_splits):
    self.__all_splits = all_splits

    self.__vector_store = InMemoryVectorStore(embeddings)

    embeddings.embed_query(self.__all_splits[0].page_content)
    embeddings.embed_query(self.__all_splits[1].page_content)

  def search(self, query: str = ''):
    if query != '':
      results = self.__vector_store.similarity_search(query)

      print(results)
      print("\n\n")

      for result in results:
        print(result)
        print("\n\n")

  def search_with_score(self, query=''):
    if query != '':
      results = self.__vector_store.similarity_search_with_score(query)

      doc, score = results[0]

      print(f"Score: {score}\n")
      print(doc)
