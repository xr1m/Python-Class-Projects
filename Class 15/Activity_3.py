# Simple Calculator:

def add(A, B):
    return A + B
def subtract(A, B):
    return A - B
def multiplication(A, B):
    return A * B
def division(A, B):
    return A / B

print("What operation do you want to use: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Choose your option [1/2/3/4]: "))

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if choice == 1:
    print(f"Addition of {num1} + {num2}:", add(num1, num2))
elif choice == 2:
    print(f"Subtraction of {num1} - {num2}:", subtract(num1, num2))
elif choice == 3:
    print(f"Product of {num1} * {num2}:", multiplication(num1, num2))
elif choice == 4:
    print(f"Division of {num1} / {num2}:", division(num1, num2))
else:
    print("Invalid Input/Operator.")