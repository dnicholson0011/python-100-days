# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# import random
# list_length = len(names)
# rand = random.randint(0, list_length - 1)
# bill = names[rand]
# print(f'{bill} is going to buy the meal today!')

# Better answer
import random
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")