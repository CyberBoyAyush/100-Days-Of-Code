class Person:
    country = 'India'

    def takeBreath(self):
        print("I am breathing....")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am employee and luckily breathing...")

class Programmer(Employee):
    company = 'Fiverr'

    def getSalary(self):
        print("No Salary to programmers")

    def takeBreath(self):
        print("I am employee and breathing++..")    

p = Person()
p.takeBreath()
# print(p.company) # Throws error

e = Employee()
print(e.company)
e.takeBreath()

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)