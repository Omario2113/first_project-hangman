#Hangman Game (First Project)

import re
word = input("Welcome to Hangman!\nWhat word would you like to have guessed?: ")
print("The word is %s letters long\n" %len(word))
word_with_guesses = list("_" * len(word))
game_state = 1
wrong_guesses = 0
guesses = []

while game_state == 1:
    print("Word is: %s" %(" ".join(word_with_guesses)))
    letter = input("What letter would you like to guess?: ")
    if len(letter) > 1:
        print("Term entered is invalid...try again!\n")
    elif letter in guesses:
        print("Letter has already been guessed...try again!\n")
    else:
        guesses.append(letter)
        if letter in word:
            print("Letter found! Filling in the spaces...\n")
            for match in re.finditer(letter, word):
                letter_index = match.span()[0]
                word_with_guesses[letter_index] = letter
            if '_' not in word_with_guesses:
                print("You figured it out, good guessing!")
                game_state = 2
        else:
            wrong_guesses += 1
while game_state == 2:
    print("\nGAME OVER")
    break