class Vehicle:
    def __init__(self, color, plate,year):
        self.color = color
        self.plate = plate
        self.year = year
    
    def start_motor(self):
        print("Start!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', ' .join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motorcycle(Vehicle):
    pass

class Car(Vehicle):
    pass   
    
class Truck(Vehicle):
    def __init__(self, color, plate,year, loaded):
        super().__init__(color, plate, year)
        self.loaded = loaded

    def Loaded(self):
        print(f"{'it is' if self.loaded else 'it is not'} loaded")

bike1 = Motorcycle("black", "1f9160", 2023)
print(bike1)

car1 = Car("white", "1bz524", 2010)
print(car1)

Truck1 = Truck("blue", "1bz850j", 2015, True)
print(Truck1)

    