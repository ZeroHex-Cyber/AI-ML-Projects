import json
from datetime import datetime

# Function to save chat history.
def chat_history(user_input, bot_response):
    with open("Chat_history.txt", "a") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"Chatbot: {bot_response}\n")

# Loads contents from JSON file.
with open("ChatResponses.json") as CR:
    responses = json.load(CR)

# Default chatbot response
print("Chatbot: Hello!")

# Chat Loop
while True:
    # Lowers the input string and removes unnecessary space from it.
    user_input = input("You: ").lower().strip()

    # Question-Response structure.
    if user_input in ["hi", "hello", "hola"]:
        response = responses.get("hi")
    
    elif user_input in ["bye", "quit", "goodbye", "exit"]:
        response = responses.get("bye")
        print("Chatbot:", response)
        chat_history(user_input, response)
        break

    elif user_input in responses:
        response = responses[user_input]

    elif "time" in user_input:
        response = f"The current time is {datetime.now().strftime('%I:%M %p')}"

    elif "date" in user_input:
        response = f"Today's date is {datetime.now().strftime('%B %d, %Y')}"

    else:
        response = responses.get(user_input, "Sorry, I don't understand that.")
    print("Chatbot:", response)
    
    # Calls the chat_history function.
    chat_history(user_input, response)
