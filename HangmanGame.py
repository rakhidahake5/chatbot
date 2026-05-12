import random

# List of predefined words
words = ["python", "hangman", "program", "developer", "script"]

# Randomly choose one word
word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman!")
print(f"You have {attempts} incorrect guesses allowed.")

# Display initial word with underscores
display_word = ["_" for _ in word]

while attempts > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)

