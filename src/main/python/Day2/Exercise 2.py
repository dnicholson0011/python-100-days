# Answer
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# BMI = float(weight) / pow(float(height),2)
# print(int(BMI))

# Less concise answer but explicitly separates operations
BMI = int(weight) / float(height) ** 2
BMI_as_int = int(BMI)
print(BMI_as_int)
