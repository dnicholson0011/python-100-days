# iterate through a list
import random

my_list_1 = [1, 2, 3]
for item in my_list_1:
    print(item)

# sum items in list
total_1 = sum(my_list_1)
print(total_1)

# sum items in a list
total_2 = 0
for item in my_list_1:
    total_2 += item
print(total_2)

# choose 2 random integers from list
my_list_2 = [1, 2, 3, 4, 5, 6]
person_1 = []
person_2 = []
for _ in range(2):
    person_1.append(random.choice(my_list_2))
    person_2.append(random.choice(my_list_2))
print(person_1)
print(person_2)