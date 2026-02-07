# Nested Loop:

x = False
while not x:
    try:
        i = int(input("Enter a number: "))
        while i%2==0:
            print("Bye Bye")
        x = True
    except ValueError:
        print("Invalid Input.")