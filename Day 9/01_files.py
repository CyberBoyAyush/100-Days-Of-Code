# use open function to read content of a file!
# f = open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/sample.txt', 'r')
f = open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/sample.txt') # by default in r mode if no mode is specified
# data = f.read() # read full file
data = f.read(5) #read only file letters in file
print(data)
f.close()