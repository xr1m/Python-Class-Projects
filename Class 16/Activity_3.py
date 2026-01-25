# Factorial Value:

def factorial(i):
    """This is a recursive function of a factorial integer."""
    if i == 0 or i == 1:
        return 1
    else:
        return i*factorial(i-1)

print(factorial.__doc__)
print("Factorial of 0:", factorial(0))
print("Factorial of 1:", factorial(1))
print("Factorial of 3:", factorial(3))