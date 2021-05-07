class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

ayush = Employee()
ayush.salary = 1000000
ayush.getSalary() #---> automatically convert into below code the self (function)
# Employee.getSalary(ayush)