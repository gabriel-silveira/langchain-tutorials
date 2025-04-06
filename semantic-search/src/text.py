from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(docs):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
  )

  all_splits = text_splitter.split_documents(docs)

  len(all_splits)

  return all_splits
