# Pair of Elements:

class pairelements:
    def pairsum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i
userinput = int(input("Enter the target sum: "))
print("Index 1 = %d, Index 2 = %d" % pairelements().pairsum((10, 20, 30, 40, 50, 60, 70), userinput))