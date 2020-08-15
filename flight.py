class Flight:
    def __init__(self,flightno,aircraftNo,takeoffpoint,arrivalpoint,time,price):
        self.flightno=flightno
        self.aircraftNo=aircraftNo
        self.takeoffpoint=takeoffpoint
        self.arrivalpoint=arrivalpoint
        self.time=time
        self.price=price

    def __str__(self):
        return f"{self.flightno}\t{self.aircraftNo}\t{self.takeoffpoint}\t{self.arrivalpoint}\t{self.time}\t{self.price}"

    def parse(line: str):
        flightno,aircraftNo,takeoffpoint,arrivalpoint,time,price =line.split("\t")
        return Flight(flightno,aircraftNo,takeoffpoint,arrivalpoint,time,price)