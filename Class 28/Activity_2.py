# Employee in and Out:

class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called, Employee deleted.")
def createobject():
    print("Making your object.")
    emp = Employee()
    print("Terminating the function.")
    return emp
print("Calling the function.")
emp = createobject()
print("Program is ending.")