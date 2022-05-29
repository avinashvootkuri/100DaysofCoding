### Day4 of Code
### Code for Rock, Paper and Scissors 

import random
from secrets import choice


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

# options = [0,1,2]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if player_choice >=3 or player_choice <0:
    print("Enter a valid number, 0, 1 or 2")
else:
    print(game_images[player_choice])

    computer_choice = random.randint(0,2)
    print(F"Computer choose: {game_images[computer_choice]}")


    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose!")
    elif computer_choice > player_choice:
        print("You lose!")
    elif player_choice > computer_choice:
        print("You win!")
    elif player_choice == computer_choice:
        print("Its a Draw!")


