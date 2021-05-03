text = input("Enter The Text: ")
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True   
elif("click this" in text):
    spam = True   
elif("subscribe this" in text):
    spam = True   
else:
    spam = False

if(spam):
    print("This Text Is spam")    
else:
    print("This is not spam")    
