from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine = MoneyMachine()

coffee = CoffeeMaker()

m = Menu()

# MItem = MenuItem()

stop = True

while stop:
    options = m.get_items()
    choice = input(F"What would you like? {options}: ")
    if choice == "off":
        stop = False
    elif choice == 'report':
        coffee.report()
        machine.report()
    else:
        drink = m.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):
                coffee.make_coffee(drink)

            
    