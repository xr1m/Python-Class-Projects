# Arrays:

import array as arr

array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 1])
print(f"Original array: {array_num}")

print("The occurance of number 3 in the array is: " + str(array_num.count(3)))
array_num.reverse()
print(f"The reverse order of the array is: {array_num}")