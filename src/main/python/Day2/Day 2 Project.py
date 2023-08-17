#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill?\n$")
tip = input("How much tip would you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")

bill_as_float = float(bill)
tip_as_int = int(tip)
people_as_int = int(people)

pay = (bill_as_float + (bill_as_float * tip_as_int / 100)) / people_as_int
pay = round(pay, 2)
final_amount = "{:.2f}".format(pay)

print(f"Each person should pay: ${final_amount}.")

# Alternate answer
print("Welcome to the tip calculator!")
bill = input("What was the total bill?\n$")
tip = input("How much tip would you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")

bill_as_float = float(bill)
tip_as_int = int(tip)
people_as_int = int(people)

pay = (bill_as_float + (bill_as_float * tip_as_int / 100)) / people_as_int
pay = round(pay, 2)

print(f"Each person should pay: ${pay:.2f}")