class Careem:
    carList = []
    def __init__(self):
        self.currentLoc = None
        self.destination = None
        self.bookStatus = False
        self.carName = None

    def bookRide(self,currentLoc,destination):
        if len(Careem.carList) != 0:
            self.currentLoc = currentLoc
            self.destination = destination
            self.bookStatus = True
            print(f"You have book ride from  {self.currentLoc} to {self.destination} \n")
            self.carName = Careem.carList[0]
            Careem.carList.remove(self.carName)
        else:
            print("Sorry No Car Present Now")

    def cancelBook(self):
        if self.bookStatus:
            print(f"You have Cancel ride of  {self.currentLoc} to {self.destination} ")
            Careem.carList.append(self.carName)
            self.bookStatus = False
        else:
            print("You have not book any ride yet")

    def rideDetail(self):
        if self.bookStatus:
            inp = int(input("For Your Car Detali Press 1. For Driver Detail press 2 :"))
            if inp == 1 :
                self.carName.carDetail()
            if  inp == 2:
                driver1.driverDetail()
        else:
            print("Please first bookride")

class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
        self.engine = Engine("hp_1500","petrol")
        self.driver = None

    def add_driver(self,b):
        self.driver = b

    def carDetail(self):
        print("____________**************____________")
        print(f"Car Name = {self.name}\n Car model = {self.model}\nCar color = {self.color}"
              f"\nCar engine{self.engine}\n Car driver = {self.driver}")
        print("____________**************____________")

class Engine:
    def __init__(self,hp,type):
        self.hp = hp
        self.type = type
    def engineDetail(self):
        print("____________**************____________")
        print(f"Engine Hourspoower = {self.hp}\nEngine Type = {self.type} ")
        print("____________**************____________")

class Driver:
        def __init__(self,name,license_num,phone_num):
            self.name = name
            self.licenseNumber = license_num
            self.phoneNumber = phone_num

        def driverDetail(self):
            print("____________**************____________")
            print(f"Driver name = { self.name}\nDriver license Number = {self.licenseNumber}\nDriver Phone Number = {self.phoneNumber} ")
            print("____________**************____________")


user = Careem()
user1 = Careem()

driver1 = Driver("Dani","lice_12303","0300_xxxxxxx")
driver2 = Driver("Faizan","lice_1560","0300_xxxxxxx")

car1 = Car("Carola","model2022","red")
car2 = Car("Honda civic","model2002","blue")

car1.add_driver(driver1)
car2.add_driver(driver2)

Careem.carList.append(car1)
Careem.carList.append(car2)

user.bookRide("MAinwali","kalabagh")
user1.bookRide("islam","kalabagh")

user.rideDetail()
user.cancelBook()
user.rideDetail()
user1.rideDetail()

