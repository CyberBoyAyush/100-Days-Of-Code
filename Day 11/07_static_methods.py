class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod #Added Static Method
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("Time is 9 pm")    

ayush = Employee()
ayush.salary = 1000000
ayush.getSalary("Thanks")
ayush.greet() #Employee.greet()
ayush.time()