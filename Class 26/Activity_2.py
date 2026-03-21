# Guess the Number Game

import random
import time

# Pick a number between 1 and 100


name = ""

def intro():
    global name
    print("May I ask you for your name?")
    name = input().strip()  # .strip() to remove any accidental spaces
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 100")

    # Tell if the number is even or odd
    if number % 2 == 0:
        x = 'even'
    else:
        x = 'odd'
    
    print(f"\nThis is an {x} number.")
    time.sleep(0.5)
    print("Go ahead. Guess!")


def pick():
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(0.25)
        enter = input("Guess: ").strip()

        try:
            guess = int(enter)

            if 1 <= guess <= 100:
                guessesTaken += 1

                if guess == number:
                    print(f"Good job, {name}! You guessed my number in {guessesTaken} guesses!")
                    return  # exit the function after correct guess

                # still have guesses left
                if guessesTaken < 6:
                    if guess < number:
                        print("The number you entered is too low.")
                    else:
                        print("The number you entered is too high.")
                    print("Try Again!")
                    time.sleep(0.5)

            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 100.")

        except ValueError:
            print(f"I don't think '{enter}' is a number. Sorry.")
            # We don't count invalid inputs as guesses

    # If we reach here → ran out of guesses
    print(f"Nope. The number I was thinking of was {number}.")


# Main game loop
playagain = "yes"

while playagain.lower() in ["yes", "y"]:
    number = random.randint(1, 100)
    intro()
    pick()

    print("\nDo you want to play again? (yes/no)")
    playagain = input().strip().lower()

print("Thanks for playing! Goodbye.")