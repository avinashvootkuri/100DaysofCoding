### Day 3 of Coding
### Write code for Treasure Island

print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")

# step1 = input("Would you like to take 'Left' or 'Right'? ")
# step2 = input("Would you like to 'Swim' or 'Wait'? ")
# step3 = input("Which door would you like to enter 'Red','Blue' or 'Yellow'? ")

if input("You are at a crossroad would you like to take 'Left' or 'Right'? ").lower() == 'left':
    if input("You have come to a lake, Would you like to 'Swim' or 'Wait'? ").lower() == 'Swin':
        if input("You are the final step, Which door would you like to enter 'Red','Blue' or 'Yellow'? ").lower() == 'Yellow':
            print("You Won!")
        else:
            print("You choose the wrong door, Game Over.")
    else:
        print("No other way to go ahead, Game Over.")
else:
    print("Fell in a hole, Game Over.")
