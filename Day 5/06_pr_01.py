mydict = {
    "Pankha" : "Fan",
    'Dabba' : "Box",
    'Vasthu' : 'Samaan'
}
print("Options Are", mydict.keys())
a = input("Enter The Hindi Word\n")
# print('The Meaning Of Word Is ', mydict[a])

#Below line will not throw an error if key is not present
print('The Meaning Of Word Is ', mydict.get(a))