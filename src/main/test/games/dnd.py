import random

dice = [1, 2, 3]
multiplier = [-1, 1]

dice_roll = random.choice(dice)
dice_multiplier = random.choice(multiplier)

roll = input("Type 'y' to roll, or 'n' to stop:\n")

should_continue = True

while should_continue:
    if roll == "y":
        dice_roll = random.choice(dice)
        dice_multiplier = random.choice(multiplier)
        print("Rolled: " + str(dice_roll))
        print("Multiplier: " + str(dice_multiplier))
        total = int(dice_roll + dice_multiplier)
        if total == 1:
            print("Critical Success!")
        elif total == 3:
            print("Success!")
        else:
            print("Fail")
        roll = input("Shall we roll again?\n")
        if roll == "y":
            continue
        elif roll == "n":
            should_continue = False
            print("Goodbye")
    elif roll == "n":
        should_continue = False
        print("Goodbye")
    else:
        roll = input("Not a valid input, try again:\n")