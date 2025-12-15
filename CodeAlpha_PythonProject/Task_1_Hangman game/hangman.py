import random

def play_hangman():
    # 1. Simplified Scope: Small list of 5 predefined words
    words = ["python", "java", "kotlin", "javascript", "swift"]
    
    # Select a random word from the list
    secret_word = random.choice(words)
    guessed_word = ["_"] * len(secret_word)
    
    attempts_left = 6  # Limit incorrect guesses to 6
    guessed_letters = [] # Track letters already guessed

    print("Welcome to Hangman!")
    print(f"I have selected a word with {len(secret_word)} letters.")
    
    # 2. Key Concepts: while loop to keep the game running
    while attempts_left > 0:
        print("\nCurrent word: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Basic console input
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # 3. Key Concepts: if-else logic for checking the guess
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            
            # Reveal the letter in the guessed_word list
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_left -= 1

        # Check for Win condition
        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word:", secret_word)
            break
    
    # Check for Loss condition
    if attempts_left == 0:
        print("\nGame Over! The word was:", secret_word)

