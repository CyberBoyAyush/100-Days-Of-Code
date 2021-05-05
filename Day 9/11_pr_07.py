cont = True
i = 1
with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/log.txt') as f:
    while cont:
        i+=1
        cont= f.readline().lower() # reads full file as lower so that our program can detect it 
        print(cont)

        if 'python' in cont:
            print(cont)
            print('Yes Python is present')
            print(i)
        i+=1