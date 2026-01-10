# Sum of Natural Numbers:

i = int(input("Enter the amount of sums you want: "))

sum = 0
n = 1

while n <= i:
    sum = sum + n
    n = n + 1
    print("Sum is: ", sum)