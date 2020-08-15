from flight import Flight

class FlightManager:
    flight = []
    file = open("flight.txt","a+")
    def __init__(self,aircraftmg):
        self.file.seek(0)
        for Flight_hist in self.file:
            self.flight.append(Flight.parse(Flight_hist))
        self.aircraftmg=aircraftmg

    def list(self):
        for f in self.flight: 
            self.show(f)
    def show(self,f):
        print(f.flightno," ",f.aircraftNo)
    def create(self,flightno,aircraftNo,takeoffpoint,arrivalpoint,time,price):
        aircraft = self.aircraftmg.find(aircraftNo)
        if aircraft == None:
            print("Not Available")
            return False
    
        f=Flight(flightno,aircraft.aircraftNo,takeoffpoint,arrivalpoint,time,price)
        self.flight.append(f)
        self.file.write(f"{str(f)}\n")
        self.file.flush()
        return True

    def update(self,flightno,aircraftNo,takeoffpoint,arrivalpoint,time,price):
        f = self.find(flightno)
        f.aircraftNo = aircraftNo
        f.takeoffpoint=takeoffpoint
        f.arrivalpoint=arrivalpoint
        f.time=time
        f.price=price
        self.__refreshFile()

    def __refreshFile(self):
        self.file = open("flight.txt", "w")
        for f in self.flight:
            self.file.write(str(f))
            self.file.write("\n")
        self.file.flush()

    def delete(self,flightno):
        f = self.find(flightno)
        if f :
            self.flight.remove(f)
            self.__refreshFile()
        else:
            print("Flight ",flightno, " not found")
        
    def find(self,flightno):
        for f in self.flight:
            if f.flightno==flightno:
                return f
            return None