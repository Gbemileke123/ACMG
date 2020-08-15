from passangers import Passangers

class PassangersManager:
    passangers= []
    file = open("passangers.txt","a+")
    def __init__(self):
        self.file.seek(0)
        for Passangers_record in self.file:
            self.passangers.append(Passangers.parse(Passangers_record))

    def list(self):
        for a in self.passangers:
            self.show(a)

    def show(self,a):
        print(a.PassangersNo," ",a.BookingNo," ", a.name," ",a.gender," ",a.address," ",a.email," ",a.PhoneNo)

    def create(self,PassangersNo,BookingNo,name,gender,address,email,PhoneNo):
        a=Passangers(PassangersNo,BookingNo,name,gender,address,email,PhoneNo)
        self.passangers.append(a)
        self.file.write(f"{str(a)}\n")
        self.file.flush()
        return True

    def find(self,PassangersNo):
        for a in self.passangers:
            if a.PassangersNo==PassangersNo:
                return a
        return None
   
 
    def update(self,PassangersNo,BookingNo,name,gender,address,email,PhoneNo):
        a = self.find(PassangersNo)
        a.BookingNo=BookingNo
        a.name=name
        a.gender=gender
        a.address=address
        a.email=email
        a.PhoneNo=PhoneNo
        self.__refreshFile()

    def __refreshFile(self):
        self.file = open("passangers.txt", "w")
        for a in self.passangers:
            self.file.write(str(a))
            self.file.write("\n")
        self.file.flush()

    def delete(self,PassangersNo):
        a =self.find(PassangersNo)
        self.passangers.remove(a)
        self.__refreshFile()
    
   



