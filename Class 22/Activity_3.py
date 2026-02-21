# Weather Prediction:

weathertuple = (1, 0, 0, 0, 1, 1, 0)

sunny = 0
rainy = 0

for i in weathertuple:
    if weathertuple[i]==0:
        rainy += 1
    else:
        sunny += 1
if sunny > rainy:
    print("Good weather condition.")
else:
    print("Bad weather condition.")