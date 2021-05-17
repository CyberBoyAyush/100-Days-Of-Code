try:
    a = int(input('Enter a number: '))
    c = 1/a
    print(c)

except ValueError as e:
    print('Enter a valid value: ')
    print(e)

except ZeroDivisionError as e:
    print('Exception2 Occured')
    print(e)

print("Thanks For using this code!")