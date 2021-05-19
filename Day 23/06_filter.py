# filter syntax: list(filter(function,list))

def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

g10 = lambda num : num>10 # also can use lambda func
l = [1, 2, 3, 6, 78, 9, 99]
print(list(filter(greater_than_5, l)))