def simple_chatbot():
    print("Simple Chatbot: Hello! Type 'bye' to exit.")
    
    # Key Concept: Loops (to keep the conversation going)
    while True:
        # Key Concept: Input/Output
        user_input = input("You: ").lower().strip() # Normalize input to lowercase
        
        # Key Concept: if-elif logic for rule-based responses
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you today?")
            
        elif "how are you" in user_input:
            print("Chatbot: I'm just a computer program, but I'm functioning perfectly! Thanks for asking.")
            
        elif "your name" in user_input:
            print("Chatbot: I am a simple Python Chatbot created for CodeAlpha.")
            
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break # Exit the loop
            
        else:
            # Default response for unknown inputs
            print("Chatbot: I'm sorry, I don't understand that. Try saying 'hello' or 'how are you'.")

# Key Concept: Functions
if __name__ == "__main__":
    simple_chatbot()