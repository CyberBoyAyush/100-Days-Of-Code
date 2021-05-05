# readline func is used to read one single line in a program
f = open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/sample.txt')
#reads first line
data = f.readline() 
print(data)

#reads second line
data = f.readline() 
print(data)

#read third line
data = f.readline() 
print(data)

#read fourth line
data = f.readline() 
print(data)
f.close()