# Functions with outputs

# Convert a string to Title case

# Add useful document to your functions called Docstrings using triple quotes """Message"""
def format_name(f_name, l_name):
    """Take a first and last name and format it to return
    the title case version of the name"""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

first_name = input("Type your first name: ")
last_name = input("Type your last name: ")

print(format_name(first_name, last_name))

# Useful tip - if you use an empty return statement, "none" will be returned.