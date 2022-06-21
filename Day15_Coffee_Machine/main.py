
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report(resources, profit):
    print(F"Water : {resources['water']}ml")
    print(F"Milk : {resources['milk']}ml")
    print(F"Coffee : {resources['coffee']}g")
    print(F"Money : ${profit}")

def  sufficient(coffee, user_i, resources):
    if user_i == 'espresso':
        if coffee[user_i]['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water.")
            return True
        elif coffee[user_i]['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee.")
            return True
    elif user_i == 'latte' or user_i == 'cappuccino':
        if coffee[user_i]['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water.")
            return True
        elif coffee[user_i]['ingredients']['milk'] > resources['milk']:
            print("Sorry there is not enough milk.")
            return True
        elif coffee[user_i]['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee.")
            return True
    return False

def check_coins(MENU, user_i):
    print("Please insert Coins.")
    quaters = int(input('How many quaters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many Pennies?: '))

    total_paid = quaters * 0.25 + dimes * 0.10 + nickles * .05 + pennies * 0.01

    if total_paid > float(MENU[user_i]['cost']):
        change = round(total_paid -  float(MENU[user_i]['cost']),2)
        print(F'Here is ${change} in change')
        print(F"Here is your {user_i} ☕")
        return False
    else:
        print("Sorry that's not enough money. Money refunded.")
        return True

def check_resources(MENU, user_i,stop):
    if stop == False and user_i == 'espresso':
        resources['water'] -=  MENU[user_i]['ingredients']['water']
        resources['coffee'] -= MENU[user_i]['ingredients']['coffee']            
    elif stop == False and user_i == 'latte' or user_i == 'cappuccino':
        resources['water'] -=  MENU[user_i]['ingredients']['water']
        resources['milk'] -= MENU[user_i]['ingredients']['milk']
        resources['coffee'] -= MENU[user_i]['ingredients']['coffee']
    return resources


profit = 0



# TODO 2: Turn off Coffee machine by entering "off"

stop = False

# TODO 3: pring report

while not stop:
# TODO 1: prompt user "what do you like"
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        report(resources, profit)
    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        flag = sufficient(MENU, user_input, resources) 
        if stop == False and flag == False:
            coin_check = check_coins(MENU, user_input)
            if coin_check == False:
                profit += MENU[user_input]['cost']
                resources = check_resources(MENU, user_input,stop)            
    else:
        if user_input == 'off':
            stop = True
        else:
            print('Please enter correct option?')









