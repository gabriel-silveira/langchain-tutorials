import bs4
from typing import Tuple
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_split(url: str, class_list: Tuple = ()):
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

  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

  all_splits = text_splitter.split_documents(docs)

  return all_splits
