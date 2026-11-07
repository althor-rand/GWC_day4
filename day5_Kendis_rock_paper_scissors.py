#Kendi's code
# use while loop to play a few times

import random

round = 0 
round_input = int(input("How many rounds do you want to play? "))

while round < round_input:

    choices = ["rock", "paper", "scissors"]

    user = input("Choose rock, paper, or scissors: ").lower()

    comp = random.choice(choices)

    print("You:", user)
    print("Computer:", comp)

    if (user == comp):
        print("There was a tie :(")

    elif ((user == "rock" and comp == "scissor") or 
        (user == "paper" and comp == "rock") or 
        (user == "scissors" and comp == "paper")):

        print("The user wins!")

        winner = "The user"

    else:
        print("The computer wins!")

        winner = "The computer"


    round += 1

 
with open("winner.txt", "w") as file:
    file.write("The winner of this round was: " + winner)
