import random

'''
snake = -1
water = 0
gun = 1
'''

# Random choice for computer
computer = random.choice([-1, 0, 1])

# Mapping
dict_033 = {"s": -1, "w": 0, "g": 1}
resevdict = {-1: "snake", 0: "water", 1: "gun"}

# User input
your_choice = input("Enter your choice (s = snake, w = water, g = gun): ").lower()

# Safety check for invalid inputs
if your_choice not in dict_033:
    print("Invalid choice! Please choose 's', 'w', or 'g'.")
else:
    you = dict_033[your_choice]

    print(f"You chose: {resevdict[you]}")
    print(f"Computer chose: {resevdict[computer]}")

    # Game logic
    if you == computer:
        print("It's a tie!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == -1 and you == 1:
        print("You win!")
    elif computer == 0 and you == -1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You lose!")
    elif computer == 1 and you == -1:
        print("You win!")
    else:
        print("Something went wrong!")
