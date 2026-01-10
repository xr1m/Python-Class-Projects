# Armstrong Value:

# To find the sum of the cube of each digit: 1^3 + 5^3 + 3^3 = 153

userinput = int(input("Enter a number to check if its an armstrong number: "))

sum = 0

# Temp variable for storing the number:

temp = userinput

while temp > 0:
    digit = temp%10
    sum += digit**3
    temp //= 10
if userinput == sum:
    print("User Input is an Armstrong Number.")
else:
    print("User Input is not an Armstrong Number.")