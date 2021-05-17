while(True):
    print('press q to quit')
    a = input('Enter a number: ')

    if a == 'q':
        break

    try:
        print('trying...')
        a = int(a)
        if a>6:
            print('You entered a number greater than 6')

    except Exception as e:
        print(f"You Input Resulted in error: {e}")

print("Thanks For Playing this Game!")