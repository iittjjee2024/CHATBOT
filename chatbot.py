import re
from datetime import datetime


RULES = {
    ("hello", "hi", "hey", "greetings", "good morning", "good evening", "good afternoon"): 
        "Hello! How can I help you today?",

    ("bye", "goodbye", "see you", "take care", "exit", "quit"): 
        "Goodbye! Have a great day!",

    ("how are you", "how do you do", "how's it going", "what's up"): 
        "I'm just a program, but I'm doing great! Thanks for asking.",

    ("your name", "who are you", "what are you"): 
        "I'm a rule-based chatbot built with Python. You can ask me simple questions!",

    ("what can you do", "help", "what do you know", "capabilities"): 
        "I can respond to greetings, answer basic questions about myself, "
        "tell you the time, and have a simple conversation. Try asking me something!",

    ("time", "what time", "current time"): 
        "TIME_RESPONSE",

    ("weather", "temperature", "forecast"): 
        "I don't have access to real-time weather data, but you can check a weather website!",

    ("how old", "your age", "when were you made"): 
        "I was just created! Age doesn't really apply to me.",

    ("thank", "thanks", "awesome", "great", "good job", "well done"): 
        "You're welcome! I'm happy to help.",

    ("who made you", "who created you", "developer", "creator"): 
        "I was built as a Python project to demonstrate rule-based chatbot logic.",

    ("joke", "funny", "make me laugh"): 
        "Why do programmers prefer dark mode? Because light attracts bugs!",

    ("meaning of life", "purpose", "why do you exist"): 
        "My purpose is to demonstrate how rule-based chatbots work. "
        "As for the meaning of life... maybe 42?",
}

FALLBACK_RESPONSE = (
    "I'm not sure how to respond to that. "
    "Try saying 'hello', asking 'what can you do', or type 'bye' to exit."
)


def get_response(user_input):
    processed_input = user_input.lower().strip()
    
    for keywords, response in RULES.items():
        for keyword in keywords:
            if keyword in processed_input:
                if response == "TIME_RESPONSE":
                    current_time = datetime.now().strftime("%H:%M:%S")
                    return f"The current time is {current_time}."
                return response
    
    return FALLBACK_RESPONSE


def should_exit(user_input):
    exit_keywords = ["bye", "goodbye", "exit", "quit"]
    return any(word in user_input.lower() for word in exit_keywords)


def main():
    print("=" * 50)
    print("  RULE-BASED CHATBOT")
    print("  Type 'bye' or 'exit' to end the conversation")
    print("=" * 50)
    print()
    print("Chatbot: Hello! I'm a simple rule-based chatbot.")
    print("         Ask me anything or type 'help' to see what I can do.")
    print()
    
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nChatbot: Goodbye! Have a great day!")
            break
        
        if not user_input:
            print("Chatbot: Please type something! I'm here to chat.\n")
            continue
        
        response = get_response(user_input)
        print(f"Chatbot: {response}\n")
        
        if should_exit(user_input):
            break


if __name__ == "__main__":
    main()
