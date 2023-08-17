# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_days = 90 * 365
total_weeks = 90 * 52
total_months = 90 * 12

days_left = total_days - (int(age) * 365)
weeks_left = total_weeks - (int(age) * 52)
months_left = total_months - (int(age) * 12)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")