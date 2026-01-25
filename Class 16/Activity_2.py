# Find the cube of cube:

def cube(n):
    return n*n*n

def is_divisible(n):
    if n%3 == 0:
        return cube(n)
    else:
        return False

print(is_divisible(9))
print(is_divisible(5))