from Aircraft import Aircraft
class AircraftManager:
    aircrafts = []
    file = open("Aircraft.txt","a+")

    def __init__(self):
        self.file.seek(0)
        for aircraft_line in self.file:
            self.aircrafts.append(Aircraft.parse(aircraft_line))

    def list(self):
        for a in self.aircrafts:
            self.show(a)

    def show(self,a):
        print(a.capacity," ",a.aircraftNo," ",a.types," ",a.name)

    def create(self,capacity,aircraftNo,types,name):
        a=Aircraft(capacity,aircraftNo,types,name)
        self.aircrafts.append(a)
        self.file.write(f"{str(a)}\n")
        self.file.flush()
    
    def update(self,capacity,aircraftNo,types,name):
        a = self.find(aircraftNo)
        a.capacity=capacity
        a.types=types
        a.name=name
        self.__refreshFile()

    def __refreshFile(self):
        self.file = open("Aircraft.txt", "w")
        for a in self.aircrafts:
            self.file.write(str(a))
            self.file.write("\n")
        self.file.flush()
        
        
    def delete(self,aircraftNo):
        a =self.find(aircraftNo)
        self.aircrafts.remove(a)
        self.__refreshFile()


    def find(self,aircraftNo):
        for a in self.aircrafts:
            if a.aircraftNo==aircraftNo:
                return a
        return None

