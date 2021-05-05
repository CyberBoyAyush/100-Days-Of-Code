s = int(input("Enter Score: "))

def game():
    return s

score = game()
with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/highscore.txt') as f:
    high = f.read()

if high == '':
    with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/highscore.txt', 'w') as f:    
        f.write(str(score))

elif int(high)<score:
    with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/highscore.txt', 'w') as f:    
        f.write(str(score))
else:
    pass