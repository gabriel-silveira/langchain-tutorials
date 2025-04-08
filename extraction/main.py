from typing import Optional
from langchain_core.prompts import ChatPromptTemplate  # , MessagesPlaceholder
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langchain.callbacks.tracers import LangChainTracer

tracer = LangChainTracer()


class Person(BaseModel):
  """Information about a person."""

  # ^ Doc-string for the entity Person.
  # This doc-string is sent to the LLM as the description of the schema Person,
  # and it can help to improve extraction results.

  # Note that:
  # 1. Each field is an `optional` -- this allows the model to decline to extract it!
  # 2. Each field has a `description` -- this description is used by the LLM.
  # Having a good description can help improve extraction results.
  name: Optional[str] = Field(default=None, description="The name of the person")
  hair_color: Optional[str] = Field(
    default=None, description="The color of the person's hair if known"
  )
  height_in_meters: Optional[str] = Field(
    default=None, description="Height measured in meters. The height must have only 2 decimal point."
  )


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

structured_llm = llm.with_structured_output(schema=Person)

text = "A minha amiga Joana tem 5 pés de altura e cabelos ruivos."

prompt = prompt_template.invoke({"text": text})

result = structured_llm.invoke(prompt, config={"callbacks": [tracer]})

print(result)
