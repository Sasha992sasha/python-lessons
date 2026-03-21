class Car:
    def __init__(self , make , model , year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        print(self.year, self.make, self.model)

car = Car("Skoda","Oktavia" , 2014)

car.get_info()