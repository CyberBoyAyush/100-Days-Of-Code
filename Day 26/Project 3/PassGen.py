import string
import random

data1 = string.ascii_lowercase
data2 = string.ascii_uppercase
data3 = string.digits
data4 = string.punctuation

try:
    passwd = int(input("Enter Length Of Your Passsword: "))
    pwd = []
    pwd.extend(list(data1))
    pwd.extend(list(data2))
    pwd.extend(list(data3))
    pwd.extend(list(data4))
    random.shuffle(pwd)

    ps = "".join(random.sample(pwd, passwd))

    print("***Your Password Is***\n")
    print(ps, '\n')

except:
    print("Please Enter Integer In Lenth Of Your Password!!")

sv = f'''
==== Thanks For Using This Password Generator ====
"Your Generated Pass Of Length {passwd} is :" {ps} + \n
'''


with open('pass.txt', 'a') as f:
    f.write(sv)

print(pwd)