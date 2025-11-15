import random

flashcards = {
    "Capital of Kenya": "Nairobi",
    "5 x 7": "35",
    "Color of the sky": "blue",
    "Opposite of hot": "cold"
}

keys = list(flashcards.keys())
score = 0

for _ in range(4):
    question = random.choice(keys)
    answer = flashcards[question]

    user = input(question + ": ").lower()
    if user == answer.lower():
        print("Correct")
        score += 1
    else:
        print("Wrong")

print(f"Score: {score}/4")
