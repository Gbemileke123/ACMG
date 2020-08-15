class Passangers:
    def __init__(self,PassangersNo,BookingNo,name,gender,address,email,PhoneNo):
        self.PassangersNo=PassangersNo
        self.BookingNo=BookingNo
        self.name=name
        self.gender=gender
        self.address=address
        self.email=email
        self.PhoneNo=PhoneNo

    def __str__(self):
        return f"{self.PassangersNo}\t{self.BookingNo}\t{self.name}\t{self.gender}\t{self.address}\t{self.email}\t{self.PhoneNo}"
    
    def parse(line: str):
        PassangersNo,BookingNo,name,gender,address,email,PhoneNo = line.split("\t")
        return Passangers(PassangersNo,BookingNo,name,gender,address,email,PhoneNo)
        



        