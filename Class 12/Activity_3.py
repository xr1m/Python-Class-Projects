# Middle product:

num = int(input("Enter your number: "))

t = num
numlen = 0

while t > 0:
    numlen = numlen + 1
    t = int(t/10)
if numlen >= 4:
    numlen = int(numlen/2)
    check = 0
    while num > 0:
        remainder = num%10
        if check == numlen:
            midone = remainder
        elif check == numlen - 1:
            middletwo = remainder
        num = int(num/10)
        check = check + 1
    product = midone * middletwo
    print(f"Product of middle digits is {midone} * {middletwo}: {product}")
else:
    print(f"It should be more or equal to 4 digits. Current digit: {num}")