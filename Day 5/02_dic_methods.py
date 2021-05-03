mydict = {
    "fast" : "In A Quick Manner",
    "ayush" : "Coder",
    "marks" : [1,4,5],
    "a_dict" : {'ayush' : 'Player'},
    1: 2
}

print(mydict.keys()) #--->print keys of the dictionary
print(mydict.values()) #--->print values of the dictionary
print(mydict.items()) #--->print (keys,items) of the dictionary

print(mydict)
updatedict = {
    'love' : 'you'
}
mydict.update(updatedict) #Update the dictionary by adding key-values pairs from updatedict
print(mydict)

print(mydict.get('ayush')) #Prints value associated with ayush
print(mydict['ayush']) #Prints value associated with ayush

#Difference btw .get and [synax]
print(mydict.get('ayush2')) #Returns none as ayush2 is not present in dictionary
print(mydict['ayush2']) #throws error as ayush2 is not in dict