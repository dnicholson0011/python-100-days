# Answer > using a simple for loop with casting
# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
#
####################################
# Write your code below this line 👇
# sum = 0
# for char in two_digit_number:
#     sum += int(char)
# print(sum)

# Answer > using a list. Sum variable is already used, therefore commenting out above to run.
# Sum is a built feature, so assigning it a variable is bad practice. Leaving as is for teaching purposes above.
# two_digit_number = input("Type a two digit number: ")
# num_list = list(two_digit_number)
# num_list = [int(i) for i in num_list]
# result = sum(num_list)
# print(result)

# Answer > Basic answer using subscripting
two_digit_number = input("Type a two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
result = first_digit + second_digit
print(result)