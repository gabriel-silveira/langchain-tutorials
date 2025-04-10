from src.chatbot import invoke

if __name__ == "__main__":
  thread_id = "chatbot_test_1"

  invoke("Hi! I'm Gabriel.", thread_id)
  invoke("What is my name?", thread_id)
