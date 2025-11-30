a = 1
b = 2
c = 3

print(b!=b)
print(b!=c)

a = "python"
b = "coding"

if a!=b:
    print(a, b, "Both the values are different.")

a = 4
b = 5

if (a == 1) != (b == 5):
    print("Both the values are different.")

a = int(input("Give an input of any number: "))
if a %2 != 0:
    print("Not an even number")
else:
    print("It is an even number.")