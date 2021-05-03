b = set()
print(type(b))

# Addding values to empty set
b.add(4)
b.add(5)
b.add(6)
b.add(5) #Adding a value repeatidly does not change a set
# Note : We Cannot add list or dict in sets

#Accessing Elements
print(b)

#Find Length
print(len(b))

#Removing Element
b.remove(5) #Removes 5 from set b
# b.remove(15) #Throws an error while removing 15
print(b)

print(b.pop())