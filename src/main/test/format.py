# String Formatting

# str.format(): This method is used to format strings. You can use {} as placeholders in the string, and then provide the values to insert in the format() method.
name = "Alice"
age = 25
print("#1 str.format: My name is {} and I am {} years old.".format(name, age))  # Output: My name is Alice and I am 25 years old.

# Positional arguments with str.format(): You can use positional arguments to specify the values for the placeholders:
print("#2 str.format positional: {0} is {1} years old.".format(name, age))  # Output: Alice is 25 years old.

# Keyword arguments with str.format(): You can use keyword arguments to specify the values for the placeholders:
print("#3 str.format keyword: {name} is {age} years old.".format(name="Bob", age=30))  # Output: Bob is 30 years old.

# f-strings: Introduced in Python 3.6, f-strings (or formatted string literals) are a new way to format strings.
# They're prefixed with an f or F, and you can put variables and expressions directly inside {} in the string.
name = "Alice"
age = 25
print(f"#4 f-string: My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 25 years old.

# Expressions in f-strings: You can include complex expressions inside the {} in an f-string:
print(f"#5 f-string expression: {age} years is {age * 12} months.")

# Function calls in f-strings: You can even include function calls inside the {} in an f-string:
print(f"#6 f-string function: {name.lower()} is a lowercase version of {name}.")

