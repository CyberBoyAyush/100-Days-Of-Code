try:
    i = int(input('Enter a num: '))
    c = 1/i

except Exception as e:
    print(e)

finally:
    print("We were done!!!!")

print("Thanks for using the program.")