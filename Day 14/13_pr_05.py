class Train:
    def __init__(self, name , fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print('************************')
        print(f"The Name Of Train is {self.name}")
        print(f"The Seats In Train is:{self.seats}")
    def fareInfo(self):
        print('************************')
        print(f"The Fare Of Train is {self.fare}")
    def bookTicket(self):
        if (self.seats>0):
            print(f"Your Seat is Booked!! Your Seat Number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry This train is full kindly try in Tatkal")    
    def cancelTicket(self):
        pass

intercity = Train("Intercity Express : 12012019", 90, 2)   
intercity.fareInfo()
intercity.bookTicket() #Booked First Ticket
intercity.bookTicket() #Booked Second Ticket
intercity.bookTicket() #Try To books Tickets Ticket
intercity.getStatus()