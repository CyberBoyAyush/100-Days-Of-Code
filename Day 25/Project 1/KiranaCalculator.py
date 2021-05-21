'''
This is a basic application whih can be used in stores to calculate and generate bill. This application will keep store the numbers user has put and will add them until the user presses "q" on their keyboard. Then the application will print the result as a bill. 
'''
sum = 0
name = input("Enter Name Of Buyer: ")
mobileNo = input("Enter Buyer Number: ")
paymode = input("Enter Payment Mode (Gpay,Cash,Card): ")

while(True):
    try:
        a = input("Enter The Price Of Product or press q: ")
        if (a != 'q'):
            sum = sum + int(a)
            print(f"The Order Total Till Now Us {sum}")

        else:
            print("****Program Exited!! Thanks For Using Kirana Calculator****")
            print(f"The Order Total is {sum}")
            break
    except:
        print("Please Enter Int Value!!")

content = f'''
****Thanks For Using kirana Calculator****
\nThe Bill Of {name} is {sum}. Contact {mobileNo}, Payment Mode = {paymode}
'''

with open('bills.txt', 'a') as f:
    f.write(content)
