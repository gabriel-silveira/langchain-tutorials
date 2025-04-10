from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage

model = init_chat_model("gpt-4o-mini", model_provider="openai")

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
  response = model.invoke(state["messages"])
  return {"messages": response}


def invoke(query: str, thread_id: str):
  if query and thread_id:
    config = {"configurable": {"thread_id": thread_id}}

    input_messages = [HumanMessage(query)]

    output = app.invoke({"messages": input_messages}, config)

    output["messages"][-1].pretty_print()  # output contains all messages in state


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
