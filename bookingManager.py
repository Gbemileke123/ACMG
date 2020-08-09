from booking import Booking

class BookingManager:
    booking = []
    def __init__(self,flightmg,passangermg):
        self.flightmg=flightmg
        self.passangermg=passangermg
    def list(self):
        for b in self.booking:
            self.show(b)
    def show(self,b):
        print(b.BookingNo," ",b.Name)
    def create(self,BookingNo,flightNo,Name,DeparturePoint,ArrivalPoint,Period,Classes):
        flight = self.flightmg.find(flightNo)
        if flight == None:
            print("Not Available") 
        else:
            b = Booking(BookingNo,Name,DeparturePoint,ArrivalPoint,Period,Classes)
            self.booking.append(b)
            return True
    def update(self,BookingNo,flightNo,Name,DeparturePoint,ArrivalPoint,Period,Classes):
        b = self.find(BookingNo)
        b.Name=Name
        b.DeparturePoint=DeparturePoint
        b.ArrivalPoint=ArrivalPoint
        b.Period=Period
        b.Classes=Classes
    def delete(self,BookingNo):
        b=self.find(BookingNo)
        self.booking.remove(b)
        
    def find(self,BookingNo):
        for b in self.booking:
            if b.BookingNo==BookingNo:
                return b




