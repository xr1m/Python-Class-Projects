# Mathematical Operation:

import math

print("Floor and Ceiling")
userinput = float(input("Enter a decimal value: "))

result = str(math.ceil(userinput))
result_floor = str(math.floor(userinput))
print(result, result_floor)

# Copying the sign:

x = 10
y = -15
print(f"The value of {x} after copying the sign from {y} is: ", str(math.copysign(x,y)))

# Absolute value:

print("Absolute value of -96 and 56 are: ", str(math.fabs(-96)), str(math.fabs(56)))

# Greatest Comma Divisor:

print("The GCD of 24 and 56 is:", str(math.gcd(24, 56)))