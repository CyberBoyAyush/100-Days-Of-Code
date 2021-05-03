letter = '''Dear <|Name|>,
Greeting From ABC Coding House

You Are Selected!

Date: <|DATE|>
'''

name = input("Enter Your Name\n")
date = input("Enter Your Date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|DATE|>", name)
print(letter)