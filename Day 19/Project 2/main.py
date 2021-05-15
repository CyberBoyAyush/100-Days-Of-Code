import random
randNumber = random.randint(1,100)
print(randNumber)
userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input('Enter Your Guess: '))
    guesses += 1
    if(userGuess==randNumber):
        print("You Guessed it right!!")

    else:
        if (userGuess>randNumber):
            print("You Guessed it wrong!!! Enter a smaller number")
        else:
            print("You Guessed it wrong!!! Enter a larger number")  
        guesses += 1

print(f"You Guesses The Number in {guesses} guesses.")        
with open('hiscore.txt', 'r') as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You Have Broken hiscore!!")    
    with open('hiscore.txt','w') as f:
        f.write(str(guesses))