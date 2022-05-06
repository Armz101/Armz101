from words import word_list

import random

word = random.choice(word_list)
allowed_errors = 7
guesses = []
done = False

def hangman():
    global word
    global allowed_errors
    global guesses
    global done
    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end= " ")
        print("")
        


        guess = input(f"Allowed Errors Left {allowed_errors}, Next Guesss:")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                break

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False

    if done and allowed_errors > 0:
        print(f"You have found the word! It was {word}!")
    else:
        print(f"Game over! The word was {word}.")
        
    
hangman()