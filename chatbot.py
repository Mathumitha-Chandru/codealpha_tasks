def get_bot_response(user_input):
     #convert input to lowercase so it's not case sensitive
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a wonderful day!"
    else:
        return "I'm sorry, I don't understand that yet. Could you try saying 'hello'?"
    
def start_chat():
    print("---Simple Chatbot(Type bye to exit)---  ")

    while True:
        #Get input from the user
        user_text = input("You: ")

        #Get the responce from our logic function
        response = get_bot_response(user_text)

        #Print the bot's response
        print(f"Bot: {response}")

        #Break the loop if the user says bye
        if "bye" in user_text.lower():
            break

if __name__ == "__main__":
    start_chat() #chat started
