from aircraftmanager import AircraftManager
from flightManager import FlightManager
from bookingManager import BookingManager
from passangersManager import PassangersManager
aircraftManager = AircraftManager()
flightManager = FlightManager(aircraftManager)
passangersManager = PassangersManager()
BookingManager =BookingManager(flightManager,PassangersManager)
def mainMenu():
    print("Enter 0 to exit")
    print("Enter 1 to Manage Aircrafts")
    print("Enter 2 to Manage Flights")
    print("Enter 3 to Manage Bookings")
    print("Enter 4 to Manage Passangers")
def showSubMenu(option):
    if option == "1":
        showManageAircraftsMenu()
        subOption=input()
        if subOption == "0":
            mainMenu()
        else:
            handleManageAircraftsAction(subOption)
            
    elif option == "2":
        showManageFlightMenu()
        subOption=input()
        if subOption == "0":
            mainMenu()
        else:
            handleManageFlightMenuAction(subOption)
    elif option == "3":
        showManageBookingMenu()
        subOption=input()
        if subOption == "0":
            mainMenu()
        else:
            handleManageBookingMenuAction(subOption)
    elif option == "4":
        showManagePassangersMenu()
        subOption=input()
        if subOption == "0":
            mainMenu()
        else:
            handleManagePassangersAction(subOption)


    
def handleManageAircraftsAction(action):
    if action == "1":
        aircraftManager.list()
    elif action == "2":
        capacity = input("Enter capacity: ")
        aircraftNo = input("Enter aircraftno")
        types = input("Enter types")
        name = input("Enter name")
        aircraftManager.create(capacity,aircraftNo,types,name)
        print("Congrats! Your AircraftNo ",aircraftNo," is created successfully")
    elif action == "3":
        capacity = input("Enter Aircraft capacity: ")
        aircraftNo = input("Enter Aircraft No")
        types = input("Enter Aircraft types")
        name = input("Enter Aircraft name")
        aircraftManager.update(capacity,aircraftNo,types,name)
        print("Update Successful! ")  
    elif action == "4":
        aircraftno = input("Enter aircraftno?")
        aircraftManager.delete(aircraftno)
        print(aircraftno,"deleted")
    showSubMenu("1") 
           

def showManageFlightMenu():
    print("Enter 0 to return to MainMenu")
    print("Enter 1 to List flights")
    print("Enter 2 to Create flight")
    print("Enter 3 to Update flight")
    print("Enter 4 to Delete flight")


def handleManageFlightMenuAction(action):
    if action == "1":
        flightManager.list()
    elif action == "2":
        flightno =input("Enter Flight No: ")
        aircraftNo =input("Enter aircraftno: ")
        takeoffpoint = input("Enter takepoint: ")
        arrivalpoint = input("Enter your Arrivalpoint: ")
        time = input("Enter Time: ")
        price = input("Enter Price: ")
        response =flightManager.create(flightno,aircraftNo,takeoffpoint,arrivalpoint,time,price)
        if response :
            print("Congrats! Your Flight ",flightno," is created successfully")
        else:
            print("Aircraft ", aircraftNo, " not available")
    elif action == "3":
        flightno =input("Enter Flight No: ")
        aircraftNo =input("Enter aircraftno: ")
        takeoffpoint = input("Enter takepoint: ")
        arrivalpoint = input("Enter your Arrivalpoint: ")
        time = input("Enter Time: ")
        price = input("Enter Price: ")
        flightManager.update(flightno,aircraftNo,takeoffpoint,arrivalpoint,time,price)
        print("Update Successful! ")
    elif action =="4":
        flightno =input("Enter Flight Number: ")
        flightManager.delete(flightno)   
    showSubMenu("2")

def showManageBookingMenu():
    print("Enter 0 to return to MainMenu")
    print("Enter 1 to List booking")
    print("Enter 2 to Create booking")
    print("Enter 3 to Update booking")
    print("Enter 4 to Delete booking")

def handleManageBookingMenuAction(action):
    if action == "1":
        flightManager.list()
    elif action == "2":
        BookingNo =input("Enter BookingNo: ")
        flightno =input("Enter flightno: ")
        Name = input("Enter your Name: ")
        DeparturePoint = input("Enter Departurepoint: ")
        ArrivalPoint = input("Enter your Arrivalpoint: ")
        Period = input("Enter Period: ")
        Classes = input("Enter Classes: ")
        response =BookingManager.create(BookingNo,flightno,Name,DeparturePoint,ArrivalPoint,Period,Classes)
        if response :
            print("Congrats! Your BookingNo ",BookingNo," is created successfully")
        else:
            print("FLight ", flightno, " not available")
    elif action == "3":
        BookingNo =input("Enter BookingNo: ")
        flightno =input("Enter flightno: ")
        Name = input("Enter your Name: ")
        DeparturePoint = input("Enter Departurepoint: ")
        ArrivalPoint = input("Enter your Arrivalpoint: ")
        Period = input("Enter Period: ")
        Classes = input("Enter Classes: ")
        BookingManager.update(BookingNo,flightno,Name,DeparturePoint,ArrivalPoint,Period,Classes)
        print("Update Successful! ")
    elif action == "4":
        BookingNo =input("Enter Booking Number? ")
        BookingManager.delete(BookingNo)
    showSubMenu("3")

def showManagePassangersMenu():
    print("Enter 0 to return to MainMenu")
    print("Enter 1 to List passangers")
    print("Enter 2 to Create passangers")
    print("Enter 3 to Update Passangers")
    print("Enter 4 to Delete Passangers")


def handleManagePassangersAction(action):
    if action == "1":
        flightManager.list()
    elif action == "2":
        PassangersNo =input("Enter ypur PassangersNo: ")
        BookingNo =input("Enter your BookingNo")
        name =input("Enter your Name: ")
        gender = input("Enter your Gender: ")
        address = input("Enter your Adddress: ")
        email = input("Enter your Email: ")
        PhoneNo = input("Enter your PhoneNo: ")
        response=passangersManager.create(PassangersNo,BookingNo,name,gender,address,email,PhoneNo)
        if response :
            print("Congrats! Your PassangersNo ",PassangersNo," is created successfully")
        else:
            print("Booking", BookingNo, " not available")
    elif action == "3":
        PassangersNo =input("Enter ypur PassangersNo: ")
        BookingNo =input("Enter your BookingNo")
        name =input("Enter your Name: ")
        gender = input("Enter your Gender: ")
        address = input("Enter your Adddress: ")
        email = input("Enter your Email: ")
        PhoneNo = input("Enter your PhoneNo: ")
        passangersManager.update(PassangersNo,BookingNo,name,gender,address,email,PhoneNo)
        print("Update Successful! ")
    elif action == "4":
        PassangersNo = input("Enter Passangers Number: ")
        passangersManager.delete(PassangersNo)    
    showSubMenu("4")

def showManageAircraftsMenu():
    print("Enter 0 to return to MainMenu")
    print("Enter 1 to List Aircrafts")
    print("Enter 2 to Create Aircraft")
    print("Enter 3 to Update Aircraft")
    print("Enter 4 to Delete Aircraft")


def main():    
    flag = True
    while(flag):
        mainMenu()
        option =input()
        if(option== "0"):
            flag=False
        else:
            showSubMenu(option)

main()