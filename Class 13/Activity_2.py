# Floyd’s triangle:

print("Floyd's Triangle (*): ")
n = int(input("Enter the number of rows: "))

no = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(no, end=" ")
        no = no + 1
    print()