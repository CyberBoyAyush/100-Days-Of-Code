num = int(input("Enter Your Number: "))

factorial = 0
i = 1
while i <= num:
    factorial = factorial*i
    i = i +1
print(f"Factorial of {num} is {factorial}")