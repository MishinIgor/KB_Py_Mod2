class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    
    def start_engine(self):
        print("Engine started")
    
    def drive(self, distance):
        print(f"Driving {distance} kilometers")
        
class ElectricCar(Car):
    def __init__(self, brand, model, color, year, battery_capacity):
        super().__init__(brand, model, color, year)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        print("Charging the battery")
    
    def drive(self, distance):
        super().drive(distance)
        self.battery_capacity -= distance
