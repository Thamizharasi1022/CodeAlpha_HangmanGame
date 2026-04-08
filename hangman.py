import random

words = ["apple", "tiger", "chair", "plant", "stone"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman Game")

while attempts > 0:
    print("\nWord:", " ".join(guessed))
    print("Used letters:", used_letters)

    letter = input("Enter a letter: ").lower()

    if letter in used_letters:
        print("Already used!")
        continue

    used_letters.append(letter)

    if letter in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print(" Wrong! Attempts left:", attempts)

    if "_" not in guessed:
        print("\n You WON! Word is:", word)
        break
else:
    print("\n You LOST! Word was:", word)
