print("Enter a number for a numerator: ")
numerator = int(input())

print("Enter a number for denominator: ")
denominator = int(input())

if numerator % denominator == 0:
    print(f"{numerator} is divisible by {denominator}")
else:
    print(f"{numerator} is not divisible by {denominator}")