# Number Game:

import random

playing = True
number = str(random.randint(1, 10))
print("I'll generate a number from 1 to 10, and you have to guess the number one digit at a time.")

while playing:
    userinput = input("Give your best guess: ")
    if number == userinput:
        print(f"You win the game! The number is {number}. Your guess: {userinput}")
        break
    else:
        print(f"Your guess isn't right, Try again. The number generated was: {number}")