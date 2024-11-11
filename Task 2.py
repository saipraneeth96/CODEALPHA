import random

# List of words for the Hangman game
words = ["python", "programming", "hangman", "challenge", "developer", "function", "variable"]


def choose_word():
    """Randomly choose a word from the list."""
    return random.choice(words)


def display_current_state(word, guessed_letters):
    """Display the current state of the guessed word."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman_game():
    word = choose_word()
    guessed_letters = set()  # Track guessed letters
    attempts = 6  # Number of incorrect guesses allowed
    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts > 0:
        print("\nWord:", display_current_state(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1

        # Check if the player has guessed all letters in the word
        if set(word).issubset(guessed_letters):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame Over. You've run out of attempts.")
        print("The word was:", word)


# Run the game
hangman_game()
