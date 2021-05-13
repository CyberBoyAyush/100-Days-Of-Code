class Person:
    def __init__(self):
        print('Initializing Person \n')
    country = 'India'

    def takeBreath(self):
        print("I am breathing....")

class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print('Initializing Employee \n')

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am employee and luckily breathing...")

class Programmer(Employee):
    company = 'Fiverr'

    def __init__(self):
        super().__init__()
        print('Initializing Programmer \n')

    def getSalary(self):
        print("No Salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am employee and breathing++..")    

# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()