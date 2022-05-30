#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''


for s in range(0,nr_symbols):
        # password.append(random.choice(symbols))
    password +=  random.choice(symbols)
for r in range(0,nr_numbers):
        # password.append(random.choice(numbers))
    password +=  random.choice(numbers)

for n in range(0,nr_letters):
    # password.append(random.choice(letters)) 
    password += random.choice(letters)


l = list(password)
random.shuffle(l)
shuffled_pwd = ''.join(l)
print(F"Your password is : {shuffled_pwd}")



