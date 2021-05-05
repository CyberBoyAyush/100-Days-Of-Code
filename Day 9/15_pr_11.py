import os

oldname = '/home/cyberboyayush/Documents/Python/Practise/Chapter 9/test.txt'
newname = 'renamed_by_python.txt'
with open(oldname) as f:
    cont = f.read()

with open(newname, 'w') as f:
    f.write(cont)

os.remove(oldname)