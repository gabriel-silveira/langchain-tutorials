from langchain_core.prompts import ChatPromptTemplate  # , MessagesPlaceholder
from langchain.chat_models import init_chat_model
from langchain.callbacks.tracers import LangChainTracer

tracer = LangChainTracer()


def extract(model, text):
  # Define a custom prompt to provide instructions and any additional context.
  # 1) You can add examples into the prompt template to improve extraction quality
  # 2) Introduce additional parameters to take context into account (e.g., include metadata
  #    about the document from which the text was extracted.)
  prompt_template = ChatPromptTemplate.from_messages(
    [
      (
        "system",
        "You are an expert extraction algorithm. "
        "Only extract relevant information from the text. "
        "If you do not know the value of an attribute asked to extract, "
        "return null for the attribute's value."
        "The returned values must be in english."
      ),
      # Please see the how-to about improving performance with
      # reference examples.
      # MessagesPlaceholder('examples'),
      ("human", "{text}"),
    ]
  )

  llm = init_chat_model("gpt-4o-mini", model_provider="openai")

  structured_llm = llm.with_structured_output(schema=model)

  prompt = prompt_template.invoke({"text": text})

  result = structured_llm.invoke(prompt, config={"callbacks": [tracer]})

  return result
