# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_num = 0
for n in student_scores:
    if n >= highest_num:
        highest_num = n
    else:
        continue

print("The highest score in the class is: " + str(highest_num))



