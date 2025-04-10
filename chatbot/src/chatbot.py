from typing import Sequence
from typing_extensions import Annotated, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

model = init_chat_model("gpt-4o-mini", model_provider="openai")

thread_id = "chatbot_test_1"


class State(TypedDict):
  messages: Annotated[Sequence[BaseMessage], add_messages]
  language: str


# Define a new graph
workflow = StateGraph(state_schema=State)

prompt_template = ChatPromptTemplate.from_messages(
  [
    (
      "system",
      "You are a helpful assistant. Answer all questions to the best of your ability in {language}."
      # "You talk like a pirate. Answer all questions to the best of your ability.",
    ),
    MessagesPlaceholder(variable_name="messages"),
  ]
)


# Define the function that calls the model
def call_model(state: State):
  prompt = prompt_template.invoke(state)
  response = model.invoke(prompt)

  return {"messages": response}


def invoke(query: str, language: str = ""):
  if query and thread_id:
    config = {"configurable": {"thread_id": thread_id}}

    input_messages = [HumanMessage(query)]

    for chunk, metadata in app.stream(
      {"messages": input_messages, "language": language},
      config,
      stream_mode="messages",
    ):
      if isinstance(chunk, AIMessage):  # Filter to just model responses
        print(chunk.content, end="|")

    if language:
      output = app.invoke({"messages": input_messages, "language": language}, config)
    else:
      output = app.invoke({"messages": input_messages}, config)

    output["messages"][-1].pretty_print()  # output contains all messages in state


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
