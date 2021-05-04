# n! = 1 * 2 * 3  * 4...*n

# n! = [1 * 2 * 3  * 4...n-1]*n

#n! = (n-1)! *n

# n = int(input("Enter Number For Factor: ")) -->Take Input from user
# n = 2
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)    

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1 
    return n * factorial_iter(n-1)       

# print(factorial_iter(4))
print(factorial_recursive(5))
