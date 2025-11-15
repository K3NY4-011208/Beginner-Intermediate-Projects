import random

words = ["python", "ocean", "castle", "jellyfish", "night", "forest"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6

print("Hangman Game")

while tries > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    print(f"Tries left: {tries}")
    letter = input("Guess a letter: ").lower()

    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed[i] = letter
        print("Correct!")
    else:
        tries -= 1
        print("Wrong!")

if "_" not in guessed:
    print("You win! The word was", word)
else:
    print("You lose! The word was", word)
