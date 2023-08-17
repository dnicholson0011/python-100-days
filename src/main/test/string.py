# String Methods:

# lower(): Converts all the characters in the string to lowercase.
my_string = "Hello, World!"
print("#1 lower: " + my_string.lower())  # Output: hello, world!

# upper(): Converts all the characters in the string to uppercase.
my_string = "Hello, World!"
print("#2 upper: " + my_string.upper())  # Output: HELLO, WORLD!

# capitalize(): Converts the first character of the string to uppercase and makes all other characters lowercase.
my_string = "hello, WORLD!"
print("#3 capitalize: " + my_string.capitalize())  # Output: Hello, world!

# title(): Converts the first character of each word to uppercase and makes all other characters lowercase.
my_string = "hello, WORLD!"
print("#4 title: " + my_string.title())  # Output: Hello, World!

# strip(): Removes leading and trailing whitespace from the string.
my_string = "   Hello, World!   "
print("#5 strip: '" + my_string.strip() + "'")  # Output: 'Hello, World!'

# startswith(prefix): Returns True if the string starts with the specified prefix, False otherwise.
my_string = "Hello, World!"
print("#6 startswith: " + str(my_string.startswith("Hello")))  # Output: True

# endswith(suffix): Returns True if the string ends with the specified suffix, False otherwise.
my_string = "Hello, World!"
print("#7 endswith: " + str(my_string.endswith("!")))  # Output: True

# find(substring): Returns the lowest index in the string where the substring is found. Returns -1 if the substring is not found.
my_string = "Hello, World!"
print("#8 find: " + str(my_string.find("World")))  # Output: 7

# replace(old, new): Returns a copy of the string with all occurrences of the old substring replaced by the new substring.
my_string = "Hello, World!"
print("#9 replace: " + my_string.replace("World", "Universe"))  # Output: Hello, Universe!

# split(separator): Returns a list of words in the string, using the separator as the delimiter string.
my_string = "Hello, World!"
print("#10 split: " + str(my_string.split(" ")))  # Output: ['Hello,', 'World!']

# join(iterable): Joins all items in an iterable (like a list or a tuple) into a single string, with the string as the delimiter.
my_list = ['Hello', 'World!']
print("#11 join: " + ' '.join(my_list))  # Output: Hello World!

# count(substring): Returns the number of non-overlapping occurrences of a substring in the string.
my_string = "Hello, World!"
print("#12 count: " + str(my_string.count('o')))  # Output: 2

# isdigit(): Returns True if all the characters in the string are digits, False otherwise.
my_string = "12345"
print("#13 isdigit: " + str(my_string.isdigit()))  # Output: True

# isalpha(): Returns True if all the characters in the string are alphabetic, False otherwise.
my_string = "Hello"
print("#14 isalpha: " + str(my_string.isalpha()))  # Output: True

# isspace(): Returns True if all the characters in the string are whitespace characters, False otherwise.
my_string = "   "
print("#15 isspace: " + str(my_string.isspace()))  # Output: True

# len(string): Returns the number of characters in the string. Note that len() is a built-in Python function, not a string method, so it's used a bit differently.
my_string = "Hello, World!"
print("#16 len: " + str(len(my_string)))  # Output: 13
