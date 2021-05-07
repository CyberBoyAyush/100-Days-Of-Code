class Employee:
    company = "Google"
    salary = 10000
ayush = Employee()    
rahni = Employee()
ayush.salary = 400000
rahni.salary = 30000
print(ayush.company)
print(rahni.company)

Employee.company = "Amazon"
print(ayush.company)
print(rahni.company)

print(ayush.salary)
print(rahni.salary)