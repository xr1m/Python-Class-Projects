# Value Error: 

try:
    x = int(input("Enter any integer: "))
    print(x)
except ValueError as ex:
    print("There is an error.", ex)