# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2
rounded_number = round(bmi)
integer_number = int(rounded_number)
# print(integer_number)

# if integer_number <= 18.5:
#     print(f'Your BMI is {integer_number}, you are underweight.')
# elif integer_number > 18.5 and integer_number < 25:
#     print(f'Your BMI is {integer_number}, you have a normal weight.')
# elif integer_number > 25 and integer_number < 30:
#     print(f'Your BMI is {integer_number}, you are slightly overweight.')
# elif integer_number > 30 and integer_number < 35:
#     print(f'Your BMI is {integer_number}, you are obese.')
# else:
#     print(f'Your BMI is {integer_number}, you are clinically obese')

# This answer is simpler and easy to read
if integer_number < 18.5:
    print(f'Your BMI is {integer_number}, you are underweight.')
elif integer_number < 25:
    print(f'Your BMI is {integer_number}, you have a normal weight.')
elif integer_number < 30:
    print(f'Your BMI is {integer_number}, you are slightly overweight.')
elif integer_number < 35:
    print(f'Your BMI is {integer_number}, you are obese.')
else:
    print(f'Your BMI is {integer_number}, you are clinically obese')