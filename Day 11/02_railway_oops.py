class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f'Name is {self.name}')
        print(f'Train is {self.train}')

ayushApplication = RailwayForm()
ayushApplication.name = "Ayush Sharma"
ayushApplication.train = "Rajdhani Express"
ayushApplication.printData()