# Right angle triangle: 

print("Right Angled Triange using (*): ")
n = int(input("Enter the amount of rows you want: "))

for i in range(n):
    for a in range(i+1):
        print("*", end=" ")
    print()