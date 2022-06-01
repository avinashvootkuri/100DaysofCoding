
#This a program to encrpyt or decrypt a work based on caesar Cipher work.
#User inputs a word, enter how many position to shift it by and weather to encode or decode

from ntpath import join
from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
 'w', 'x', 'y', 'z']

print(logo)

def caesar(text, shift_amount , perform):
    new_word = ""
    if perform == "decode":
        shift_amount *= -1

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_word += alphabet[new_position]
        else:
            new_word += letter
    print(f"The {perform}d text is {new_word}")  

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text=text, shift_amount=shift%26, perform=direction)

    yes_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if yes_or_no == 'no':
        should_continue = False
        print("Goodbye")


