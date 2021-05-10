class Programmer:
    company = 'Microsoft'

    def __init__(self, name , product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f'the name of {self.company} programmer is {self.name} and product is {self.product}')

ayush = Programmer('Ayush', 'Skype')  
anuj = Programmer('Anuj','github')
ayush.getInfo()
anuj.getInfo()