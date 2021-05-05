with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/log.txt') as f:
    cont= f.read().lower() # reads full file as lower so that our program can detect it 

if 'python' in cont:
    print('yes python is present')
else:
    print('python is not present')