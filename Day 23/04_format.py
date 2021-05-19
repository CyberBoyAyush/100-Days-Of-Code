name = 'Ayush'
channel = "Google"
# a = f"This is {name}" --->f string
# a = 'this is {}'.format(name) ---> format
# a = 'This is {} and his channel is {}'.format(name,channel) ---> format multiple
a = 'This is {1} and his channel is {0}'.format(name,channel) 
print(a)