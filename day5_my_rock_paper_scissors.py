import random
# 1) TODO make a list of possible choices (aka rock, paper, scissors )
choices = ["rock", "paper", "scissors"]

# ask user for their choice (lower makes sure all our strings are lowercase!)
user = input("Choose rock, paper, or scissors: ").lower()

# ranomly pick one for the computer
comp = random.choice(choices)

#show both choices
print("You: ", user)
print("Computer: ", comp)

# TODO: add the logic here for:
# - 2) checking if it is a tie
if user == comp:
    print("It is a tie!")
# - 3) checking win and lose conditions
elif comp == "rock" and user == "scissors":
    print("Computer wins!")
elif user == "rock" and comp == "scissors":
    print("You win!")
elif comp == "scissors" and user == "paper":
    print("Computer wins!")
elif user == "scissors" and comp == "paper":
    print("You win!")
elif comp == "paper" and user == "rock":
    print("Computer wins!")
elif user == "paper" and comp == "rock":
    print("You win!")   
# - optional 4) saving results to a file    
