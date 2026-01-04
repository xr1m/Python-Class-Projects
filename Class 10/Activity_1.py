# Sum of whole numbers:

userinput = int(input("Enter whose whole number you want to find: "))

sum = 0
for i in range(1, userinput+1):
    sum = sum + i
    print(sum)