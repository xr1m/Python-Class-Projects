a = 3
b = 0.1

if type(a) is int:
    print("It is an integer.")
else:
    print("It is not an integer.")

if type(b) is not float:
    print("True.")
else:
    print("False")

if a is b:
    print("They have the same value.")
else:
    print("They do not have the same value.")