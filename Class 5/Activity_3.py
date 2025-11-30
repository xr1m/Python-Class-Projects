number1 = int(input("Enter the first number: "))

if number1 < 10:
    print(f"{number1} is smaller than 10")
    print("I'm an if block")

else:
    print(f"{number1} is greater than 10")
    print("I'm an else block")

print("\nI'm nor an if nor an else\n")