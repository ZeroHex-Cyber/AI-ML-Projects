import json
from datetime import datetime

def chat_history(user_input, bot_response): # Logs chat conversation to 'Chat_history.txt' file.
    with open("Chat_history.txt", "a") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"Chatbot: {bot_response}\n")

with open("ChatResponses.json") as CR: # Loads contents from ChatResponses.json file.
    responses = json.load(CR)

print("Chatbot: Hello! ")

while True:
    user_input = input("You: ").lower().strip() # Getting input from the user.

    # ---Pattern matching with use_inputs---

    if user_input in ["hi", "hello", "hola"]:
        print("Chatbot:", responses.get("hi"))
        cr = responses.get("hi")
        chat_history(user_input, cr)

    elif user_input in ["bye", "quit", "goodbye", "exit"]:
        print("Chatbot:", responses.get("bye"))
        cr = responses.get("bye")
        chat_history(user_input, cr)
        break

    elif user_input == "how are you":
        print("Chatbot:", responses.get("how are you"))
        cr = responses.get("how are you")
        chat_history(user_input, cr)

    elif user_input == "what is your name":
        print("Chatbot:", responses.get("what is you name"))
        cr = responses.get("what is your name")
        chat_history(user_input, cr)

    elif user_input == "help":
        print("Chatbot:", responses.get("help"))
        cr = responses.get("help")
        chat_history(user_input, cr)

    elif user_input == "thank you":
        print("Chatbot:", responses.get("thank you"))
        cr = responses.get("thank you")
        chat_history(user_input, cr)

    elif user_input == "thanks":
        print("Chatbot:", responses.get("thanks"))
        cr = responses.get("thanks")
        chat_history(user_input, cr)

    elif user_input == "who created you":
        print("Chatbot:", responses.get("who created you"))
        cr = responses.get("who created you")
        chat_history(user_input, cr)

    elif user_input == "what can you do":
        print("Chatbot:", responses.get("what can you do"))    
        cr = responses.get("what can you do")
        chat_history(user_input, cr)

    elif user_input == "what is your age":
        print("Chatbot:", responses.get("what is your age"))  
        cr = responses.get("what is your age")
        chat_history(user_input, cr)

    elif user_input == "who am i":
        print("Chatbot:", responses.get("who am i")) 
        cr = responses.get("who am i")
        chat_history(user_input, cr)

    elif user_input == "what should i wear":
        print("Chatbot:", responses.get("what should i wear")) 
        cr = responses.get("what should i wear")
        chat_history(user_input, cr)

    elif user_input == "how do i stay healthy":
        print("Chatbot:", responses.get("how do i stay healthy")) 
        cr = responses.get("how do i stay healthy")
        chat_history(user_input, cr)

    elif user_input == "ok":
        print("Chatbot:", responses.get("ok")) 
        cr = responses.get("ok")
        chat_history(user_input, cr)

    elif user_input == "what do you like":
        print("Chatbot:", responses.get("what do you like")) 
        cr = responses.get("what do you like")
        chat_history(user_input, cr)

    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        ct = f"The current time is {current_time}"
        chat_history(user_input, ct)

    elif "date" in user_input:
        current_date = datetime.now().strftime("%B %d, %Y")
        cd = f"Today's date is {current_date}"
        chat_history(user_input, cd)

    else:
        response = responses.get(user_input, "Sorry, I don't understand that.")
        res = f"Chatbot: {response}"
        chat_history(user_input, res)
        
       
