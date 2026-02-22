# Check the frequency:


my_dict = {"codingal": 2, "is": 3, "best": 2, "for": 4, "coding": 2}

print(f"The original dictionary is: {my_dict}")

k = 2
result = 0

for key in my_dict:
    if my_dict[key] == k:
        # result += 1
        result = result + 1
print(f"The frequency of {k} is: {result}")