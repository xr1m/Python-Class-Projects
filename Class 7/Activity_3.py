maths = int(input("Enter your marks in maths: "))
eng = int(input("Enter your marks in english: "))
sst = int(input("Enter your marks in sst: "))
it = int(input("Enter your marks in I.T: "))

total = (maths + eng + sst + it)

avg = total/4
print(f"Total is {total} and Average is {avg}")

if avg >= 91 and avg <= 100:
    print("Your grade is: A+")
elif avg >= 81 and avg <= 91:
    print("Your grade is: A")
elif avg >= 71 and avg <= 81:
    print("Your grade is: B+")
elif avg >= 61 and avg <= 71:
    print("Your grade is: B")
else:
    print("Your grade is: C")