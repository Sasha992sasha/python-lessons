class Human:
    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers(self):
        if self.passengers != []:
            print(f"Список пасажирів {self.brand}:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print("Пасажирів немає")


sasha = Human('Sasha')
anna = Human('Anna')

car = Auto('Mercedes')

car.add_passenger(sasha)
car.add_passenger(anna)

car.print_passengers()
 