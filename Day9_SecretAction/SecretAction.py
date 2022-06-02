from cmath import log
from art import logo

print(logo)
print("Welcome to the Secret Action!!")

Action_dict = {}

entry = True

while entry:
    Name = input("What is your name?: ")
    Price = int(input("What is your bid? $"))
    Action_dict[Name] = Price

    # add_entry(Name, Price)
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.")
    if yes_or_no == 'no':
        entry = False
        max_value = max(Action_dict.values())
        keys = [x for x,y in Action_dict.items() if y == max_value]
        print(F"The Winner of the bid is {keys[0]}, bidded {max_value}")





