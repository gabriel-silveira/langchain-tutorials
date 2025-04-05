from src.translator import translate

if __name__ == "__main__":
  userText = input("Type the text you want to translate:\n")

  response = translate(userText)

  print(response)
