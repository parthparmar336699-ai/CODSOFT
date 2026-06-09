import time

def bot_reply(text):
    print("Bot: ", end="")
    time.sleep(0.4) 
    print(text)

print("=========================================")
print("     CODSOFT AI INTERN: TASK 1           ")
print("    RULE-BASED INTELLIGENT CHATBOT       ")
print("=========================================")
print("Type 'bye' anytime to exit the chatbot.\n")

while True:
    user_input = input("You: ").lower().strip()
    
    if user_input == "hello" or user_input == "hi":
        bot_reply("Namaste Parth! Welcome back. How can I help you today?")
        
    elif user_input == "college" or user_input == "btech":
        bot_reply("I am currently acting as your BTECH Assistant Bot. Keep grinding!")
        
    elif user_input == "joke" or user_input == "meme":
        bot_reply("Why do programmers love Python? Because it's easy to read, unlike code syntax errors!")
        
    elif user_input == "bye" or user_input == "exit":
        bot_reply("Goodbye Parth! Thank you for chatting. Have a great day ahead!")
        break
        
    else:
        bot_reply("Sorry, I didn't quite catch that. Try asking about 'college' or 'joke'!")
        
    print("-" * 41)