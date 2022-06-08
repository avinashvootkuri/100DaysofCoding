#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number_choosen = random.randint(1,100)

difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ")

def easy(choosen, attempts):
    while attempts!= 0:
        guess = int(input('Make a guess: '))

        if guess == choosen:
            print(F'You guessed it right {choosen}')
            return
        elif guess > choosen:
            print(F'Too high!')
        else:
            print('Too Low!')

        attempts-= 1
        print(F'You have {attempts} attempts remaining to guess the number.')
    print(F'You have lost the game! Current guess was {choosen}!!')

def hard(choosen, attempts):
    while attempts!= 0:
        guess = int(input('Make a guess: '))

        if guess == choosen:
            print(F'You guessed it right {choosen}')
            return
        elif guess > choosen:
            print(F'Too high!')
        else:
            print('Too Low!')

        attempts-= 1
        print(F'You have {attempts} attempts remaining to guess the number.')
    print(F'You have lost the game! Current guess was {choosen}!!')
    

    

if difficulty == 'easy':
    print('you have 10 attempts remaining to guess the number.')
    easy(number_choosen, 10)
elif difficulty == 'hard':
    print('you have 5 attempts remaining to guess the number.')
    hard(number_choosen, 5)
else:
    print('enter a valid option!')
    

