# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

# Rock
ascii_rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
ascii_paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
ascii_scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
import random
npc = random.randint(0,2)

game = ["Rock", "Paper", "Scissor"]
image = [ascii_rock, ascii_paper, ascii_scissors]

Rock = 0
Paper = 1
Scissors = 2

print(f"You chose " + game[choice] + "\n" + image[choice])
print(f"Computer chose " + game[npc] + "\n" + image[npc])

if choice == Rock and npc == Scissors:
    print("You Win!")
elif choice == Scissors and npc == Paper:
    print("You Win!")
elif choice == npc:
    print("It's a draw")
else:
    print("You Lose")
