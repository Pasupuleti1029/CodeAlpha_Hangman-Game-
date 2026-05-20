import random

# List of predefined words
words = ["python", "apple", "chair", "robot", "tiger"]

# Randomly choose a word
word = random.choice(words)

# Create empty display with underscores
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Game loop
while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect attempts left:", attempts)

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if letter is in word
    if guess in word:
        print("✅ Correct guess!")

        # Reveal the letter in the word
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("❌ Wrong guess!")
        attempts -= 1

# Final result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)