# Percent String Formatting

# Backslash (\): In Python, the backslash (\) is the escape character.
# It is used to introduce special character sequences known as escape sequences, which represent certain special characters.
# For example, \n represents a newline, \t represents a tab, \" represents a double quote, \' represents a single quote, and \\ represents a backslash.
print("Hello\nWorld")  # Prints "Hello" and "World" on separate lines
print("Hello\\World")  # Prints "Hello\World"

# Percent (%): In the context of string formatting with the % operator, you can use %% to represent a literal % character.
# This is a bit like an escape sequence, but it's specific to the % operator for string formatting.
discount = 20
print("Get a %d%% discount!" % discount)  # Prints "Get a 20% discount!"

# %s: String (or any object with a string representation, like numbers)
name = "Alice"
print("#1 %%s: My name is %s." % name)  # Output: My name is Alice.

# %d: Integers
age = 25
print("#2 %%d: I am %d years old." % age)  # Output: I am 25 years old.

# %f: Floating point numbers
pi = 3.14159
print("#3 %%f: Pi is approximately %f." % pi)  # Output: Pi is approximately 3.141590.

# %.<number of digits>f: Floating point numbers with a fixed amount of digits to the right of the dot.
pi = 3.14159
print("#4 %%.2f: Pi is approximately %.2f." % pi)  # Output: Pi is approximately 3.14.

# %x/%X: Integers in hex representation (lowercase/uppercase)
number = 255
print("#5 %%x/%%X: The number %d is %x in hexadecimal and %X in hexadecimal uppercase." % (number, number, number))  # Output: The number 255 is ff in hexadecimal and FF in hexadecimal uppercase.
