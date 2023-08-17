# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# bill = 0
#
# if size.lower() == "s":
#     bill += 15
#     if add_pepperoni.lower() == "y":
#         bill += 2
#     else:
#         bill += 0
#
# if size.lower() == "m":
#     bill += 20
#     if add_pepperoni.lower() == "y":
#         bill += 3
#     else:
#         bill += 0
#
# if size.lower() == "l":
#     bill += 25
#     if add_pepperoni.lower() == "y":
#         bill += 3
#     else:
#         bill += 0
#
# if extra_cheese.lower() == "y":
#     bill += 1
# else:
#     bill += 0
#
# print(f"Your final bill is: ${bill}.")

# Much better solution below
#Write your code below this line 👇
bill = 0

# Pizza size pricing
size = size.lower()
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

# Pepperoni pricing
if add_pepperoni.lower() == "y":
    bill += 2 if size == "s" else 3

# Extra cheese pricing
if extra_cheese.lower() == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")