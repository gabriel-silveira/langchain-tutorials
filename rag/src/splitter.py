from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_docs(docs: List[Document]):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

  all_splits = text_splitter.split_documents(docs)

  return all_splits
