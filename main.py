from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
from pairs import pairs

# Reflections is a dictionary to convert user inputs to bot responses
from reflections import reflections

# Create Chat Bot
chatbot = Chat(pairs, reflections)


# Start conversation
def chatbot_conversation():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    continue_chat = True
    while continue_chat:
        user_input = input(">")
        if user_input.lower() == "quit":
            print("Bye for now. See you soon!")
            continue_chat = False
        else:
            response = chatbot.respond(user_input)
            print(response)
        
chatbot_conversation()
