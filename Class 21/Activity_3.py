# Play with Lists:

list1 = [2, 3, 5, 7, 9, 1]
count = 0
for i in list1:
    count += i
avg = count/len(list1)
print(f"The sum of the list: {count} and the average is: {avg}")

list1.sort()
print(f"The largest element in the list is: {list1[-1]}")
print(f"The smallest element in the list is: {list1[0]}")

# Remove specific elements (ADDON):

list1.remove(3)
print(f"After removing specific elements: {list1}")

# Pop: (which should pop the last element)

list1.pop(2)
print(list1)