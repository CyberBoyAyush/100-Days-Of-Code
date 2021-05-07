class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print('Employee is created')

    def getDetails(self):
        print(f"The name of employes is {self.name}") 
        print(f"The name of employes is {self.salary}") 
        print(f"The name of employes is {self.subunit}") 

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod #Added Static Method
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("Time is 9 pm")

ayush = Employee("Ayush", 100 ,"Youtube")
# ayush = Employee() #throws error misiing 3 requiorements argimuments
ayush.getDetails()
rahul = Employee("Rahul", 20, "Canon")
rahul.getDetails()