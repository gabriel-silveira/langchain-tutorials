from langchain.chat_models import init_chat_model
from src.vector_store import get_vector_store
from langchain import hub
from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from langgraph.graph import START, StateGraph

llm = init_chat_model("gpt-4o-mini", model_provider="openai")

vector_store = get_vector_store("text-embedding-3-large")

# Define prompt for question-answering
prompt = hub.pull("rlm/rag-prompt")


# Define state for application
class State(TypedDict):
  question: str
  context: List[Document]
  answer: str


# Define application steps
def retrieve(state: State):
  retrieved_docs = vector_store.similarity_search(state["question"])

  return {"context": retrieved_docs}


def generate(state: State):
  docs_content = "\n\n".join(doc.page_content for doc in state["context"])
  messages = prompt.invoke({"question": state["question"], "context": docs_content})
  generation_response = llm.invoke(messages)

  return {"answer": generation_response.content}


# Compile application and test
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")

graph = graph_builder.compile()
