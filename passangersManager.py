from passangers import Passangers

class PassangersManager:
    passangers=[]
    
    def list(self):
        for a in self.passangers:
            self.show(a)
    def show(self,a):
        print(a.PassangersNo," ",a.name)
    def create(self,PassangersNo,BookingNo,name,gender,address,email,PhoneNo):
        a=Passangers(PassangersNo,BookingNo,name,gender,address,email,PhoneNo)
        if a == None:
            print("Space limit exceeded Try another flight")
        else:
            a=Passangers(PassangersNo,BookingNo,name,gender,address,email,PhoneNo)
            self.passangers.append(a)
            return True
      
    def update(self,PassangersNo,BookingNo,name,gender,address,email,PhoneNo):
        a = self.find(PassangersNo)
        a.BookingNo=BookingNo
        a.name=name
        a.gender=gender
        a.address=address
        a.email=email
        a.PhoneNo=PhoneNo

    def delete(self,PassangersNo):
        a =self.find(PassangersNo)
        self.passangers.remove(a)
        
    def find(self,PassangersNo):
        for a in self.passangers:
            if a.PassangersNo==PassangersNo:
                return a
   
   



