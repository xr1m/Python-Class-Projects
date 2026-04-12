# Fruit Quiz:

import random

class fruit:
    def __init__(self):
        self.fruits = {"apple": "red", "banana": "yellow", "orange": "orange", "watermelon": "green"}
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit))
            userinput = input()
            if userinput.lower() == color:
                print("Correct Answer")
            else:
                print("Wrong Answer")
            option = int(input("Enter 0 if you want to add again otherwise enter 1: "))
            if option:
                break

print("Fruit Quiz:")
obj1 = fruit()
obj1.quiz()