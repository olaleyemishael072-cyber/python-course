print("Chatbot: Hi! I can answer a few simple questions. Type 'bye' to stop.")

while True:
    message = input("You: ").strip().lower()

    if message in ("hi", "hello", "hey"):
        print("Chatbot: Hello! How can I help you?")
    elif "how are you" in message:
        print("Chatbot: I'm doing well. Thanks for asking!")
    elif "your name" in message:
        print("Chatbot: I'm a simple Python chatbot.")
    elif message in ("bye", "exit", "quit"):
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot: Sorry, I don't understand. Try saying hello or asking my name.")
