#Hangman Game (First Project)
import re
play_again =True

while play_again == True:
    #Initializes the program's variables
    game_state, wrong_guesses = 0, 0
    guesses = []
    head, larm, body, rarm, lleg, rleg = "", "", "", "", "", ""
    hangman_body = {1:"O",
                    2:"|",
                    3:"/",
                    4:"\\",
                    5:"/",
                    6:"\\"}

    #Checks the validity of the word inputed by Player 1
    while game_state == 0:
        word = input("\n\nWelcome to Hangman!\n\nWhat word do ya wanna guess?: ")
        if re.search(r"[^a-zA-z]", word):
            print("Word entered is invalid...try again!\n")
        else:
            print("Initializing...word is %d letters long\n" % len(word))
            word_with_guesses = list("_" * len(word))
            game_state = 1

    while game_state == 1:
        #Prints current hangman body and word with filled in guesses
        print(f"""  __
                \n | {head}
                \n |{larm}{body}{rarm}
                \n_| {lleg}{rleg}""")
        print("Word is: %s" % (" ".join(word_with_guesses)))
        letter = input("What letter would you like to guess?: ")

        #Checks the validity of the guesses by Player 2
        if len(letter) > 1:
            print("Term entered is invalid...try again!\n")
        elif letter in guesses:
            print("Letter has already been guessed...try again!\n")

        #Continues if guess is valid
        else:
            guesses.append(letter)
            if re.search(letter, word, re.I):
                print("Letter found! Filling in the spaces...\n")
                for match in re.finditer(letter, word, re.I):
                    word_with_guesses[match.span()[0]] = letter
                if '_' not in word_with_guesses:
                    print("YOU WON, good guessing!")
                    game_state = 2
            else:
                wrong_guesses += 1
                if wrong_guesses == 5:
                    print("Uh oh...one more wrong guess and you're done...")

    #Sees if users want to play again
    while game_state == 2:
        rematch = input("\nGAME OVER...play again? (Y/N): ")
        if rematch != "Y" and rematch != "N":
            print("Input is not valid...try again!")
        elif rematch == "N":
            print("Bhet, Cya l8r :)")
            play_again = False
            break
        elif rematch == "Y":
            break
    continue
