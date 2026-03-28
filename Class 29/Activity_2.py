# Employee inheritance:

# Parent Class:

class Employer(object):
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no
    def display(self):
        print(self.name, self.id_no)

# Child Class:

class Employee(Employer):
    def __init__(self, name, id_no, salary, course):
        self.salary = salary
        self.course = course
        Employer.__init__(self, name, id_no)

ob = Employee("Rahul,", 50, 35000, "Intern")
ob.display()