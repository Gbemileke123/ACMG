from booking import Booking

class BookingManager:
    booking = []
    file = open("booking.txt","a+")
    def __init__(self,flightmg,passangermg):
        self.file.seek(0)
        for Booking_record in self.file:
            self.booking.append(Booking.parse(Booking_record))
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
            return False
        
        b = Booking(BookingNo,Name,DeparturePoint,ArrivalPoint,Period,Classes)
        self.booking.append(b)
        self.file.write(f"{str(b)}\n")
        self.file.flush()
        return True
    
    def find(self,BookingNo):
        for b in self.booking:
            if b.BookingNo==BookingNo:
                return b

    def update(self,BookingNo,flightNo,Name,DeparturePoint,ArrivalPoint,Period,Classes):
        b = self.find(BookingNo)
        b.Name=Name
        b.DeparturePoint=DeparturePoint
        b.ArrivalPoint=ArrivalPoint
        b.Period=Period
        b.Classes=Classes
        self.__refreshFile()

    def __refreshFile(self):
        self.file = open("booking.txt", "w")
        for b in self.booking:
            self.file.write(str(b))
            self.file.write("\n")
        self.file.flush()

    def delete(self,BookingNo):
        b=self.find(BookingNo)
        self.booking.remove(b)
        self.__refreshFile()
        
    