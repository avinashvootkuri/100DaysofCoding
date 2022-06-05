import random
from art import logo

print(logo)

def deal_card():
    """Returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculate and return sum of card score """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def is_blackjack(user_score, computer_score):
    if computer_score == user_score:
        print("Draw")
    elif computer_score == 0:
        print('computer wins')
    elif user_score == 0:
        print('user wins')
    elif computer_score > 21:
        print('User wins')
    elif user_score > 21:
        print('Computer wins')
    elif user_score > computer_score:
        print("User wins")
    else:
        print("Computer Wins")


def play_game():
    user_choices = []
    computer_choices = []
    is_game_over = False

    for _ in range(2):
        user_choices.append(deal_card())
        computer_choices.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_choices)
        computer_score = calculate_score(computer_choices)

        print(F"Your cards : {user_choices}, your score :{user_score}")
        print(F"Computer first card : {computer_choices[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:        
            is_game_over = True
        else:
            yes_or_no = input(" Would you like to pick another cards? yes or no: ")
            if yes_or_no == 'yes':
                user_choices.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score < 17:
        computer_choices.append(deal_card())
        computer_score = calculate_score(computer_choices)

    print(F" Final hand {user_choices}, Final Score : {user_score}")
    print(F" Computer's Final hand {computer_choices}, Final Score : {computer_score}")
    is_blackjack(user_score, computer_score)

while input("Do you want to play a game of blackjack? 'yes' or 'no': ").lower() == 'yes':
    play_game()



    









