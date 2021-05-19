name = input("Enter your Name:\n")
marks = int(input("Enter your marks:\n"))
phone = input("Enter your phone:\n")

template = "The name of student is {}, his marks are {} and phone number is {}"
output = template.format(name,marks,phone)
print(output)