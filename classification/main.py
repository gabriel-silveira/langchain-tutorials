from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class Classification(BaseModel):
  sentiment: str = Field(
    description="The sentiment of the text"
  )

  aggressiveness: int = Field(
    description="How aggressive the text is on a scale from 1 to 10"
  )

  language: str = Field(
    description="The language the text is written in"
  )


if __name__ == '__main__':
  tagging_prompt = ChatPromptTemplate.from_template(
    """
  Extract the desired information from the following passage.

  Only extract the properties mentioned in the 'Classification' function.

  Passage:
  {input}
  """
  )

  llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o-mini"
  ).with_structured_output(Classification)

  input1 = "Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"
  input2 = "Estoy muy enojado con vos! Te voy a dar tu merecido!"
  input3 = "Vaffanculo!"
  input4 = "Get that shit out of here!"
  input5 = "Yo te amo."

  prompt = tagging_prompt.invoke({"input": input1})
  response = llm.invoke(prompt)

  print(response.model_dump())
