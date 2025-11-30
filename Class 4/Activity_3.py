# Calculating the percentage:

maths = int(input("Enter your marks in maths: "))
science = int(input("Enter your marks in science: "))
sst = int(input("Enter your marks in sst: "))
tech = int(input("Enter your marks in Tech: "))

marks = {maths,science,sst,tech}

percentage = (sum(marks)/400) * 100
print(percentage)