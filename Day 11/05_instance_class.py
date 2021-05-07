class Employee:
    company = "Google"
    salary = 10000

ayush = Employee()    
rahni = Employee()

# Creating instance attribute salary for  of the objects
# ayush.salary = 400000
# rahni.salary = 30000

ayush.salary = 2222
print(ayush.salary)
print(rahni.salary)

# Below line will throws error as there is not attribute with address
# print(rahni.address)