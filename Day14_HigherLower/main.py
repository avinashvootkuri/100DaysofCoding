from art import logo, vs
from game_data import data
import random

# Priting logo for the game
print(logo)

compare_A = random.randint(0,len(data)-1)
compare_B = random.randint(0,len(data)-1)

def compare(A, B, user,end):
    """Compare follower count and return end flag"""
    if A['follower_count'] > B ['follower_count'] and user == 'A':
        end = False
    elif A['follower_count'] < B ['follower_count'] and user == 'B':
        end = False
    else:
        end = True
    return end

score = 0
end_of_game = False

while not end_of_game:
    print(F" Compare A: {data[compare_A]['name']}, {data[compare_A]['description']}, {data[compare_A]['country']} ")
    print(vs)
    print(F" Compare B: {data[compare_B]['name']}, {data[compare_B]['description']}, {data[compare_B]['country']} ")
    user_choice = input("Who as the most followers? 'A' or 'B'?").upper()
    flag =  compare(data[compare_A], data[compare_B], user_choice, end_of_game)
    if flag == False:
        score += 1
        print(F"You're right! Current Score {score}." )
        compare_A = compare_B
        compare_B = random.randint(0,len(data)-1)
        while compare_A == compare_B:
            compare_B = random.randint(0,len(data)-1)
    else:
        end_of_game = True
        print(F"Final Score! {score}.")