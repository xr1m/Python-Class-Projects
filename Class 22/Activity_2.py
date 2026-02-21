# Flip-Flop (palendrome):


def palendrome(i):
    x = len(i)-1
    j = 0
    while j < x:
        if (i[j]!=i[x]):
            return False
        x = x-1
        j = j+1
    return True

i = (1, 2, 3, 3, 2, 1)
if palendrome(i):
    print("Tuple is a Palendrome.")
else:
    print("Tuple is not a Palendrome.")