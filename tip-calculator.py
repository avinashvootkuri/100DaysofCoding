print("Welcome to the tip Calculator!")
total_bill = float(input("What was the total bill?"))

percent_tip = int(input("What is the percentage tip you like to give? 10,12 or 15?"))

no_of_splits = int(input("How many people to split the bill?"))

total_with_tip = total_bill + total_bill * (percent_tip/100)
each_person_amount = total_with_tip/no_of_splits

print(F"Each person should pay: {each_person_amount}")
