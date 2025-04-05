from langchain.chat_models import init_chat_model

from langchain_core.prompts import ChatPromptTemplate

model = init_chat_model("gpt-4o-mini", model_provider="openai")

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
  [("system", system_template), ("user", "{text}")]
)


def translate(text="", language="Italian"):
  try:
    prompt = prompt_template.invoke({
      "language": language,
      "text": text,
    })

    prompt.to_messages()

    response = model.invoke(prompt)

    return response.content
  except Exception as e:
    return e
