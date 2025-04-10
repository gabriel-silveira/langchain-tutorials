import bs4
from typing import Tuple
from langchain_community.document_loaders import WebBaseLoader


def load_docs(url: str, class_list: Tuple = ()):
  if url == "":
    return None

  # Load and chunk contents of the blog
  loader = WebBaseLoader(
    web_paths=(url,),
    bs_kwargs=dict(
      parse_only=bs4.SoupStrainer(
        class_=class_list
      )
    ),
  )

  docs = loader.load()

  return docs
