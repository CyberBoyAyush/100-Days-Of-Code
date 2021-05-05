with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/this.txt') as f:
    cont = f.read()

with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/copy.txt','w') as f:
    f.write(cont)