import random
#snake water gun or rock paper scissors
def gameWin(you, comp):
    #If two values are equal declare a tie
    if comp == you:
        return None

        #check for all possibilities when comp choose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True  

        #check for all possibilities when comp choose w     
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True  
        #check for all possibilities when comp choose g     
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True   
            

print("Comp Turn = Snake(1), Water(2), Gun(3)?")
randNo = random.randint(1 , 3)
print(randNo)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"   
elif randNo == 3:
    comp = "g"

you = input("Your's Turn = Snake(1), Water(2), Gun(3)?")
a = gameWin(comp, you)

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if a == None:
    print("The Game Is Tie!")
elif a:
    print("You Win!")
else:
    print("You Loose!")