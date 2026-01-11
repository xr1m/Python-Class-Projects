# Is this a Prime Number within the range:


upper = int(input("Enter your ending number: "))
lower = int(input("Enter your starting number: "))

for i in range(lower,upper+1):
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
                print(f"{i} is a prime number.")