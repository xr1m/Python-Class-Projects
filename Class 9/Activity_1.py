# Exam Eligibility Check:

med_leave = input("Enter 'yes' if you have given the medical leave: ")
attendance = int(input("Enter the percentage of this year's attendance: "))

if (med_leave.lower() == 'yes'):
    print("You are allowed for the exam.")
else:
    if attendance >= 75:
        print("You are allowed to enter for the exam.")
    else:
        print("You are not allowed to enter for the exam.")