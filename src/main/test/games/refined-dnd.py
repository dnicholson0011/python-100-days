import random

def roll_dice(sides):
    return random.randint(1, sides)

def print_result(total, sides):
    print(f"Rolled a {total} on a d{sides}")
    if sides == 20:
        if total >= 20:
            print("Critical Success!")
        elif total <= 1:
            print("Critical Failure!")
        elif total >= 10:
            print("Success!")
        else:
            print("Failure!")

def main():
    while True:
        sides = input("Enter the number of sides on the dice, or 'q' to quit:\n")
        if sides.lower() == 'q':
            print("Goodbye")
            break
        elif sides.isdigit() and int(sides) in {4, 6, 8, 10, 12, 20}:
            modifier = input("Enter a modifier to add to the roll:\n")
            if modifier.lstrip('-').isdigit():  # Check if the input is a number (including negative numbers)
                total = roll_dice(int(sides)) + int(modifier)
                print_result(total, int(sides))
            else:
                print("Invalid modifier, try again.")
        else:
            print("Not a valid input, try again.")

if __name__ == "__main__":
    main()
