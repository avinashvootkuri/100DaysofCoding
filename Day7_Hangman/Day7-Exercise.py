from hangman_art import stages, logo
from hangman_wordslist import word_list
import random

print(logo)

chosen_word = random.choice(word_list)

display = []

for n in chosen_word:
    display.append("_")

print(display)

print("You have 6 lifes to win")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False
# user_guess = ""
no_of_lifes = 6
while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      print(F"You guessed {guess}, that is not in word, you lose a life.")

    print(display)

    if guess not in chosen_word:
        no_of_lifes -= 1
        if no_of_lifes == 0:
            end_of_game = True
            print("You lose")


    if '_' not in display:
        end_of_game = True
        print("You win")  

    print(stages[no_of_lifes])

    