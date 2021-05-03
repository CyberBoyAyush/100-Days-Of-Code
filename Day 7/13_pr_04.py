num = int(input("Enter Your Number: "))
prime = True
for i in range(2, num):
    if(num%1 == 0):
        prime = False
        break
if prime:
    print("Number Is Prime")
else:
    print("Number Is Not Prime")     