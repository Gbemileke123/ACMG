from Aircraft import Aircraft
class AircraftManager:
    aircrafts = []
    def list(self):
        for a in self.aircrafts:
            self.show(a)
    def show(self,a):
        print(a.capacity," ",a.aircraftNo)
    def create(self,capacity,aircraftNo,types,name):
        a=Aircraft(capacity,aircraftNo,types,name)
        self.aircrafts.append(a)
    def update(self,capacity,aircraftNo,types,name):
        a = self.find(aircraftNo)
        a.capacity=capacity
        a.types=types
        a.name=name
       
    def delete(self,aircraftNo):
        a =self.find(aircraftNo)
        self.aircrafts.remove(a)
        
    def find(self,aircraftNo):
        for a in self.aircrafts:
            if a.aircraftNo==aircraftNo:
                return a
            


   

