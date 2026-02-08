# Rock, Paper, Scissors:


import random

while True:
    userinput = input("Enter a choice in Rock, Paper, or Scissors: ")
    possibleaction = ["Rock", "Paper", "Scissors"]
    computeraction = random.choice(possibleaction)
    print(f"Your option: {userinput}, The Computer's choice: {computeraction}")
    if userinput == computeraction:
        print(f"Both players selected the same option, It's a Tie! Both player's choice: {userinput}")
    elif userinput == "Rock":
        if computeraction == "Scissors":
            print("You win!")
        else:
            print("You lose. Try again")
    elif userinput == "Paper":
        if computeraction == "Rock":
            print("You win!")
        else:
            print("You lose. Try again")
    elif userinput == "Scissors":
        if computeraction == "Paper":
            print("You win!")
        else:
            print("You lose. Try again")
    playagain = input("Do you want to play again? Y/N: ")
    if playagain != "Y":
        print("Bye Bye.")
        break