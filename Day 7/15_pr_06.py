# n! = 1 x 2 x 3  x ............. X n

num = int(input("Enter Your Number: "))
factorial = 1
for i in range (1 , num +1):
    factorial = factorial*i
print(f"Factorial of this {num}5 is {factorial}")