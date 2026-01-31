# Continue:

user_input = int(input("Enter your integer: "))

while user_input > 0:
    user_input -= 1
    if user_input == 5:
        continue
    print(f"Current variable value is: {user_input}")