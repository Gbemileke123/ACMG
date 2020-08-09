from flight import Flight

class FlightManager:
    flight = []
    def __init__(self,aircraftmg):
        self.aircraftmg=aircraftmg
    
    def list(self):
        for f in self.flight: 
            self.show(f)
    def show(self,f):
        print(f.flightno," ",f.aircraft)
    def create(self,flightno,aircraftNo,takeoffpoint,arrivalpoint,time,price):
        aircraft = self.aircraftmg.find(aircraftNo)
        if aircraft == None:
            print("Not Available") 
        else:
            f=Flight(flightno,aircraftNo,takeoffpoint,arrivalpoint,time,price)
            self.flight.append(f)
            return True

    def update(self,flightno,aircraftNo,takeoffpoint,arrivalpoint,time,price):
        f = self.find(flightno)
        f.aircraftNo = aircraftNo
        f.takeoffpoint=takeoffpoint
        f.arrivalpoint=arrivalpoint
        f.time=time
        f.price=price
    def delete(self,flightno):
        f=self.find(flightno)
        if f :
            self.flight.remove(f)
        else:
            print("Flight ",flightno, " not found")
        
    def find(self,flightno):
        for f in self.flight:
            if f.flightno==flightno:
                return f
            return None
            
            
   







