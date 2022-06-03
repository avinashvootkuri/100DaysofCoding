### Program to create a calculator
from art import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for k in operations:
        print(k)
    continue_c = True

    while continue_c:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        for k in operations:
            print(k)
        
        calculation_function = operations[operation_symbol]
        result = float(calculation_function(num1, num2))
        print(F"{num1} {operation_symbol} {num2} = {result}")

        y_or_n = input(F"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.: ")
        if y_or_n == 'n':
            continue_c = False
            calculator()
        num1 = result

calculator()
