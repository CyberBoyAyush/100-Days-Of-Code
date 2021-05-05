with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/sample.txt') as f:
    content = f.read()

content = content.replace('Donkey',"*&*&*#")

with open('Practise/Chapter 9/sample.txt','w') as f:
    f.write(content)