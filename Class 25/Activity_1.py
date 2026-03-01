# Hands-on Map:

num1 = [1, 2, 3]
num2 = [4, 5, 6]

result = map(lambda x, y: x + y, num1, num2)
print(f"The addition of the two lists is: {list(result)}")
result2 = num1 + num2
print(f"The result otherwise would be: {result2}")

def square(number):
    return number * number
square = list(map(square, result2))
print(f"The result of square of {result2} is: {square}")