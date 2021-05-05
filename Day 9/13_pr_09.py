file1 = '/home/cyberboyayush/Documents/Python/Practise/Chapter 9/copy.txt'
file2 = '/home/cyberboyayush/Documents/Python/Practise/Chapter 9/this.txt'

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1==f2:
    print("Files are identical")    
else:
    print('files are not identical')    

