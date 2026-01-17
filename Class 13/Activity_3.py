# Diamond Shape:


print("Diamond Shape using (Numbers): ")
n = int(input("Enter the number of rows: "))

if n%2==0:
    half_dia_row = (n//2)
else:
    half_dia_row = (n//2) + 1

space = half_dia_row - 1

for i in range(1, half_dia_row + 1):
    for j in range(1, space + 1):
        print(end=" ")
    space = space - 1
    number = 1
    for j in range(2*i-1):
        print(end = str(number))
        number = number + 1
    print()

space = 1

for i in range(1, half_dia_row):
    for j in range(1, space + 1):
        print(end=" ")
    space = space + 1
    number = 1
    for j in range(1, 2*(half_dia_row-i)):
        print(end= str(number))
        number = number + 1
    print()