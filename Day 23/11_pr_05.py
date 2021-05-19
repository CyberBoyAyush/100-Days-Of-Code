from functools import reduce
l = [3, 54, 6, 7, 8, 3, 32, 99]

# print(max(l))

a = reduce(max, l)
print(a)