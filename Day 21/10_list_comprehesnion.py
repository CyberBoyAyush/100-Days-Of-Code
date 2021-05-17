a = [3, 5,6,7,9,123,31,233,88,76,56]
# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)

# print(b)

# Shortcut to write the same as above code
b = [i for i in a if i%2==0]
print(b)

t = [1, 4, 5, 8, 0, 2, 2]
s = {i for i in t}
print(s)