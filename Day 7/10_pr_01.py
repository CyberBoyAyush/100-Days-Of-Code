num = int(input("Enter Your Number: "))
for i in range(1,11):
    print(str(num) + "x" + str(i) + "=" + str(i*num))
    # print(num , "x" , i , "=" , i*num) --->Way 2
    # print(f"{num}X{i}={num*i}") --> Way 3