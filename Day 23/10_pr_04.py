l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 35, 45, 78, 98, 76, 65]

a = list(filter(lambda a: a % 5 == 0, l))
print(a)