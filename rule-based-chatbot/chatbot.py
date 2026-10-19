import re

def get_response(user_input):
    # Normalize input: lowercase and remove extra whitespace
    user_input = user_input.lower().strip()

    # Rule-based logic using keyword matching
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! I'm your rule-based chatbot. How can I help you today?"
    
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot created for this project."
    
    elif any(word in user_input for word in ["how are you", "how's it going"]):
        return "I'm doing great, thank you for asking! How about you?"
    
    elif "help" in user_input:
        return "I can answer basic questions, greet you, or just chat. Try asking my name!"
    
    elif "purpose" in user_input or "what do you do" in user_input:
        return "My purpose is to demonstrate how simple rule-based systems work in Python."

    elif any(word in user_input for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! Have a wonderful day!"

    else:
        return "I'm sorry, I don't understand that. Could you try rephrasing? I can handle greetings, introductions, and basic questions."

def main():
    print("--- Rule-Based Chatbot ---")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    
    while True:
        try:
            user_input = input("You: ")
            
            response = get_response(user_input)
            print(f"Chatbot: {response}")
            
            # Check for exit condition to break the loop
            if any(word in user_input.lower() for word in ["bye", "exit", "quit"]):
                break
        except KeyboardInterrupt:
            print("\nChatbot: Goodbye!")
            break

if __name__ == "__main__":
    main()
