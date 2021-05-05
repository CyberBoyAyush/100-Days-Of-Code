words = ['donkey','kaddu','mote']

with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/sample.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word,"*&*&*#")

with open('Practise/Chapter 9/sample.txt','w') as f:
    f.write(content)