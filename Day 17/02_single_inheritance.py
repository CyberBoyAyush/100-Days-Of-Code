# Single Inheritance

class Employee:
    company = 'Google'

    def showDeatils(self):
        print("This is an employee")

class Programmer(Employee):
    language = 'Python'
    company = 'Youtube'
    def getLanguage(self):
        print(f"The Language is {self.name}") 

    def showDeatils(self):
        print("This is an programmer")         

e = Employee()
p = Programmer()
e.showDeatils()
p.showDeatils()
print(p.company)