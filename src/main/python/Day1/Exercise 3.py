# Counts only characters, compact method
num = input("Name ")
print(sum(c.isalpha() for c in num))

# Same as above, not compact method
num = input("Name ")

count = 0
for c in num:
    if c.isalpha():
        count += 1

print(count)

# Counts spaces only
num = input("Name ")
print(num.count(' '))

# Answer > counts spaces and characters = full length of the string. Len is short for length!
num = input("What is your name? ")
print(len(num))

#Alternate solution
num = "Hello " + input('What is your name? ') + "!"
print(num)
print(len(num))