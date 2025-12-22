speed1 = 10
speed2 = 20
speed3 = 30
total = (speed1 , speed2 , speed3)

avg = sum(total) / len(total)
print(avg)

if avg > speed1 and avg > speed2 and avg > speed3:
    print("%d is higher than %d, %d, %d" % (avg, speed1, speed2, speed3))
elif avg > speed1 and speed2:
    print("%d is higher than %d, %d" % (avg, speed1, speed2))
elif avg > speed1 and speed3:
    print("%d is higher than %d, %d" % (avg, speed1, speed3))
elif avg > speed2 and speed3:
    print("%d is higher than %d, %d" % (avg, speed2, speed3))
elif avg > speed1:
    print("%d is higher than %d" % (avg, speed1))
elif avg > speed2:
    print("%d is higher than %d" % (avg, speed2))
elif avg > speed3:
    print("%d is higher than %d" % (avg, speed3))
else:
    print("Invalid Input.")