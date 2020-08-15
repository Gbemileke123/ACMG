class Booking:
    def __init__(self,BookingNo,Name,DeparturePoint,ArrivalPoint,Period,Classes):
        self.BookingNo=BookingNo
        self.Name = Name
        self.DeparturePoint = DeparturePoint
        self.ArrivalPoint = ArrivalPoint
        self.Period = Period
        self.Classes = Classes

    def __str__(self):
        return f"{self.BookingNo}\t{self.Name}\t{self.DeparturePoint}\t{self.ArrivalPoint}\t{self.Period}\t{self.Classes}"

    def parse(line: str):
        BookingNo,Name,DeparturePoint,ArrivalPoint,Period,Classes = line.split("\t")
        return Booking(BookingNo,Name,DeparturePoint,ArrivalPoint,Period,Classes)

